import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from "@angular/router";

@Injectable()
export class AuthService {

  // Http options used for making API calls
  private httpOptions: any;
  // Actual JWT token
  public token: string;
  // Token expiration date
  public token_expires: Date;
  // Username of the logged in user
  public username: string;
  // Error messages received from the login attempt
  public errors: any = [];

  constructor(private http: HttpClient, private router: Router) {
    this.httpOptions = {
      headers: new HttpHeaders({'Content-Type': 'application/json'})
    };
  }

  // Use HTTP POST with user credentials to get JWT token from the Django backend
  public login(user) {
    this.http.post('http://127.0.0.1:8000/jwt-auth/', JSON.stringify(user), this.httpOptions).subscribe(
      data => {
        this.updateData(data['token']);
        this.router.navigate(['/home/employee']);
      },
      err => {
        this.errors = err['error'];
      }
    );
  }

  // Use HTTP POST with existing token to refresh JWT token from the Django backend
  public refreshToken() {
    this.http.post('http://127.0.0.1:8000/jwt-refresh/', JSON.stringify({token: this.token}), this.httpOptions).subscribe(
      data => {
        this.updateData(data['token']);
      },
      err => {
        this.errors = err['error'];
      }
    );
  }

  public logout() {
    this.token = null;
    this.token_expires = null;
    this.username = null;

    this.router.navigate(['/signin']);
  }

  private updateData(token) {
    this.token = token;
    this.errors = [];

    // decode the token to read the username and expiration timestamp
    const token_parts = this.token.split(/\./);
    const token_decoded = JSON.parse(window.atob(token_parts[1]));
    this.token_expires = new Date(token_decoded.exp * 1000);
    this.username = token_decoded.username;
  }

}

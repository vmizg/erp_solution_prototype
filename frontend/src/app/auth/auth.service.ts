import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from "@angular/router";
import { JwtHelperService } from '@auth0/angular-jwt';

const jwtHelper = new JwtHelperService();

@Injectable()
export class AuthService {

  // Http options used for making API calls
  private httpOptions: any;
  // Error messages received from the login attempt
  public errors: any = [];

  constructor(private http: HttpClient, private router: Router) {
    this.httpOptions = {
      headers: new HttpHeaders({'Content-Type': 'application/json'})
    };
  }

  // Use HTTP POST with user credentials to get JWT token from the Django backend
  public login(user) {
    this.http.post('http://127.0.0.1:8000/jwt-auth/',
      JSON.stringify(user), this.httpOptions).subscribe(
      data => {
        this.updateData(data['token']);
        this.router.navigate(['/home']);
      },
      err => {
        this.errors = err['error'];
      }
    );
  }

  // Use HTTP POST with existing token to refresh JWT token from the Django backend
  public refreshToken() {
    this.http.post('http://127.0.0.1:8000/jwt-refresh/',
      JSON.stringify({token: localStorage.getItem('token')}), this.httpOptions).subscribe(
      data => {
        this.updateData(data['token']);
      },
      err => {
        this.errors = err['error'];
      }
    );
  }

  private updateData(token) {
    localStorage.setItem('token', token);
    this.errors = [];

    // Decode the token to read the username
    const token_decoded = jwtHelper.decodeToken(token);
    localStorage.setItem('user_id', token_decoded.user_id);
  }

  public logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user_id');

    this.router.navigate(['/signin']);
  }

  public getToken() {
    return localStorage.getItem('token');
  }

  public isAuthenticated(): boolean {
    const token = this.getToken();
    return (token != null && !jwtHelper.isTokenExpired(token));
  }

}

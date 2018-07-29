import { Component, OnInit } from '@angular/core';
import { AuthService } from "../auth.service";
import { Router } from "@angular/router";

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {

  public user: any;

  constructor(public authService: AuthService, private router: Router) { }

  ngOnInit() {
    if (localStorage.getItem('token')) {
      this.router.navigate(['/home']);
    }

    this.user = {
      username: '',
      password: ''
    };
  }

  login() {
    this.authService.login({'username': this.user.username, 'password': this.user.password});
  }

  logout() {
    this.authService.logout();
  }

}

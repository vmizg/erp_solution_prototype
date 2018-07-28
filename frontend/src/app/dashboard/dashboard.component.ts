import { Component } from '@angular/core';
import { AuthService } from "../auth/auth.service";

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css'],
})
export class DashboardComponent {
  title = "John Johnson";

  constructor(private authService: AuthService) {}

  logout() {
    this.authService.logout();
  }
}

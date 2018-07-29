import { Component, OnInit } from '@angular/core';
import { ApiService } from "../../services/api.service";
import { Router } from "@angular/router";

@Component({
  selector: 'app-employee-list',
  templateUrl: './employeelist.component.html',
  styleUrls: ['./employeelist.component.css']
})
export class EmployeeListComponent implements OnInit {

  employeeList = {};
  noEmployees = false;

  constructor(private apiService: ApiService, private router: Router) { }

  ngOnInit() {
    this.apiService.getUsers()
      .subscribe(
        data => this.employeeList = data,
        err => {
          if (err.status == 404)
            this.noEmployees = true;
        }
      );
  }

  onSelect(user_id) {
    if (user_id == localStorage.getItem('user_id')) {
      this.router.navigateByUrl('/home');
    } else {
      this.router.navigateByUrl('/home/list/' + user_id);
    }
  }

}

import { Component, OnInit } from '@angular/core';
import { ApiService } from "../../services/api.service";
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: 'app-employee-foreign',
  templateUrl: './employeeforeign.component.html',
  styleUrls: ['./employeeforeign.component.css']
})
export class EmployeeForeignComponent implements OnInit {

  userId = null;

  forbidden = false;
  noProfile = false;
  noContract = false;

  first_name = "";
  last_name = "";
  employeeData = {};
  contractData = {};
  workpermitData = {};

  constructor(private apiService: ApiService, private route: ActivatedRoute) { }

  ngOnInit() {
    // This checks the route path and will fetch the required user id
    // from the route argument
      this.route.params.subscribe(params => {
          this.userId = params['id'];
      });

    this.apiService.getUserById(this.userId)
      .subscribe(
        data => {
          this.first_name = data['first_name'];
          this.last_name = data['last_name'];
        },
        err => console.error(err)
      );
    this.apiService.getEmployeeById(this.userId)
      .subscribe(
        data => this.employeeData = data,
        err => {
          if (err.status == 404) {
            this.noProfile = true;
          }
        }
      );
    this.apiService.getContractById(this.userId)
      .subscribe(
        data => {
          this.contractData = {
            'job_title': data['job_title'],
            'dc_type': data['dc_type'],
            'wage': data['wage'],
            'salary_struct': data['salary_struct'],
            'tp_duration_begin': data['tp_duration_begin'],
            'tp_duration_end': data['tp_duration_end'],
            'schedule': data['schedule'],
            'pay_schedule': data['pay_schedule']
          };
          this.workpermitData = {
            'visa_no': data['visa_no'],
            'visa_expiry': data['visa_expiry'],
            'work_permit_no': data['work_permit_no']
          };
        },
        err => {
          if (err.status == 403) {
            this.forbidden = true;
          } else if (err.status == 404) {
            this.noContract = true;
          }
        }
      )
  }

}

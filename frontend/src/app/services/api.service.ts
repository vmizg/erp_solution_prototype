import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AuthService } from "../auth/auth.service";

@Injectable()
export class ApiService {

  constructor(private http: HttpClient, private authService: AuthService) {
  }

  public getEmployee() {
    let user_id = localStorage.getItem('user_id');
    return this.http.get('http://127.0.0.1:8000/employee/' + user_id + "/");
  }

  public getEmployeeById(user_id) {
    return this.http.get('http://127.0.0.1:8000/employee/' + user_id + "/");
  }

  public getUser() {
    let user_id = localStorage.getItem('user_id');
    return this.http.get('http://127.0.0.1:8000/user/' + user_id + "/");
  }

  public getUserById(user_id) {
    return this.http.get('http://127.0.0.1:8000/user/' + user_id + "/");
  }

  public getUsers() {
    return this.http.get('http://127.0.0.1:8000/user/');
  }

  public getContract() {
    let user_id = localStorage.getItem('user_id');
    return this.http.get('http://127.0.0.1:8000/contract/' + user_id + "/");
  }

  public getContractById(user_id) {
    return this.http.get('http://127.0.0.1:8000/contract/' + user_id + "/");
  }

}

import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { TokenInterceptor } from './auth/token.interceptor';
import { RouterModule, Routes } from "@angular/router";
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import {
  MatGridListModule, MatCardModule, MatMenuModule,
  MatIconModule, MatButtonModule, MatToolbarModule,
  MatTabsModule, MatFormFieldModule, MatInputModule,
  MatListModule, MatTooltipModule, MatDividerModule
} from '@angular/material';
import { MatSidenavModule } from '@angular/material/sidenav';

import { LayoutModule } from '@angular/cdk/layout';
import { SigninComponent } from './auth/signin/signin.component';
import { AuthService } from "./auth/auth.service";
import { AuthGuard } from "./auth/guards/auth.guard";
import { EmployeeComponent } from './content/employee/employee.component';
import { ApiService } from "./services/api.service";
import { MapToIterable } from "./pipes/maptoiterable.pipe";
import { EmployeeListComponent } from "./content/employeelist/employeelist.component";
import { EmployeeForeignComponent } from "./content/employeeforeign/employeeforeign.component";

const appRoutes: Routes = [
  {
    path: 'home', component: DashboardComponent, canActivate: [AuthGuard],
    children: [
      { path: '', component: EmployeeComponent },
      { path: 'list', component: EmployeeListComponent },
      { path: 'list/:id', component: EmployeeForeignComponent }
    ]
  },
  { path: 'signin', component: SigninComponent },
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: '**', redirectTo: 'home', pathMatch: 'full' }
];

@NgModule({
  declarations: [
      AppComponent,
      DashboardComponent,
      SigninComponent,
      EmployeeComponent,
      EmployeeListComponent,
      EmployeeForeignComponent,
      MapToIterable
  ],
  imports: [
      BrowserModule,
      BrowserAnimationsModule,
      HttpClientModule,
      MatGridListModule,
      MatCardModule,
      MatMenuModule,
      MatIconModule,
      MatButtonModule,
      MatTabsModule,
      MatToolbarModule,
      MatFormFieldModule,
      MatInputModule,
      MatSidenavModule,
      MatListModule,
      MatTooltipModule,
      MatDividerModule,
      LayoutModule,
      FormsModule,
      RouterModule.forRoot(appRoutes)
  ],
  providers: [
    ApiService,
    AuthService,
    AuthGuard,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

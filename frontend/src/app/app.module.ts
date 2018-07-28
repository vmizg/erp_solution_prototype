import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes } from "@angular/router";
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { MatGridListModule, MatCardModule, MatMenuModule,
  MatIconModule, MatButtonModule, MatToolbarModule,
  MatTabsModule, MatFormFieldModule, MatInputModule } from '@angular/material';
import { LayoutModule } from '@angular/cdk/layout';
import { SigninComponent } from './auth/signin/signin.component';
import { AuthService } from "./auth/auth.service";
import { AuthGuard } from "./auth/guards/auth.guard";

const appRoutes: Routes = [
  { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
  { path: 'signin', component: SigninComponent },
  { path: 'dashboard', component: DashboardComponent, canActivate: [AuthGuard] }
];

@NgModule({
  declarations: [
      AppComponent,
      DashboardComponent,
      SigninComponent
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
      LayoutModule,
      FormsModule,
      RouterModule.forRoot(appRoutes)
  ],
  providers: [
    AuthService,
    AuthGuard
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

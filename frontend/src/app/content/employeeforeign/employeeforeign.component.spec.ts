import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EmployeeForeignComponent } from './employeeforeign.component';

describe('EmployeeForeignComponent', () => {
  let component: EmployeeForeignComponent;
  let fixture: ComponentFixture<EmployeeForeignComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EmployeeForeignComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EmployeeForeignComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

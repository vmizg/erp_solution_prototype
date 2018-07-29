# anquan_assignment
ERP website prototype based on Django REST Framework + Angular

Addresses:
* DRF is launched at http://127.0.0.1:8000/
* Angular is launched at http://localhost:4200/

Missing features for a simplistic, but fully usable ERP system:
* Proper display of info fields rather than JSON keywords (hardcode display text for JSON keywords)
* Editing of employee and employee contract data from front-end app
* Creating and editing users from front-end app
All of the above are possible within the back-end API GUI interface provided by Django REST Framework.

TODOs:
* DRF: Possibly get rid of duplicated email field on both User `email` and Employee `work_email` models
* Angular: Extend the employee dashboard component to support viewing other employees, removing the need for `employeeforeign.component.ts`, which is almost a copy of `employee.component.ts`

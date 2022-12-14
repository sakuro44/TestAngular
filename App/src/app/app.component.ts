import { Component } from '@angular/core';
import { AbstractControl, FormBuilder, FormGroup, Validators } from '@angular/forms';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  formGrp: FormGroup;

  constructor(formBuilder: FormBuilder) {
    this.formGrp = formBuilder.group({
      emailctrl: ['', [Validators.required, Validators.email]]
    })
  }

  get emailid(){
    return this.formGrp.controls;
  }

  doSubmit() {
    console.log(this.formGrp.value);
  }
  name = 'SAKURA';
  myimaage1:string = '/assets/pic/icons8-blossom-64.png';
  myimaage2:string = '/assets/pic/me.jpg';
  myimaage3:string = '/assets/pic/barbie.jpg';
  myimaage4:string = '/assets/pic/but.png';
  myimaage5:string = '/assets/pic/pic2.jpg';
  myimaage6:string = '/assets/pic/img.png';
  myimaage7:string = '/assets/pic/icons8-facebook-64.png';
  myimaage8:string = '/assets/pic/icons8-github-64.png';
}

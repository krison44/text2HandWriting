import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { DomSanitizer } from '@angular/platform-browser';
import { timer } from 'rxjs';
import { take } from 'rxjs/operators';
import { AppService } from '../app.service';

@Component({
  selector: 'app-text-to-handwriting',
  templateUrl: './text-to-handwriting.component.html'
})
export class TextToHandwritingComponent implements OnInit {
  textToHandWritingForm: FormGroup;
  isResultAvailable: boolean;
  handWrittednOutputUrl: any;
  isLoading: boolean;
  url: string;

  constructor(private fb: FormBuilder, private service: AppService, private sanitizer: DomSanitizer) {
    this.isResultAvailable = false;
    this.url = '/api/url';
  }

  ngOnInit(): void {
    this.createForm();
    this.handWrittednOutputUrl = null;
  }

  createForm() {
    this.textToHandWritingForm = this.fb.group({
      userText: ['', Validators.required]
    })
  }

  submitForm() {
    this.isLoading = true;
    this.isResultAvailable = false;
    this.sanitizer.bypassSecurityTrustResourceUrl(this.url);
    this.service.postText(this.textToHandWritingForm.value).subscribe(response => {
      this.handWrittednOutputUrl = this.sanitizer.bypassSecurityTrustResourceUrl(this.url);
      this.isResultAvailable = true;
      this.isLoading = false;
    });
  }

  clearForm() {
    this.textToHandWritingForm.reset();
    this.isResultAvailable = false;
    this.handWrittednOutputUrl = null;
  }
}

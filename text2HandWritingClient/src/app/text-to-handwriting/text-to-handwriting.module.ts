import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TextToHandwritingComponent } from './text-to-handwriting.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  imports: [
    CommonModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatProgressSpinnerModule
  ],
  providers: [],
  declarations: [TextToHandwritingComponent],
  exports: [TextToHandwritingComponent]
})
export class TextToHandwritingModule { }

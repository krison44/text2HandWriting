import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from  '@angular/common/http';  

@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor(private http: HttpClient) { }

  postText(userText) {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })
    };
    return this.http.post(`/api/userText`, userText, httpOptions);
  }

  getOutput() {
    return this.http.get('/api/url');
  }
}

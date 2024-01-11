import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class MessageService {
  private baseUrl = 'http://localhost:3001/messages';

  constructor(private http: HttpClient) { }

  getMessages() {
    return this.http.get(this.baseUrl);
  }

  getMessage(id: string) {
    return this.http.get(`${this.baseUrl}/${id}`);
  }

  createMessage(message: any) {
    return this.http.post(this.baseUrl, message);
  }

  updateMessage(id: string, message: any) {
    return this.http.put(`${this.baseUrl}/${id}`, message);
  }

  deleteMessage(id: string) {
    return this.http.delete(`${this.baseUrl}/${id}`);
  }
}
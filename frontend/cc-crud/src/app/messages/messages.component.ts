import { Component } from '@angular/core';
import { MessageService } from '../message.service';
import { toArray } from 'rxjs/operators';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-messages',
  standalone: true,
  imports: [],
  templateUrl: './messages.component.html',
  styleUrl: './messages.component.css'
})
export class MessagesComponent {
 constructor(public messageService: MessageService) {}

 getMessageList(): Observable<any[]> {
   return this.messageService.getMessages().pipe(toArray());
 }
}

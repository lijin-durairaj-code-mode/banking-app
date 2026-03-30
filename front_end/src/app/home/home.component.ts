import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  private messagesSubject = new BehaviorSubject<any[]>([
    {
      "type": "bot",
      "message": "Hello! How can I help you?"
    },
    {
      "type": "user",
      "message": "Hi, I need help"
    }
  ]);
  messages$ = this.messagesSubject.asObservable();

  userInput = new FormControl('');  


  add_user_query() {
    const current = this.messagesSubject.value;
    this.messagesSubject.next([
      ...current,
      { type: 'user', message: this.userInput.value }
    ]);
    this.userInput.reset()
  }
}

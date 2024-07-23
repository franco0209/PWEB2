// cursos.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CursosService {
  private apiUrl = 'http://localhost:8000/api/cursos/';

  constructor(private http: HttpClient) { }

  getCursos(): Observable<any> {
    return this.http.get(this.apiUrl);
  }

  // Métodos adicionales para crear, actualizar, eliminar, etc.
}

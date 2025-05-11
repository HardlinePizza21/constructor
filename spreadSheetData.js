import ExcelJS from 'exceljs';
import fs from 'fs';


const workbook = new ExcelJS.Workbook();
await workbook.xlsx.readFile('./birthSheet.xlsx');

const birthSheet = workbook.worksheets[0];

const diasDeLaSemana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"];

let base = "";
let diaDelMes = 0;
let diaDeLaSemana = 2;

birthSheet.eachRow((row, rowNumber) => {

  if (rowNumber != 1) {


    if (diaDelMes != row.values[2]) {
      diaDelMes++;
      diaDeLaSemana++;
      if (diaDeLaSemana > 6) {
        diaDeLaSemana = 0;
      }
      base = base + `<h4>${diasDeLaSemana[diaDeLaSemana]}, ${diaDelMes} de Mayo</h4>\n`
    }

    base = base + `<p>${row.values[1]}, ${row.values[4]}<br/></p>\n`

  }

})

fs.writeFile('birthPage.txt', base, (err) => {
  if (err) {
    console.error('Error al escribir el archivo:', err);
  } else {
    console.log('Archivo creado con éxito.');
  }
});

console.log(base);
import 'dart:convert';
import 'dart:io';

import 'package:praktos_dart3/praktos_dart3.dart' as praktos_dart3;

void main(List<String> arguments) {


var pygrades = [
  {'Python':[5,4,3]},
  {'Python':[5,2,5]},
  {'Python':[5,5,5]}
];

var javagrades =[
  {'Java':[4,4,3]},
  {'Java':[3,4,3]},
  {'Java':[4,5,5]},
];

var cgrades =[
  {'C#':[3,3,5]},
  {'C#':[3,3,3]},
  {'C#':[5,4,5]}
];
var allgrades =[
  {'RP':[4], 'RJ':[4], 'RC#':[4], 'All':[4]},
  {'RP':[3], 'RJ':[3], 'RC#':[3], 'All':[3]},
  {'RP':[5], 'RJ':[5], 'RC#':[5], 'All':[5]}
];
var students =[
{'name': "Григорий Ульев  "},
{'name': "Олег Орлов      "},
{'name': "Екатерина Мирова"}
];

int counter=0;
print("   Студент            Python      Java         C#   Итог: Py Java  C#  Общая");
while(counter < students.length){
  print("\n ${students[counter].values} ${pygrades[counter].values} ${javagrades[counter].values} ${cgrades[counter].values} ${allgrades[counter].values} ");
counter++;
}

print("Поиск по фамилии");
print("Введите фамилию:");
String surname = stdin.readLineSync(encoding: utf8)!;
int stud=0;
String u;
while(stud<students.length){
u = students[stud]['name']!;
if(u.contains(surname)){
int t=0;
double u=0;
List<int> arrayP = [];
int arN;
double forAll=0;
int op=0;
double arN2=0;
int ostal=0;
int horosh=0;
int otlich=0;
  print("Python: ${(pygrades[stud].values)}");
  arrayP = pygrades[stud]['Python']!; 
  arN= arrayP.fold<int>(0,(prev, element) => prev+element);
  arN=arN~/3;
  arN=arN.round();

   print("Средний балл: ${arN}");
   forAll=forAll+arN;

   print("Java: ${(javagrades[stud].values)}");
   arrayP = javagrades[stud]['Java']!; 
  arN= arrayP.fold<int>(0,(prev, element) => prev+element);
  arN2 = arN/arrayP.length;
  arN=arN2.round();
   print("Средний балл: ${arN}");
    forAll=forAll+arN;

  print("C#: ${(cgrades[stud].values)}");
   arrayP = cgrades[stud]['C#']!; 
  arN= arrayP.fold<int>(0,(prev, element) => prev+element);
  arN2=arN/arrayP.length;
   arN=arN2.round();
   print("Средний балл: ${arN}");

   forAll=forAll+arN;
int forAllInt;
  forAll=forAll/arrayP.length;
  forAllInt=forAll.round();
  print("Общий результат: ${forAllInt}");
  if(forAllInt <4){
    print("Категория: Остальные");
    ostal++;
  }else if(forAllInt>=4 && forAllInt<5){
    print("Категория: Хорошист");
    horosh++;
  }else if(forAllInt>=5){
    print("Категория: Отличник");
    otlich++;
  }
}
stud++;
}

print("Уникальные оценки:"); 
int p=0;
List<int> py= [];
List<int> jv= [];
List<int> cs= [];
List<List<int>> list =[];
while(p<students.length){
py = pygrades[p]['Python']!;
jv = javagrades[p]['Java']!;
cs = cgrades[p]['C#']!;
list.add(py);
list.add(jv);
list.add(cs);
p++;
}
var uniquelist = list.expand((row) =>row).toSet().toList();
print(uniquelist);

print("Максимальные и минимальные оценки: "); //Работает только на C#
int counterPy=0;
int itogpy =py[0];
int counter1Py=0;
while(counterPy < pygrades.length){
py = pygrades[counterPy]['Python']!;

while(counter1Py<py.length){
if(itogpy<py[counter1Py]){
  itogpy = py[counter1Py+1];
}

counter1Py=counter1Py+2;
}
counterPy++;
}



int counterC=0;
int counter1C=0;
int itogcs=cs[0];
while(counterC < cgrades.length){
cs = cgrades[counterC]['C#']!;

while(counter1C<cs.length){
if(itogcs<cs[counter1C]){
  itogcs = cs[counter1C+1];
}

counter1C=counter1C+2;
}
counterC++;
}


int counterJv=0;
int counter1Jv=0;
int itogjv=jv[0];
while(counterJv < javagrades.length){
jv = javagrades[counterJv]['Java']!;

while(counter1Jv<jv.length){
if(itogjv<jv[counter1Jv]){
  itogjv = jv[counter1Jv+1];
}

counter1Jv=counter1Jv+2;
}
counterJv++;
}


int counterPy1=1;
int itogpy1 = py[0];
int counter1Py1=0;
while(counterPy1 < pygrades.length){
py = pygrades[counterPy1]['Python']!;

while(counter1Py1<py.length){
if(itogpy1>py[counter1Py1]){
  itogpy1 = py[counter1Py1+1];
}

counter1Py1=counter1Py1+2;
}
counterPy1++;
}


int counterC1=1;
int counter1C1=0;
int itogcs1=cs[0];
while(counterC1 < cgrades.length){
cs = cgrades[counterC1]['C#']!;

while(counter1C1<cs.length){
if(itogcs1>cs[counter1C1]){
  itogcs1 = cs[counter1C1+1];
}

counter1C1=counter1C1+2;
}
counterC1++;
}

int counterJv1=1;
int counter1Jv1=0;
int itogjv1=jv[0];
while(counterJv1 < javagrades.length){
jv = javagrades[counterJv1]['Java']!;

while(counter1Jv1<jv.length){
if(itogjv1<jv[counter1Jv1]){
  itogjv1 = jv[counter1Jv1+1];
}

counter1Jv1=counter1Jv1+2;
}
counterJv1++;
}
  print("Python(max): ${itogpy}");
  print("Java(max): ${itogjv}");
  print("C#(max): ${itogcs}");
  print("Python(min): ${itogpy1}");
  print("Java(min): ${itogjv1}");
  print("C#(min): ${itogcs1}");
  
print("Лучший предмет в группе:");
int countC=0;
int countC2=0;
int qC=0;
while(countC<cgrades.length){

  while(countC2<cs.length){
    qC = qC+ cs[countC2];
    countC2++;
  }
  countC++;
}

int countP=0;
int countP2=0;
int qP=0;
while(countP<pygrades.length){

  while(countP2<py.length){
    qP = qP+ py[countP2];
    countP2++;
  }
  countP++;
}

int countJ=0;
int countJ2=0;
int qJ=0;
while(countJ<javagrades.length){

  while(countJ2<jv.length){
    qJ = qJ+ jv[countJ2];
    countJ2++;
  }
  countJ++;
}


double qCA = qC/3;
double qPA = qP/3;
double qJA = qJ/3;

if(qCA>qJA && qCA>qPA){
  print("C# - ${qCA}");
}
else if (qPA>qCA && qPA > qJA){
  print("Python - ${qPA}");
}
else{
  print("Java - ${qJA}");
}



// print("Студенты с оценкой 2:");
// int countCs=0;
// int otvetCs=0;
// while(countCs < cgrades.length){
// cs = cgrades[0]['C#']!;
// Iterable<int> dva  = cs.where((num0) => num0<3);
// if(dva.isNotEmpty){
//   otvetCs= countCs;
//   countCs=cgrades.length;
//   print("C# - ${students[otvetCs]}");
// }
// countCs++;
// }
// int countPy=0;
// int otvetPy=0;
// while(countPy < pygrades.length){
// cs = pygrades[0]['Python']!;
// Iterable<int> dva1  = py.where((num1) => num1<3);
// if(dva1.isNotEmpty){
//   otvetPy= countPy;
//   countPy=pygrades.length;
//   print("Python - ${students[otvetPy]}");
// }
// countPy++;
// }
// int countJv=0;
// int otvetJv=0;
// while(countJv < javagrades.length){
// jv = javagrades[0]['Java']!;
// Iterable<int> dva2  = jv.where((num2) => num2<3);
// if(dva2.isNotEmpty){
//   otvetJv= countJv;
//   countJv=javagrades.length;
//   print("Java - ${students[otvetJv]}");
// }
// countJv++;
// }

}

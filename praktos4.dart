// import 'package:praktos4/praktos4.dart' as praktos4;
import 'dart:io';
List<Instr> instr = [];
List<Cloth> clothes = [];
class Cup{
  
  int volume;
  Cup(this.volume);
  void drink(){
    print("Скольько выпить?(ml)");
    String how = stdin.readLineSync()!;
    int howw = int.tryParse(how)!;
    volume-=howw;
    print("Осталось ${volume}");
  }

}
class Person{
  String name;
  Person(this.name);

void drinking(Cup cup){
  cup.drink();
}

}
class Instr{
  String title;
  Instr(this.title);

}

class Cloth{
  String title;
  Cloth(this.title);

}

class Closet{
  int counter=0;
  void access(counter){
    counter++;
    if (counter==5){
      print("Шкаф развалился из-за того, что вы положили туда слишком много(. Придется покупать новый");
    }
  }
  void putIntoInstr(Instr smth){
    print("${smth.title} положили в ящик инструментов внутри шкафа");
    instr.add(smth);
    access(counter);
  }
  void putIntoCloth(Cloth clth){
    print("${clth.title} повесили в шкафу");
    clothes.add(clth);
    access(counter);
  }
  void dropSmth(){
    print("Что вы хоите забрать?(1.Одежда/2.Инструменты)");
    String answ = stdin.readLineSync()!;
    int answw = int.tryParse(answ)!;
    if (answw==1){
      print("Вы забрали последнюю повешенную одежду");
      clothes.remove(clothes.last);
    }
    if (answw==2){
      print("Вы забрали последний положенный инструмент");
      instr.remove(instr.last);
      
    }
  }
  void In(){
    print("${clothes} ${instr}");
  }
  }



class Griph{
  String side;
  int weight;
  List<Pancake> pancakes;
  Griph(this.side, this.weight, this.pancakes);
  void access(){
    if(pancakes.length>=10){
      print("Перевес! Все блины вылетели!");
      pancakes.clear();
    }
    }
  void another(Griph firstGriph, Griph griphAn){
    print("Блин перекинут на другой гриф");
    griphAn.pancakes.add(firstGriph.pancakes.last);
    firstGriph.pancakes.remove(pancakes.last);
    firstGriph.weight-=griphAn.pancakes.last.weight;
    griphAn.weight+=griphAn.pancakes.last.weight;
    firstGriph.access();
    griphAn.access();
    
  } 
  void hoW(){
    print("Нагрузка: ${weight}");
  }
  void give(Pancake panck){
    print("Вы положили блин");
    pancakes.add(panck);
    weight+=pancakes.last.weight;

  }
  void drop(){
    print("Вы забрали первый блин");
    weight-=pancakes[0].weight;
    pancakes.remove(0);
    
  }
  }


class Pancake{
  int weight;
  Pancake(this.weight);
}


class Dollar{
double quantity;
Dollar(this.quantity);
void convertToD(Ruble rub){
  quantity = rub.quantity*0.013;
  print(quantity);

}
}

class Ruble{
double quantity;
Ruble(this.quantity);
void convertToR(Dollar dol){
  quantity = dol.quantity*75.48;
  print(quantity);
}
}

class Operation{
  int a;
  int b;
  Operation(this.a,this.b);
  Operation operator +(Operation other){
    return Operation(a, b);
  }
}


class Car{
  String title;
  Statuses status;
  Car(this.title, this.status);
  void changeStat(Statuses stat){
    status= stat;
  }
  void whatStat(){ //Проверить такое написание
    print(status.stat);
  }
}


enum Statuses{
  stop("stop"),
  go("go"),
  turn("Turn");

final String stat;
const Statuses(this.stat);
}



class Figure{
  int s;
  int v;
  Figure(this.s, this.v);
  void WhIsIt(){
    print("Это фигура");
  }
  void S(){
    print("S=${s}");
  }
  void V(){
    print("V=${v}");
  }
  
}
class Trangle extends Figure{
  int corners;
  Trangle(super.s,super.v, this.corners);
  void corn(){
    print("В треугольнике $corners углов");
  }
  @override
  void WhIsIt(){
    print("Это треугольник");
  }
  void S(){
    print("S=${s}");
  }
  void V(){
    print("V=${v}");
  }


  
}
class Cuboid extends Figure{
  int corners;
  int edges;
  Cuboid(super.s, super.v, this.corners, this.edges);
  void corn(){
    print("В параллелепипеде $corners углов");
  }
  void edge(){
    print("В Параллелепипеде ${edges} граней");
  }
  @override
  void WhIsIt(){
    print("Это параллелепипед");
  }
  void S(){
    print("S=${s}");
  }
  void V(){
    print("V=${v}");
  }
}
class Circle extends Figure{
  int r;
  int d;
  Circle(super.s,super.v,this.r,this.d);
  void D(){
    print("Диаметр окружности равен ${d}");
  }
  void R(){
    print("Радиус окружности равен ${r}");
  }
  @override
  void WhIsIt(){
    print("Это окружность");
  }
  void S(){
    print("S=${s}");
  }
  void V(){
    print("V=${v}");
  }
}

class Ten{
  int num;
  Ten(this.num);
  void printing(){
    print("Число в десятичной системе: ${num}");
  }
  static void converter(String num2, int radix){
    print(int.parse(num2, radix: radix));
  }
  
}
class SxT{
  String num;
  SxT(this.num);
  void printing(){
    print("Число в шестнадцатеричной системе: ${num}");
  }
  static void converter(int num2){
    print(num2.toRadixString(16));
  }
  
}

class Two{
  String num;
  Two(this.num);
  void printing() {
    print("Число в двоичной системе: ${num}");
  }
  static void converter(int num2){
    print(num2.toRadixString(2));
  }
}


class Geometric{
  int s;
  Geometric(this.s);
  static void whichMost(figures){
    int id=0;
    for(int i=0; i<figures.length-1; i++){
      if(figures[i].s<figures[i+1].s){
        id=i+1;
      }
    }
    print(id);
  }

}

class Dishes{
  String title;
  String size;
  Dishes(this.title, this.size);
}
class Fork extends Dishes{
  Fork(super.title, super.size);
}
class Plate extends Dishes{
  Plate(super.title, super.size);
}

class Table{
  List<Dishes> list;
  Table(this.list);
  void addOnTable(Dishes what){
    list.add(what);
  }
  void dropOutTable(int id){
    list.remove(list[id]);
  }
  void whatInTable(){
    print(list);
  }
}

class Ariphmetic{
  int a;
  int b;
  Ariphmetic(this.a,this.b);

  Ariphmetic operator +(Ariphmetic){
    return Ariphmetic(a+b*2, b+a*3);
  }

}

void main(List<String> arguments) {
  Cup cup= Cup(1000);
  Person pers = Person("Alex");
  pers.drinking(cup);

  print("\n \n \n \n ----------Следующее задание");

  Closet mini = Closet();
  Instr instrum = Instr("Отвертка");
  Instr instrum2 = Instr("Шуруповерт");
  Cloth cloth = Cloth("Футболка");
  Cloth cloth2 = Cloth("Куртка");
  Cloth cloth3 = Cloth("Пиджак");
  mini.In();
  mini.putIntoInstr(instrum);
  mini.putIntoCloth(cloth2);
  mini.In();
  mini.dropSmth();
  mini.In();

  print("\n \n \n \n ----------Следующее задание");

  List<Pancake> panckL = [];
  List<Pancake> panckR = [];
  Pancake panck1 = Pancake(1);
  Pancake panck2 = Pancake(2);
  Griph griphL = Griph("Left", 0, panckL);
  Griph griphR = Griph("Right", 0, panckR);
  griphR.give(panck1);
  griphL.give(panck2);
  griphR.hoW();
  griphL.hoW();
  griphR.another(griphR, griphL);
  griphL.hoW();
  griphL.drop();
  griphL.hoW();

  print("\n \n \n \n ----------Следующее задание");

  Ruble rub = Ruble(100);
  Dollar dol = Dollar(2);
  Dollar convertionR = Dollar(0);
  Ruble convertionD = Ruble(0);
  convertionD.convertToR(dol);
  convertionR.convertToD(rub);

  print("\n \n \n \n ----------Следующее задание");

  int x =3;
  int y=4;
  print(Ariphmetic(x,y));

  print("\n \n \n \n ----------Следующее задание");

  Car car = Car("Lada Granta", Statuses.stop); 
  car.whatStat();
  car.changeStat(Statuses.go);
  car.whatStat();

  print("\n \n \n \n ----------Следующее задание");

  Figure fig  =Figure(9, 12);
  fig.WhIsIt();
  fig.S();
  fig.V();
  Trangle tr = Trangle(8, 12, 3);
  tr.WhIsIt();
  tr.S();
  tr.V();
  tr.corn();
  Cuboid cub = Cuboid(25, 50, 8, 6);
  cub.WhIsIt();
  cub.S();
  cub.V();
  cub.corn();
  cub.edge();
  Circle circle = Circle(10, 15, 5, 10);
  circle.WhIsIt();
  circle.D();
  circle.R();
  circle.S();
  circle.V();

  print("\n \n \n \n ----------Следующее задание");

  int num = 28;
  SxT.converter(num);
  Two.converter(num);
  SxT sxT = SxT("1A");
  Two two = Two("1101");
  Ten.converter(sxT.num, 16);
  Ten.converter(two.num, 2);

  print("\n \n \n \n ----------Следующее задание");

  Geometric geom = Geometric(12);
  Geometric geom2 = Geometric(13);
  Geometric geom3 = Geometric(8);
  List<Geometric> figures = [geom,geom3,geom2];
  Geometric.whichMost(figures);
  
  print("\n \n \n \n ----------Следующее задание");

  Fork frok = Fork("Fork", "tea");
  Fork fork = Fork("fork2", "big");
  Plate palte = Plate("Palte", "big");
  Plate plate = Plate("plate2", "small");
  List<Dishes> list =[palte, frok];
  Table table = Table(list);
  table.whatInTable();
  table.addOnTable(plate);
  table.whatInTable();
  table.dropOutTable(0);
  table.whatInTable();
}

import 'dart:convert';
import 'dart:io';
import 'dart:math';

import 'package:praktos_dart2/praktos_dart2.dart' as praktos_dart2;
import 'package:characters/characters.dart';


enum Mood{
    happy("\u{1f643}"),
    chill("\u{1f60c}"),
    sad("\u{1f614}"),
    excited("\u{1f61f}"),
    angry("\u{1f620}");
final String title;
const Mood(this.title);



}







void main(List<String> arguments) {
  var rand = Random().nextInt(4);
  var emote;
  var energy = Random().nextInt(10);
  var emotetext;
  switch(rand){
    case 0:
    emote = Mood.happy.title;
    emotetext = "веселый";
    case 1:
    emote = Mood.chill.title;
    emotetext = "расслабленный";
    case 2:
    emote = Mood.sad.title;
    emotetext = "грустный";
    case 3:
    emote = Mood.excited.title;
    emotetext = "напуганный";
    case 4:
    emote = Mood.angry.title;
    emotetext = "напряженный";
  }
print("Ваше имя:");
String ? name = stdin.readLineSync();
print("Генерируем случайное настроение...");
print("Привет, ${name}, Твое настроение: ${emote} ${emotetext} (Энергия: ${energy}/10)");
print("Юникод вашего эмодзи: U+${emote.runes.first.toRadixString(16)}");
print("Хотите просмотреть сложные эмодзи? (да/нет): ");
String ? a = stdin.readLineSync(encoding: utf8);
if (a == "да"){
  print("Введите комбинацию эмодзи: ");
  var emoji2 = "👨‍👩‍👧‍👦";
  var emoji2List = emoji2.characters.toList();
  print(emoji2List);
  print(emoji2List.length);
  print("Анализ строки: ${emoji2}");
  print("- 16-битных единиц: ${emoji2.length}");
  print("- Кодовых символов: ${emoji2.runes.length}");
  print("- Реальных символов: ${emoji2.characters.length}");
  int count=1;
for(var y in emoji2.runes){
  print(" Символ ${count}: U+${y.toRadixString(16)}");
  count++;
}

}
else{
  print("df");
}




}
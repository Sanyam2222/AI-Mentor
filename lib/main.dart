import 'package:flutter/material.dart';
import 'screens/quiz_page.dart';

void main() {
  runApp(AIMentorApp());
}

class AIMentorApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'AI Mentor',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: QuizPage(),
    );
  }
}

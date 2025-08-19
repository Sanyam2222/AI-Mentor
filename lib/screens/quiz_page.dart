import 'package:flutter/material.dart';
import '../services/career_service.dart';
import 'result_page.dart';

class QuizPage extends StatefulWidget {
  @override
  _QuizPageState createState() => _QuizPageState();
}

class _QuizPageState extends State<QuizPage> {
  final CareerService _careerService = CareerService();
  List<int> answers = [];

  // Example questions, can later load from model or JSON
  final List<String> questions = [
    "Do you enjoy coding?",
    "Do you like problem-solving?",
    "Do you prefer working with people?",
  ];

  int currentQuestionIndex = 0;

  void selectAnswer(int choice) {
    answers.add(choice);
    if (currentQuestionIndex < questions.length - 1) {
      setState(() {
        currentQuestionIndex++;
      });
    } else {
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => ResultPage(answers: answers),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("AI Mentor Quiz")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(questions[currentQuestionIndex], style: TextStyle(fontSize: 20)),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => selectAnswer(1),
              child: Text("Yes"),
            ),
            ElevatedButton(
              onPressed: () => selectAnswer(0),
              child: Text("No"),
            ),
          ],
        ),
      ),
    );
  }
}

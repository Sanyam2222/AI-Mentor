import 'package:flutter/material.dart';
import '../services/career_service.dart';
import 'result_page.dart';

class QuizPage extends StatefulWidget {
  @override
  _QuizPageState createState() => _QuizPageState();
}

class _QuizPageState extends State<QuizPage> {
  final CareerService _careerService = CareerService();

  // Initialize with -1 to track unanswered questions
  List<int> answers = List.filled(5, -1);

  // Updated to 5 questions
  final List<String> questions = [
    "Do you enjoy coding?",
    "Do you like problem-solving?",
    "Do you prefer working with people?",
    "Are you interested in data analysis?",
    "Do you like creative work?",
  ];

  int currentQuestionIndex = 0;

  void selectAnswer(int choice) {
    answers[currentQuestionIndex] = choice;

    if (currentQuestionIndex < questions.length - 1) {
      setState(() {
        currentQuestionIndex++;
      });
    } else {
      // All questions answered, navigate to ResultPage
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
            Padding(
              padding: EdgeInsets.symmetric(horizontal: 16),
              child: Text(
                questions[currentQuestionIndex],
                style: TextStyle(fontSize: 20),
                textAlign: TextAlign.center,
              ),
            ),
            SizedBox(height: 30),
            ElevatedButton(
              onPressed: () => selectAnswer(1),
              child: Text("Yes"),
            ),
            SizedBox(height: 10),
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

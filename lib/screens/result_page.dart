import 'package:flutter/material.dart';
import '../services/career_service.dart';

class ResultPage extends StatefulWidget {
  final List<int> answers;

  ResultPage({required this.answers});

  @override
  _ResultPageState createState() => _ResultPageState();
}

class _ResultPageState extends State<ResultPage> {
  final CareerService _careerService = CareerService();
  String? career;
  String? explanation;
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    fetchCareer();
  }

  void fetchCareer() async {
    try {
      final predictedCareer = await _careerService.predictCareer(widget.answers);
      final careerExplanation = await _careerService.explainCareer(predictedCareer);

      setState(() {
        career = predictedCareer;
        explanation = careerExplanation;
        isLoading = false;
      });
    } catch (e) {
      setState(() {
        career = "Error";
        explanation = e.toString();
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Your Career Suggestion")),
      body: Center(
        child: isLoading
            ? CircularProgressIndicator()
            : Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text("Suggested Career: $career", style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            SizedBox(height: 20),
            Text("Explanation: $explanation", style: TextStyle(fontSize: 16)),
          ],
        ),
      ),
    );
  }
}

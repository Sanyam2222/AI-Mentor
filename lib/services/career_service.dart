import 'dart:convert';
import 'package:http/http.dart' as http;

class CareerService {
  final String baseUrl = "http://127.0.0.1:8080";

  // Send quiz answers to predict career
  Future<String> predictCareer(List<int> answers) async {
    final url = Uri.parse('$baseUrl/predict');
    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'answers': answers}),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      return data['career_field'];
    } else {
      throw Exception('Failed to predict career: ${response.body}');
    }
  }

  // Get AI explanation for a career
  Future<String> explainCareer(String careerField) async {
    final url = Uri.parse('$baseUrl/explain');
    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'career_field': careerField}),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      return data['explanation'];
    } else {
      throw Exception('Failed to get explanation: ${response.body}');
    }
  }
}

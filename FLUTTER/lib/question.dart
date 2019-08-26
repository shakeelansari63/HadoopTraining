import 'package:flutter/material.dart';

class  Question extends StatelessWidget {
  final String questionText;

  Question(this.questionText);

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Text(this.questionText, style: TextStyle(
        fontSize: 20
      ),
      textAlign: TextAlign.center,),
      width: double.infinity,
      margin: EdgeInsets.all(10)
    );
  }
}
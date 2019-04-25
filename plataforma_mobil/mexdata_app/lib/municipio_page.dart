import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

class municipioPage extends StatelessWidget{

  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      body: Container(
        child: Container(
          padding: EdgeInsets.all(4.0),
          child: WebView(
            initialUrl: "https://flutter.io",
            javascriptMode: JavascriptMode.unrestricted ,
          ),
        ),
      ),
    );
  }
}
import 'package:flutter/material.dart';
import './pais_page.dart' as paispage;
import './estado_page.dart' as estadopage;
import './municipio_page.dart' as municipiopage;

void main() => runApp(MaterialApp(
  home: MyApp(),
  debugShowCheckedModeBanner: false,
  theme: ThemeData(
    primarySwatch: Colors.indigo,
  ),
));

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> with SingleTickerProviderStateMixin{
  TabController controller;

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    controller= new TabController(length: 3, vsync: this);
  }

  @override
  void dispose() {
    // TODO: implement dispose
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: new Text("MexData"),
      backgroundColor: Colors.indigo,
        bottom:  new TabBar(
          controller: controller,
          tabs: <Widget>[
            new Tab(icon: new Icon(Icons.assistant_photo), text: "País"),
            new Tab(icon: new Icon(Icons.account_balance), text:  "Estado"),
            new Tab(icon: new Icon(Icons.terrain), text: "Municipio",)
          ],
        ),
      ),
      body: new TabBarView(
          controller: controller,
          children: <Widget>[
        new paispage.paisPage(),
        new estadopage.estadoPage(),
        new municipiopage.municipioPage(),
      ]),

    );
  }

}
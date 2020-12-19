import React, { Component } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';


class MyClass extends Component {

  constructor(props){
    super(props);
    this.state = {
      textInput : [],
      inputData : []
    }
  }

  //function to add TextInput dynamically
  addTextInput = (index) => {
    let textInput = this.state.textInput;
    textInput.push(<TextInput style={styles.textInput}
      onChangeText={(text) => this.addValues(text, index)} />);
    this.setState({ textInput });
  }

  //function to remove TextInput dynamically
  removeTextInput = () => {
    let textInput = this.state.textInput;
    let inputData = this.state.inputData;
    textInput.pop();
    inputData.pop();
    this.setState({ textInput,inputData });
  }

  //function to add text from TextInputs into single array
  addValues = (text, index) => {
    let dataArray = this.state.inputData;
    let checkBool = false;
    if (dataArray.length !== 0){
      dataArray.forEach(element => {
        if (element.index === index ){
          element.text = text;
          checkBool = true;
        }
      });
    }
    if (checkBool){
    this.setState({
      inputData: dataArray
    });
  }
  else {
    dataArray.push({'text':text,'index':index});
    this.setState({
      inputData: dataArray
    });
  }
  }

  //function to console the output
  //change to send data
  getValues = () => {
    console.log('Data',this.state.inputData);
  }


  render(){
    return(
      <View>
        <View style={styles.header}>
          <Text style={styles.title}>What do you have in Fridge?</Text>
        </View>
        <View style= {styles.row}>
          <View style={{margin: 5}}>
        <Button color = 'purple' title='Add' onPress={() => this.addTextInput(this.state.textInput.length)} />
        </View>
        <View style={{margin: 5}}>
        <Button color = 'purple' title='Remove' onPress={() => this.removeTextInput()} />
        </View>
        </View>
        {this.state.textInput.map((value) => {
          return value
        })}
        <Button color = 'purple' title='Get Recipes' onPress={() => this.getValues()} />
      </View>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'grey',
  },
  buttonView: {
  flexDirection: 'row'
  },
  textInput: {
  height: 40,
  borderColor: 'black', 
  borderWidth: 1,
  margin: 5
},
header: {
  padding: 0
},
title: {
  fontWeight: "bold",
  fontSize: "1.5rem",
  marginVertical: "1em",
  textAlign: "center"
},
row:{
  flexDirection: 'row',
  justifyContent: 'center'
  },
});

export default MyClass;
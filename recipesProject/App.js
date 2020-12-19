import React from 'react';
import { StyleSheet, Text, View, ImageBackground, Dimensions} from 'react-native';

const { width, height } = Dimensions.get("window");


export default function App() {
    return (
      <View style={styles.container}>
          <ImageBackground source = {require('./Images/FoodCamImage.jpg')} style = {styles.image1}>
          <View style = {styles.transparant}>
            <Text style = {[styles.textStyle , {backgroundColor: 'transparent'}]}>Use camera to scan</Text>
          </View>
          </ImageBackground>

          <ImageBackground source = {require('./Images/FoodTypingImage.jpg')} style = {styles.image2}>
          <View style = {styles.transparant}>
            <Text style = {[styles.textStyle , {backgroundColor: 'transparent'}]}>Type Ingredients</Text>
          </View>
          </ImageBackground>
      </View>
    );
  }
  
  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    },

    image1: {
      justifyContent: 'center' , 
      alignItems : 'center',
      width: width,
      height: height/3,
      top: -20,
    },

    image2: {
      justifyContent: 'center' , 
      alignItems : 'center',
      width: width,
      height: height/3,
      top: 40,
    },

    transparant: {
      flex: 1,
      justifyContent:'center',
      alignItems : 'center',
      alignSelf: 'stretch',
      backgroundColor:'rgba(255 , 255 , 255 , 0.5)',
    },
    
    textStyle: {
      fontSize: 30,
      fontWeight: 'bold',
      color: 'black',
      fontStyle: 'italic',
      fontFamily: 'Baskerville',
    }
  });

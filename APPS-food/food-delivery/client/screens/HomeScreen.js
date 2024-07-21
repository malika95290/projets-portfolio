import { View, Text, TextInput, ScrollView, TouchableOpacity } from 'react-native'
import React, { useEffect, useState } from 'react'
import { SafeAreaView } from 'react-native-safe-area-context'
import { StatusBar } from 'expo-status-bar'
import * as Icon from "react-native-feather";
import { themeColors } from '../theme/theme';
import Categories from '../components/categories';
import FeaturedRow from '../components/featuredRow';
import { featured } from '../constants'
import { getFeaturedRestaurants } from '../api';

export default function HomeScreen() {

    const [featuredRestaurants, setFeaturedRestaurants] = useState([]);

    useEffect(()=>{
        getFeaturedRestaurants().then(data=>{
            setFeaturedRestaurants(data);
        })
    })
  return (
    <SafeAreaView className="bg-white">
        <StatusBar barStyle="dark-content"/>
        {/* Search Bar */}
        <View className="flex-row items-center space-x-2 px-4 pb-2">
            <View className='flex-row flex-1 items-center p-3 rounded-full border border-gray-300'>
                <Icon.Search width="25" height="25" stroke="grey"/>
                <TextInput placeholder="Restaurants" className="ml-2 flex-1"/>
                <View className="flex-row items-center space-x-1 border-0 border-l-2 pl-2 border-l-gray-300">
                    <Icon.MapPin height="20" width="20" stroke="grey"/>
                    <Text className="text-gray-600">Paris, 75006</Text>
                </View>
            </View>
            <View style={{backgroundColor:themeColors.bgColor(1)}} className="p-3 rounded-full">
                <Icon.Sliders height="20" idth="20" strokeWidth={2.5} stroke="white"/>
            </View>
        </View>

        {/* Main */}
        <ScrollView showsVerticalScrollIndicator={false}
            contentContainerStyle={{
                paddingBottom : 20
            }}
        >
        {/* Catégories */}
            <Categories/>

        {/* Featured */}
        <View className="mt-5">
            {
                featuredRestaurants.map((item,index)=>{
                    return(
                        <FeaturedRow
                            key={index}
                            title={item.name}
                            restaurants={item.restaurants}
                            description={item.description}
                        />
                    )
                })
            }
        </View>

        </ScrollView>
    </SafeAreaView>
  )
}
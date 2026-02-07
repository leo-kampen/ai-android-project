package com.example.ai_proj_test1

import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.ai_proj_test1.ui.HomeScreen
import com.example.ai_proj_test1.ui.SecondScreen

@Composable
fun NavGraph() {
    val navController = rememberNavController()
    NavHost(navController = navController, startDestination = "home") {
        composable("home") {
            HomeScreen(onNext = { navController.navigate("second") })
        }
        composable("second") {
            SecondScreen(onBack = { navController.popBackStack() })
        }
    }
}

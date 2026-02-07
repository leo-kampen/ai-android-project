package com.example.ai_proj_test1

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import com.example.ai_proj_test1.NavGraph
import com.example.ai_proj_test1.ui.theme.Ai_proj_test1Theme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            Ai_proj_test1Theme {
                NavGraph()
            }
        }
    }
}
# NeuroticSnake
Deep Q learning neural network to play snake game  
  
11-256-3, input-hidden-output  
output: straight, left, right (pick highest activated neuron)  

loss: mean squared error  

reward:  
+10 when eat food  
-10 when die  
+0 else  
  
input: [  
danger_right, danger_left, danger_forward,  
direction_right, direction_up, direction_down, direction_left,  
food_right, food_up, food_down, food_left  
]  
  
Agent: trains the model  
Game: snake game  
Model: linear q net  
  
Uses bellman-equation  
Gradually lower gamma so that we value exploration highly at first and gradually switch to exploitation  
  
To keep things simple the state is simply based on the exact step, like moving one block in the game, and not about cumulative reward  

All thanks to Vijay and Patrick Loeber!

# Evolve To Find The Bitcoin
 A visulization of a simple evolutionary algorithm where little cartoon humans try to locate a bitcoin.
 
# What I Learnt
<ol>
 <li>Implemented a simple evolutionary algorithm. Each human is given a brain object that contains a random list of 2D vectors that the human will travel sequentially. Once all the humans have traveled every distance contained in their brain or they have all died the fitness of the generation is calculated and the best human is selected for breeding. The algorithm uses two seperate fitness functions. The first is implemented while the humans haven't yet located the bitcoin and is calculated by taking the inverse of the distance between the human and the bitcoin. The second fitness function activates once the bitcoin has been located and is calculated based on the time taken to reach the bitcoin. Once the best human is selected a new generation is created by cloning this human and then the new popultion is mutated. To mutate humans in the new generation certain directions in their brains get overwritten with a new random direction. The amount of directions that get overwritten depend on a mutation rate set within the program.</li>
 <li>Used pygame python module to develope visual interface.</li>
</ol>

# User Instructions
<ol>
 <li>Clone repository onto your local computer.</li>
 <li>You will need to create a python environment with the pygame module installed and activate it.</li>
 <li>Once the environment is active run the game.py file located in the human-code folder.</li>
 <li>To toggle between the three levels use the keyboard keys "1", "2", and "3".</li>
 <li>To start the algorithm hit the spacebar.</li>
 <li>To stop the algorithm hit the spacebar again.</li>
</ol>

# Visulation Preview
https://youtu.be/yxlrF3kI0aw

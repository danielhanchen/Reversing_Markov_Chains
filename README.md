# Reversing_Markov_Chains

Sometimes we want to ”reverse” a Markov Chain process. Taking the inverse of the transition matrix allows this to work, but the inverse result is not a transition matrix. 

If I wanted to model a population going to work, and then going back home, negative and greater than 1 probabilities in the inverse matrix will cause issues. I propose a method to compute the ”inverse” of a transition matrix, and the result is still a transition matrix

# Applications of Process

I wanted a reverse Markov process, as I was modelling how a disease
spread through a population. I had computed probabilistic movements for
2transiting people, but the problem was that I didn’t want to compute night
and day cycles separately (it would be too much work). 

So instead, I wanted to find a method to reverse my transition matrix to account for day and night
cycles. Inverse couldn’t work, as I needed real probabilities. So, I decided
to make a new method.

This process can be used to do less work when modelling Markov systems.
If you want to model mass gatherings, and then they had to go back home
after some event, you can reverse the processes easily using this technique.

Likewise, if you wanted to somehow find what a reversed system or
”inversed” Markov process would look like, you can use this method to go
”backwards” in time.

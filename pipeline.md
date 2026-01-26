# Pipeline

1) make available at least two models **VV**
2) create a script that requests the Morpheus api only for the words having  Conflicts **VV**
3) in the same script, add a part in which these results provided by Morpheus are compared to probabilistic results of the two models
4) make a statatistic of how many cases this approach resolved, insted of leaving blank the fields

**First version** 
This draft script deals with only major conflicts (verb, noun, adj, pronoun, conj, adverbs, particles) that do not have inside minor conflicts. Up to now, only a model gives its proposals. In the future, this aims to manage major conflicts, major conflicts with minor conflicts inside, minor conflicts and it will exploits the proposals of two or three models. 



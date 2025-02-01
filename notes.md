# IQuHack IONQ challenge

## Problems to solve
--------------------

- odd vs even vertices
- parameterization of symmetry
- We need to adjust the ansatz generator and see if the score improves. How can the ansantz generator work better?

## Rationale
------------

## Ideas
-------

- Maximizing the number of cuts will give us a minimum energy state.
- equal cardinality means that the two groups have to have even number. cardinality is just the number of vertices.
- pure max cut has no constraint. Balanced max cut needs to not have unbalanced states. Connected max cut, each sub graph can't have an island that isn't connected to anything.
    - Need to add extra terms into the hamiltonian that will penalized any states that are unbalanced. This will add energy to the states we don't want.
- We can translate the Hamiltonian into a quantum circuit and evolve it with time.
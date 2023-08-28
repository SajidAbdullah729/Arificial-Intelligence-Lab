male(shuvo).
male(sumon).
male(nirjoy).
male(ripon).
male(mahim).
male(jewel).
male(rashid).
male(jasim).
male(sakib).



female(rima).
female(suma).
female(rabeka).
female(rani).
female(nodi).



parent('sumon','rima').
parent('sumon','nirjoy').
parent('rani','ripon').
parent('rani','suma').
parent('jasim','rakib').
parent('mahim','rima').
parent('mahim','rabeka').
parent('rashid','jasim').
parent('shuvo','sumon').
parent('shuvo','rani').
parent('rima','sakib').
parent('nirjoy','nodi').



father(X,Y):-parent(X,Y),male(X).
mother(X,Y):-parent(X,Y),female(X).
sibling(X,Y):-parent(Z,X),parent(Z,Y),X\=Y.
brother(X,Y):-sibling(X,Y),male(X).
sister(X,Y):-sibling(X,Y),female(X).



uncle(X,Y):-brother(X,Z),parent(Z,Y),male(X).
aunt(X,Y):-sister(X,Z),parent(Z,Y),female(X).


grandparent(X,Z):-
	parent(X,Y),parent(Y,Z).

findGp:-
	write('enter the grand child name: '),read(Gchild),write('enter the grand parent name: '),read(Gparent),grandparent(Gparent,Gchild),write(Gparent),tab(5),
	fail.
findGp.


findBr:-
	write('name :'),read(Y),brother(Br,Y),
	write(Br),tab(5),fail.
findBr.

findSister:-
	write('name:'),read(C),sister(X,C),write(X),tab(5),fail.
findSister.

findAunt:-write('name:'),read(Y),aunt(X,Y),write(X),tab(5),fail.
findAunt.

findUncle:-write('name:'),read(Y),uncle(X,Y),write(X),tab(5),fail.
findUncle.





% Facts about students
student(varnit_b).
student(ramneek_s).
student(kevin_g).
student(anirudh_s).

% Course enrollments
enrolled(varnit_b, cse_class).
enrolled(ramneek_s, cse_class).
enrolled(kevin_g, cse_class).
enrolled(anirudh_s, cse_class).

% Additional facts about interests
likes_coding(varnit_b).
likes_coding(kevin_g).
likes_gaming(ramneek_s).
likes_gaming(anirudh_s).

% Rules
% Rule to determine if someone is a programmer
programmer(X) :- student(X), likes_coding(X).

% Rule to determine if someone is a gamer
gamer(X) :- student(X), likes_gaming(X).

% Rule to determine if two students are classmates
classmates(X, Y) :- 
    student(X), 
    student(Y), 
    X \= Y,
    enrolled(X, Course), 
    enrolled(Y, Course).

% Rule to identify study buddies (classmates who share interests)
study_buddies(X, Y) :- 
    classmates(X, Y),
    ((likes_coding(X), likes_coding(Y));
     (likes_gaming(X), likes_gaming(Y))).

% Test queries
test_queries :-
    write('Testing queries:'), nl,
    write('Is Varnit a student?'), nl,
    (student(varnit_b) -> write('Yes') ; write('No')), nl,
    write('Is Varnit a programmer?'), nl,
    (programmer(varnit_b) -> write('Yes') ; write('No')), nl,
    write('Are Varnit and Kevin study buddies?'), nl,
    (study_buddies(varnit_b, kevin_g) -> write('Yes') ; write('No')), nl.

% Run test
:- test_queries.
CREATE TABLE athletes (
    id integers,
    names text,
    sex text,
    weight integers,
);

CREATE TABLE age(
    id integers,
    age integers,
    height integers,
);

CREATE TABLE events(
    id integers,
    events text,
    sports text,
    season text,
);



CREATE TABLE NOC (
    id integers,
    NOC text,
    region text,
);

CREATE TABLE athletes_age (
    id integers,
    athletes_id integers,
    age_id integers,
    years integers,
    team text,
    city text,

);

CREATE TABLE athletes_age_games_noc(
    athletes_age_id integers,
    NOC_id integers,
    events_id integers,
    medal text,
);


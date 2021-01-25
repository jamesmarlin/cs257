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

CREATE TABLE games(
    id integers,
    sport text,
    games text,
    medal text,
    team text,
    event text,
    city text,
);

CREATE TABLE NOC (
    id integers,
    NOC text,
    region text,
);

CREATE TABLE athletes_age_games_noc(
    athletes_id integers,
    age_id integers,
    games_id integers,
    NOC_id integers,
)


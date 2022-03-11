-- upgrade --
ALTER TABLE "guest" ADD "coming" BOOL NOT NULL  DEFAULT False;
ALTER TABLE "guest" ADD "travel_needs" VARCHAR(65535) NOT NULL;
ALTER TABLE "guest" ADD "email" VARCHAR(255) NOT NULL;
CREATE TABLE IF NOT EXISTS "mealtype" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(64) NOT NULL
);;

CREATE TABLE IF NOT EXISTS "meal" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "type_id" INT NOT NULL REFERENCES "mealtype" ("id") ON DELETE CASCADE
);;
CREATE TABLE "guest_guest" ("guest_rel_id" UUID NOT NULL REFERENCES "guest" ("id") ON DELETE CASCADE,"guest_id" UUID NOT NULL REFERENCES "guest" ("id") ON DELETE CASCADE);
-- downgrade --
DROP TABLE IF EXISTS "guest_guest";
ALTER TABLE "guest" DROP COLUMN "coming";
ALTER TABLE "guest" DROP COLUMN "travel_needs";
ALTER TABLE "guest" DROP COLUMN "email";
DROP TABLE IF EXISTS "meal";
DROP TABLE IF EXISTS "mealtype";

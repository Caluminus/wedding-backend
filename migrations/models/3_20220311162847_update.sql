-- upgrade --
ALTER TABLE "guest" ALTER COLUMN "travel_needs" DROP NOT NULL;
-- downgrade --
ALTER TABLE "guest" ALTER COLUMN "travel_needs" SET NOT NULL;

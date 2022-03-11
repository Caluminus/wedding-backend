-- upgrade --
CREATE extension IF NOT EXISTS "uuid-ossp";
ALTER TABLE guest ALTER id SET DEFAULT uuid_generate_v4();
-- downgrade --
ALTER TABLE guest ALTER id SET DEFAULT NULL;
DROP extension IF EXISTS "uuid-ossp"; 
---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/setting-up-the-destination-database-for-use-with-oracle-goldengate.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Setting up the destination database for use with Oracle GoldenGate
<a name="setting-up-the-destination-database-for-use-with-oracle-goldengate"></a>

 The following steps must be performed on the target database for GoldenGate replication to work. These steps are the same for both Amazon RDS and Oracle Database on Amazon EC2.

1.  Create a GoldenGate user account on the destination database.

1.  Grant the necessary privileges that are listed in the following example to the GoldenGate user:

```
CREATE SESSION
ALTER SESSION
CREATE CLUSTER
CREATE INDEXTYPE
CREATE OPERATOR
CREATE PROCEDURE
CREATE SEQUENCE
CREATE TABLE
CREATE TRIGGER
CREATE TYPE
SELECT ANY DICTIONARY
CREATE ANY TABLE
ALTER ANY TABLE
LOCK ANY TABLE
SELECT ANY TABLE
INSERT ANY TABLE
UPDATE ANY TABLE
DELETE ANY TABLE
```

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/setting-up-the-source-database-for-use-with-oracle-goldengate.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Setting up the source database for use with Oracle GoldenGate
<a name="setting-up-the-source-database-for-use-with-oracle-goldengate"></a>

 To replicate data to the destination database in AWS, you need to set up a source database for GoldenGate. Use the following procedure to set up the source database. This process is the same for both Amazon RDS and Oracle Database on Amazon EC2.

1.  Set the compatible parameter to the same as your destination database (for Amazon RDS as the destination).

1.  Enable supplemental logging and force logging.

1.  Verify the database is in `archivelog` mode.

1.  Set `ENABLE_GOLDENGATE_REPLICATION` parameter to `TRUE`.

1.  Set the retention period for archived redo logs for the GoldenGate source database.

1.  Create a GoldenGate user account on the source database.

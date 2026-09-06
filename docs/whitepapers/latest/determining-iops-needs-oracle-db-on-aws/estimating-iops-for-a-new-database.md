---
source_url: https://docs.aws.amazon.com/whitepapers/latest/determining-iops-needs-oracle-db-on-aws/estimating-iops-for-a-new-database.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Estimating IOPS for a new database
<a name="estimating-iops-for-a-new-database"></a>

 If you are setting up a database for the first time on AWS and you don’t have any existing statistics, you can use an IOPS number based on the expected number of application transactions per second. Though the IOPS necessary per transaction can vary widely—based on the amount of data involved, the number of queries in a transaction, and the query complexity—generally, 30 IOPS per transaction is a good number to consider.

 For example, if you are expecting 100 transactions per second, you can start with 3,000 IOPS Amazon EBS volumes. Because the amount of data in a new database is usually small, changing the IOPS associated with Amazon EBS will be relatively simple whether your database is on Amazon RDS or Amazon EC2.

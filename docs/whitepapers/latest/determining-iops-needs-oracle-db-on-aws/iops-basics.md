---
source_url: https://docs.aws.amazon.com/whitepapers/latest/determining-iops-needs-oracle-db-on-aws/iops-basics.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# IOPS basics
<a name="iops-basics"></a>

 IOPS is the standard measure of I/O operations per second on a storage device. It includes both read and write operations. The amount of I/O used by Oracle Database can vary greatly in a time period, based on the server load and the specific queries running. If you are migrating an existing Oracle Database to AWS, to ensure that you get the best performance regardless of load, you must determine the peak IOPS used by your database and provision Amazon EBS volumes on AWS accordingly. If you choose an IOPS number based on the average IOPS used by your existing database, you should have sufficient IOPS for the database in most cases, but database performance will suffer at peak load. You can mitigate this issue to some extent by using Amazon EBS `gp2` volumes, which have the ability to burst to higher IOPS for small periods of time.

 Customers sometimes assume that they need much more IOPS than they actually do. This assumption occurs if customers confuse storage system IOPS with database IOPS. Most enterprises use storage area network (SAN) systems that can provide 100,000–200,000 or more IOPS for storage. The same SAN storage is usually shared by multiple databases and file systems, which means the total IOPS provided by the storage system is used by many more applications than a single database.

 Most Oracle Database production systems in domains such as enterprise resource planning (ERP) and customer relationship management (CRM) are in the range of 3,000–30,000 IOPS. Your individual application might have different IOPS requirements. A performance test environment’s IOPS needs are generally identical to those of production environments, but for other test and development environments, the range is usually 200–2,000 IOPS.

 Some online transaction processing (OLTP) systems use up to 60,000 IOPS. There are Oracle databases that use more than 60,000 IOPS, but that is unusual. If your environment shows numbers outside these parameters, you should complete further analysis to confirm your numbers.

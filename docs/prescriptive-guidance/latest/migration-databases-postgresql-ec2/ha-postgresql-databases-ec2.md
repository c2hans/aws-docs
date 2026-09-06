---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/ha-postgresql-databases-ec2.html
---

# Setting up high availability
<a name="ha-postgresql-databases-ec2"></a>

As a best practice, we recommend that you set up high availability and disaster recovery (HADR) for your PostgreSQL database on Amazon EC2. You can use replication mechanisms that are native to PostgreSQL to set up HADR and data protection for your PostgreSQL database on Amazon EC2. The following options are available in PostgreSQL:
+ Physical replication
+ Logical replication
+ Patroni and etcd

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/editions-versions.html
---

# Editions and versions
<a name="editions-versions"></a>

In addition to choosing your licensing model, you need to choose the edition that supports your database requirements. Amazon RDS for Oracle supports the following options:
+ Oracle Database Enterprise Edition (EE) is the most common choice for production workloads in many large organizations and enterprises. EE provides key features for mission-critical applications, including Active Data Guard and Oracle Partitioning.
+ Oracle Database Standard Edition 2 (SE2) is an affordable database and supports a variety of use cases, from small business single-server environments to highly distributed branch environments. SE2 can be licensed on servers with a maximum of two sockets. However, the core counts per two-socket server can increase over time without impacting your license obligation. With Oracle Database SE2, your license costs remain the same regardless of the number of cores in the socket. Currently AWS supports up to 16 virtual CPUs (vCPUs).

From the aspect of license cost, Oracle Database SE2 is much less expensive than EE. If your application uses very few or none of the EE features, consider downgrading from EE to SE2. For more information, see the [Evaluate downgrading Oracle databases to Standard Edition 2 on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/welcome.html) guide.

For more details about the availability of features, options, and management packs in different editions, see the [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/dblic/Licensing-Information.html#GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87).

Each replatform option supports different Oracle editions. The following table lists the latest support information.

|
|
| Editions and versions | Amazon RDS for Oracle | Amazon RDS Custom for Oracle |
| --- |--- |--- |
| Enterprise Edition | Yes | Yes |
| Standard Edition 2 | Yes | Yes |
| Versions | 19c<br />21c | 12.1.0.2<br />12.2.0.1<br />18c<br />19c |

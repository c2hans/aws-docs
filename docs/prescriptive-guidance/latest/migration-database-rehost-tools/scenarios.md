---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-database-rehost-tools/scenarios.html
---

# Migration scenarios
<a name="scenarios"></a>

Migration scenarios can be differentiated based on scale (how many servers or applications are involved), migration time (how fast it must be done), and length of downtime allowed during cutover. These considerations affect the choice of AWS services to best support the migration.
+ A large-scale migration (such as a full data center exit) includes multiple business units, and many applications and their databases. These typically have a tight time frame or a fixed deadline (such as completion before the closure of the data center) but less strict downtime limitations, which allow for longer cutover windows.
+ A large but less complex migration of a business unit or an enterprise group might also involve multiple applications. However, these might have a more flexible timeline and sometimes stricter downtime requirements (shorter cutover windows).
+ The migration of a single, large, business-critical application usually includes a highly intensive database server or a cluster, such as an online transaction processing (OLTP) database that handles a large number of transactions. These migrations typically require minimal or near zero downtime during the cutover window.

The migration requirements for these use cases range from moving at the fastest possible pace, which is generally associated with the most downtime, to maximum granularity and the closest attention to details, which generally support the least possible downtime during the migration. Most migrations represent some combination of these factors.

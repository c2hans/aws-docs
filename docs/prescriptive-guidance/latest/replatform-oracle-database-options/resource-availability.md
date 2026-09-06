---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/resource-availability.html
---

# Resource availability
<a name="resource-availability"></a>

Your replatforming choice might depend on the AWS Region you are using and the resources required by your business. Both Amazon RDS for Oracle and Amazon RDS Custom for Oracle use AWS services, but not all of the services are available in all AWS Regions. AWS services also vary in supported engine versions and instance classes. Amazon RDS for Oracle provides more choices in AWS Regions and instance classes than Amazon RDS Custom for Oracle. This is because Amazon RDS Custom for Oracle is still in the process of expanding.

It's also important to consider scaling needs. The AWS BYOL model is based on CPU cores. After you create an Amazon RDS for Oracle instance, you cannot change the DB instance class to a different number of cores unless the change is agreed to by the Oracle license policy. However, the AWS License Included model gives you the flexibility to dynamically change the number of cores by scaling the instance class up and down.

|
|
|  Resource availability | Amazon RDS for Oracle | Amazon RDS Custom for Oracle |
| --- |--- |--- |
| AWS Region | [Most](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html#Concepts.RegionsAndAvailabilityZones.Regions) | [Limited](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.html#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.ora) |
| DB instance class | [Most](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.InstanceClasses.html) | [Limited](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits.html#custom-reqs-limits.instances) |
| CPU scalability | License Included model | Not available |

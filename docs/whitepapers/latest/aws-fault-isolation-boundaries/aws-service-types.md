---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/aws-service-types.html
---

# AWS service types
<a name="aws-service-types"></a>

 AWS operates three different categories of services based on their fault isolation boundary: zonal, Regional, and *global*. This section describes in more detail how these different types of services have been designed so that you can determine how failures within a service of a certain service type might impact your application running on AWS. It also provides high-level guidance on how to architect your applications to use these services in a resilient way.

**Topics**
+ [Zonal services](zonal-services.md)
+ [Regional services](regional-services.md)
+ [Global services](global-services.md)

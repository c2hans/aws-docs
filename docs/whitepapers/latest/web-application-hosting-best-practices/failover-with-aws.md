---
source_url: https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/failover-with-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Failover with AWS
<a name="failover-with-aws"></a>

Another key advantage of AWS over traditional web hosting is the [Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) that give you easy access to redundant deployment locations. Availability Zones are physically distinct locations that are engineered to be insulated from failures in other Availability Zones. They provide inexpensive, low-latency network connectivity to other Availability Zones in the same [AWS Region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions). As the AWS web hosting architecture diagram shows, AWS recommends that you deploy EC2 hosts across multiple Availability Zones to make your web application more fault tolerant.

It’s important to ensure that there are provisions for migrating single points of access across Availability Zones in the case of failure. For example, you should set up a database standby in a second Availability Zone so that the persistence of data remains consistent and highly available, even during an unlikely failure scenario. You can do this on Amazon EC2 or Amazon RDS with the click of a button.

While some architectural changes are often required when moving an existing web application to the AWS Cloud, there are significant improvements to scalability, reliability, and cost-effectiveness that make using the AWS Cloud well worth the effort. The next section discusses those improvements.

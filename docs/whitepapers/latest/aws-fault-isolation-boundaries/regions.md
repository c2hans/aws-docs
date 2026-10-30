---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/regions.html
---

# Regions
<a name="regions"></a>

 AWS also has the concept of Regions, which are geographical locations around the world where we cluster data centers. Each Region is composed of multiple independent and physically separate Availability Zones. Public AWS Regions are built with at least three Availability Zones. AWS Region physical infrastructure and software services are isolated and independent from other Regions with a few exceptions noted later in this document. This separation between Regions limits service failures, when they occur, to a single Region. Other Regions’ normal operations are unaffected in this case. The resources and data that you create in one Region don’t exist in any other Region unless you explicitly use a replication or copy feature offered by an AWS service or replicate the resource yourself. AWS Regions are interconnected through the AWS Global Network, which provides private connectivity through over 9 million kilometers of terrestrial and subsea fiber-optic cabling. This provides resilient, high-bandwidth, low-latency connectivity to customers and applications globally. The following figure shows AWS Regions around the world.

![AWS Regions around the world.](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/images/new-regions-map.png)

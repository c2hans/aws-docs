---
source_url: https://docs.aws.amazon.com/whitepapers/latest/using-power-bi-with-aws-cloud/connecting-to-data-sources-through-the-internet.html
---

# Connecting to data sources through the internet
<a name="connecting-to-data-sources-through-the-internet"></a>

 In this model, the Power BI Desktop application places an outbound connection that is routed over the internet to an IP address of an internet-accessible AWS data source. For example, Amazon RDS and Amazon Redshift, which are instantiated within a customers’ Amazon Virtual Private Cloud (Amazon Amazon VPC), support the *public accessibility* option to make instances accessible over the internet. Amazon Athena can be queried directly from the internet by using the service endpoint for your specific Region.

![A diagram depicting Power BI connectivity to AWS data sources over the internet.](http://docs.aws.amazon.com/whitepapers/latest/using-power-bi-with-aws-cloud/images/powerbi2.png)

*Power BI connectivity to AWS data sources over the internet *

 Although this method of connectivity is technically possible, we don’t recommend it for anything other than a small number of users. The following table lists important considerations.

* Table 1 — Considerations for accessing AWS data sources over the internet *

|  Criteria  |  Considerations for accessing AWS data sources over the internet  |
| --- | --- |
|  Network connectivity  | Data sources are available by connecting to private IP addresses in a VPC, or using a regional or VPC service endpoint. Power BI Desktop connects via VPN and either accesses data sources directly (Amazon RDS, Amazon Redshift, Amazon EC2-based data sources), or for services with a regional endpoint (Amazon Athena) by using a private VPC endpoint or the regional endpoint, depending on the DNS configuration. |
|  Security  | **IP access control** <br />A *security group* acts as a virtual firewall for your instance to control inbound and outbound traffic. In order to limit access to trusted entities, configure security groups to only allow inbound IP ranges associated with known Classless Inter-Domain Routing (CIDR) ranges. <br />**Encryption in transit** <br />AWS recommends that you configure encryption for any data sources that use public IP addresses, such as Amazon RDS, Amazon Redshift, or any Amazon EC2-based data sources. This ensures that the risk of data or credentials being compromised while in transit, is reduced. Failure to configure encryption represents a significant risk. Do not overlook this aspect. <br />Regional service endpoints, such as Amazon Athena, are TLS encrypted. In addition, Amazon Athena query results that stream to JDBC or ODBC clients are encrypted using Transport Layer Security (TLS). <br />**Authentication and authorization** <br />AWS recommends that you use credentials that provide read-only access to datasets, and set up processes to rotate credentials per your company policy.  |
|  Performance  | Some factors that might impact the overall Power BI Desktop performance when accessing AWS data sources over the internet include: +   The size of the dataset being accessed. Larger datasets take longer to retrieve. We recommend limiting queries and using filters to reduce the amount of data retrieved over the internet.  <br />+   The quality of the internet connection, including bandwidth, latency, and packet loss. Where possible, access data in AWS Regions which you are geographically close to in order to reduce the effect of latency. If your internet is shared, consider loading data sources at off peak times and ensuring that enough bandwidth is available.  <br />In general, AWS recommends testing the experience at different times of the day, with different datasets, and with progressively larger number of users.  |
|  Cost  | Data sources that reside in a VPC and are queried using public IP address over the internet incur standard Amazon VPC data egress charges. In order to reduce costs, we recommend limiting queries and using filters to reduce the amount of data retrieved over the internet.  |

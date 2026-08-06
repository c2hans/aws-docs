---
source_url: https://docs.aws.amazon.com/whitepapers/latest/using-power-bi-with-aws-cloud/connecting-to-data-sources-via-aws-vpn.html
---

# Connecting to data sources via Site-to-Site VPN
<a name="connecting-to-data-sources-via-aws-vpn"></a>

In this model, Power BI Desktop installations connect to data sources in the AWS network using one of two Site-to-Site VPN methods: AWS Site-to-Site VPN or AWS Client VPN. Each connection type delivers a highly available, managed, and elastic cloud VPN solution to protect your network traffic.

Site-to-Site VPN creates encrypted tunnels between your network and your AWS VPN or AWS Transit Gateway. Client VPN connects your users to AWS or on-premises resources using a free VPN software client.

VPN traffic from both Site-to-Site VPN and Client VPN connections stops in your VPC. As such, it can route to private IP addresses so your instances no longer need public-facing IP addresses. For services with a data path accessible from a publicly facing service endpoint, such as Athena, these service requests can either be routed over the internet, or over the VPN connection and through a VPC endpoint.

![A diagram depicting how Power BI Desktop connects to AWS data sources over Site-to-Site VPN and Client VPN.](http://docs.aws.amazon.com/whitepapers/latest/using-power-bi-with-aws-cloud/images/powerbi3.png)

*Connecting Power BI Desktop to AWS data sources over Site-to-Site VPN and Client VPN*

 Site-to-Site VPN can also connect to AWS Transit Gateway, facilitating access to data sources spread across multiple VPCs.

 Using Site-to-Site VPN provides the benefit of employing encryption when accessing data sources stored in AWS, without requiring that each data source to be explicitly configured. Once configured, VPN technology is largely seamless to end users.

* Table 2 — Considerations for accessing AWS data sources using Site-to-Site VPN *

|  Criteria  |  Considerations for accessing AWS data sources using Site-to-Site VPN  |
| --- | --- |
|  Network connectivity  | Data sources are available by connecting to private IP addresses in a VPC, or using a regional or VPC service endpoint. Power BI Desktop connects via VPN and either access data sources directly (Amazon RDS, Amazon Redshift, Amazon EC2-based data sources), or for services with a regional endpoint (Amazon Athena) by using a private VPC endpoint or the regional endpoint, depending on the DNS configuration.  |
|  Security  | IP access controlYou can use a combination of routing and security groups to control access to data sources stored in the AWS Cloud. <br />**Encryption in transit** <br />Both types of Site-to-Site VPN use [IPsec](https://en.wikipedia.org/wiki/IPsec) encryption, meaning that data transferred is encrypted as it travels between AWS and on premises. This ensures that even if data sources are not configured to use encrypted communications, that data is protected while traversing the internet. <br />**Authentication** <br />Site-to-Site VPN requires a one-time configuration and, once established, is seamless to users. End users are not required to authenticate to use the Site-to-Site VPN, but they require authentication to data sources. <br />On the other hand, Client VPN does require authentication by the end users in order to establish the connection. Client VPN authentication can take place via Active Directory (user-based), mutual authentication (certificate-based), or SAML SSO (user-based). Once authenticated, the connection is seamless to the end user. AWS data sources added to Power BI Desktop require authentication. <br />AWS recommends that you authenticate with AWS data sources using an identity that has read-only access only to the datasets required.  |
|  Performance  | The use of Site-to-Site VPN occurs over the internet. As such, its performance envelope is similar to the first scenario presented. Some factors can impact the overall Power BI Desktop performance when accessing AWS data sources over the internet. They include: +   The size of the dataset being accessed. Larger datasets take longer to retrieve. We recommend limiting queries and using filters to reduce the amount of data retrieved over the internet.  <br />+   The quality of the internet connection, including bandwidth, latency, and packet loss. Where possible, access data in AWS Regions that you are geographically close to. This reduces the effect of latency. If your internet is shared, consider loading data sources at off-peak times and/or ensuring that enough bandwidth is available.  <br />In general, AWS recommends testing the experience at different times of the day, with different datasets, and with progressively larger number of users.  |
|  Cost  | Data sources that reside in a VPC and are queried using Site-to-Site VPN incur standard Site-to-Site VPN data transfer charges. To reduce costs, we recommend limiting queries and using filters to reduce the amount of data retrieved over the internet.  |

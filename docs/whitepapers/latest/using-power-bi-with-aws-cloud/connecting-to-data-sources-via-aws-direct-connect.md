---
source_url: https://docs.aws.amazon.com/whitepapers/latest/using-power-bi-with-aws-cloud/connecting-to-data-sources-via-aws-direct-connect.html
---

# Connecting to data sources via AWS Direct Connect
<a name="connecting-to-data-sources-via-aws-direct-connect"></a>

AWS Direct Connect links your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an AWS Direct Connect router. With this connection, you can create virtual interfaces directly to public AWS services (for example, to Amazon S3) or to Amazon VPC, bypassing internet service providers in your network path. An AWS Direct Connect location provides access to AWS in the Region with which it is associated. You can use a single connection in a public Region or AWS GovCloud (US) to access public AWS services in all other public Regions.

In this model, the customer’s on-premises network is connected through AWS Direct Connect directly to the AWS network. While there are multiple methods for configuring AWS Direct Connect, in its simplest mode, you are given access to IP ranges within a VPC using a construct known as a private virtual interfaces (private VIF). You access to the internet/public IP ranges using a public virtual interface (public VIF).

![A diagram depicting Power BI Desktop connecting to AWS data sources over AWS Direct Connect](https://docs.aws.amazon.com/whitepapers/latest/using-power-bi-with-aws-cloud/images/powerbi4.png)

*Connecting Power BI Desktop to AWS data sources over AWS Direct Connect *

 When adding data sources in Power BI, you select the private IP address if it’s located in a VPC, or a private VPC endpoint for the service, depending on how your DNS is configured.

* Table 3 — Considerations for accessing AWS data sources using AWS Direct Connect *

|  Criteria  |  Considerations for accessing AWS data sources using AWS Direct Connect  |
| --- | --- |
|  Network connectivity  | After you configure Direct Connect, it can access data sources by connecting to private IPs in a VPC, or by using a regional service endpoint.  |
|  Security  | **IP access control** <br />You can use a combination of routing and security groups to control access to data sources stored in the AWS Cloud. <br />**Encryption in transit** <br />Direct Connect does not provide line-level encryption of data. We recommend that you either enable TLS encryption at the data source level, or combine Site-to-Site VPN with Direct Connect to ensure that data and credentials are not compromised during transmission. <br />**Authentication** <br />Direct Connect does not require any additional authentication once configured. <br />AWS recommends that you authenticate AWS data sources using an identity that has read-only access only to the datasets required.  |
|  Performance  | With Direct Connect, 1 Gbps and 10 Gbps ports are available. You can order speeds of 50 Mbps, 100 Mbps, 200 Mbps, 300 Mbps, 400 Mbps, and 500 Mbps from any APN Partners that support Direct Connect. <br />When compared to internet-based connections, Direct Connect connections typically provide increased bandwidth and reduced latency. Depending on the capacity of the connection, Power BI Desktop performance might no longer be constrained by the network when loading data sources. As such, when accessing datasets in the same Region that the Direct Connect is associated to, your users can expect good performance for queries. <br />Be mindful of loading large datasets, and note that Power BI Desktop has a 10 GB dataset limit.  |
|  Cost  | In addition to standard Direct Connect port charges, data sources that are accessed using a Direct Connect connection incur standard Direct Connect data transfer charges, as explained in [AWS Direct Connect pricing](https://aws.amazon.com/directconnect/pricing/). Data sent to the AWS Cloud over Direct Connect does not incur any charges. <br />To reduce costs, AWS recommends limiting queries and using filters to reduce the amount of data retrieved.  |

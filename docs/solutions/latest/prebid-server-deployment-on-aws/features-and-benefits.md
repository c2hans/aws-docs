---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

Guidance for Deploying a Prebid Server on AWS provides the following features:

 **Prebid Server purpose built for AWS infrastructure**

Deploy Prebid Server in a scalable and cost-efficient manner. It provides the end-to-end infrastructure to host a Prebid Server with production-grade availability, scalability, and low-latency for a variety of request loads (documented up to 100,000 RPS).

 **Built-in observability**

Observability is available throughout the infrastructure. This includes operational resource metrics, alarms, runtime logs, and business metrics.

 **Decrease time to market**

This solution uses a deployment template to establish the necessary infrastructure to get customers running within days instead of months or weeks.

 **Ownership of all operational and business data**

All data from Prebid Server metrics extract, transform, and load (ETL) to AWS Glue Data Catalog for seamless integration with various clients, such as Amazon Athena, Amazon Redshift, and Amazon SageMaker AI.

 **AWS RTB Fabric integration**

Optionally route bid requests through [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/), a private network purpose-built for real-time bidding. RTB Fabric provides low-latency, cost-optimized connectivity between Prebid Server and bidder endpoints without traversing the public internet.

 **Quick start with bidder simulator**

Deploy an optional bidder simulator stack to quickly test and validate your Prebid Server deployment without needing to configure external bidders. The simulator supports banner and video ad formats, including VAST instream video.

 **Demo website**

Demo website with Prebid.js integration can be used to validate the end-to-end flow from prebid.js through Prebid Server to the bidder simulator.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

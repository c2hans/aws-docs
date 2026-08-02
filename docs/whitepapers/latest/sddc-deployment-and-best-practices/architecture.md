---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Architecture
<a name="architecture"></a>

 This is a high-level overview architecture.

![A diagram that depicts the high-level architecture of the VMware Cloud on an AWS managed account connected to a customer owned AWS account.](http://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/images/region.png)

 This paper covers key preparation steps, associated resources, and deployment instructions to guide you through deployment of your first SDDC environment within your chosen [Region and Availability Zone](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/). This includes the following:
+  Creating a single Virtual Private Cloud (VPC) within your AWS account
+  Planning and provisioning a private subnet network within your chosen Availability Zone (AZ) for SDDC integration
+  Activating the VMware Cloud on the AWS service
+  Deployment of a non-stretched SDDC within a single AZ

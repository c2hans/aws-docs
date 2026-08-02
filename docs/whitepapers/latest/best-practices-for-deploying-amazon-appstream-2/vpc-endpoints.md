---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/vpc-endpoints.html
---

# VPC endpoints
<a name="vpc-endpoints"></a>

## Amazon S3 VPC endpoint
<a name="amazon-s3-vpc-endpoint"></a>

 Many Amazon WorkSpaces Applications deployments require user state persistence through home folders and application settings. Enable private communication to these [https://aws.amazon.com/s3/](https://aws.amazon.com/s3/) (Amazon S3) locations, as this avoids using the public internet. You can achieve this through a VPC endpoint gateway. A VPC endpoint gateway is preferred over the [https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) because:
+  It is cost optimized for WorkSpaces Applications network access requirements
+  Amazon S3 bucket access is not required from on-premises resources
+  A custom policy document can be used to restrict access only from the WorkSpaces Applications instances

 Once you create the VPC endpoint gateway, it is a best practice to secure the privatized connection by creating a [https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-vpce-iam-policy.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-vpce-iam-policy.html). Custom policy starts with the Amazon Resource Name (ARN) of the WorkSpaces Applications service Identity and Access Management role. Explicitly specify the S3 actions required for user state persistence.

**Note**
The following example in the `Resources` section specifies the state home folder path first and the applications settings path second.

**Example**

## Amazon WorkSpaces Applications API interface VPC endpoint
<a name="amazon-appstream-2.0-api-interface-vpc-endpoint"></a>

 In design scenarios where API and CLI commands to Amazon WorkSpaces Applications originate in your VPC, privatize these programmatic calls through an [https://docs.aws.amazon.com/appstream2/latest/developerguide/access-api-cli-through-interface-vpc-endpoint.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/access-api-cli-through-interface-vpc-endpoint.html).

## Amazon WorkSpaces Applications streaming interface VPC endpoint
<a name="amazon-appstream-2.0-streaming-interface-vpc-endpoint"></a>

 While it is possible to [https://docs.aws.amazon.com/appstream2/latest/developerguide/creating-streaming-from-interface-vpc-endpoints.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/creating-streaming-from-interface-vpc-endpoints.html), use this configuration with caution. The default streaming behavior through the public internet is the most efficient and performant delivery method for Amazon WorkSpaces Applications streaming traffic.

![Diagram showing how traffic moves between Amazon WorkSpaces Applications Streaming Gateways via the internet.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/images/appstream-streaming-interface.png)

 *Amazon WorkSpaces Applications streaming interface VPC endpoint*

 As shown in the previous figure, the public internet is the most efficient path to Amazon WorkSpaces Applications Streaming Gateways. Routing through the customer-managed VPC and networking adds complexity and latency. It also adds data transfer fees over Direct Connect.

**Note**
Only streaming is supported by the VPC endpoint, and authentication must still take place over the public internet. Prerequisite access such as SAML Single Sign-On (SSO) Identity Provider (IdP) remain a requirement that are accessible only through the public internet.

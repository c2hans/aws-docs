---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-teradata-vantagecloud-lake/connectivity-options.html
---

# Connectivity options
<a name="connectivity-options"></a>

There are two supported connectivity options for connecting to Teradata VantageCloud Lake:
+ AWS PrivateLink (recommended) – Connect from cloud to cloud. You can use this option to connect your AWS account to VantageCloud Lake.
+ Public internet – Connect over the internet. You can use this option to connect your on-premises system to VantageCloud Lake.

The following diagram shows these supported connectivity methods.

![AWS PrivateLink and public internet options for connecting to Teradata VantageCloud Lake on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-teradata-vantagecloud-lake/images/guide-img/54b73adc-60e6-4e76-a7be-f62261514119/images/e9b1ed0e-a86a-4637-87f3-3a2c0210ff4c.png)

## PrivateLink architecture
<a name="private-link"></a>

AWS PrivateLink provides connectivity between virtual private clouds (VPCs). You can access Teradata VantageCloud Lake over private IP addresses from your virtual network while keeping the data flow on the AWS secure backbone network. Data never traverses the public internet. This significantly reduces exposure to common security threats.

PrivateLink allows only unidirectional network connectivity. Applications that require a connection to be initiated from both endpoints require two PrivateLink connections.

The following diagram shows a PrivateLink architecture where a private endpoint in an AWS account uses PrivateLink to connect to Teradata Session Manager, which connects to a VantageCloud Lake primary cluster.

![Using PrivateLink to access Teradata VantageCloud Lake on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-teradata-vantagecloud-lake/images/guide-img/54b73adc-60e6-4e76-a7be-f62261514119/images/9c82aa37-f48c-40cb-afe3-937bef6c1129.png)

For more information, see [AWS PrivateLink](https://aws.amazon.com/privatelink/) or contact your [Teradata account team.](https://www.teradata.com/About-Us/Contact)

## Public internet
<a name="public-internet"></a>

If your architecture requires hybrid connectivity from on premises to Teradata VantageCloud Lake, you can use the public internet connectivity option. You can also use this option to connect from another VPC over the internet. You control the allowed CIDR ranges. The following diagram shows a user's VPC using the internet to connect to Teradata-managed VantageCloud Lake.

![Using the public internet to access Teradata VantageCloud Lake on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-teradata-vantagecloud-lake/images/guide-img/54b73adc-60e6-4e76-a7be-f62261514119/images/e39adf7f-d253-4557-801f-d975b7f163eb.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

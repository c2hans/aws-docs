---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/leverage-vpc-endpoints.html
---

# Leverage VPC endpoints
<a name="leverage-vpc-endpoints"></a>

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a connection between your VPC and serverless services like AWS Lambda and AWS Step Functions. You can use this connection to invoke your Serverless resources without crossing the public internet.

 To establish a private connection between your VPC and serverless resources, you can create an interface VPC endpoint. Interface endpoints are powered by AWS PrivateLink, which enables you to privately access APIs without needing an internet gateway or NAT device within your architecture.

 Leveraging VPC endpoints will most likely contribute to cost savings if you are leveraging NAT and Internet gateways for the sole purpose of accessing Serverless APIs from AWS resources that do not have access to the internet. The cost optimisation is achieved from the fact that interface endpoints are more cost effective VPC structures compared to NAT and Internet gateways.

 The example diagrams below show two different patterns of Lambda functions accessing the Amazon SNS service. In the first diagram, there are two NAT Gateways in two AZs for high availability and an Internet Gateway. In the second diagram, there are interface endpoints in two AZs. The second pattern is more cost effective than the first one because interface endpoints are more cost effective than using NAT and Internet Gateways combined.

![Diagram showing a Lambda function accessing Amazon SNS via NAT and Internet Gateways](http://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/images/lambda-function-accessing-amazon-sns-via-nat-and-internet-gateways.png)

![Diagram showing a Lambda function accessing Amazon SNS via interface endpoints](http://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/images/lambda-function-accessing-amazon-sns-via-interface-endpoints.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

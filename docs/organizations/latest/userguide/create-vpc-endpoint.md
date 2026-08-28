---
source_url: https://docs.aws.amazon.com/organizations/latest/userguide/create-vpc-endpoint.html
---

# Creating a VPC endpoint for AWS Organizations
<a name="create-vpc-endpoint"></a>

You can create an AWS Organizations endpoint in your VPC using the Amazon VPC Console, the AWS Command Line Interface (AWS CLI) or CloudFormation.

For information about creating and configuring an endpoint using the Amazon VPC console or the AWS CLI, see [Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *Amazon VPC User Guide*. For information about creating and configuring an endpoint using CloudFormation, see the [AWS::EC2::VPCEndpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html) resource in the *AWS CloudFormation User Guide*.

AWS Organizations is a global service with its control plane located in US East (N. Virginia) (us-east-1) for commercial AWS Regions. You can create an interface VPC endpoint for AWS Organizations only in us-east-1. Use the following service name:

```
com.amazonaws.us-east-1.organizations
```

If you require FIPS 140-2 validated cryptographic modules when accessing AWS Organizations, use the following AWS Organizations FIPS service name:

```
com.amazonaws.us-east-1.organizations-fips
```

If your VPC is in a different Region, you must use AWS Transit Gateway to access the endpoint from that Region. For the AWS China and AWS GovCloud partitions, use the service name that corresponds to the AWS Organizations control plane Region in that partition.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

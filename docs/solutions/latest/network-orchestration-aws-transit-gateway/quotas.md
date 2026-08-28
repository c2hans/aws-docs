---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/quotas.html
---

# Quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this solution
<a name="quotas-for-aws-services-in-this-solution"></a>

Make sure you have sufficient quota for each of the [services implemented in this solution](architecture-details.md#aws-services-in-this-solution). For more information, refer to [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

Select one of the following links to go to the page for that service. To see the service quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the *AWS General Reference guide* PDF instead.

|  |  |
| --- |--- |
|  [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-quotas.html)  |  [AWS X-Ray](https://docs.aws.amazon.com/general/latest/gr/xray.html)  |
|  [Lambda](https://docs.aws.amazon.com/general/latest/gr/lambda-service.html)  |  [Amazon SNS](https://docs.aws.amazon.com/general/latest/gr/sns.html)  |
|  [Step Functions](https://docs.aws.amazon.com/general/latest/gr/step-functions.html)  |  [Amazon Cognito](https://docs.aws.amazon.com/general/latest/gr/cognito_identity.html)  |
|  [DynamoDB](https://docs.aws.amazon.com/general/latest/gr/ddb.html)  |  [AWS AppSync](https://docs.aws.amazon.com/general/latest/gr/appsync.html)  |
|  [EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-quota.html)  |  [Amazon S3](https://docs.aws.amazon.com/general/latest/gr/s3.html)  |
|  [AWS WAF](https://docs.aws.amazon.com/general/latest/gr/waf.html)  |  [CloudFront](https://docs.aws.amazon.com/general/latest/gr/cf_region.html)  |

## CloudFormation quotas
<a name="cloudformation-quotas"></a>

Your AWS account has [CloudFormation](https://aws.amazon.com/cloudformation/) quotas that you must be aware of when launching the stacks for this solution. By understanding these quotas, you can avoid limitation errors that can prevent you from deploying this solution successfully. For more information, refer to [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *AWS CloudFormation Users Guide*.

## Lambda quotas
<a name="lambda-quotas"></a>

In the hub account, the state machine invokes Lambda functions to run the scan in parallel depending on the VPCs and subnets tagged across multiple accounts in your organization. [Review](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html) and [increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) your Lambda invocation limit to avoid throttling.

## Transit Gateway quotas
<a name="transit-gateway-quotas"></a>

The solution creates a new transit gateway for each hub stack deployment unless you provide an existing transit gateway in the hub template parameter **(Optional) Do you wish to use an existing transit gateway? If yes, you must provide the transit gateway id below.** Your account has a default Transit Gateway quota of five.

## AWS Transit Gateway Network Manager quotas
<a name="aws-transit-gateway-network-manager-quotas"></a>

The solution creates a new [global network](https://docs.aws.amazon.com/network-manager/latest/tgwnm/what-are-global-networks.html) for each hub stack deployment unless you provide an existing global network ID in the hub template parameter **(Optional) Do you wish to use an existing global network? If yes, you must provide the global network id below.** Your account has default global network quota of five. Only one global network is recommended for all the other deployments in different AWS Regions in the hub account. Provide the global network ID created by the first deployment in the other deployments in different AWS Regions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Network Orchestration for AWS Transit Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

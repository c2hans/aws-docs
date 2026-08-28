---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

 This section describes the [cost](cost.md), [security](security.md), [Regions](#supported-aws-regions), and other considerations prior to deploying the solution.

## Supported AWS Regions
<a name="supported-aws-regions"></a>

 This solution can be launched in any AWS Region of your choice in which regional resources will be created:
+  Secrets in Secrets Manager
+  Step Functions workflows
+  Lambda functions
+  Dynamo DB tables

 Note that because automatic session revocation module is deployed as a separate CloudFormation stack, you can deploy it in a different Region as the main stack. This can be beneficial in terms of reducing the costs arising from cross region Athena queries. Refer to [Querying across regions](https://docs.aws.amazon.com/athena/latest/ug/querying-across-regions.html) for additional Amazon S3 data transfer.

 No matter in what target Region you deploy the main stack, which includes the core components of the solution, a dependency with US East (N. Virginia) (us-east-1) Region will exist as some of the components must be defined in that region. This is because those components can be associated with the CloudFront distribution which is a global service. These components are WAF rule group and Lambda@Edge function for signing requests towards API Gateway. Both of these resources are created through custom resource logic synthesized in the main CloudFormation stack deployed in the target region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

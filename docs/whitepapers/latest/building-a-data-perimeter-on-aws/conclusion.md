---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/conclusion.html
---

# Conclusion
<a name="conclusion"></a>

 This paper has reviewed how to implement a data perimeter on AWS using SCPs, RCPs, and VPC endpoint policies. These controls are used to ensure **Only Trusted Identities**, **Only Trusted Resources**, and **Only Expected Networks** are allowed access to *my AWS*.

 The following is a list of the recommendations made throughout this paper as part of achieving the perimeter’s six objectives.
+  Use the `aws:PrincipalOrgID` condition in RCPs and VPC endpoint policies to help prevent untrusted identities. Use the `aws:PrincipalIsAWSService` and `aws:SourceOrgID` conditions to restrict access by AWS services so that it is only on your behalf.
+  Use the `aws:ResourceOrgID` condition in SCPs to help prevent your IAM principals from accessing untrusted resources. Additionally, add this condition to your VPC endpoint policies as a defense in depth approach. Create exceptions using a `NotAction` list in your SCPs and list explicit resources that should be trusted in your VPC endpoint policies. Use the `aws:CalledVia` condition to allow specific AWS services to access resources you don’t own.
+  Use an SCP to prevent access from unexpected network locations. Additionally, add similar policy statements to your RCPs as a defense in depth approach. Use the `aws:ViaAWSService` condition to create exceptions when AWS acts on your behalf using your credentials.
+  Audit your policies to ensure that permissions guardrails are applied to help prevent misconfiguration. Use IAM Access Analyzer to review resource-based policy configuration and effective permissions on your resources.
+  Block all outbound internet access, except for required AWS endpoints and allowed external services that are dependencies for your workloads. This prevents data movement to non-AWS destinations, out-of-Region AWS endpoints, and unintended VPC hosted data plane services (like Amazon RDS instances).
+  Route out-of-Region requests through VPC endpoints so that the network boundary controls are consistently applied.
+  Where AWS provides an option to run a resource publicly or inside a customer-owned VPC, use the VPC configuration (that is, [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) (OpenSearch Service), [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) notebooks, and [AWS Lambda](https://aws.amazon.com/lambda)) and turn off the public access options (for example, [Amazon Redshift](https://aws.amazon.com/redshift) and Amazon RDS) in order to use network controls.
+  Configure RCPs to limit access to your IAM roles so that they can only be assumed by trusted identities.
+  Prevent external resource sharing and targeting external resources with an SCP.
+ Use the AWS Management Console Private Access feature to help ensure users can only access intended AWS accounts and organizations from your expected networks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

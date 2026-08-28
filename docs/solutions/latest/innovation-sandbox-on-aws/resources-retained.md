---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/resources-retained.html
---

# Resources retained after deletion
<a name="resources-retained"></a>

Some resources, which contain customer data, are not deleted automatically when you uninstall the stacks. The cost of these resources is minimal, and you can manually delete these resources.

 **Compute stack**
+ Customer Managed Key
  +  `AwsSolutions/InnovationSandbox/InnovationSandbox-Compute`
+ CloudWatch log groups
  +  `InnovationSandbox-Compute-ISBLogGroupXXXXX`
  +  `InnovationSandbox-Compute-ISBLogGroupCustomResourcesXXXXX`
+ S3 buckets
  + CloudFront distribution host (`innovationsandbox-compute-cloudfrontuiapiisbfronte-XXXXX`)
  + CloudFront distribution access log (`innovationsandbox-compute-cloudfrontuiapiisbfronte-XXXXX`)
  + Application logs archive (`innovationsandbox-compute-logarchivingisblogsarchi-XXXXX`)

 **Data stack**
+ Customer Managed Key
  +  `AwsSolutions/InnovationSandbox/InnovationSandbox-Data`
+ CloudWatch log group
  +  `InnovationSandbox-Data-ISBLogGroupCustomResourcesXXXXX`
+ DynamoDB tables
  +  `InnovationSandbox-Data-LeaseTableXXXXX`
  +  `InnovationSandbox-Data-LeaseTemplateTableXXXXX`
  +  `InnovationSandbox-Data-AccountTableXXXXX`
  +  `InnovationSandbox-Data-ConfigTableXXXXX`

 **IDC stack**
+ Customer Managed Key
  +  `AwsSolutions/InnovationSandbox/InnovationSandbox-IDC`
+ CloudWatch log group
  +  `InnovationSandbox-IDC-ISBLogGroupCustomResourcesXXXXX`
+ Innovation Sandbox groups
  + <NAMESPACE>\_IsbUsersGroup
  + <NAMESPACE>\_IsbManagersGroup
  + <NAMESPACE>\_IsbAdminsGroup

 **Account Pool stack**
+ Customer Managed Key
  +  `AwsSolutions/InnovationSandbox/InnovationSandbox-AccountPool`
+ CloudWatch log group
  +  `InnovationSandbox-AccountPool-ISBLogGroupCustomResourcesXXXXX`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

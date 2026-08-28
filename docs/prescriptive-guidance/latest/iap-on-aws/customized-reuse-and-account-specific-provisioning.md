---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iap-on-aws/customized-reuse-and-account-specific-provisioning.html
---

# Customized reuse and account-specific provisioning
<a name="customized-reuse-and-account-specific-provisioning"></a>

Products should be made reusable for as many different customized purposes as possible. Service Catalog supports reusability through product parameters. You can provide these parameters as input to a product at provisioning time.

You can also specify these parameters as AWS Systems Manager Parameter Store values at the CloudFormation template level, to apply account-specific and OU-specific values. This is a best practice for CloudFormation provisioning template design. The value of the named parameter within the target account is applied when the product is provisioned. For example, you can specify a subnet parameter as a Parameter Store value and apply that subnet at product provisioning time for a specific OU account. For more information about Parameter Store values as CloudFormation template parameters, see  [Using dynamic references to specify template values](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html) in the AWS CloudFormation documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

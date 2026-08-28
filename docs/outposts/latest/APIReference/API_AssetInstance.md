---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_AssetInstance.html
---

# AssetInstance
<a name="API_AssetInstance"></a>

An Amazon EC2 instance.

## Contents
<a name="API_AssetInstance_Contents"></a>

 ** AccountId **   <a name="outposts-Type-AssetInstance-AccountId"></a>
The ID of the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** AssetId **   <a name="outposts-Type-AssetInstance-AssetId"></a>
The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(\w+)$`
Required: No

 ** AwsServiceName **   <a name="outposts-Type-AssetInstance-AwsServiceName"></a>
The AWS service name of the instance.
Type: String
Valid Values: `AWS | EC2 | EKS | ELASTICACHE | ELB | RDS | ROUTE53`
Required: No

 ** InstanceId **   <a name="outposts-Type-AssetInstance-InstanceId"></a>
The ID of the instance.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 32.
Pattern: `^i-[0-9a-z]+$`
Required: No

 ** InstanceType **   <a name="outposts-Type-AssetInstance-InstanceType"></a>
The type of instance.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z0-9\-\.]+`
Required: No

## See Also
<a name="API_AssetInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/AssetInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/AssetInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/AssetInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

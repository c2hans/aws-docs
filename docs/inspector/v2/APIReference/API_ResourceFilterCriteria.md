---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceFilterCriteria.html
---

# ResourceFilterCriteria
<a name="API_ResourceFilterCriteria"></a>

The resource filter criteria for a Software bill of materials (SBOM) report.

## Contents
<a name="API_ResourceFilterCriteria_Contents"></a>

 ** accountId **   <a name="inspector2-Type-ResourceFilterCriteria-accountId"></a>
The account IDs used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ec2InstanceTags **   <a name="inspector2-Type-ResourceFilterCriteria-ec2InstanceTags"></a>
The EC2 instance tags used as resource filter criteria.
Type: Array of [ResourceMapFilter](API_ResourceMapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrImageTags **   <a name="inspector2-Type-ResourceFilterCriteria-ecrImageTags"></a>
The ECR image tags used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrRepositoryName **   <a name="inspector2-Type-ResourceFilterCriteria-ecrRepositoryName"></a>
The ECR repository names used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lambdaFunctionName **   <a name="inspector2-Type-ResourceFilterCriteria-lambdaFunctionName"></a>
The AWS Lambda function name used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lambdaFunctionTags **   <a name="inspector2-Type-ResourceFilterCriteria-lambdaFunctionTags"></a>
The AWS Lambda function tags used as resource filter criteria.
Type: Array of [ResourceMapFilter](API_ResourceMapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceId **   <a name="inspector2-Type-ResourceFilterCriteria-resourceId"></a>
The resource IDs used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceType **   <a name="inspector2-Type-ResourceFilterCriteria-resourceType"></a>
The resource types used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_ResourceFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ResourceFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ResourceFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ResourceFilterCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ResourceIdentifierSummary.html
---

# ResourceIdentifierSummary
<a name="API_ResourceIdentifierSummary"></a>

Describes the target resources of a specific type in your import template (for example, all `AWS::S3::Bucket` resources) and the properties you can provide during the import to identify resources of that type.

## Contents
<a name="API_ResourceIdentifierSummary_Contents"></a>

 ** LogicalResourceIds.member.N **
The logical IDs of the target resources of the specified `ResourceType`, as defined in the import template.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

 ** ResourceIdentifiers.member.N **
The resource properties you can provide during the import to identify your target resources. For example, `BucketName` is a possible identifier property for `AWS::S3::Bucket` resources.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ResourceType **
The template resource type of the target resources, such as `AWS::S3::Bucket`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_ResourceIdentifierSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ResourceIdentifierSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ResourceIdentifierSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ResourceIdentifierSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

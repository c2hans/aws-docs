---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ChangeSetHookResourceTargetDetails.html
---

# ChangeSetHookResourceTargetDetails
<a name="API_ChangeSetHookResourceTargetDetails"></a>

Specifies `RESOURCE` type target details for activated Hooks.

## Contents
<a name="API_ChangeSetHookResourceTargetDetails_Contents"></a>

 ** LogicalResourceId **
The resource's logical ID, which is defined in the stack's template.
Type: String
Required: No

 ** ResourceAction **
Specifies the action of the resource.
Type: String
Valid Values: `Add | Modify | Remove | Import | Dynamic | SyncWithActual`
Required: No

 ** ResourceType **
The type of CloudFormation resource, such as `AWS::S3::Bucket`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}$`
Required: No

## See Also
<a name="API_ChangeSetHookResourceTargetDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ChangeSetHookResourceTargetDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ChangeSetHookResourceTargetDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ChangeSetHookResourceTargetDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

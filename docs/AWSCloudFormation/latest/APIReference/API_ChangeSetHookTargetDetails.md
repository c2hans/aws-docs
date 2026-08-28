---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ChangeSetHookTargetDetails.html
---

# ChangeSetHookTargetDetails
<a name="API_ChangeSetHookTargetDetails"></a>

Specifies target details for an activated Hook.

## Contents
<a name="API_ChangeSetHookTargetDetails_Contents"></a>

 ** ResourceTargetDetails **
Required if `TargetType` is `RESOURCE`.
Type: [ChangeSetHookResourceTargetDetails](API_ChangeSetHookResourceTargetDetails.md) object
Required: No

 ** TargetType **
The Hook target type.
Type: String
Valid Values: `RESOURCE`
Required: No

## See Also
<a name="API_ChangeSetHookTargetDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ChangeSetHookTargetDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ChangeSetHookTargetDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ChangeSetHookTargetDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

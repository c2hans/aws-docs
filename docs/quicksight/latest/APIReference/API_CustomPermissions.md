---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomPermissions.html
---

# CustomPermissions
<a name="API_CustomPermissions"></a>

The custom permissions profile.

## Contents
<a name="API_CustomPermissions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-CustomPermissions-Arn"></a>
The Amazon Resource Name (ARN) of the custom permissions profile.
Type: String
Required: No

 ** Capabilities **   <a name="QS-Type-CustomPermissions-Capabilities"></a>
A set of actions in the custom permissions profile.
Type: [Capabilities](API_Capabilities.md) object
Required: No

 ** CustomPermissionsName **   <a name="QS-Type-CustomPermissions-CustomPermissionsName"></a>
The name of the custom permissions profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9+=,.@_-]+$`
Required: No

 ** Governance **   <a name="QS-Type-CustomPermissions-Governance"></a>
The governance configuration for the custom permissions profile. When you enable governance for a category, Amazon Quick denies access to any current or new capability in that category unless you explicitly set that capability to `ALLOW` in `Capabilities`.
Type: [Governance](API_Governance.md) object
Required: No

## See Also
<a name="API_CustomPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CustomPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CustomPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CustomPermissions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

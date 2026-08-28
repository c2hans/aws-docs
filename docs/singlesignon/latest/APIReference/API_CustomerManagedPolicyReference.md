---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CustomerManagedPolicyReference.html
---

# CustomerManagedPolicyReference
<a name="API_CustomerManagedPolicyReference"></a>

Specifies the name and path of a customer managed policy. You must have an IAM policy that matches the name and path in each AWS account where you want to deploy your permission set.

## Contents
<a name="API_CustomerManagedPolicyReference_Contents"></a>

 ** Name **   <a name="singlesignon-Type-CustomerManagedPolicyReference-Name"></a>
The name of the IAM policy that you have configured in each account where you want to deploy your permission set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** Path **   <a name="singlesignon-Type-CustomerManagedPolicyReference-Path"></a>
The path to the IAM policy that you have configured in each account where you want to deploy your permission set. The default is `/`. For more information, see [Friendly names and paths](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `((/[A-Za-z0-9\.,\+@=_-]+)*)/`
Required: No

## See Also
<a name="API_CustomerManagedPolicyReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/CustomerManagedPolicyReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/CustomerManagedPolicyReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/CustomerManagedPolicyReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

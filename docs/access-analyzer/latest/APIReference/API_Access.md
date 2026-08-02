---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Access.html
---

# Access
<a name="API_Access"></a>

Contains information about actions and resources that define permissions to check against a policy.

## Contents
<a name="API_Access_Contents"></a>

 ** actions **   <a name="accessanalyzer-Type-Access-actions"></a>
A list of actions for the access permissions. Any strings that can be used as an action in an IAM policy can be used in the list of actions to check.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** resources **   <a name="accessanalyzer-Type-Access-resources"></a>
A list of resources for the access permissions. Any strings that can be used as an Amazon Resource Name (ARN) in an IAM policy can be used in the list of resources to check. You can only use a wildcard in the portion of the ARN that specifies the resource ID.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_Access_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/Access)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/Access)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/Access)

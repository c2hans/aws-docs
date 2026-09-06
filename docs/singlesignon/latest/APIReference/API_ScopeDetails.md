---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ScopeDetails.html
---

# ScopeDetails
<a name="API_ScopeDetails"></a>

A structure that describes an IAM Identity Center access scope and its authorized targets.

## Contents
<a name="API_ScopeDetails_Contents"></a>

 ** Scope **   <a name="singlesignon-Type-ScopeDetails-Scope"></a>
The name of the access scope.
Type: String
Pattern: `([A-Za-z0-9_]{1,50})(:[A-Za-z0-9_]{1,50}){0,1}(:[A-Za-z0-9_]{1,50}){0,1}`
Required: Yes

 ** AuthorizedTargets **   <a name="singlesignon-Type-ScopeDetails-AuthorizedTargets"></a>
An array list of ARNs of applications.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::(\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}|:instance/(sso)?ins-[a-zA-Z0-9-.]{16})`
Required: No

## See Also
<a name="API_ScopeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/ScopeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/ScopeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/ScopeDetails)

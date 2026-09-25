---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_AdminAccountSummary.html
---

# AdminAccountSummary
<a name="API_AdminAccountSummary"></a>

Summary information about an AWS Network Security Manager administrator account.

## Contents
<a name="API_AdminAccountSummary_Contents"></a>

 ** accountId **   <a name="networksecuritymanager-Type-AdminAccountSummary-accountId"></a>
The AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `(?:[0-9]{12})`
Required: Yes

 ** email **   <a name="networksecuritymanager-Type-AdminAccountSummary-email"></a>
The email address associated with the account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** name **   <a name="networksecuritymanager-Type-AdminAccountSummary-name"></a>
The name of the administrator account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** priority **   <a name="networksecuritymanager-Type-AdminAccountSummary-priority"></a>
The priority assigned to the administrator account.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

## See Also
<a name="API_AdminAccountSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/AdminAccountSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/AdminAccountSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/AdminAccountSummary)

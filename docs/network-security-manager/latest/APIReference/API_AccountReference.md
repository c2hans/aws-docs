---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_AccountReference.html
---

# AccountReference
<a name="API_AccountReference"></a>

A reference to an AWS account, with optional display metadata.

## Contents
<a name="API_AccountReference_Contents"></a>

 ** accountId **   <a name="networksecuritymanager-Type-AccountReference-accountId"></a>
The AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `(?:[0-9]{12})`
Required: Yes

 ** email **   <a name="networksecuritymanager-Type-AccountReference-email"></a>
The email address associated with the account.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Required: No

 ** name **   <a name="networksecuritymanager-Type-AccountReference-name"></a>
The display name of the account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

## See Also
<a name="API_AccountReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/AccountReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/AccountReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/AccountReference)

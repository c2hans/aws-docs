---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_DelegatedAdminAccount.html
---

# DelegatedAdminAccount
<a name="API_DelegatedAdminAccount"></a>

Details of the Amazon Inspector delegated administrator for your organization.

## Contents
<a name="API_DelegatedAdminAccount_Contents"></a>

 ** accountId **   <a name="inspector2-Type-DelegatedAdminAccount-accountId"></a>
The AWS account ID of the Amazon Inspector delegated administrator for your organization.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** status **   <a name="inspector2-Type-DelegatedAdminAccount-status"></a>
The status of the Amazon Inspector delegated administrator.
Type: String
Valid Values: `ENABLED | DISABLE_IN_PROGRESS`
Required: No

## See Also
<a name="API_DelegatedAdminAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/DelegatedAdminAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/DelegatedAdminAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/DelegatedAdminAccount)

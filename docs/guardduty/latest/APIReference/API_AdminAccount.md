---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AdminAccount.html
---

# AdminAccount
<a name="API_AdminAccount"></a>

The account within the organization specified as the GuardDuty delegated administrator.

## Contents
<a name="API_AdminAccount_Contents"></a>

 ** adminAccountId **   <a name="guardduty-Type-AdminAccount-adminAccountId"></a>
The AWS account ID for the account.
Type: String
Required: No

 ** adminStatus **   <a name="guardduty-Type-AdminAccount-adminStatus"></a>
Indicates whether the account is enabled as the delegated administrator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `ENABLED | DISABLE_IN_PROGRESS`
Required: No

## See Also
<a name="API_AdminAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AdminAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AdminAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AdminAccount)

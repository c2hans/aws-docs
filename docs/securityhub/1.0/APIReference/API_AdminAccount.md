---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AdminAccount.html
---

# AdminAccount
<a name="API_AdminAccount"></a>

Represents a Security Hub CSPM administrator account designated by an organization management account.

## Contents
<a name="API_AdminAccount_Contents"></a>

 ** AccountId **   <a name="securityhub-Type-AdminAccount-AccountId"></a>
The AWS account identifier of the Security Hub CSPM administrator account.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AdminAccount-Status"></a>
The current status of the Security Hub CSPM administrator account. Indicates whether the account is currently enabled as a Security Hub CSPM administrator.
Type: String
Valid Values: `ENABLED | DISABLE_IN_PROGRESS`
Required: No

## See Also
<a name="API_AdminAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AdminAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AdminAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AdminAccount)

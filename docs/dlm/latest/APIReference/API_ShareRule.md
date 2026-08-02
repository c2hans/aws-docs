---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_ShareRule.html
---

# ShareRule
<a name="API_ShareRule"></a>

 **[Custom snapshot policies only]** Specifies a rule for sharing snapshots across AWS accounts.

## Contents
<a name="API_ShareRule_Contents"></a>

 ** TargetAccounts **   <a name="dlm-Type-ShareRule-TargetAccounts"></a>
The IDs of the AWS accounts with which to share the snapshots.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** UnshareInterval **   <a name="dlm-Type-ShareRule-UnshareInterval"></a>
The period after which snapshots that are shared with other AWS accounts are automatically unshared.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** UnshareIntervalUnit **   <a name="dlm-Type-ShareRule-UnshareIntervalUnit"></a>
The unit of time for the automatic unsharing interval.
Type: String
Valid Values: `DAYS | WEEKS | MONTHS | YEARS`
Required: No

## See Also
<a name="API_ShareRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/ShareRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/ShareRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/ShareRule)

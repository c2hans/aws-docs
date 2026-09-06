---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_AccountSetting.html
---

# AccountSetting
<a name="API_AccountSetting"></a>

A regional account-level EVS setting, represented as a name and value pair.

## Contents
<a name="API_AccountSetting_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** name **   <a name="evs-Type-AccountSetting-name"></a>
The name of the EVS setting. Valid values are:
+  `vcfPortedCoreCount` (type: numeric string) - The total number of VCF license cores ported to Amazon EVS for the account in that Region. The maximum value is 1,000,000 cores. This setting value is shared with Broadcom for record-keeping.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** value **   <a name="evs-Type-AccountSetting-value"></a>
The value of the EVS setting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

## See Also
<a name="API_AccountSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/AccountSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/AccountSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/AccountSetting)

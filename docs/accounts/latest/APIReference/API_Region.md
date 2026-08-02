---
source_url: https://docs.aws.amazon.com/accounts/latest/APIReference/API_Region.html
---

# Region
<a name="API_Region"></a>

This is a structure that expresses the Region for a given account, consisting of a name and opt-in status.

## Contents
<a name="API_Region_Contents"></a>

 ** RegionName **   <a name="accounts-Type-Region-RegionName"></a>
The Region code of a given Region (for example, `us-east-1`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** RegionOptStatus **   <a name="accounts-Type-Region-RegionOptStatus"></a>
One of potential statuses a Region can undergo (Enabled, Enabling, Disabled, Disabling, Enabled\_By\_Default).
Type: String
Valid Values: `ENABLED | ENABLING | DISABLING | DISABLED | ENABLED_BY_DEFAULT`
Required: No

## See Also
<a name="API_Region_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/Region)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/Region)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/Region)

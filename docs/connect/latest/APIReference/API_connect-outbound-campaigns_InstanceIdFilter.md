---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_InstanceIdFilter.html
---

# InstanceIdFilter
<a name="API_connect-outbound-campaigns_InstanceIdFilter"></a>

Contains the filter to apply when retrieving outbound campaigns.

## Contents
<a name="API_connect-outbound-campaigns_InstanceIdFilter_Contents"></a>

 ** operator **   <a name="connect-Type-connect-outbound-campaigns_InstanceIdFilter-operator"></a>
The operator to use in the filter.
Type: String
Valid Values: `Eq`
Required: Yes

 ** value **   <a name="connect-Type-connect-outbound-campaigns_InstanceIdFilter-value"></a>
The value to use in the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

## See Also
<a name="API_connect-outbound-campaigns_InstanceIdFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/InstanceIdFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/InstanceIdFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/InstanceIdFilter)

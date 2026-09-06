---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_SupportPlan.html
---

# SupportPlan
<a name="API_channel_SupportPlan"></a>

Configuration for different types of support plans.

## Contents
<a name="API_channel_SupportPlan_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** partnerLedSupport **   <a name="AWSPartnerCentral-Type-channel_SupportPlan-partnerLedSupport"></a>
Configuration for partner-led support plans.
Type: [PartnerLedSupport](API_channel_PartnerLedSupport.md) object
Required: No

 ** resoldEnterprise **   <a name="AWSPartnerCentral-Type-channel_SupportPlan-resoldEnterprise"></a>
Configuration for resold enterprise support plans.
Type: [ResoldEnterprise](API_channel_ResoldEnterprise.md) object
Required: No

 ** resoldUnifiedOperations **   <a name="AWSPartnerCentral-Type-channel_SupportPlan-resoldUnifiedOperations"></a>
Configuration for resold unified operations support plans.
Type: [ResoldUnifiedOperations](API_channel_ResoldUnifiedOperations.md) object
Required: No

## See Also
<a name="API_channel_SupportPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/SupportPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/SupportPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/SupportPlan)

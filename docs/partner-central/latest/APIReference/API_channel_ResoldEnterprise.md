---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ResoldEnterprise.html
---

# ResoldEnterprise
<a name="API_channel_ResoldEnterprise"></a>

Configuration for resold enterprise support plans.

## Contents
<a name="API_channel_ResoldEnterprise_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** coverage **   <a name="AWSPartnerCentral-Type-channel_ResoldEnterprise-coverage"></a>
The coverage level for resold enterprise support.
Type: String
Valid Values: `ENTIRE_ORGANIZATION | MANAGEMENT_ACCOUNT_ONLY`
Required: Yes

 ** tamLocation **   <a name="AWSPartnerCentral-Type-channel_ResoldEnterprise-tamLocation"></a>
The location of the Technical Account Manager (TAM).
Type: String
Required: Yes

 ** chargeAccountId **   <a name="AWSPartnerCentral-Type-channel_ResoldEnterprise-chargeAccountId"></a>
The AWS account ID to charge for the support plan.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: No

## See Also
<a name="API_channel_ResoldEnterprise_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/ResoldEnterprise)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/ResoldEnterprise)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/ResoldEnterprise)

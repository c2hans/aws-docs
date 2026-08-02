---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_VdmAttributes.html
---

# VdmAttributes
<a name="API_VdmAttributes"></a>

The VDM attributes that apply to your Amazon SES account.

## Contents
<a name="API_VdmAttributes_Contents"></a>

 ** VdmEnabled **   <a name="SES-Type-VdmAttributes-VdmEnabled"></a>
Specifies the status of your VDM configuration. Can be one of the following:
+  `ENABLED` – Amazon SES enables VDM for your account.
+  `DISABLED` – Amazon SES disables VDM for your account.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** DashboardAttributes **   <a name="SES-Type-VdmAttributes-DashboardAttributes"></a>
Specifies additional settings for your VDM configuration as applicable to the Dashboard.
Type: [DashboardAttributes](API_DashboardAttributes.md) object
Required: No

 ** GuardianAttributes **   <a name="SES-Type-VdmAttributes-GuardianAttributes"></a>
Specifies additional settings for your VDM configuration as applicable to the Guardian.
Type: [GuardianAttributes](API_GuardianAttributes.md) object
Required: No

## See Also
<a name="API_VdmAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/VdmAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/VdmAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/VdmAttributes)

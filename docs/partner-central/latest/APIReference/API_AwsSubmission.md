---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AwsSubmission.html
---

# AwsSubmission
<a name="API_AwsSubmission"></a>

Indicates the level of AWS involvement in the opportunity. This field helps track AWS participation throughout the engagement, such as providing technical support, deal assistance, and sales support.

## Contents
<a name="API_AwsSubmission_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InvolvementType **   <a name="AWSPartnerCentral-Type-AwsSubmission-InvolvementType"></a>
Specifies the type of AWS involvement in the opportunity, such as coselling, deal support, or technical consultation. This helps categorize the nature of AWS participation.
Type: String
Valid Values: `For Visibility Only | Co-Sell`
Required: Yes

 ** Visibility **   <a name="AWSPartnerCentral-Type-AwsSubmission-Visibility"></a>
Determines who can view AWS involvement in the opportunity. Typically, this field is set to `Full` for most cases, but it may be restricted based on special program requirements or confidentiality needs.
Type: String
Valid Values: `Full | Limited`
Required: No

## See Also
<a name="API_AwsSubmission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AwsSubmission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AwsSubmission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AwsSubmission)

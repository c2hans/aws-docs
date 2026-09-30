---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModificationQuoteCurrentConfiguration.html
---

# ModificationQuoteCurrentConfiguration
<a name="API_ModificationQuoteCurrentConfiguration"></a>

Describes the configuration that a Capacity Reservation has at the time a modification quote is generated.

## Contents
<a name="API_ModificationQuoteCurrentConfiguration_Contents"></a>

 ** instanceCount **
The number of instances in the Capacity Reservation.
Type: Integer
Required: No

 ** originalStartDate **
The start date that the Capacity Reservation was originally requested with. This value does not change when you push out the start date.
Type: Timestamp
Required: No

 ** reservationState **
The current state of the Capacity Reservation.
Type: String
Required: No

 ** startDate **
The start date that the Capacity Reservation has before the quoted modification is applied.
Type: Timestamp
Required: No

## See Also
<a name="API_ModificationQuoteCurrentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModificationQuoteCurrentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModificationQuoteCurrentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModificationQuoteCurrentConfiguration)

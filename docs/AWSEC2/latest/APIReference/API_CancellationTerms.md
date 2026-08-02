---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancellationTerms.html
---

# CancellationTerms
<a name="API_CancellationTerms"></a>

Describes the cancellation terms for cancelling a future-dated Capacity Reservation during its commitment duration.

## Contents
<a name="API_CancellationTerms_Contents"></a>

 ** cancellationType **
The type of cancellation charge. Possible values include `commitment-wind-down`.
Type: String
Valid Values: `commitment-wind-down`
Required: No

 ** chargeCommitmentDurationHours **
The number of hours for which cancellation charges will apply.
Type: Long
Required: No

 ** chargeEndDate **
The date and time at which cancellation charges will stop.
Type: Timestamp
Required: No

 ** committedInstanceCount **
The number of instances under commitment after cancellation.
Type: Integer
Required: No

 ** reservationState **
The state that the Capacity Reservation will transition to after cancellation.
Type: String
Required: No

## See Also
<a name="API_CancellationTerms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CancellationTerms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CancellationTerms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CancellationTerms)

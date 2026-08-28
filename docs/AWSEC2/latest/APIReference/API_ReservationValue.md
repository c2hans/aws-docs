---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReservationValue.html
---

# ReservationValue
<a name="API_ReservationValue"></a>

The cost associated with the Reserved Instance.

## Contents
<a name="API_ReservationValue_Contents"></a>

 ** hourlyPrice **
The hourly rate of the reservation.
Type: String
Required: No

 ** remainingTotalValue **
The balance of the total value (the sum of remainingUpfrontValue \+ hourlyPrice \* number of hours remaining).
Type: String
Required: No

 ** remainingUpfrontValue **
The remaining upfront cost of the reservation.
Type: String
Required: No

## See Also
<a name="API_ReservationValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReservationValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReservationValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReservationValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

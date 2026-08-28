---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Ec2CapacityReservation.html
---

# Ec2CapacityReservation
<a name="API_Ec2CapacityReservation"></a>

The EC2 capacity reservations that are shared to an ML capacity reservation.

## Contents
<a name="API_Ec2CapacityReservation_Contents"></a>

 ** AvailableInstanceCount **   <a name="sagemaker-Type-Ec2CapacityReservation-AvailableInstanceCount"></a>
The number of instances that are currently available in the EC2 capacity reservation.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Ec2CapacityReservationId **   <a name="sagemaker-Type-Ec2CapacityReservation-Ec2CapacityReservationId"></a>
The unique identifier for an EC2 capacity reservation that's part of the ML capacity reservation.
Type: String
Required: No

 ** TotalInstanceCount **   <a name="sagemaker-Type-Ec2CapacityReservation-TotalInstanceCount"></a>
The number of instances that you allocated to the EC2 capacity reservation.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** UsedByCurrentEndpoint **   <a name="sagemaker-Type-Ec2CapacityReservation-UsedByCurrentEndpoint"></a>
The number of instances from the EC2 capacity reservation that are being used by the endpoint.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_Ec2CapacityReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Ec2CapacityReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Ec2CapacityReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Ec2CapacityReservation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

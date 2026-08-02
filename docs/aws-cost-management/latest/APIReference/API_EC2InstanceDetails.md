---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_EC2InstanceDetails.html
---

# EC2InstanceDetails
<a name="API_EC2InstanceDetails"></a>

Details about the Amazon EC2 reservations that AWS recommends that you purchase.

## Contents
<a name="API_EC2InstanceDetails_Contents"></a>

 ** AvailabilityZone **   <a name="awscostmanagement-Type-EC2InstanceDetails-AvailabilityZone"></a>
The Availability Zone of the recommended reservation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentGeneration **   <a name="awscostmanagement-Type-EC2InstanceDetails-CurrentGeneration"></a>
Determines whether the recommendation is for a current-generation instance.
Type: Boolean
Required: No

 ** Family **   <a name="awscostmanagement-Type-EC2InstanceDetails-Family"></a>
The instance family of the recommended reservation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** InstanceType **   <a name="awscostmanagement-Type-EC2InstanceDetails-InstanceType"></a>
The type of instance that AWS recommends.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Platform **   <a name="awscostmanagement-Type-EC2InstanceDetails-Platform"></a>
The platform of the recommended reservation. The platform is the specific combination of operating system, license model, and software on an instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Region **   <a name="awscostmanagement-Type-EC2InstanceDetails-Region"></a>
The AWS Region of the recommended reservation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** SizeFlexEligible **   <a name="awscostmanagement-Type-EC2InstanceDetails-SizeFlexEligible"></a>
Determines whether the recommended reservation is size flexible.
Type: Boolean
Required: No

 ** Tenancy **   <a name="awscostmanagement-Type-EC2InstanceDetails-Tenancy"></a>
Determines whether the recommended reservation is dedicated or shared.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_EC2InstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/EC2InstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/EC2InstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/EC2InstanceDetails)

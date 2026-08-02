---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RDSInstanceDetails.html
---

# RDSInstanceDetails
<a name="API_RDSInstanceDetails"></a>

Details about the Amazon RDS reservations that AWS recommends that you purchase.

## Contents
<a name="API_RDSInstanceDetails_Contents"></a>

 ** CurrentGeneration **   <a name="awscostmanagement-Type-RDSInstanceDetails-CurrentGeneration"></a>
Determines whether the recommendation is for a current-generation instance.
Type: Boolean
Required: No

 ** DatabaseEdition **   <a name="awscostmanagement-Type-RDSInstanceDetails-DatabaseEdition"></a>
The database edition that the recommended reservation supports.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** DatabaseEngine **   <a name="awscostmanagement-Type-RDSInstanceDetails-DatabaseEngine"></a>
The database engine that the recommended reservation supports.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** DeploymentModel **   <a name="awscostmanagement-Type-RDSInstanceDetails-DeploymentModel"></a>
Determines whether the recommendation is for a reservation for RDS Custom.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** DeploymentOption **   <a name="awscostmanagement-Type-RDSInstanceDetails-DeploymentOption"></a>
Determines whether the recommendation is for a reservation in a single Availability Zone or a reservation with a backup in a second Availability Zone.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Family **   <a name="awscostmanagement-Type-RDSInstanceDetails-Family"></a>
The instance family of the recommended reservation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** InstanceType **   <a name="awscostmanagement-Type-RDSInstanceDetails-InstanceType"></a>
The type of instance that AWS recommends.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** LicenseModel **   <a name="awscostmanagement-Type-RDSInstanceDetails-LicenseModel"></a>
The license model that the recommended reservation supports.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Region **   <a name="awscostmanagement-Type-RDSInstanceDetails-Region"></a>
The AWS Region of the recommended reservation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** SizeFlexEligible **   <a name="awscostmanagement-Type-RDSInstanceDetails-SizeFlexEligible"></a>
Determines whether the recommended reservation is size flexible.
Type: Boolean
Required: No

## See Also
<a name="API_RDSInstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/RDSInstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/RDSInstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/RDSInstanceDetails)

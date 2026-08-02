---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_EC2ResourceDetails.html
---

# EC2ResourceDetails
<a name="API_EC2ResourceDetails"></a>

Details on the Amazon EC2 Resource.

## Contents
<a name="API_EC2ResourceDetails_Contents"></a>

 ** HourlyOnDemandRate **   <a name="awscostmanagement-Type-EC2ResourceDetails-HourlyOnDemandRate"></a>
The hourly public On-Demand rate for the instance type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** InstanceType **   <a name="awscostmanagement-Type-EC2ResourceDetails-InstanceType"></a>
The type of AWS instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Memory **   <a name="awscostmanagement-Type-EC2ResourceDetails-Memory"></a>
The memory capacity of the AWS instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** NetworkPerformance **   <a name="awscostmanagement-Type-EC2ResourceDetails-NetworkPerformance"></a>
The network performance capacity of the AWS instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Platform **   <a name="awscostmanagement-Type-EC2ResourceDetails-Platform"></a>
The platform of the AWS instance. The platform is the specific combination of operating system, license model, and software on an instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Region **   <a name="awscostmanagement-Type-EC2ResourceDetails-Region"></a>
The AWS Region of the instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Sku **   <a name="awscostmanagement-Type-EC2ResourceDetails-Sku"></a>
The SKU of the product.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Storage **   <a name="awscostmanagement-Type-EC2ResourceDetails-Storage"></a>
The disk storage of the AWS instance. This doesn't include EBS storage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Vcpu **   <a name="awscostmanagement-Type-EC2ResourceDetails-Vcpu"></a>
The number of VCPU cores in the AWS instance type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_EC2ResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/EC2ResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/EC2ResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/EC2ResourceDetails)

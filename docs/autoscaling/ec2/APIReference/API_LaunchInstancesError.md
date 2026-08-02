---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LaunchInstancesError.html
---

# LaunchInstancesError
<a name="API_LaunchInstancesError"></a>

 Contains details about errors encountered during instance launch attempts.

## Contents
<a name="API_LaunchInstancesError_Contents"></a>

 ** AvailabilityZone **
 The Availability Zone where the instance launch was attempted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** AvailabilityZoneId **
 The Availability Zone ID where the launch error occurred.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ErrorCode **
 The error code representing the type of error encountered (e.g., InsufficientInstanceCapacity).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ErrorMessage **
 A descriptive message providing details about the error encountered during the launch attempt.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** InstanceType **
 The instance type that failed to launch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** MarketType **
 The market type (On-Demand or Spot) that encountered the launch error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** SubnetId **
 The subnet ID where the instance launch was attempted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_LaunchInstancesError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/LaunchInstancesError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/LaunchInstancesError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/LaunchInstancesError)

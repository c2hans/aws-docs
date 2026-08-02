---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Ec2InstanceAggregationResponse.html
---

# Ec2InstanceAggregationResponse
<a name="API_Ec2InstanceAggregationResponse"></a>

A response that contains the results of a finding aggregation by Amazon EC2 instance.

## Contents
<a name="API_Ec2InstanceAggregationResponse_Contents"></a>

 ** instanceId **   <a name="inspector2-Type-Ec2InstanceAggregationResponse-instanceId"></a>
The Amazon EC2 instance ID.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** accountId **   <a name="inspector2-Type-Ec2InstanceAggregationResponse-accountId"></a>
The AWS account for the Amazon EC2 instance.
Type: String
Required: No

 ** ami **   <a name="inspector2-Type-Ec2InstanceAggregationResponse-ami"></a>
The Amazon Machine Image (AMI) of the Amazon EC2 instance.
Type: String
Pattern: `ami-([a-z0-9]{8}|[a-z0-9]{17}|\*)`
Required: No

 ** instanceTags **   <a name="inspector2-Type-Ec2InstanceAggregationResponse-instanceTags"></a>
The tags attached to the instance.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** networkFindings **   <a name="inspector2-Type-Ec2InstanceAggregationResponse-networkFindings"></a>
The number of network findings for the Amazon EC2 instance.
Type: Long
Required: No

 ** operatingSystem **   <a name="inspector2-Type-Ec2InstanceAggregationResponse-operatingSystem"></a>
The operating system of the Amazon EC2 instance.
Type: String
Required: No

 ** severityCounts **   <a name="inspector2-Type-Ec2InstanceAggregationResponse-severityCounts"></a>
An object that contains the count of matched findings per severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_Ec2InstanceAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Ec2InstanceAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Ec2InstanceAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Ec2InstanceAggregationResponse)

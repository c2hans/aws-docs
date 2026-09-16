---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTerminationPolicyTypes.html
---

# DescribeTerminationPolicyTypes
<a name="API_DescribeTerminationPolicyTypes"></a>

Describes the termination policies supported by Amazon EC2 Auto Scaling.

For more information, see [Configure termination policies for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Response Elements
<a name="API_DescribeTerminationPolicyTypes_ResponseElements"></a>

The following element is returned by the service.

 **TerminationPolicyTypes.member.N**
The termination policies supported by Amazon EC2 Auto Scaling: `OldestInstance`, `OldestLaunchConfiguration`, `NewestInstance`, `ClosestToNextInstanceHour`, `Default`, `OldestLaunchTemplate`, and `AllocationStrategy`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_DescribeTerminationPolicyTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DescribeTerminationPolicyTypes_Examples"></a>

### Example
<a name="API_DescribeTerminationPolicyTypes_Example_1"></a>

This example illustrates one usage of DescribeTerminationPolicyTypes.

#### Sample Request
<a name="API_DescribeTerminationPolicyTypes_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeTerminationPolicyTypes
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTerminationPolicyTypes_Example_1_Response"></a>

```
<DescribeTerminationPolicyTypesResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeTerminationPolicyTypesResult>
    <TerminationPolicyTypes>
      <member>AllocationStrategy</member>
      <member>ClosestToNextInstanceHour</member>
      <member>Default</member>
      <member>NewestInstance</member>
      <member>OldestInstance</member>
      <member>OldestLaunchConfiguration</member>
     <member>OldestLaunchTemplate</member>
    </TerminationPolicyTypes>
  </DescribeTerminationPolicyTypesResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeTerminationPolicyTypesResponse>
```

## See Also
<a name="API_DescribeTerminationPolicyTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeTerminationPolicyTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeTerminationPolicyTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeTerminationPolicyTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeTerminationPolicyTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeTerminationPolicyTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeTerminationPolicyTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeTerminationPolicyTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeTerminationPolicyTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeTerminationPolicyTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeTerminationPolicyTypes)

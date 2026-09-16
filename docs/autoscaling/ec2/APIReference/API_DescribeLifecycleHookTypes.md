---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLifecycleHookTypes.html
---

# DescribeLifecycleHookTypes
<a name="API_DescribeLifecycleHookTypes"></a>

Describes the available types of lifecycle hooks.

The following hook types are supported:
+  `autoscaling:EC2_INSTANCE_LAUNCHING`
+  `autoscaling:EC2_INSTANCE_TERMINATING`

## Response Elements
<a name="API_DescribeLifecycleHookTypes_ResponseElements"></a>

The following element is returned by the service.

 **LifecycleHookTypes.member.N**
The lifecycle hook types.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_DescribeLifecycleHookTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DescribeLifecycleHookTypes_Examples"></a>

### Example
<a name="API_DescribeLifecycleHookTypes_Example_1"></a>

This example illustrates one usage of DescribeLifecycleHookTypes.

#### Sample Request
<a name="API_DescribeLifecycleHookTypes_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeLifecycleHookTypes
&AutoScalingGroupName=my-asg
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeLifecycleHookTypes_Example_1_Response"></a>

```
<DescribeLifecycleHookTypesResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeLifecycleHookTypesResult>
    <LifecycleHookTypes>
      <member>autoscaling:EC2_INSTANCE_LAUNCHING</member>
      <member>autoscaling:EC2_INSTANCE_TERMINATING</member>
    </LifecycleHookTypes>
  </DescribeLifecycleHookTypesResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeLifecycleHookTypesResponse>
```

## See Also
<a name="API_DescribeLifecycleHookTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeLifecycleHookTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeLifecycleHookTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeLifecycleHookTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeLifecycleHookTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeLifecycleHookTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeLifecycleHookTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeLifecycleHookTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeLifecycleHookTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeLifecycleHookTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeLifecycleHookTypes)

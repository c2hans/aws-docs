---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLaunchConfigurations.html
---

# DescribeLaunchConfigurations
<a name="API_DescribeLaunchConfigurations"></a>

Gets information about the launch configurations in the account and Region.

## Request Parameters
<a name="API_DescribeLaunchConfigurations_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **LaunchConfigurationNames.member.N**
The launch configuration names. If you omit this property, all launch configurations are described.
Array Members: Maximum number of 50 items.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** MaxRecords **
The maximum number of items to return with this call. The default value is `50` and the maximum value is `100`.
Type: Integer
Required: No

 ** NextToken **
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Response Elements
<a name="API_DescribeLaunchConfigurations_ResponseElements"></a>

The following elements are returned by the service.

 **LaunchConfigurations.member.N**
The launch configurations.
Type: Array of [LaunchConfiguration](API_LaunchConfiguration.md) objects

 ** NextToken **
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the `NextToken` value when requesting the next set of items. This value is null when there are no more items to return.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_DescribeLaunchConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextToken **
The `NextToken` value is not valid.
 ** message **

HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DescribeLaunchConfigurations_Examples"></a>

### Example
<a name="API_DescribeLaunchConfigurations_Example_1"></a>

This example illustrates one usage of DescribeLaunchConfigurations.

#### Sample Request
<a name="API_DescribeLaunchConfigurations_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeLaunchConfigurations
&LaunchConfigurationNames.member.1=my-lc
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeLaunchConfigurations_Example_1_Response"></a>

```
<DescribeLaunchConfigurationsResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeLaunchConfigurationsResult>
    <LaunchConfigurations>
      <member>
        <KernelId />
        <EbsOptimized>false</EbsOptimized>
        <RamdiskId />
        <UserData />
        <ImageId>ami-0abcdef1234567890</ImageId>
        <BlockDeviceMappings />
        <ClassicLinkVPCSecurityGroups />
        <InstanceType>t2.micro</InstanceType>
        <KeyName />
        <LaunchConfigurationARN>arn:aws:autoscaling:us-east-1:123456789012:launchConfiguration:12345678-1234-1234-1234-123456789012:launchConfigurationName/my-lc</LaunchConfigurationARN>
        <LaunchConfigurationName>my-lc</LaunchConfigurationName>
        <CreatedTime>2022-01-21T23:04:42.200Z</CreatedTime>
        <SecurityGroups>
          <member>sg-1a2b3c4d</member>
        </SecurityGroups>
        <InstanceMonitoring>
          <Enabled>true</Enabled>
        </InstanceMonitoring>
      </member>
    </LaunchConfigurations>
  </DescribeLaunchConfigurationsResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeLaunchConfigurationsResponse>
```

## See Also
<a name="API_DescribeLaunchConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeLaunchConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeLaunchConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeLaunchConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeLaunchConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeLaunchConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeLaunchConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeLaunchConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeLaunchConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeLaunchConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeLaunchConfigurations)

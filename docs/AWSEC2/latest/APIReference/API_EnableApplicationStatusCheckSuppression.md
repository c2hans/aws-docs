---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableApplicationStatusCheckSuppression.html
---

# EnableApplicationStatusCheckSuppression
<a name="API_EnableApplicationStatusCheckSuppression"></a>

Suppresses application status checks for the specified instances. While suppressed, health checks continue to run but do not affect the instance-level application status. The following rules apply:
+ Maximum 100 instance IDs per request.
+ Use `DisableApplicationStatusCheckSuppression` to resume normal health check reporting.
+ If you do not specify `DurationSeconds`, suppression continues indefinitely until you call `DisableApplicationStatusCheckSuppression`.

## Request Parameters
<a name="API_EnableApplicationStatusCheckSuppression_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **DurationSeconds**
The duration, in seconds, for which to suppress application status checks. If omitted, the application status check is suppressed indefinitely until you call `DisableApplicationStatusCheckSuppression`.
Type: Integer
Required: No

 **InstanceId.N**
The IDs of the instances for which to suppress application status checks.
Type: Array of strings
Required: No

## Response Elements
<a name="API_EnableApplicationStatusCheckSuppression_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **successfulResultSet**
The instances for which suppression was successfully enabled.
Type: Array of [SuccessfulSuppressionResponseObject](API_SuccessfulSuppressionResponseObject.md) objects

 **unsuccessfulResultSet**
The instances for which suppression failed to be enabled.
Type: Array of [UnsuccessfulSuppressionResponseObject](API_UnsuccessfulSuppressionResponseObject.md) objects

## Errors
<a name="API_EnableApplicationStatusCheckSuppression_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_EnableApplicationStatusCheckSuppression_Examples"></a>

### To enable application status check suppression
<a name="API_EnableApplicationStatusCheckSuppression_Example_1"></a>

This example enables suppression for the specified instance.

#### Sample Request
<a name="API_EnableApplicationStatusCheckSuppression_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=EnableApplicationStatusCheckSuppression
&InstanceId.1=i-0123456789abcdef0
&DurationSeconds=3600
&AUTHPARAMS
```

#### Sample Response
<a name="API_EnableApplicationStatusCheckSuppression_Example_1_Response"></a>

```
<EnableApplicationStatusCheckSuppressionResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <successfulResultSet>
        <item>
            <instanceId>i-0123456789abcdef0</instanceId>
            <suppressAt>1609459200000</suppressAt>
            <resumeAt>1609462800000</resumeAt>
        </item>
    </successfulResultSet>
</EnableApplicationStatusCheckSuppressionResult>
```

## See Also
<a name="API_EnableApplicationStatusCheckSuppression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/EnableApplicationStatusCheckSuppression)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/EnableApplicationStatusCheckSuppression)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnableApplicationStatusCheckSuppression)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/EnableApplicationStatusCheckSuppression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnableApplicationStatusCheckSuppression)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/EnableApplicationStatusCheckSuppression)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/EnableApplicationStatusCheckSuppression)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/EnableApplicationStatusCheckSuppression)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/EnableApplicationStatusCheckSuppression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnableApplicationStatusCheckSuppression)

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableApplicationStatusCheckSuppression.html
---

# DisableApplicationStatusCheckSuppression
<a name="API_DisableApplicationStatusCheckSuppression"></a>

Disables suppression of application status checks for the specified instances. After suppression is disabled, health check results resume affecting the instance-level application status. You can specify a maximum of 100 instance IDs for each request.

## Request Parameters
<a name="API_DisableApplicationStatusCheckSuppression_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a request with the same token, the service ignores the request but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId.N**
The IDs of the instances for which to disable application status check suppression.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DisableApplicationStatusCheckSuppression_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **successfulResultSet**
The instances for which suppression was successfully disabled.
Type: Array of [SuccessfulSuppressionResponseObject](API_SuccessfulSuppressionResponseObject.md) objects

 **unsuccessfulResultSet**
The instances for which suppression failed to be disabled.
Type: Array of [UnsuccessfulSuppressionResponseObject](API_UnsuccessfulSuppressionResponseObject.md) objects

## Errors
<a name="API_DisableApplicationStatusCheckSuppression_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisableApplicationStatusCheckSuppression_Examples"></a>

### To disable application status check suppression
<a name="API_DisableApplicationStatusCheckSuppression_Example_1"></a>

This example disables suppression for the specified instance.

#### Sample Request
<a name="API_DisableApplicationStatusCheckSuppression_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisableApplicationStatusCheckSuppression
&InstanceId.1=i-0123456789abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisableApplicationStatusCheckSuppression_Example_1_Response"></a>

```
<DisableApplicationStatusCheckSuppressionResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <successfulResultSet>
        <item>
            <instanceId>i-0123456789abcdef0</instanceId>
            <suppressAt>1609459200000</suppressAt>
            <resumeAt>1609462800000</resumeAt>
        </item>
    </successfulResultSet>
</DisableApplicationStatusCheckSuppressionResult>
```

## See Also
<a name="API_DisableApplicationStatusCheckSuppression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisableApplicationStatusCheckSuppression)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisableApplicationStatusCheckSuppression)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisableApplicationStatusCheckSuppression)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisableApplicationStatusCheckSuppression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisableApplicationStatusCheckSuppression)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisableApplicationStatusCheckSuppression)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisableApplicationStatusCheckSuppression)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisableApplicationStatusCheckSuppression)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisableApplicationStatusCheckSuppression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisableApplicationStatusCheckSuppression)

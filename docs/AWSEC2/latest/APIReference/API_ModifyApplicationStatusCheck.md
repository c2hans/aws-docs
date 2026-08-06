---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyApplicationStatusCheck.html
---

# ModifyApplicationStatusCheck
<a name="API_ModifyApplicationStatusCheck"></a>

Modifies an existing application status check. You can update the protocol, port, path, thresholds, and other configuration settings. The following rules apply:
+ The application status check must exist and belong to your account.
+ Changes take effect on the next health check interval.

## Request Parameters
<a name="API_ModifyApplicationStatusCheck_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Aggregation**
The aggregation setting for the application status check. When set to `included`, the result of this check contributes to the instance-level application status reported by `DescribeApplicationStatus`. When set to `excluded`, the check runs independently and does not affect the instance-level status. Valid values: `included` \| `excluded`.
Type: String
Valid Values: `included | excluded`
Required: No

 **ApplicationStatusCheckId**
The ID of the application status check to modify.
Type: String
Required: Yes

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DeviceIndex**
The index of the network device to use for the health check.
Type: Integer
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FailureThreshold**
The number of consecutive failed health checks before the application status is considered impaired.
Type: Integer
Required: No

 **HealthCheckPath.N**
The health check paths to use for the application status check.
Type: Array of [HealthCheckPathRequestObject](API_HealthCheckPathRequestObject.md) objects
Required: No

 **InitializationGracePeriodSeconds**
The number of seconds to wait before starting health checks after an instance is launched. Valid values: 1 to 600.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 600.
Required: No

 **Interval**
The interval, in seconds, between health checks.
Type: Integer
Required: No

 **IpScope**
The IP scope to use for the health check. Valid values: `private` \| `public`.
Type: String
Valid Values: `private`
Required: No

 **IpVersion**
The IP version to use for the health check. Valid values: `ipv4`.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 **Path**
The URL path to use for the health check HTTP request (for example, `/health` or `/status`).
Type: String
Required: No

 **Port**
The port to use for the health check. Valid values: 1 to 65535.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 **Protocol**
The protocol to use for the health check. Valid values: `http` \| `https`.
Type: String
Valid Values: `http | https`
Required: No

 **StatusCodeMatcher**
The HTTP status codes that indicate a successful health check response.
Type: String
Required: No

 **SuccessThreshold**
The number of consecutive successful health checks before the application status is considered healthy.
Type: Integer
Required: No

 **Timeout**
The amount of time, in seconds, to wait for a health check response before considering it failed.
Type: Integer
Required: No

## Response Elements
<a name="API_ModifyApplicationStatusCheck_ResponseElements"></a>

The following elements are returned by the service.

 **applicationStatusCheck**
Information about the modified application status check.
Type: [ApplicationStatusCheckResponseObject](API_ApplicationStatusCheckResponseObject.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyApplicationStatusCheck_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyApplicationStatusCheck_Examples"></a>

### To modify an application status check
<a name="API_ModifyApplicationStatusCheck_Example_1"></a>

This example modifies the port of an existing application status check.

#### Sample Request
<a name="API_ModifyApplicationStatusCheck_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyApplicationStatusCheck
&ApplicationStatusCheckId=asc-0123456789abcdef0
&Port=8080
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyApplicationStatusCheck_Example_1_Response"></a>

```
<ModifyApplicationStatusCheckResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <applicationStatusCheck>
        <applicationStatusCheckId>asc-0123456789abcdef0</applicationStatusCheckId>
        <protocol>http</protocol>
        <port>8080</port>
    </applicationStatusCheck>
</ModifyApplicationStatusCheckResult>
```

## See Also
<a name="API_ModifyApplicationStatusCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyApplicationStatusCheck)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyApplicationStatusCheck)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyApplicationStatusCheck)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyApplicationStatusCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyApplicationStatusCheck)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyApplicationStatusCheck)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyApplicationStatusCheck)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyApplicationStatusCheck)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyApplicationStatusCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyApplicationStatusCheck)

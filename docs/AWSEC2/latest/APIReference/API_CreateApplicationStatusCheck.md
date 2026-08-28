---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateApplicationStatusCheck.html
---

# CreateApplicationStatusCheck
<a name="API_CreateApplicationStatusCheck"></a>

Creates an application status check for monitoring the health of applications running on your instances. You can configure the protocol, port, path, and thresholds for the health check. The following rules apply:
+ You can create a maximum of 50 application status checks for each account.
+ You must associate the check with instances or tags using `AssociateApplicationStatusCheck` before health checks start.
+ You must set the `Timeout` value to less than the `Interval` value.
+ You must start the `Path` with a forward slash (`/`). Default: `/`.
+ You can specify `Aggregation` as `included` or `excluded`. If you do not specify a value, it defaults to `included`, which means the check contributes to the instance-level application status.
+ You can use the following default values: `Interval` is 60 seconds, `Timeout` is 6 seconds, `FailureThreshold` is 2, `SuccessThreshold` is 2, `StatusCodeMatcher` is `200`, `InitializationGracePeriodSeconds` is 300 seconds.
+ You can tag the application status check during creation. For more information, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html).

## Request Parameters
<a name="API_CreateApplicationStatusCheck_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Aggregation**
The aggregation setting for the application status check. When set to `included`, the result of this check contributes to the instance-level application status reported by `DescribeApplicationStatus`. When set to `excluded`, the check runs independently and does not affect the instance-level status. Valid values: `included` \| `excluded`.
Type: String
Valid Values: `included | excluded`
Required: No

 **ClientToken**
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a request with the same token, the service ignores the request but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DeviceIndex**
The index of the network device to use for the health check. The value must be greater than or equal to 0.
Type: Integer
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FailureThreshold**
The number of consecutive failed health checks before the application status is considered impaired. The value must be greater than 0.
Type: Integer
Required: No

 **HealthCheckPath.N**
The health check paths to use for the application status check. Health check paths define the network path from a source subnet to one or more destination subnets for cross-Availability Zone or Availability Zone to Local Zone health checking. If omitted, health checks are performed in the same subnet as the instance.
Type: Array of [HealthCheckPathRequestObject](API_HealthCheckPathRequestObject.md) objects
Required: No

 **InitializationGracePeriodSeconds**
The number of seconds to wait before starting health checks after an instance is launched. Valid values: 1 to 600.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 600.
Required: No

 **Interval**
The interval, in seconds, between health checks. Valid value: 60.
Type: Integer
Required: No

 **IpScope**
The IP scope to use for the health check. Valid value: `private`.
Type: String
Valid Values: `private`
Required: No

 **IpVersion**
The IP version to use for the health check. Valid values: `ipv4` and `ipv6`.
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
Required: Yes

 **Protocol**
The protocol to use for the health check. Valid values: `http` \| `https`.
Type: String
Valid Values: `http | https`
Required: Yes

 **StatusCodeMatcher**
The HTTP status codes that indicate a successful health check response. Specify a comma-separated list of individual status codes or ranges, for example, `200,202,300-399`. For a range, the first value must be less than the second value. Maximum length: 64 characters. Default: `200`.
Type: String
Required: No

 **SuccessThreshold**
The number of consecutive successful health checks before the application status is considered healthy. The value must be greater than 0.
Type: Integer
Required: No

 **TagSpecification.N**
The tags to apply to the application status check.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **Timeout**
The amount of time, in seconds, to wait for a health check response before considering it failed. Valid values: 1 to 30. The value must be less than `Interval`.
Type: Integer
Required: No

## Response Elements
<a name="API_CreateApplicationStatusCheck_ResponseElements"></a>

The following elements are returned by the service.

 **applicationStatusCheck**
Information about the application status check.
Type: [ApplicationStatusCheckResponseObject](API_ApplicationStatusCheckResponseObject.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateApplicationStatusCheck_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateApplicationStatusCheck_Examples"></a>

### To create an application status check
<a name="API_CreateApplicationStatusCheck_Example_1"></a>

This example creates an application status check with HTTP protocol on port 80.

#### Sample Request
<a name="API_CreateApplicationStatusCheck_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateApplicationStatusCheck
&Protocol=http
&Port=80
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateApplicationStatusCheck_Example_1_Response"></a>

```
<CreateApplicationStatusCheckResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <applicationStatusCheck>
        <applicationStatusCheckId>asc-0123456789abcdef0</applicationStatusCheckId>
        <protocol>http</protocol>
        <port>80</port>
    </applicationStatusCheck>
</CreateApplicationStatusCheckResult>
```

## See Also
<a name="API_CreateApplicationStatusCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateApplicationStatusCheck)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateApplicationStatusCheck)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateApplicationStatusCheck)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateApplicationStatusCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateApplicationStatusCheck)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateApplicationStatusCheck)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateApplicationStatusCheck)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateApplicationStatusCheck)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateApplicationStatusCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateApplicationStatusCheck)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

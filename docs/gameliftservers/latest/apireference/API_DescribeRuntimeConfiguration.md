---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeRuntimeConfiguration.html
---

# DescribeRuntimeConfiguration
<a name="API_DescribeRuntimeConfiguration"></a>

 **This API works with the following fleet types:** EC2

Retrieves a fleet's runtime configuration settings. The runtime configuration determines which server processes run, and how, on computes in the fleet. For managed EC2 fleets, the runtime configuration describes server processes that run on each fleet instance. You can update a fleet's runtime configuration at any time using [UpdateRuntimeConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateRuntimeConfiguration.html).

To get the current runtime configuration for a fleet, provide the fleet ID.

If successful, a `RuntimeConfiguration` object is returned for the requested fleet. If the requested fleet has been deleted, the result set is empty.

 **Learn more**

 [Setting up Amazon GameLift Servers fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

 [Running multiple processes on a fleet](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-multiprocess.html)

## Request Syntax
<a name="API_DescribeRuntimeConfiguration_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeRuntimeConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_DescribeRuntimeConfiguration_RequestSyntax) **   <a name="gameliftservers-DescribeRuntimeConfiguration-request-FleetId"></a>
A unique identifier for the fleet to get the runtime configuration for. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

## Response Syntax
<a name="API_DescribeRuntimeConfiguration_ResponseSyntax"></a>

```
{
   "RuntimeConfiguration": {
      "GameSessionActivationTimeoutSeconds": number,
      "MaxConcurrentGameSessionActivations": number,
      "ServerProcesses": [
         {
            "ConcurrentExecutions": number,
            "LaunchPath": "string",
            "Parameters": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeRuntimeConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RuntimeConfiguration](#API_DescribeRuntimeConfiguration_ResponseSyntax) **   <a name="gameliftservers-DescribeRuntimeConfiguration-response-RuntimeConfiguration"></a>
Instructions that describe how server processes are launched and maintained on computes in the fleet.
Type: [RuntimeConfiguration](API_RuntimeConfiguration.md) object

## Errors
<a name="API_DescribeRuntimeConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_DescribeRuntimeConfiguration_Examples"></a>

### Request the runtime configuration for a fleet
<a name="API_DescribeRuntimeConfiguration_Example_1"></a>

This example retrieves the current runtime configuration for a specified fleet. As shown, the requested fleet is configured to run four concurrent processes of the game server executable, one with debug mode turned on. The property `MaxConcurrentGameSessionActivations` is set to the default value, which places no limit on concurrent activations.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeRuntimeConfiguration_Example_1_Request"></a>

```
{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
}
```

#### Sample Response
<a name="API_DescribeRuntimeConfiguration_Example_1_Response"></a>

```
{
    "RuntimeConfiguration": {
        "ServerProcesses": [
            {
                "LaunchPath": "C:\game\Bin64.Release.Dedicated\MegaFrogRace_Server.exe",
                "Parameters": "+gamelift_start_server",
                "ConcurrentExecutions": 3
            },
            {
                "LaunchPath": "C:\game\Bin64.Release.Dedicated\MegaFrogRace_Server.exe",
                "Parameters": "+gamelift_start_server +debug",
                "ConcurrentExecutions": 1
            }
        ],
        "MaxConcurrentGameSessionActivations": 2147483647,
        "GameSessionActivationTimeoutSeconds": 300
    }
}
```

## See Also
<a name="API_DescribeRuntimeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeRuntimeConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeRuntimeConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeRuntimeConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeRuntimeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeRuntimeConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeRuntimeConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeRuntimeConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeRuntimeConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeRuntimeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeRuntimeConfiguration)

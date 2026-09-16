---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateRuntimeConfiguration.html
---

# UpdateRuntimeConfiguration
<a name="API_UpdateRuntimeConfiguration"></a>

 **This API works with the following fleet types:** EC2

Updates the runtime configuration for the specified fleet. The runtime configuration tells Amazon GameLift Servers how to launch server processes on computes in managed EC2 and Anywhere fleets. You can update a fleet's runtime configuration at any time after the fleet is created; it does not need to be in `ACTIVE` status.

To update runtime configuration, specify the fleet ID and provide a `RuntimeConfiguration` with an updated set of server process configurations.

If successful, the fleet's runtime configuration settings are updated. Fleet computes that run game server processes regularly check for and receive updated runtime configurations. The computes immediately take action to comply with the new configuration by launching new server processes or by not replacing existing processes when they shut down. Updating a fleet's runtime configuration never affects existing server processes.

 **Learn more**

 [Setting up Amazon GameLift Servers fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

## Request Syntax
<a name="API_UpdateRuntimeConfiguration_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "RuntimeConfiguration": {
      "GameSessionActivationTimeoutSeconds": {{number}},
      "MaxConcurrentGameSessionActivations": {{number}},
      "ServerProcesses": [
         {
            "ConcurrentExecutions": {{number}},
            "LaunchPath": "{{string}}",
            "Parameters": "{{string}}"
         }
      ]
   }
}
```

## Request Parameters
<a name="API_UpdateRuntimeConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_UpdateRuntimeConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateRuntimeConfiguration-request-FleetId"></a>
A unique identifier for the fleet to update runtime configuration for. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [RuntimeConfiguration](#API_UpdateRuntimeConfiguration_RequestSyntax) **   <a name="gameliftservers-UpdateRuntimeConfiguration-request-RuntimeConfiguration"></a>
Instructions for launching server processes on fleet computes. Server processes run either a custom game build executable or a Amazon GameLift Servers Realtime script. The runtime configuration lists the types of server processes to run, how to launch them, and the number of processes to run concurrently.
Type: [RuntimeConfiguration](API_RuntimeConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateRuntimeConfiguration_ResponseSyntax"></a>

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
<a name="API_UpdateRuntimeConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RuntimeConfiguration](#API_UpdateRuntimeConfiguration_ResponseSyntax) **   <a name="gameliftservers-UpdateRuntimeConfiguration-response-RuntimeConfiguration"></a>
The runtime configuration currently in use by computes in the fleet. If the update is successful, all property changes are shown.
Type: [RuntimeConfiguration](API_RuntimeConfiguration.md) object

## Errors
<a name="API_UpdateRuntimeConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidFleetStatusException **
The requested operation would cause a conflict with the current state of a resource associated with the request and/or the fleet. Resolve the conflict before retrying.
HTTP Status Code: 400

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** LimitExceededException **
The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRuntimeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/UpdateRuntimeConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/UpdateRuntimeConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/UpdateRuntimeConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/UpdateRuntimeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/UpdateRuntimeConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/UpdateRuntimeConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/UpdateRuntimeConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/UpdateRuntimeConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/UpdateRuntimeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/UpdateRuntimeConfiguration)

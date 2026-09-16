---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StartFleetActions.html
---

# StartFleetActions
<a name="API_StartFleetActions"></a>

 **This API works with the following fleet types:** EC2, Container

Resumes certain types of activity on fleet instances that were suspended with [StopFleetActions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StopFleetActions.html). For multi-location fleets, fleet actions are managed separately for each location. Currently, this operation is used to restart a fleet's auto-scaling activity.

This operation can be used in the following ways:
+ To restart actions on instances in the fleet's home Region, provide a fleet ID and the type of actions to resume.
+ To restart actions on instances in one of the fleet's remote locations, provide a fleet ID, a location name, and the type of actions to resume.

If successful, Amazon GameLift Servers once again initiates scaling events as triggered by the fleet's scaling policies. If actions on the fleet location were never stopped, this operation will have no effect.

 **Learn more**

 [Setting up Amazon GameLift Servers fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

## Request Syntax
<a name="API_StartFleetActions_RequestSyntax"></a>

```
{
   "Actions": [ "{{string}}" ],
   "FleetId": "{{string}}",
   "Location": "{{string}}"
}
```

## Request Parameters
<a name="API_StartFleetActions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Actions](#API_StartFleetActions_RequestSyntax) **   <a name="gameliftservers-StartFleetActions-request-Actions"></a>
List of actions to restart on the fleet.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `AUTO_SCALING`
Required: Yes

 ** [FleetId](#API_StartFleetActions_RequestSyntax) **   <a name="gameliftservers-StartFleetActions-request-FleetId"></a>
A unique identifier for the fleet to restart actions on. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [Location](#API_StartFleetActions_RequestSyntax) **   <a name="gameliftservers-StartFleetActions-request-Location"></a>
The fleet location to restart fleet actions for. Specify a location in the form of an AWS Region code, such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

## Response Syntax
<a name="API_StartFleetActions_ResponseSyntax"></a>

```
{
   "FleetArn": "string",
   "FleetId": "string"
}
```

## Response Elements
<a name="API_StartFleetActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetArn](#API_StartFleetActions_ResponseSyntax) **   <a name="gameliftservers-StartFleetActions-response-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [FleetId](#API_StartFleetActions_ResponseSyntax) **   <a name="gameliftservers-StartFleetActions-response-FleetId"></a>
A unique identifier for the fleet to restart actions on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`

## Errors
<a name="API_StartFleetActions_Errors"></a>

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

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_StartFleetActions_Examples"></a>

### Restart automatic scaling activity for a fleet
<a name="API_StartFleetActions_Example_1"></a>

In this example, we want to resume the use a fleet's scaling policies that had be previously suspended. Once started, the scaling policies immediately begin tracking their respective metrics.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_StartFleetActions_Example_1_Request"></a>

```
{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "Actions": ["AUTO_SCALING"]
}
```

#### Sample Response
<a name="API_StartFleetActions_Example_1_Response"></a>

```
{
   "FleetArn": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
   "FleetId": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
}
```

## See Also
<a name="API_StartFleetActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/StartFleetActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/StartFleetActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/StartFleetActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/StartFleetActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/StartFleetActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/StartFleetActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/StartFleetActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/StartFleetActions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/StartFleetActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/StartFleetActions)

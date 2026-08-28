---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteFleetLocations.html
---

# DeleteFleetLocations
<a name="API_DeleteFleetLocations"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Removes locations from a multi-location fleet. When deleting a location, all game server process and all instances that are still active in the location are shut down.

To delete fleet locations, identify the fleet ID and provide a list of the locations to be deleted.

If successful, GameLift sets the location status to `DELETING`, and begins to shut down existing server processes and terminate instances in each location being deleted. When completed, the location status changes to `TERMINATED`.

 **Learn more**

 [Setting up Amazon GameLift Servers fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

## Request Syntax
<a name="API_DeleteFleetLocations_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "Locations": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DeleteFleetLocations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_DeleteFleetLocations_RequestSyntax) **   <a name="gameliftservers-DeleteFleetLocations-request-FleetId"></a>
A unique identifier for the fleet to delete locations for. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [Locations](#API_DeleteFleetLocations_RequestSyntax) **   <a name="gameliftservers-DeleteFleetLocations-request-Locations"></a>
The list of fleet locations to delete. Specify locations in the form of an AWS Region code, such as `us-west-2`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteFleetLocations_ResponseSyntax"></a>

```
{
   "FleetArn": "string",
   "FleetId": "string",
   "LocationStates": [
      {
         "Location": "string",
         "PlayerGatewayStatus": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DeleteFleetLocations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetArn](#API_DeleteFleetLocations_ResponseSyntax) **   <a name="gameliftservers-DeleteFleetLocations-response-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [FleetId](#API_DeleteFleetLocations_ResponseSyntax) **   <a name="gameliftservers-DeleteFleetLocations-response-FleetId"></a>
A unique identifier for the fleet that location attributes are being deleted for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [LocationStates](#API_DeleteFleetLocations_ResponseSyntax) **   <a name="gameliftservers-DeleteFleetLocations-response-LocationStates"></a>
The remote locations that are being deleted, with each location status set to `DELETING`.
Type: Array of [LocationState](API_LocationState.md) objects

## Errors
<a name="API_DeleteFleetLocations_Errors"></a>

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

## See Also
<a name="API_DeleteFleetLocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DeleteFleetLocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DeleteFleetLocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DeleteFleetLocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DeleteFleetLocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DeleteFleetLocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DeleteFleetLocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DeleteFleetLocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DeleteFleetLocations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DeleteFleetLocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DeleteFleetLocations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

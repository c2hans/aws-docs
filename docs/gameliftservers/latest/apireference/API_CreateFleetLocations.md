---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateFleetLocations.html
---

# CreateFleetLocations
<a name="API_CreateFleetLocations"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Adds remote locations to an EC2 and begins populating the new locations with instances. The new instances conform to the fleet's instance type, auto-scaling, and other configuration settings.

**Note**
You can't add remote locations to a fleet that resides in an AWS Region that doesn't support multiple locations. Fleets created prior to March 2021 can't support multiple locations.

To add fleet locations, specify the fleet to be updated and provide a list of one or more locations.

If successful, this operation returns the list of added locations with their status set to `NEW`. Amazon GameLift Servers initiates the process of starting an instance in each added location. You can track the status of each new location by monitoring location creation events using [DescribeFleetEvents](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetEvents.html).

 **Learn more**

 [Setting up fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

 [Update fleet locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-editing.html#fleets-update-locations)

 [ Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting.

## Request Syntax
<a name="API_CreateFleetLocations_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "Locations": [
      {
         "Location": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateFleetLocations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_CreateFleetLocations_RequestSyntax) **   <a name="gameliftservers-CreateFleetLocations-request-FleetId"></a>
A unique identifier for the fleet to add locations to. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [Locations](#API_CreateFleetLocations_RequestSyntax) **   <a name="gameliftservers-CreateFleetLocations-request-Locations"></a>
A list of locations to deploy additional instances to and manage as part of the fleet. You can add any Amazon GameLift Servers-supported AWS Region as a remote location, in the form of an AWS Region code such as `us-west-2`.
Type: Array of [LocationConfiguration](API_LocationConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_CreateFleetLocations_ResponseSyntax"></a>

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
<a name="API_CreateFleetLocations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetArn](#API_CreateFleetLocations_ResponseSyntax) **   <a name="gameliftservers-CreateFleetLocations-response-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [FleetId](#API_CreateFleetLocations_ResponseSyntax) **   <a name="gameliftservers-CreateFleetLocations-response-FleetId"></a>
A unique identifier for the fleet that was updated with new locations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [LocationStates](#API_CreateFleetLocations_ResponseSyntax) **   <a name="gameliftservers-CreateFleetLocations-response-LocationStates"></a>
The remote locations that are being added to the fleet, and the life-cycle status of each location. For new locations, the status is set to `NEW`. During location creation, Amazon GameLift Servers updates each location's status as instances are deployed there and prepared for game hosting. This list does not include the fleet home Region or any remote locations that were already added to the fleet.
Type: Array of [LocationState](API_LocationState.md) objects

## Errors
<a name="API_CreateFleetLocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.

HTTP Status Code: 400

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

 ** NotReadyException **
 The operation failed because Amazon GameLift Servers has not yet finished validating this compute. We recommend attempting 8 to 10 retries over 3 to 5 minutes with [exponential backoffs and jitter](http://aws.amazon.com/blogs/https:/aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/).
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_CreateFleetLocations_Examples"></a>

### Add remote locations to an existing fleet
<a name="API_CreateFleetLocations_Example_1"></a>

This example adds three five remote locations to a fleet that resides in the AWS Region `eu-central-1`. As shown, the status of each new location is initially set to `NEW`.

#### Sample Request
<a name="API_CreateFleetLocations_Example_1_Request"></a>

```
{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "Locations": [
        { "Location": "me-south-1"},
        { "Location": "eu-west-2"},
        { "Location": "eu-south-1"},
        { "Location": "eu-west-3"},
        { "Location": "eu-north-1"}
    ]
}
```

#### Sample Response
<a name="API_CreateFleetLocations_Example_1_Response"></a>

```
{
    "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "LocationStates": [
        {
            "Location": "eu-north-1",
            "Status": "NEW"
        },
        {
            "Location": "eu-west-3",
            "Status": "NEW"
        },
        {
            "Location": "eu-south-1",
            "Status": "NEW"
        },
        {
            "Location": "eu-west-2",
            "Status": "NEW"
        },
        {
            "Location": "me-south-1",
            "Status": "NEW"
        }
    ]
}
```

## See Also
<a name="API_CreateFleetLocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreateFleetLocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreateFleetLocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreateFleetLocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreateFleetLocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreateFleetLocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreateFleetLocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreateFleetLocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreateFleetLocations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreateFleetLocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreateFleetLocations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetLocationAttributes.html
---

# DescribeFleetLocationAttributes
<a name="API_DescribeFleetLocationAttributes"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves information on a fleet's remote locations, including life-cycle status and any suspended fleet activity.

This operation can be used in the following ways:
+ To get data for specific locations, provide a fleet identifier and a list of locations. Location data is returned in the order that it is requested.
+ To get data for all locations, provide a fleet identifier only. Location data is returned in no particular order.

When requesting attributes for multiple locations, use the pagination parameters to retrieve results as a set of sequential pages.

If successful, a `LocationAttributes` object is returned for each requested location. If the fleet does not have a requested location, no information is returned.

 **Learn more**

 [Setting up Amazon GameLift Servers fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

 [ Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting

## Request Syntax
<a name="API_DescribeFleetLocationAttributes_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "Limit": {{number}},
   "Locations": [ "{{string}}" ],
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFleetLocationAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_DescribeFleetLocationAttributes_RequestSyntax) **   <a name="gameliftservers-DescribeFleetLocationAttributes-request-FleetId"></a>
A unique identifier for the fleet to retrieve remote locations for. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [Limit](#API_DescribeFleetLocationAttributes_RequestSyntax) **   <a name="gameliftservers-DescribeFleetLocationAttributes-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages. This limit is not currently enforced.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Locations](#API_DescribeFleetLocationAttributes_RequestSyntax) **   <a name="gameliftservers-DescribeFleetLocationAttributes-request-Locations"></a>
A list of fleet locations to retrieve information for. Specify locations in the form of an AWS Region code, such as `us-west-2`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** [NextToken](#API_DescribeFleetLocationAttributes_RequestSyntax) **   <a name="gameliftservers-DescribeFleetLocationAttributes-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_DescribeFleetLocationAttributes_ResponseSyntax"></a>

```
{
   "FleetArn": "string",
   "FleetId": "string",
   "LocationAttributes": [
      {
         "LocationState": {
            "Location": "string",
            "PlayerGatewayStatus": "string",
            "Status": "string"
         },
         "StoppedActions": [ "string" ],
         "UpdateStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeFleetLocationAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetArn](#API_DescribeFleetLocationAttributes_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetLocationAttributes-response-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [FleetId](#API_DescribeFleetLocationAttributes_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetLocationAttributes-response-FleetId"></a>
A unique identifier for the fleet that location attributes were requested for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [LocationAttributes](#API_DescribeFleetLocationAttributes_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetLocationAttributes-response-LocationAttributes"></a>
 Location-specific information on the requested fleet's remote locations.
Type: Array of [LocationAttributes](API_LocationAttributes.md) objects

 ** [NextToken](#API_DescribeFleetLocationAttributes_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetLocationAttributes-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DescribeFleetLocationAttributes_Errors"></a>

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
<a name="API_DescribeFleetLocationAttributes_Examples"></a>

### Retrieve remote fleet locations
<a name="API_DescribeFleetLocationAttributes_Example_1"></a>

This example retrieves information on all remote locations for a fleet. The requested fleet's home Region is `us-west-2`. It can deploy instances in the following AWS Regions: `us-west-2`, `us-west-1`, and `ca-central-1`. In this example, auto-scaling has been suspended in `ca-central-1`, and there is a fleet update that has not yet been completed for that location.

#### Sample Request
<a name="API_DescribeFleetLocationAttributes_Example_1_Request"></a>

```
{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
}
```

#### Sample Response
<a name="API_DescribeFleetLocationAttributes_Example_1_Response"></a>

```
{
   "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
   "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
   "LocationAttributes": [
      {
         "LocationState": {
            "Location": "us-west-1",
            "Status": "ACTIVE"
         }
      },
      {
         "LocationState": {
            "Location": "ca-central-1",
            "Status": "ACTIVE"
         },
         "StoppedActions": [ "AUTO_SCALING" ],
         "UpdateStatus": "PENDING_UPDATE"
      }
   ],
   "NextToken": "string"
}
```

## See Also
<a name="API_DescribeFleetLocationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeFleetLocationAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeFleetLocationAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeFleetLocationAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeFleetLocationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeFleetLocationAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeFleetLocationAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeFleetLocationAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeFleetLocationAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeFleetLocationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeFleetLocationAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

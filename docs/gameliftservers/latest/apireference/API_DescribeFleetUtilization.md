---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetUtilization.html
---

# DescribeFleetUtilization
<a name="API_DescribeFleetUtilization"></a>

 **This API works with the following fleet types:** EC2, Container

Retrieves utilization statistics for one or more fleets. Utilization data provides a snapshot of how the fleet's hosting resources are currently being used. For fleets with remote locations, this operation retrieves data for the fleet's home Region only. See [DescribeFleetLocationUtilization](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationUtilization.html) to get utilization statistics for a fleet's remote locations.

This operation can be used in the following ways:
+ To get utilization data for one or more specific fleets, provide a list of fleet IDs or fleet ARNs.
+ To get utilization data for all fleets, do not provide a fleet identifier.

When requesting multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages.

If successful, a [FleetUtilization](https://docs.aws.amazon.com/gamelift/latest/apireference/API_FleetUtilization.html) object is returned for each requested fleet ID, unless the fleet identifier is not found. Each fleet utilization object includes a `Location` property, which is set to the fleet's home Region.

**Note**
Some API operations may limit the number of fleet IDs allowed in one request. If a request exceeds this limit, the request fails and the error message includes the maximum allowed.

 **Learn more**

 [Setting up Amazon GameLift Servers Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

 [GameLift Metrics for Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet)

## Request Syntax
<a name="API_DescribeFleetUtilization_RequestSyntax"></a>

```
{
   "FleetIds": [ "{{string}}" ],
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFleetUtilization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetIds](#API_DescribeFleetUtilization_RequestSyntax) **   <a name="gameliftservers-DescribeFleetUtilization-request-FleetIds"></a>
A unique identifier for the fleet to retrieve utilization data for. You can use either the fleet ID or ARN value. To retrieve attributes for all current fleets, do not include this parameter.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** [Limit](#API_DescribeFleetUtilization_RequestSyntax) **   <a name="gameliftservers-DescribeFleetUtilization-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_DescribeFleetUtilization_RequestSyntax) **   <a name="gameliftservers-DescribeFleetUtilization-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_DescribeFleetUtilization_ResponseSyntax"></a>

```
{
   "FleetUtilization": [
      {
         "ActiveGameSessionCount": number,
         "ActiveServerProcessCount": number,
         "CurrentPlayerSessionCount": number,
         "FleetArn": "string",
         "FleetId": "string",
         "Location": "string",
         "MaximumPlayerSessionCount": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeFleetUtilization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetUtilization](#API_DescribeFleetUtilization_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetUtilization-response-FleetUtilization"></a>
A collection of objects containing utilization information for each requested fleet ID. Utilization objects are returned only for fleets that currently exist.
Type: Array of [FleetUtilization](API_FleetUtilization.md) objects

 ** [NextToken](#API_DescribeFleetUtilization_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetUtilization-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DescribeFleetUtilization_Errors"></a>

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
<a name="API_DescribeFleetUtilization_Examples"></a>

### Request utilization data for a list of fleets
<a name="API_DescribeFleetUtilization_Example_1"></a>

This example retrieves current usage information for a specific fleet. The fleet's home Region is `us-west-2`.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeFleetUtilization_Example_1_Request"></a>

```
{
    "FleetIds": ["fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"]
}
```

#### Sample Response
<a name="API_DescribeFleetUtilization_Example_1_Response"></a>

```
{
    "FleetUtilization": [
        {
            "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
            "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
            "ActiveServerProcessCount": 100,
            "ActiveGameSessionCount": 62,
            "CurrentPlayerSessionCount": 329,
            "MaximumPlayerSessionCount": 1000,
            "Location": "us-west-2"
        }
    ]
}
```

### Request utilization data for all fleets
<a name="API_DescribeFleetUtilization_Example_2"></a>

This example returns fleet usage data for all fleets with any status. This example uses the pagination parameters to return results for two fleets at a time. The home Region for both fleets is `us-west-2`.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeFleetUtilization_Example_2_Request"></a>

```
{
    "Limit": 2
    "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE1"
}
```

#### Sample Response
<a name="API_DescribeFleetUtilization_Example_2_Response"></a>

```
{
    "FleetUtilization": [
        {
            "FleetId": "fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
            "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
            "ActiveServerProcessCount": 100,
            "ActiveGameSessionCount": 13,
            "CurrentPlayerSessionCount": 98,
            "MaximumPlayerSessionCount": 1000,
            "Location": "us-west-2"
        },
        {
            "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
            "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
            "ActiveServerProcessCount": 100,
            "ActiveGameSessionCount": 62,
            "CurrentPlayerSessionCount": 329,
            "MaximumPlayerSessionCount": 1000,
            "Location": "us-west-2"
        }
    ],
    "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE2"
}
```

## See Also
<a name="API_DescribeFleetUtilization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeFleetUtilization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeFleetUtilization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeFleetUtilization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeFleetUtilization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeFleetUtilization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeFleetUtilization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeFleetUtilization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeFleetUtilization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeFleetUtilization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeFleetUtilization)

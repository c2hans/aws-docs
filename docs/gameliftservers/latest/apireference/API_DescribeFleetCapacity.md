---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetCapacity.html
---

# DescribeFleetCapacity
<a name="API_DescribeFleetCapacity"></a>

 **This API works with the following fleet types:** EC2, Container

Retrieves the resource capacity settings for one or more fleets. For a container fleet, this operation also returns counts for game server container groups.

With multi-location fleets, this operation retrieves data for the fleet's home Region only. To retrieve capacity for remote locations, see [https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html).

This operation can be used in the following ways:
+ To get capacity data for one or more specific fleets, provide a list of fleet IDs or fleet ARNs.
+ To get capacity data for all fleets, do not provide a fleet identifier.

When requesting multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages.

If successful, a `FleetCapacity` object is returned for each requested fleet ID. Each `FleetCapacity` object includes a `Location` property, which is set to the fleet's home Region. Capacity values are returned only for fleets that currently exist.

**Note**
Some API operations may limit the number of fleet IDs that are allowed in one request. If a request exceeds this limit, the request fails and the error message includes the maximum allowed.

 **Learn more**

 [Setting up Amazon GameLift Servers fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

 [GameLift metrics for fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet)

## Request Syntax
<a name="API_DescribeFleetCapacity_RequestSyntax"></a>

```
{
   "FleetIds": [ "{{string}}" ],
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFleetCapacity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetIds](#API_DescribeFleetCapacity_RequestSyntax) **   <a name="gameliftservers-DescribeFleetCapacity-request-FleetIds"></a>
A unique identifier for the fleet to retrieve capacity information for. You can use either the fleet ID or ARN value. Leave this parameter empty to retrieve capacity information for all fleets.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** [Limit](#API_DescribeFleetCapacity_RequestSyntax) **   <a name="gameliftservers-DescribeFleetCapacity-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_DescribeFleetCapacity_RequestSyntax) **   <a name="gameliftservers-DescribeFleetCapacity-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_DescribeFleetCapacity_ResponseSyntax"></a>

```
{
   "FleetCapacity": [
      {
         "FleetArn": "string",
         "FleetId": "string",
         "GameServerContainerGroupCounts": {
            "ACTIVE": number,
            "IDLE": number,
            "PENDING": number,
            "TERMINATING": number
         },
         "InstanceCounts": {
            "ACTIVE": number,
            "DESIRED": number,
            "IDLE": number,
            "MAXIMUM": number,
            "MINIMUM": number,
            "PENDING": number,
            "TERMINATING": number
         },
         "InstanceType": "string",
         "Location": "string",
         "ManagedCapacityConfiguration": {
            "ScaleInAfterInactivityMinutes": number,
            "ZeroCapacityStrategy": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeFleetCapacity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetCapacity](#API_DescribeFleetCapacity_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetCapacity-response-FleetCapacity"></a>
A collection of objects that contains capacity information for each requested fleet ID. Capacity objects are returned only for fleets that currently exist. Changes in desired instance value can take up to 1 minute to be reflected.
Type: Array of [FleetCapacity](API_FleetCapacity.md) objects

 ** [NextToken](#API_DescribeFleetCapacity_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetCapacity-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DescribeFleetCapacity_Errors"></a>

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
<a name="API_DescribeFleetCapacity_Examples"></a>

### Request capacity status for a list of fleets
<a name="API_DescribeFleetCapacity_Example_1"></a>

This example retrieves fleet capacity information for a list of two fleets. The first result shows capacity for a container fleet that's configured to hold five game server container groups per instance. The second result shows a fleet in the middle of a scale down event: instances are being terminated so that the active instances count matches the desired instances count.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeFleetCapacity_Example_1_Request"></a>

```
{
    "FleetIds": [
        "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "arn:aws:gamelift:us-west-2::fleet/fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
    ]
}
```

#### Sample Response
<a name="API_DescribeFleetCapacity_Example_1_Response"></a>

```
{
    "FleetCapacity": [
        {
            "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
            "FleetArn": "arn:aws:gamelift:us-east-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
            "InstanceCounts": {
                "DESIRED": 10,
                "MINIMUM": 1,
                "MAXIMUM": 20,
                "PENDING": 0,
                "ACTIVE": 10,
                "IDLE": 3,
                "TERMINATING": 0
            },
            "InstanceType": "c5.large",
            "Location": "us-west-2",
            "GameServerContainerGroupCounts": {
                "ACTIVE": 50,
                "IDLE": 15,
                "PENDING": 0,
                "TERMINATING": 0
        },
        {
            "FleetId": "fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
            "FleetArn": "arn:aws:gamelift:us-east-2::fleet/fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
            "InstanceCounts": {
                "DESIRED": 13,
                "MINIMUM": 1,
                "MAXIMUM": 20,
                "PENDING": 0,
                "ACTIVE": 15,
                "IDLE": 2,
                "TERMINATING": 2
            }
            "InstanceType": "c5.large",
            "Location": "us-west-2"
        }
    ]
}
```

## See Also
<a name="API_DescribeFleetCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeFleetCapacity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeFleetCapacity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeFleetCapacity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeFleetCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeFleetCapacity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeFleetCapacity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeFleetCapacity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeFleetCapacity)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeFleetCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeFleetCapacity)

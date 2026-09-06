---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetAttributes.html
---

# DescribeFleetAttributes
<a name="API_DescribeFleetAttributes"></a>

 **This API works with the following fleet types:** EC2, Anywhere

Retrieves core fleet-wide properties for fleets in an AWS Region. Properties include the computing hardware and deployment configuration for instances in the fleet.

You can use this operation in the following ways:
+ To get attributes for specific fleets, provide a list of fleet IDs or fleet ARNs.
+ To get attributes for all fleets, do not provide a fleet identifier.

When requesting attributes for multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages.

If successful, a `FleetAttributes` object is returned for each fleet requested, unless the fleet identifier is not found.

**Note**
Some API operations limit the number of fleet IDs that allowed in one request. If a request exceeds this limit, the request fails and the error message contains the maximum allowed number.

 **Learn more**

 [Setting up Amazon GameLift Servers fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

## Request Syntax
<a name="API_DescribeFleetAttributes_RequestSyntax"></a>

```
{
   "FleetIds": [ "{{string}}" ],
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFleetAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetIds](#API_DescribeFleetAttributes_RequestSyntax) **   <a name="gameliftservers-DescribeFleetAttributes-request-FleetIds"></a>
A list of unique fleet identifiers to retrieve attributes for. You can use either the fleet ID or ARN value. To retrieve attributes for all current fleets, do not include this parameter.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** [Limit](#API_DescribeFleetAttributes_RequestSyntax) **   <a name="gameliftservers-DescribeFleetAttributes-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_DescribeFleetAttributes_RequestSyntax) **   <a name="gameliftservers-DescribeFleetAttributes-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_DescribeFleetAttributes_ResponseSyntax"></a>

```
{
   "FleetAttributes": [
      {
         "AnywhereConfiguration": {
            "Cost": "string"
         },
         "BuildArn": "string",
         "BuildId": "string",
         "CertificateConfiguration": {
            "CertificateType": "string"
         },
         "ComputeType": "string",
         "CreationTime": number,
         "Description": "string",
         "FleetArn": "string",
         "FleetId": "string",
         "FleetType": "string",
         "InstanceRoleArn": "string",
         "InstanceRoleCredentialsProvider": "string",
         "InstanceType": "string",
         "LogPaths": [ "string" ],
         "MetricGroups": [ "string" ],
         "Name": "string",
         "NewGameSessionProtectionPolicy": "string",
         "OperatingSystem": "string",
         "PlayerGatewayConfiguration": {
            "GameServerIpProtocolSupported": "string"
         },
         "PlayerGatewayMode": "string",
         "ResourceCreationLimitPolicy": {
            "NewGameSessionsPerCreator": number,
            "PolicyPeriodInMinutes": number
         },
         "ScriptArn": "string",
         "ScriptId": "string",
         "ServerLaunchParameters": "string",
         "ServerLaunchPath": "string",
         "Status": "string",
         "StoppedActions": [ "string" ],
         "TerminationTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeFleetAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetAttributes](#API_DescribeFleetAttributes_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetAttributes-response-FleetAttributes"></a>
A collection of objects containing attribute metadata for each requested fleet ID. Attribute objects are returned only for fleets that currently exist.
Type: Array of [FleetAttributes](API_FleetAttributes.md) objects

 ** [NextToken](#API_DescribeFleetAttributes_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetAttributes-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DescribeFleetAttributes_Errors"></a>

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
<a name="API_DescribeFleetAttributes_Examples"></a>

### Request attributes for a list of fleets
<a name="API_DescribeFleetAttributes_Example_1"></a>

This example retrieves attributes for an EC2 fleet.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeFleetAttributes_Example_1_Request"></a>

```
{
    "FleetIds": [
        "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    ]
}
```

#### Sample Response
<a name="API_DescribeFleetAttributes_Example_1_Response"></a>

```
{
    "FleetAttributes": [
        {
            "BuildArn": "arn:aws:gamelift:us-west-2::build/build-3333cccc-44dd-55ee-66ff-00001111aa22",
            "BuildId": "build-3333cccc-44dd-55ee-66ff-00001111aa22",
            "CertificateConfiguration": {
                "CertificateType": "DISABLED"
            },
            "ComputeType": "EC2",
            "CreationTime": 1568836191.995,
            "Description": "On-demand hosts for v2 North America",
            "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
            "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
            "FleetType": "SPOT",
            "InstanceType": "c5.large",
            "MetricGroups": [
                "default"
            ],
            "Name": "MegaFrogRaceServer.NA.v2-spot",
            "NewGameSessionProtectionPolicy": "NoProtection",
            "OperatingSystem": "WINDOWS_2022",
            "Status": "ACTIVE"
        }
    ]
}
```

### Request attributes for all fleets
<a name="API_DescribeFleetAttributes_Example_2"></a>

This example returns fleet attributes for all fleets with any status. This example uses the pagination parameters to return one fleet at a time.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeFleetAttributes_Example_2_Request"></a>

```
{
    "Limit": 1
    "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE1"
}
```

#### Sample Response
<a name="API_DescribeFleetAttributes_Example_2_Response"></a>

```
{
    "FleetAttributes": [
        {
            "FleetId": "fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
            "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
            "FleetType": "SPOT",
            "InstanceType": "c4.large",
            "Description": "On-demand hosts for v2 North America",
            "Name": "MegaFrogRaceServer.NA.v2-spot",
            "CreationTime": 1568838275.379,
            "Status": "ACTIVATING",
            "BuildId": "build-3333cccc-44dd-55ee-66ff-00001111aa22",
            "BuildArn": "arn:aws:gamelift:us-west-2::build/build-3333cccc-44dd-55ee-66ff-00001111aa22",
            "ServerLaunchPath": "C:\\game\\MegaFrogRace_Server.exe",
            "NewGameSessionProtectionPolicy": "NoProtection",
            "OperatingSystem": "WINDOWS_2022",
            "MetricGroups": [
                "default"
            ],
            "CertificateConfiguration": {
                "CertificateType": "GENERATED"
            }
        }
    ],
    "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjQwMTY4MDEwMjY5NCJ9LCJmbGVldElkIjp7InMiOiJmbGVldC00ZjcyY2E4ZS1iMmVjLTQ3N2UtODg4ZS1jMDFiZTUxOTc3Y2QifX0="
}
```

## See Also
<a name="API_DescribeFleetAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeFleetAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeFleetAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeFleetAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeFleetAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeFleetAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeFleetAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeFleetAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeFleetAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeFleetAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeFleetAttributes)

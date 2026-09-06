---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeVpcPeeringConnections.html
---

# DescribeVpcPeeringConnections
<a name="API_DescribeVpcPeeringConnections"></a>

 **This API works with the following fleet types:** EC2

Retrieves information on VPC peering connections. Use this operation to get peering information for all fleets or for one specific fleet ID.

To retrieve connection information, call this operation from the AWS account that is used to manage the Amazon GameLift Servers fleets. Specify a fleet ID or leave the parameter empty to retrieve all connection records. If successful, the retrieved information includes both active and pending connections. Active connections identify the IpV4 CIDR block that the VPC uses to connect.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_DescribeVpcPeeringConnections_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeVpcPeeringConnections_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_DescribeVpcPeeringConnections_RequestSyntax) **   <a name="gameliftservers-DescribeVpcPeeringConnections-request-FleetId"></a>
A unique identifier for the fleet. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`
Required: No

## Response Syntax
<a name="API_DescribeVpcPeeringConnections_ResponseSyntax"></a>

```
{
   "VpcPeeringConnections": [
      {
         "FleetArn": "string",
         "FleetId": "string",
         "GameLiftVpcId": "string",
         "IpV4CidrBlock": "string",
         "PeerVpcId": "string",
         "Status": {
            "Code": "string",
            "Message": "string"
         },
         "VpcPeeringConnectionId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeVpcPeeringConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcPeeringConnections](#API_DescribeVpcPeeringConnections_ResponseSyntax) **   <a name="gameliftservers-DescribeVpcPeeringConnections-response-VpcPeeringConnections"></a>
A collection of VPC peering connection records that match the request.
Type: Array of [VpcPeeringConnection](API_VpcPeeringConnection.md) objects

## Errors
<a name="API_DescribeVpcPeeringConnections_Errors"></a>

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

## See Also
<a name="API_DescribeVpcPeeringConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeVpcPeeringConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeVpcPeeringConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeVpcPeeringConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeVpcPeeringConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeVpcPeeringConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeVpcPeeringConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeVpcPeeringConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeVpcPeeringConnections)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeVpcPeeringConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeVpcPeeringConnections)

---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateVpcPeeringConnection.html
---

# CreateVpcPeeringConnection
<a name="API_CreateVpcPeeringConnection"></a>

 **This API works with the following fleet types:** EC2

Establishes a VPC peering connection between a virtual private cloud (VPC) in an AWS account with the VPC for your Amazon GameLift Servers fleet. VPC peering enables the game servers on your fleet to communicate directly with other AWS resources. You can peer with VPCs in any AWS account that you have access to, including the account that you use to manage your Amazon GameLift Servers fleets. You cannot peer with VPCs that are in different Regions. For more information, see [VPC Peering with Amazon GameLift Servers Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html).

Before calling this operation to establish the peering connection, you first need to use [CreateVpcPeeringAuthorization](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.html) and identify the VPC you want to peer with. Once the authorization for the specified VPC is issued, you have 24 hours to establish the connection. These two operations handle all tasks necessary to peer the two VPCs, including acceptance, updating routing tables, etc.

To establish the connection, call this operation from the AWS account that is used to manage the Amazon GameLift Servers fleets. Identify the following values: (1) The ID of the fleet you want to be enable a VPC peering connection for; (2) The AWS account with the VPC that you want to peer with; and (3) The ID of the VPC you want to peer with. This operation is asynchronous. If successful, a connection request is created. You can use continuous polling to track the request's status using [DescribeVpcPeeringConnections](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeVpcPeeringConnections.html) , or by monitoring fleet events for success or failure using [DescribeFleetEvents](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetEvents.html) .

**Note**
Amazon GameLift Servers uses the caller's credentials to update peer-VPC resources. The IAM user that calls this operation must have the following Amazon EC2 permissions enabled:
 `ec2:AcceptVpcPeeringConnection`
 `ec2:AuthorizeSecurityGroupEgress`
 `ec2:AuthorizeSecurityGroupIngress`
 `ec2:CreateRoute`
 `ec2:DescribeRouteTables`
 `ec2:DescribeSecurityGroups`

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_CreateVpcPeeringConnection_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "PeerVpcAwsAccountId": "{{string}}",
   "PeerVpcId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateVpcPeeringConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_CreateVpcPeeringConnection_RequestSyntax) **   <a name="gameliftservers-CreateVpcPeeringConnection-request-FleetId"></a>
A unique identifier for the fleet. You can use either the fleet ID or ARN value. This tells Amazon GameLift Servers which GameLift VPC to peer with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`
Required: Yes

 ** [PeerVpcAwsAccountId](#API_CreateVpcPeeringConnection_RequestSyntax) **   <a name="gameliftservers-CreateVpcPeeringConnection-request-PeerVpcAwsAccountId"></a>
A unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift Servers fleet with. You can find your Account ID in the AWS Management Console under account settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [PeerVpcId](#API_CreateVpcPeeringConnection_RequestSyntax) **   <a name="gameliftservers-CreateVpcPeeringConnection-request-PeerVpcId"></a>
A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the [VPC Dashboard](https://console.aws.amazon.com/vpc/) in the AWS Management Console. Learn more about VPC peering in [VPC Peering with Amazon GameLift Servers Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Response Elements
<a name="API_CreateVpcPeeringConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateVpcPeeringConnection_Errors"></a>

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
<a name="API_CreateVpcPeeringConnection_Examples"></a>

### Peer the VPC for your Amazon GameLift Servers fleet with a VPC on your Amazon GameLift Servers account
<a name="API_CreateVpcPeeringConnection_Example_1"></a>

This example builds on Example 1 in [CreateVpcPeeringAuthorization](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.html#API_CreateVpcPeeringAuthorization_Examples). If authorization succeeded, the next step is to tell Amazon GameLift Servers to request the peering connection. In this example, you want your game servers that are running on an Amazon GameLift Servers fleet to be able to access a web service. The web service is managed through the same AWS account that you use to manage your Amazon GameLift Servers fleet. To request the peering, provide the following details for the two VPCs to peer: (1) the Amazon GameLift Servers fleet ID, and (2) the account and VPC for the web service. The account ID and VPC for the web service must be the same one you used in the authorization.

 The fleet's ID is *fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa*. The AWS account (the same as the one you use to manage your Amazon GameLift Servers fleet) is *111122223333*. The VPC ID for the web service is *vpc-a12bc345*.

To make this request, sign in using your credentials for AWS account 111122223333.

#### Sample Request
<a name="API_CreateVpcPeeringConnection_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: gamelift.us-west-2.amazonaws.com;
Accept-Encoding: identity
Content-Length: 141
User-Agent: aws-cli/1.11.36 Python/2.7.9 Windows/7 botocore/1.4.93
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256  Credential=AKIAIOSFODNN7EXAMPLE/20170406/us-west-2/gamelift/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
X-Amz-Date: 20170406T004805Z
X-Amz-Target: GameLift.CreateVpcPeeringConnection

{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "PeerVpcAwsAccountId": "111122223333",
    "PeerVpcId": "vpc-a12bc345"}
```

### Peer the VPC for your Amazon GameLift Servers fleet with a VPC on a different account
<a name="API_CreateVpcPeeringConnection_Example_2"></a>

This example builds on Example 2 in [CreateVpcPeeringAuthorization](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.html#API_CreateVpcPeeringAuthorization_Examples). If authorization succeeded, the next step is to tell Amazon GameLift Servers to request the peering connection. As in the previous example, you want your game servers that are running on an Amazon GameLift Servers fleet to be able to access a web service. But in this example, the web service is managed by a different account from the one that you use to manage your Amazon GameLift Servers fleet. To request the peering, provide the following details for the two VPCs to peer: (1) the Amazon GameLift Servers fleet ID, and (2) the account and VPC for the web service. The account ID and VPC for the web service must be the same one you used in the authorization.

The fleet's ID is *fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa*. Your Amazon GameLift Servers account ID is *111122223333*. The AWS account with the web service is *444455556666*. The VPC ID for the web service is *vpc-c67ef890*.

To make this request, sign in using your credentials for AWS account 111122223333 (your Amazon GameLift Servers account).

#### Sample Request
<a name="API_CreateVpcPeeringConnection_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: gamelift.us-west-2.amazonaws.com;
Accept-Encoding: identity
Content-Length: 141
User-Agent: aws-cli/1.11.36 Python/2.7.9 Windows/7 botocore/1.4.93
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256  Credential=AKIAIOSFODNN7EXAMPLE/20170406/us-west-2/gamelift/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
X-Amz-Date: 20170406T004805Z
X-Amz-Target: GameLift.CreateVpcPeeringConnection

{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "PeerVpcAwsAccountId": "444455556666",
    "PeerVpcId": "vpc-c67ef890"}
```

## See Also
<a name="API_CreateVpcPeeringConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreateVpcPeeringConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreateVpcPeeringConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreateVpcPeeringConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreateVpcPeeringConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreateVpcPeeringConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreateVpcPeeringConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreateVpcPeeringConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreateVpcPeeringConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreateVpcPeeringConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreateVpcPeeringConnection)

---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateVpcPeeringAuthorization.html
---

# CreateVpcPeeringAuthorization
<a name="API_CreateVpcPeeringAuthorization"></a>

 **This API works with the following fleet types:** EC2

Requests authorization to create or delete a peer connection between the VPC for your Amazon GameLift Servers fleet and a virtual private cloud (VPC) in your AWS account. VPC peering enables the game servers on your fleet to communicate directly with other AWS resources. After you've received authorization, use [CreateVpcPeeringConnection](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateVpcPeeringConnection.html) to establish the peering connection. For more information, see [VPC Peering with Amazon GameLift Servers Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html).

You can peer with VPCs that are owned by any AWS account you have access to, including the account that you use to manage your Amazon GameLift Servers fleets. You cannot peer with VPCs that are in different Regions.

To request authorization to create a connection, call this operation from the AWS account with the VPC that you want to peer to your Amazon GameLift Servers fleet. For example, to enable your game servers to retrieve data from a DynamoDB table, use the account that manages that DynamoDB resource. Identify the following values: (1) The ID of the VPC that you want to peer with, and (2) the ID of the AWS account that you use to manage Amazon GameLift Servers. If successful, VPC peering is authorized for the specified VPC.

To request authorization to delete a connection, call this operation from the AWS account with the VPC that is peered with your Amazon GameLift Servers fleet. Identify the following values: (1) VPC ID that you want to delete the peering connection for, and (2) ID of the AWS account that you use to manage Amazon GameLift Servers.

The authorization remains valid for 24 hours unless it is canceled. You must create or delete the peering connection while the authorization is valid.

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
<a name="API_CreateVpcPeeringAuthorization_RequestSyntax"></a>

```
{
   "GameLiftAwsAccountId": "{{string}}",
   "PeerVpcId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateVpcPeeringAuthorization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameLiftAwsAccountId](#API_CreateVpcPeeringAuthorization_RequestSyntax) **   <a name="gameliftservers-CreateVpcPeeringAuthorization-request-GameLiftAwsAccountId"></a>
A unique identifier for the AWS account that you use to manage your Amazon GameLift Servers fleet. You can find your Account ID in the AWS Management Console under account settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [PeerVpcId](#API_CreateVpcPeeringAuthorization_RequestSyntax) **   <a name="gameliftservers-CreateVpcPeeringAuthorization-request-PeerVpcId"></a>
A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the [VPC Dashboard](https://console.aws.amazon.com/vpc/) in the AWS Management Console. Learn more about VPC peering in [VPC Peering with Amazon GameLift Servers Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_CreateVpcPeeringAuthorization_ResponseSyntax"></a>

```
{
   "VpcPeeringAuthorization": {
      "CreationTime": number,
      "ExpirationTime": number,
      "GameLiftAwsAccountId": "string",
      "PeerVpcAwsAccountId": "string",
      "PeerVpcId": "string"
   }
}
```

## Response Elements
<a name="API_CreateVpcPeeringAuthorization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcPeeringAuthorization](#API_CreateVpcPeeringAuthorization_ResponseSyntax) **   <a name="gameliftservers-CreateVpcPeeringAuthorization-response-VpcPeeringAuthorization"></a>
Details on the requested VPC peering authorization, including expiration.
Type: [VpcPeeringAuthorization](API_VpcPeeringAuthorization.md) object

## Errors
<a name="API_CreateVpcPeeringAuthorization_Errors"></a>

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
<a name="API_CreateVpcPeeringAuthorization_Examples"></a>

### Authorize VPC peering between your Amazon GameLift Servers fleet and resources on your Amazon GameLift Servers account
<a name="API_CreateVpcPeeringAuthorization_Example_1"></a>

In this example, you want your Amazon GameLift Servers hosted game servers to access a web service. You manage the Amazon GameLift Servers fleet and the web service through the same AWS account (account ID *111122223333*). The web service already has a VPC set up, with ID *vpc-a12bc345*.

When making this request, use credentials for AWS account 111122223333.

#### Sample Request
<a name="API_CreateVpcPeeringAuthorization_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: gamelift.us-west-2.amazonaws.com;
Accept-Encoding: identity
Content-Length: 77
User-Agent: aws-cli/1.11.36 Python/2.7.9 Windows/7 botocore/1.4.93
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256  Credential=AKIAIOSFODNN7EXAMPLE/20170406/us-west-2/gamelift/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
X-Amz-Date: 20170406T004805Z
X-Amz-Target: GameLift.CreateVpcPeeringAuthorization

{ "GameLiftAwsAccountId": "111122223333",
    "PeerVpcId": "vpc-a12bc345"
}
```

#### Sample Response
<a name="API_CreateVpcPeeringAuthorization_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: b34f8665-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 225
Date: Thu, 06 Apr 2017 00:48:07 GMT

{"VpcPeeringAuthorization":
  {"CreationTime": 1503608847.489,
   "ExpirationTime": 1503695247,
   "GameLiftAwsAccountId": "111122223333",
   "PeerVpcAwsAccountId": "111122223333",
   "PeerVpcId": "vpc-a12bc345"}
}
```

### Authorize VPC peering between your Amazon GameLift Servers fleet and resources on a different account
<a name="API_CreateVpcPeeringAuthorization_Example_2"></a>

As in the previous example, you want your game servers to access a web service. But in this example, the Amazon GameLift Servers fleet and the web service are managed through different AWS accounts. Your Amazon GameLift Servers account ID is *111122223333*, while the web service account ID is *444455556666*. A VPC on account 444455556666 with the web service is set up with the ID *vpc-c67ef890*.

When making this request, use credentials for AWS account 444455556666. If you don't have rights to this account, work with the account owner to make the request. You'll need to provide your Amazon GameLift Servers account ID.

#### Sample Request
<a name="API_CreateVpcPeeringAuthorization_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: gamelift.us-west-2.amazonaws.com;
Accept-Encoding: identity
Content-Length: 82
User-Agent: aws-cli/1.11.36 Python/2.7.9 Windows/7 botocore/1.4.93
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256  Credential=AKIAIOSFODNN7EXAMPLE/20170406/us-west-2/gamelift/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
X-Amz-Date: 20170406T004805Z
X-Amz-Target: GameLift.CreateVpcPeeringAuthorization

{
    "GameLiftAwsAccountId": "111122223333",
    "PeerVpcId": "vpc-c67ef890"
}
```

#### Sample Response
<a name="API_CreateVpcPeeringAuthorization_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: b34f8665-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 225
Date: Thu, 06 Apr 2017 00:48:07 GMT

{"VpcPeeringAuthorization":
  {"CreationTime": 1503608847.489,
   "ExpirationTime": 1503695247,
   "GameLiftAwsAccountId": "111122223333",
   "PeerVpcAwsAccountId": "444455556666",
   "PeerVpcId": "vpc-c67ef890"}
}
```

## See Also
<a name="API_CreateVpcPeeringAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreateVpcPeeringAuthorization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreateVpcPeeringAuthorization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreateVpcPeeringAuthorization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreateVpcPeeringAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreateVpcPeeringAuthorization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreateVpcPeeringAuthorization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreateVpcPeeringAuthorization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreateVpcPeeringAuthorization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreateVpcPeeringAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreateVpcPeeringAuthorization)

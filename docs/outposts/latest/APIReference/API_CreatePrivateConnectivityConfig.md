---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreatePrivateConnectivityConfig.html
---

# CreatePrivateConnectivityConfig
<a name="API_CreatePrivateConnectivityConfig"></a>

Creates the private connectivity configuration for the specified Outpost. Private connectivity establishes a service link VPN connection between the Outpost and its home AWS Region using a VPC and subnet that you specify, which allows the service link traffic to flow through your VPC and minimizes public internet exposure.

## Request Syntax
<a name="API_CreatePrivateConnectivityConfig_RequestSyntax"></a>

```
POST /outposts/{{OutpostId}}/privateConnectivity HTTP/1.1
Content-type: application/json

{
   "VpcInformationList": [
      {
         "SubnetIds": [ "{{string}}" ],
         "VpcEndpointId": "{{string}}",
         "VpcId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreatePrivateConnectivityConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [OutpostId](#API_CreatePrivateConnectivityConfig_RequestSyntax) **   <a name="outposts-CreatePrivateConnectivityConfig-request-uri-OutpostId"></a>
The ID or ARN of the Outpost.
Despite the parameter name, you can make the request with an ARN. The parameter name is `OutpostId` for backward compatibility.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_CreatePrivateConnectivityConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [VpcInformationList](#API_CreatePrivateConnectivityConfig_RequestSyntax) **   <a name="outposts-CreatePrivateConnectivityConfig-request-VpcInformationList"></a>
Information about the VPC used for private connectivity, including the VPC, its subnets, and an associated VPC endpoint. You can specify at most one entry.
Type: Array of [VpcInformation](API_VpcInformation.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

## Response Syntax
<a name="API_CreatePrivateConnectivityConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "OutpostId": "string",
   "PrivateConnectivityConfig": {
      "PrivateConnectivityStatus": "string",
      "ProvisioningRoleArn": "string",
      "RoleArn": "string",
      "VpcInformationList": [
         {
            "SubnetIds": [ "string" ],
            "VpcEndpointId": "string",
            "VpcId": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreatePrivateConnectivityConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OutpostId](#API_CreatePrivateConnectivityConfig_ResponseSyntax) **   <a name="outposts-CreatePrivateConnectivityConfig-response-OutpostId"></a>
The ID of the Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`

 ** [PrivateConnectivityConfig](#API_CreatePrivateConnectivityConfig_ResponseSyntax) **   <a name="outposts-CreatePrivateConnectivityConfig-response-PrivateConnectivityConfig"></a>
The private connectivity configuration for the Outpost.
Type: [PrivateConnectivityConfig](API_PrivateConnectivityConfig.md) object

## Errors
<a name="API_CreatePrivateConnectivityConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting this resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource causing the conflict.
 ** ResourceType **
The type of the resource causing the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## Examples
<a name="API_CreatePrivateConnectivityConfig_Examples"></a>

### Example
<a name="API_CreatePrivateConnectivityConfig_Example_1"></a>

This example creates the private connectivity configuration for the specified Outpost. `VpcInformationList` is required and specifies the VPC, subnet, and associated VPC endpoint used for private connectivity.

#### Sample Request
<a name="API_CreatePrivateConnectivityConfig_Example_1_Request"></a>

```
aws outposts create-private-connectivity-config --outpost-id op-1234567890example --vpc-information-list '[{"VpcId":"vpc-0abcd1234example","SubnetIds":["subnet-0abcd1234example"],"VpcEndpointId":"vpce-0ab1234cd5678ef90"}]'
```

#### Sample Response
<a name="API_CreatePrivateConnectivityConfig_Example_1_Response"></a>

```
{
  "OutpostId": "op-1234567890example",
  "PrivateConnectivityConfig": {
    "RoleArn": "arn:aws:iam::123456789012:role/aws-service-role/outposts.amazonaws.com/AWSServiceRoleForOutposts_op-1234567890example",
    "PrivateConnectivityStatus": "ENABLED",
    "VpcInformationList": [
      {
        "VpcId": "vpc-0abcd1234example",
        "SubnetIds": [
          "subnet-0abcd1234example"
        ],
        "VpcEndpointId": "vpce-0ab1234cd5678ef90"
      }
    ],
    "ProvisioningRoleArn": "arn:aws:iam::123456789012:role/service-role/AWSOutpostsProvisioningRole_op-1234567890example"
  }
}
```

## See Also
<a name="API_CreatePrivateConnectivityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/CreatePrivateConnectivityConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/CreatePrivateConnectivityConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/CreatePrivateConnectivityConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/CreatePrivateConnectivityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/CreatePrivateConnectivityConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/CreatePrivateConnectivityConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/CreatePrivateConnectivityConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/CreatePrivateConnectivityConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/CreatePrivateConnectivityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/CreatePrivateConnectivityConfig)

---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateVpcEndpoint.html
---

# CreateVpcEndpoint
<a name="API_CreateVpcEndpoint"></a>

Creates an Amazon OpenSearch Service-managed VPC endpoint.

## Request Syntax
<a name="API_CreateVpcEndpoint_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/vpcEndpoints HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "DomainArn": "{{string}}",
   "VpcOptions": {
      "EgressEnabled": {{boolean}},
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_CreateVpcEndpoint_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateVpcEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateVpcEndpoint_RequestSyntax) **   <a name="opensearchservice-CreateVpcEndpoint-request-ClientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [DomainArn](#API_CreateVpcEndpoint_RequestSyntax) **   <a name="opensearchservice-CreateVpcEndpoint-request-DomainArn"></a>
The Amazon Resource Name (ARN) of the domain to create the endpoint for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`
Required: Yes

 ** [VpcOptions](#API_CreateVpcEndpoint_RequestSyntax) **   <a name="opensearchservice-CreateVpcEndpoint-request-VpcOptions"></a>
Options to specify the subnets and security groups for the endpoint.
Type: [VPCOptions](API_VPCOptions.md) object
Required: Yes

## Response Syntax
<a name="API_CreateVpcEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "VpcEndpoint": {
      "DomainArn": "string",
      "Endpoint": "string",
      "Status": "string",
      "VpcEndpointId": "string",
      "VpcEndpointOwner": "string",
      "VpcOptions": {
         "AvailabilityZones": [ "string" ],
         "EgressEnabled": boolean,
         "SecurityGroupIds": [ "string" ],
         "SubnetIds": [ "string" ],
         "VPCId": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateVpcEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcEndpoint](#API_CreateVpcEndpoint_ResponseSyntax) **   <a name="opensearchservice-CreateVpcEndpoint-response-VpcEndpoint"></a>
Information about the newly created VPC endpoint.
Type: [VpcEndpoint](API_VpcEndpoint.md) object

## Errors
<a name="API_CreateVpcEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** ConflictException **
An error occurred because the client attempts to remove a resource that is currently in use.
HTTP Status Code: 409

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_CreateVpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/CreateVpcEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/CreateVpcEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CreateVpcEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/CreateVpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CreateVpcEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/CreateVpcEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/CreateVpcEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/CreateVpcEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/CreateVpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CreateVpcEndpoint)

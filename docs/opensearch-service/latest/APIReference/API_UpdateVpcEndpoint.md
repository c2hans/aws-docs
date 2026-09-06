---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateVpcEndpoint.html
---

# UpdateVpcEndpoint
<a name="API_UpdateVpcEndpoint"></a>

Modifies an Amazon OpenSearch Service-managed interface VPC endpoint.

## Request Syntax
<a name="API_UpdateVpcEndpoint_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/vpcEndpoints/update HTTP/1.1
Content-type: application/json

{
   "VpcEndpointId": "{{string}}",
   "VpcOptions": {
      "EgressEnabled": {{boolean}},
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_UpdateVpcEndpoint_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateVpcEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [VpcEndpointId](#API_UpdateVpcEndpoint_RequestSyntax) **   <a name="opensearchservice-UpdateVpcEndpoint-request-VpcEndpointId"></a>
The unique identifier of the endpoint.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 256.
Pattern: `^aos-[a-zA-Z0-9]*$`
Required: Yes

 ** [VpcOptions](#API_UpdateVpcEndpoint_RequestSyntax) **   <a name="opensearchservice-UpdateVpcEndpoint-request-VpcOptions"></a>
The security groups and/or subnets to add, remove, or modify.
Type: [VPCOptions](API_VPCOptions.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateVpcEndpoint_ResponseSyntax"></a>

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
<a name="API_UpdateVpcEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcEndpoint](#API_UpdateVpcEndpoint_ResponseSyntax) **   <a name="opensearchservice-UpdateVpcEndpoint-response-VpcEndpoint"></a>
The endpoint to be updated.
Type: [VpcEndpoint](API_VpcEndpoint.md) object

## Errors
<a name="API_UpdateVpcEndpoint_Errors"></a>

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

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_UpdateVpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/UpdateVpcEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/UpdateVpcEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/UpdateVpcEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/UpdateVpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/UpdateVpcEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/UpdateVpcEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/UpdateVpcEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/UpdateVpcEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/UpdateVpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/UpdateVpcEndpoint)

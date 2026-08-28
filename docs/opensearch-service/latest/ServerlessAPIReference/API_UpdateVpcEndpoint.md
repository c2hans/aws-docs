---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateVpcEndpoint.html
---

# UpdateVpcEndpoint
<a name="API_UpdateVpcEndpoint"></a>

Updates an OpenSearch Serverless-managed interface endpoint. For more information, see [Access Amazon OpenSearch Serverless using an interface endpoint](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html).

## Request Syntax
<a name="API_UpdateVpcEndpoint_RequestSyntax"></a>

```
{
   "addSecurityGroupIds": [ "{{string}}" ],
   "addSubnetIds": [ "{{string}}" ],
   "clientToken": "{{string}}",
   "id": "{{string}}",
   "removeSecurityGroupIds": [ "{{string}}" ],
   "removeSubnetIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateVpcEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [addSecurityGroupIds](#API_UpdateVpcEndpoint_RequestSyntax) **   <a name="opensearchserverless-UpdateVpcEndpoint-request-addSecurityGroupIds"></a>
The unique identifiers of the security groups to add to the endpoint. Security groups define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+\-]+`
Required: No

 ** [addSubnetIds](#API_UpdateVpcEndpoint_RequestSyntax) **   <a name="opensearchserverless-UpdateVpcEndpoint-request-addSubnetIds"></a>
The ID of one or more subnets to add to the endpoint.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `subnet-([0-9a-f]{8}|[0-9a-f]{17})`
Required: No

 ** [clientToken](#API_UpdateVpcEndpoint_RequestSyntax) **   <a name="opensearchserverless-UpdateVpcEndpoint-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [id](#API_UpdateVpcEndpoint_RequestSyntax) **   <a name="opensearchserverless-UpdateVpcEndpoint-request-id"></a>
The unique identifier of the interface endpoint to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `vpce-[0-9a-z]*`
Required: Yes

 ** [removeSecurityGroupIds](#API_UpdateVpcEndpoint_RequestSyntax) **   <a name="opensearchserverless-UpdateVpcEndpoint-request-removeSecurityGroupIds"></a>
The unique identifiers of the security groups to remove from the endpoint.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+\-]+`
Required: No

 ** [removeSubnetIds](#API_UpdateVpcEndpoint_RequestSyntax) **   <a name="opensearchserverless-UpdateVpcEndpoint-request-removeSubnetIds"></a>
The unique identifiers of the subnets to remove from the endpoint.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `subnet-([0-9a-f]{8}|[0-9a-f]{17})`
Required: No

## Response Syntax
<a name="API_UpdateVpcEndpoint_ResponseSyntax"></a>

```
{
   "UpdateVpcEndpointDetail": {
      "id": "string",
      "lastModifiedDate": number,
      "name": "string",
      "securityGroupIds": [ "string" ],
      "status": "string",
      "subnetIds": [ "string" ]
   }
}
```

## Response Elements
<a name="API_UpdateVpcEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UpdateVpcEndpointDetail](#API_UpdateVpcEndpoint_ResponseSyntax) **   <a name="opensearchserverless-UpdateVpcEndpoint-response-UpdateVpcEndpointDetail"></a>
Details about the updated VPC endpoint.
Type: [UpdateVpcEndpointDetail](API_UpdateVpcEndpointDetail.md) object

## Errors
<a name="API_UpdateVpcEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE\_FAILED state.
HTTP Status Code: 400

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_UpdateVpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/UpdateVpcEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/UpdateVpcEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/UpdateVpcEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/UpdateVpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/UpdateVpcEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/UpdateVpcEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/UpdateVpcEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/UpdateVpcEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/UpdateVpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/UpdateVpcEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

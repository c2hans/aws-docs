---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AuthorizeVpcEndpointAccess.html
---

# AuthorizeVpcEndpointAccess
<a name="API_AuthorizeVpcEndpointAccess"></a>

Provides access to an Amazon OpenSearch Service domain through the use of an interface VPC endpoint.

## Request Syntax
<a name="API_AuthorizeVpcEndpointAccess_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/domain/{{DomainName}}/authorizeVpcEndpointAccess HTTP/1.1
Content-type: application/json

{
   "Account": "{{string}}",
   "Service": "{{string}}",
   "ServiceOptions": {
      "SupportedRegions": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_AuthorizeVpcEndpointAccess_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_AuthorizeVpcEndpointAccess_RequestSyntax) **   <a name="opensearchservice-AuthorizeVpcEndpointAccess-request-uri-DomainName"></a>
The name of the OpenSearch Service domain to provide access to.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_AuthorizeVpcEndpointAccess_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Account](#API_AuthorizeVpcEndpointAccess_RequestSyntax) **   <a name="opensearchservice-AuthorizeVpcEndpointAccess-request-Account"></a>
The AWS account ID to grant access to.
Type: String
Pattern: `^[0-9]+$`
Required: No

 ** [Service](#API_AuthorizeVpcEndpointAccess_RequestSyntax) **   <a name="opensearchservice-AuthorizeVpcEndpointAccess-request-Service"></a>
The AWS service SP to grant access to.
Type: String
Valid Values: `application.opensearchservice.amazonaws.com`
Required: No

 ** [ServiceOptions](#API_AuthorizeVpcEndpointAccess_RequestSyntax) **   <a name="opensearchservice-AuthorizeVpcEndpointAccess-request-ServiceOptions"></a>
The options for the service, including the supported Regions for the endpoint access.
Type: [ServiceOptions](API_ServiceOptions.md) object
Required: No

## Response Syntax
<a name="API_AuthorizeVpcEndpointAccess_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AuthorizedPrincipal": {
      "Principal": "string",
      "PrincipalType": "string",
      "ServiceOptions": {
         "SupportedRegions": [ "string" ]
      }
   }
}
```

## Response Elements
<a name="API_AuthorizeVpcEndpointAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthorizedPrincipal](#API_AuthorizeVpcEndpointAccess_ResponseSyntax) **   <a name="opensearchservice-AuthorizeVpcEndpointAccess-response-AuthorizedPrincipal"></a>
Information about the AWS account or service that was provided access to the domain.
Type: [AuthorizedPrincipal](API_AuthorizedPrincipal.md) object

## Errors
<a name="API_AuthorizeVpcEndpointAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_AuthorizeVpcEndpointAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/AuthorizeVpcEndpointAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/AuthorizeVpcEndpointAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AuthorizeVpcEndpointAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/AuthorizeVpcEndpointAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AuthorizeVpcEndpointAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/AuthorizeVpcEndpointAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/AuthorizeVpcEndpointAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/AuthorizeVpcEndpointAccess)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/AuthorizeVpcEndpointAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AuthorizeVpcEndpointAccess)

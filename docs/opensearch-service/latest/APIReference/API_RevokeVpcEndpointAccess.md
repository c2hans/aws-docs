---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RevokeVpcEndpointAccess.html
---

# RevokeVpcEndpointAccess
<a name="API_RevokeVpcEndpointAccess"></a>

Revokes access to an Amazon OpenSearch Service domain that was provided through an interface VPC endpoint.

## Request Syntax
<a name="API_RevokeVpcEndpointAccess_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/domain/{{DomainName}}/revokeVpcEndpointAccess HTTP/1.1
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
<a name="API_RevokeVpcEndpointAccess_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_RevokeVpcEndpointAccess_RequestSyntax) **   <a name="opensearchservice-RevokeVpcEndpointAccess-request-uri-DomainName"></a>
The name of the OpenSearch Service domain.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_RevokeVpcEndpointAccess_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Account](#API_RevokeVpcEndpointAccess_RequestSyntax) **   <a name="opensearchservice-RevokeVpcEndpointAccess-request-Account"></a>
The account ID to revoke access from.
Type: String
Pattern: `^[0-9]+$`
Required: No

 ** [Service](#API_RevokeVpcEndpointAccess_RequestSyntax) **   <a name="opensearchservice-RevokeVpcEndpointAccess-request-Service"></a>
The service SP to revoke access from.
Type: String
Valid Values: `application.opensearchservice.amazonaws.com`
Required: No

 ** [ServiceOptions](#API_RevokeVpcEndpointAccess_RequestSyntax) **   <a name="opensearchservice-RevokeVpcEndpointAccess-request-ServiceOptions"></a>
The options for the service, including the supported Regions for the endpoint access.
Type: [ServiceOptions](API_ServiceOptions.md) object
Required: No

## Response Syntax
<a name="API_RevokeVpcEndpointAccess_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_RevokeVpcEndpointAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RevokeVpcEndpointAccess_Errors"></a>

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

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_RevokeVpcEndpointAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/RevokeVpcEndpointAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/RevokeVpcEndpointAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/RevokeVpcEndpointAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/RevokeVpcEndpointAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/RevokeVpcEndpointAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/RevokeVpcEndpointAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/RevokeVpcEndpointAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/RevokeVpcEndpointAccess)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/RevokeVpcEndpointAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/RevokeVpcEndpointAccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

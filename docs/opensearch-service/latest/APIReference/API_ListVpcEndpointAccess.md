---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListVpcEndpointAccess.html
---

# ListVpcEndpointAccess
<a name="API_ListVpcEndpointAccess"></a>

Retrieves information about each AWS principal that is allowed to access a given Amazon OpenSearch Service domain through the use of an interface VPC endpoint.

## Request Syntax
<a name="API_ListVpcEndpointAccess_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}}/listVpcEndpointAccess?nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListVpcEndpointAccess_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_ListVpcEndpointAccess_RequestSyntax) **   <a name="opensearchservice-ListVpcEndpointAccess-request-uri-DomainName"></a>
The name of the OpenSearch Service domain to retrieve access information for.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [NextToken](#API_ListVpcEndpointAccess_RequestSyntax) **   <a name="opensearchservice-ListVpcEndpointAccess-request-uri-NextToken"></a>
If your initial `ListVpcEndpointAccess` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListVpcEndpointAccess` operations, which returns results in the next page.

## Request Body
<a name="API_ListVpcEndpointAccess_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListVpcEndpointAccess_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AuthorizedPrincipalList": [
      {
         "Principal": "string",
         "PrincipalType": "string",
         "ServiceOptions": {
            "SupportedRegions": [ "string" ]
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListVpcEndpointAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthorizedPrincipalList](#API_ListVpcEndpointAccess_ResponseSyntax) **   <a name="opensearchservice-ListVpcEndpointAccess-response-AuthorizedPrincipalList"></a>
A list of [IAM principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) that can currently access the domain.
Type: Array of [AuthorizedPrincipal](API_AuthorizedPrincipal.md) objects

 ** [NextToken](#API_ListVpcEndpointAccess_ResponseSyntax) **   <a name="opensearchservice-ListVpcEndpointAccess-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListVpcEndpointAccess_Errors"></a>

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

## See Also
<a name="API_ListVpcEndpointAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListVpcEndpointAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListVpcEndpointAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListVpcEndpointAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListVpcEndpointAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListVpcEndpointAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListVpcEndpointAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListVpcEndpointAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListVpcEndpointAccess)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListVpcEndpointAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListVpcEndpointAccess)

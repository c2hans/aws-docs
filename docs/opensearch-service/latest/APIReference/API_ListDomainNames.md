---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDomainNames.html
---

# ListDomainNames
<a name="API_ListDomainNames"></a>

Returns the names of all Amazon OpenSearch Service domains owned by the current user in the active Region.

## Request Syntax
<a name="API_ListDomainNames_RequestSyntax"></a>

```
GET /2021-01-01/domain?engineType={{EngineType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDomainNames_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EngineType](#API_ListDomainNames_RequestSyntax) **   <a name="opensearchservice-ListDomainNames-request-uri-EngineType"></a>
Filters the output by domain engine type.
Valid Values: `OpenSearch | Elasticsearch`

## Request Body
<a name="API_ListDomainNames_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDomainNames_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainNames": [
      {
         "DomainName": "string",
         "EngineType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListDomainNames_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainNames](#API_ListDomainNames_ResponseSyntax) **   <a name="opensearchservice-ListDomainNames-response-DomainNames"></a>
The names of all OpenSearch Service domains owned by the current user and their respective engine types.
Type: Array of [DomainInfo](API_DomainInfo.md) objects

## Errors
<a name="API_ListDomainNames_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_ListDomainNames_Examples"></a>

### Example
<a name="API_ListDomainNames_Example_1"></a>

This example illustrates one usage of ListDomainNames.

#### Sample Request
<a name="API_ListDomainNames_Example_1_Request"></a>

```
GET /2021-01-01/domain HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.15.13 Python/3.11.6 Windows/10 exe/AMD64 prompt/off command/opensearch.list-domain-names
X-Amz-Date: 20240209T223114Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEEcaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240209/us-east-1/es/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature=47e588909eb82143e199bb6e4ec3c0cae11f20e4778fda277d68b0518bca962a
```

#### Sample Response
<a name="API_ListDomainNames_Example_1_Response"></a>

```
{
   "DomainNames":[
      {
         "DomainName":"my-domain-1",
         "EngineType":"OpenSearch"
      },
      {
         "DomainName":"my-domain-2",
         "EngineType":"OpenSearch"
      },
      {
         "DomainName":"my-domain-3",
         "EngineType":"OpenSearch"
      },
      {
         "DomainName":"my-domain-4",
         "EngineType":"OpenSearch"
      },
      {
         "DomainName":"my-domain-5",
         "EngineType":"OpenSearch"
      },
      {
         "DomainName":"my-domain-6",
         "EngineType":"OpenSearch"
      }
   ]
}
```

## See Also
<a name="API_ListDomainNames_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListDomainNames)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListDomainNames)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListDomainNames)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListDomainNames)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListDomainNames)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListDomainNames)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListDomainNames)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListDomainNames)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListDomainNames)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListDomainNames)

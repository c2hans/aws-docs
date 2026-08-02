---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetCompatibleVersions.html
---

# GetCompatibleVersions
<a name="API_GetCompatibleVersions"></a>

Returns a map of OpenSearch or Elasticsearch versions and the versions you can upgrade them to.

## Request Syntax
<a name="API_GetCompatibleVersions_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/compatibleVersions?domainName={{DomainName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCompatibleVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_GetCompatibleVersions_RequestSyntax) **   <a name="opensearchservice-GetCompatibleVersions-request-uri-DomainName"></a>
The name of an existing domain. Provide this parameter to limit the results to a single domain.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`

## Request Body
<a name="API_GetCompatibleVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCompatibleVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CompatibleVersions": [
      {
         "SourceVersion": "string",
         "TargetVersions": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_GetCompatibleVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompatibleVersions](#API_GetCompatibleVersions_ResponseSyntax) **   <a name="opensearchservice-GetCompatibleVersions-response-CompatibleVersions"></a>
A map of OpenSearch or Elasticsearch versions and the versions you can upgrade them to.
Type: Array of [CompatibleVersionsMap](API_CompatibleVersionsMap.md) objects

## Errors
<a name="API_GetCompatibleVersions_Errors"></a>

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

## Examples
<a name="API_GetCompatibleVersions_Examples"></a>

### Example
<a name="API_GetCompatibleVersions_Example_1"></a>

This example illustrates one usage of GetCompatibleVersions.

#### Sample Request
<a name="API_GetCompatibleVersions_Example_1_Request"></a>

```
GET /2021-01-01/opensearch/compatibleVersions HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.15.13 Python/3.11.6 Windows/10 exe/AMD64 prompt/off command/opensearch.get-compatible-versions
X-Amz-Date: 20240205T201155Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEI3wEaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240205/us-east-1/es/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature=5e11eba0d22362bc27334dd0143baa002edee9d967b2653fd9bd7d87bec71b8c
```

#### Sample Response
<a name="API_GetCompatibleVersions_Example_1_Response"></a>

```
{
   "CompatibleVersions":[
      {
         "SourceVersion":"Elasticsearch_7.7",
         "TargetVersions":[
            "Elasticsearch_7.8",
            "Elasticsearch_7.9",
            "Elasticsearch_7.10",
            "OpenSearch_1.0",
            "OpenSearch_1.1",
            "OpenSearch_1.2",
            "OpenSearch_1.3"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_6.8",
         "TargetVersions":[
            "Elasticsearch_7.1",
            "Elasticsearch_7.4",
            "Elasticsearch_7.7",
            "Elasticsearch_7.8",
            "Elasticsearch_7.9",
            "Elasticsearch_7.10",
            "OpenSearch_1.0",
            "OpenSearch_1.1",
            "OpenSearch_1.2",
            "OpenSearch_1.3"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_7.8",
         "TargetVersions":[
            "Elasticsearch_7.9",
            "Elasticsearch_7.10",
            "OpenSearch_1.0",
            "OpenSearch_1.1",
            "OpenSearch_1.2",
            "OpenSearch_1.3"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_7.9",
         "TargetVersions":[
            "Elasticsearch_7.10",
            "OpenSearch_1.0",
            "OpenSearch_1.1",
            "OpenSearch_1.2",
            "OpenSearch_1.3"
         ]
      },
      {
         "SourceVersion":"OpenSearch_2.3",
         "TargetVersions":[
            "OpenSearch_2.5",
            "OpenSearch_2.7",
            "OpenSearch_2.9",
            "OpenSearch_2.11"
         ]
      },
      {
         "SourceVersion":"OpenSearch_2.5",
         "TargetVersions":[
            "OpenSearch_2.7",
            "OpenSearch_2.9",
            "OpenSearch_2.11"
         ]
      },
      {
         "SourceVersion":"OpenSearch_1.0",
         "TargetVersions":[
            "OpenSearch_1.1",
            "OpenSearch_1.2",
            "OpenSearch_1.3"
         ]
      },
      {
         "SourceVersion":"OpenSearch_1.1",
         "TargetVersions":[
            "OpenSearch_1.2",
            "OpenSearch_1.3"
         ]
      },
      {
         "SourceVersion":"OpenSearch_1.2",
         "TargetVersions":[
            "OpenSearch_1.3"
         ]
      },
      {
         "SourceVersion":"OpenSearch_1.3",
         "TargetVersions":[
            "OpenSearch_2.3",
            "OpenSearch_2.5",
            "OpenSearch_2.7",
            "OpenSearch_2.9",
            "OpenSearch_2.11"
         ]
      },
      {
         "SourceVersion":"OpenSearch_2.7",
         "TargetVersions":[
            "OpenSearch_2.9",
            "OpenSearch_2.11"
         ]
      },
      {
         "SourceVersion":"OpenSearch_2.9",
         "TargetVersions":[
            "OpenSearch_2.11"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_7.10",
         "TargetVersions":[
            "OpenSearch_1.0",
            "OpenSearch_1.1",
            "OpenSearch_1.2",
            "OpenSearch_1.3"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_6.0",
         "TargetVersions":[
            "Elasticsearch_6.3",
            "Elasticsearch_6.4",
            "Elasticsearch_6.5",
            "Elasticsearch_6.7",
            "Elasticsearch_6.8"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_5.1",
         "TargetVersions":[
            "Elasticsearch_5.6"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_7.1",
         "TargetVersions":[
            "Elasticsearch_7.4",
            "Elasticsearch_7.7",
            "Elasticsearch_7.8",
            "Elasticsearch_7.9",
            "Elasticsearch_7.10",
            "OpenSearch_1.0",
            "OpenSearch_1.1",
            "OpenSearch_1.2",
            "OpenSearch_1.3"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_6.2",
         "TargetVersions":[
            "Elasticsearch_6.3",
            "Elasticsearch_6.4",
            "Elasticsearch_6.5",
            "Elasticsearch_6.7",
            "Elasticsearch_6.8"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_5.3",
         "TargetVersions":[
            "Elasticsearch_5.6"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_6.3",
         "TargetVersions":[
            "Elasticsearch_6.4",
            "Elasticsearch_6.5",
            "Elasticsearch_6.7",
            "Elasticsearch_6.8"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_6.4",
         "TargetVersions":[
            "Elasticsearch_6.5",
            "Elasticsearch_6.7",
            "Elasticsearch_6.8"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_5.5",
         "TargetVersions":[
            "Elasticsearch_5.6"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_7.4",
         "TargetVersions":[
            "Elasticsearch_7.7",
            "Elasticsearch_7.8",
            "Elasticsearch_7.9",
            "Elasticsearch_7.10",
            "OpenSearch_1.0",
            "OpenSearch_1.1",
            "OpenSearch_1.2",
            "OpenSearch_1.3"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_6.5",
         "TargetVersions":[
            "Elasticsearch_6.7",
            "Elasticsearch_6.8"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_5.6",
         "TargetVersions":[
            "Elasticsearch_6.3",
            "Elasticsearch_6.4",
            "Elasticsearch_6.5",
            "Elasticsearch_6.7",
            "Elasticsearch_6.8"
         ]
      },
      {
         "SourceVersion":"Elasticsearch_6.7",
         "TargetVersions":[
            "Elasticsearch_6.8"
         ]
      }
   ]
}
```

## See Also
<a name="API_GetCompatibleVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/GetCompatibleVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/GetCompatibleVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/GetCompatibleVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/GetCompatibleVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/GetCompatibleVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/GetCompatibleVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/GetCompatibleVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/GetCompatibleVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/GetCompatibleVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/GetCompatibleVersions)

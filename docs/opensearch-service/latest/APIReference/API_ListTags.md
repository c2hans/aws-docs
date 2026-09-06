---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListTags.html
---

# ListTags
<a name="API_ListTags"></a>

Returns all resource tags for an Amazon OpenSearch Service domain, data source, or application. For more information, see [Tagging Amazon OpenSearch Service resources](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging.html).

## Request Syntax
<a name="API_ListTags_RequestSyntax"></a>

```
GET /2021-01-01/tags/?arn={{ARN}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTags_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ARN](#API_ListTags_RequestSyntax) **   <a name="opensearchservice-ListTags-request-uri-ARN"></a>
Amazon Resource Name (ARN) for the domain, data source, or application to view tags for.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: Yes

## Request Body
<a name="API_ListTags_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTags_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "TagList": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TagList](#API_ListTags_ResponseSyntax) **   <a name="opensearchservice-ListTags-response-TagList"></a>
List of resource tags associated with the specified domain, data source, or application.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ListTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

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
<a name="API_ListTags_Examples"></a>

### Example
<a name="API_ListTags_Example_1"></a>

This example illustrates one usage of ListTags.

#### Sample Request
<a name="API_ListTags_Example_1_Request"></a>

```
GET /2021-01-01/tags/?arn=arn%3Aaws%3Aes%3Aus-east-1%3A302040998751%3Adomain%2Fmarketing HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.15.13 Python/3.11.6 Windows/10 exe/AMD64 prompt/off command/opensearch.list-tags
X-Amz-Date: 20240212T221352Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEIwEaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240212/us-east-1/es/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature=8f19277a8b3e677b1f8efcfa58e419c04e83b6b79c2db3125b151c1c2f4c8539
```

#### Sample Response
<a name="API_ListTags_Example_1_Response"></a>

```
{
    "TagList": [
        {
            "Key": "department",
            "Value": "marketing"
        }
    ]
}
```

## See Also
<a name="API_ListTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListTags)

---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RemoveTags.html
---

# RemoveTags
<a name="API_RemoveTags"></a>

Removes the specified set of tags from an Amazon OpenSearch Service domain, data source, or application. For more information, see [ Tagging Amazon OpenSearch Service resources](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains.html#managedomains-awsresorcetagging).

## Request Syntax
<a name="API_RemoveTags_RequestSyntax"></a>

```
POST /2021-01-01/tags-removal HTTP/1.1
Content-type: application/json

{
   "ARN": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_RemoveTags_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RemoveTags_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ARN](#API_RemoveTags_RequestSyntax) **   <a name="opensearchservice-RemoveTags-request-ARN"></a>
The Amazon Resource Name (ARN) of the domain, data source, or application from which you want to delete the specified tags.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: Yes

 ** [TagKeys](#API_RemoveTags_RequestSyntax) **   <a name="opensearchservice-RemoveTags-request-TagKeys"></a>
The list of tag keys to remove from the domain, data source, or application.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_RemoveTags_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_RemoveTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemoveTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_RemoveTags_Examples"></a>

### Example
<a name="API_RemoveTags_Example_1"></a>

This example illustrates one usage of RemoveTags.

#### Sample Request
<a name="API_RemoveTags_Example_1_Request"></a>

```
POST /2021-01-01/tags-removal HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Type: application/json
User-Agent: aws-cli/2.15.13 Python/3.11.6 Windows/10 exe/AMD64 prompt/off command/opensearch.remove-tags
X-Amz-Date: 20240212T221612Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEI3wEaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240212/us-east-1/es/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-security-token, Signature=8fe55108204bb96b157bd4a5ca747c54264cb3c9c01a8137b1daffdf2eabb654
Content-Length: 100
{"ARN": "arn:aws:es:us-east-1:123456789012:domain/marketing", "TagKeys": ["department", "marketing"]}
```

#### Sample Response
<a name="API_RemoveTags_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: ab0cd0ef-123g-4h5j-678k-l6m534no08p7
Content-Type: application/json
Content-Length: 0
Date: Mon, 12 Feb 2024 22:16:12 GMT
Connection: keep-alive
```

## See Also
<a name="API_RemoveTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/RemoveTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/RemoveTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/RemoveTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/RemoveTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/RemoveTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/RemoveTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/RemoveTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/RemoveTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/RemoveTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/RemoveTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

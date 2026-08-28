---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AddTags.html
---

# AddTags
<a name="API_AddTags"></a>

Attaches tags to an existing Amazon OpenSearch Service domain, data source, or application.

Tags are a set of case-sensitive key-value pairs. A domain, data source, or application can have up to 10 tags. For more information, see [Tagging Amazon OpenSearch Service resources](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging.html).

## Request Syntax
<a name="API_AddTags_RequestSyntax"></a>

```
POST /2021-01-01/tags HTTP/1.1
Content-type: application/json

{
   "ARN": "{{string}}",
   "TagList": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_AddTags_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AddTags_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ARN](#API_AddTags_RequestSyntax) **   <a name="opensearchservice-AddTags-request-ARN"></a>
Amazon Resource Name (ARN) for the OpenSearch Service domain, data source, or application to which you want to attach resource tags.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: Yes

 ** [TagList](#API_AddTags_RequestSyntax) **   <a name="opensearchservice-AddTags-request-TagList"></a>
List of resource tags.
Type: Array of [Tag](API_Tag.md) objects
Required: Yes

## Response Syntax
<a name="API_AddTags_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AddTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AddTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_AddTags_Examples"></a>

### Example
<a name="API_AddTags_Example_1"></a>

This example illustrates one usage of AddTags.

#### Sample Request
<a name="API_AddTags_Example_1_Request"></a>

```
POST /2021-01-01/tags HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Type: application/json
User-Agent: aws-cli/2.15.13 Python/3.11.6 Windows/10 exe/AMD64 prompt/off command/opensearch.add-tags
X-Amz-Date: 20240212T212009Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEI3wEaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240212/us-east-1/es/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-security-token, Signature=92f6df10a81b7b553dbdab348594794df6272ea6799e4e9bae8aec96cfa44510
Content-Length: 118
{"ARN": "arn:aws:es:us-east-1:123456789012:domain/marketing", "TagList": [{"Key": "department", "Value": "marketing"}]}
```

#### Sample Response
<a name="API_AddTags_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 6ab4cde74-63fg-4h65-1101-d1112f029bbb
Content-Type: application/json
Content-Length: 0
Date: Mon, 12 Feb 2024 21:20:10 GMT
Connection: keep-alive
```

## See Also
<a name="API_AddTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/AddTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/AddTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AddTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/AddTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AddTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/AddTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/AddTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/AddTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/AddTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AddTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

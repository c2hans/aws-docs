---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_amazon-q-connect_ListTagsForResource"></a>

Lists the tags for the specified resource.

## Request Syntax
<a name="API_amazon-q-connect_ListTagsForResource_RequestSyntax"></a>

```
GET /tags/{{resourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_amazon-q-connect_ListTagsForResource_RequestSyntax) **   <a name="connect-amazon-q-connect_ListTagsForResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource.
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_amazon-q-connect_ListTagsForResource_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListTagsForResource-response-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_amazon-q-connect_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

## See Also
<a name="API_amazon-q-connect_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ListTagsForResource)

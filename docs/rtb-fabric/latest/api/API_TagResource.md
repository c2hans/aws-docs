---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Assigns one or more tags (key-value pairs) to the specified resource.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /tags/{{resourceArn}} HTTP/1.1
Content-type: application/json

{
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_TagResource_RequestSyntax) **   <a name="rtbfabric-TagResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource that you want to tag.
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:aws:rtbfabric:[a-zA-Z0-9_-]+:[0-9]{12}:gateway/[a-zA-Z0-9-]+(/link/[a-zA-Z0-9-]+(/routing-rule/[a-zA-Z0-9-]+)?)?`
Required: Yes

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_TagResource_RequestSyntax) **   <a name="rtbfabric-TagResource-request-tags"></a>
A map of the key-value pairs of the tag or tags to assign to the resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(resourceArn|internalId|[a-zA-Z0-9+\-=._:/@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 1600.
Required: Yes

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/TagResource)

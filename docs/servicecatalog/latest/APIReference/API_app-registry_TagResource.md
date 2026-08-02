---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_TagResource.html
---

# TagResource
<a name="API_app-registry_TagResource"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

Assigns one or more tags (key-value pairs) to the specified resource.

Each tag consists of a key and an optional value. If a tag with the same key is already associated with the resource, this action updates its value.

This operation returns an empty response if the call was successful.

## Request Syntax
<a name="API_app-registry_TagResource_RequestSyntax"></a>

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
<a name="API_app-registry_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_app-registry_TagResource_RequestSyntax) **   <a name="servicecatalog-app-registry_TagResource-request-uri-resourceArn"></a>
The Amazon resource name (ARN) that specifies the resource.
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
Required: Yes

## Request Body
<a name="API_app-registry_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_app-registry_TagResource_RequestSyntax) **   <a name="servicecatalog-app-registry_TagResource-request-tags"></a>
The new or modified tags for the resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Required: Yes

## Response Syntax
<a name="API_app-registry_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_app-registry_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_app-registry_TagResource_Errors"></a>

 ** InternalServerException **
The service is experiencing internal problems.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ValidationException **
The request has invalid or missing parameters.
HTTP Status Code: 400

## See Also
<a name="API_app-registry_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/TagResource)

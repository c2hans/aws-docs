---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Tags a resource.

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

 ** [resourceArn](#API_TagResource_RequestSyntax) **   <a name="API-TagResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) associated with the resource you want to tag.
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:[\d\w/-]+`
Required: Yes

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_TagResource_RequestSyntax) **   <a name="API-TagResource-request-tags"></a>
A map of objects specifying each key name and value.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/TagResource)

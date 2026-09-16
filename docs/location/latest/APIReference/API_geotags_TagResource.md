---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_TagResource.html
---

# TagResource
<a name="API_geotags_TagResource"></a>

Assigns one or more tags (key-value pairs) to the specified Amazon Location Service resource.

Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.

You can use the `TagResource` operation with an Amazon Location Service resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the tags already associated with the resource. If you specify a tag key that's already associated with the resource, the new tag value that you specify replaces the previous value for that tag.

You can associate up to 50 tags with a resource.

## Request Syntax
<a name="API_geotags_TagResource_RequestSyntax"></a>

```
POST /tags/{{ResourceArn}} HTTP/1.1
Content-type: application/json

{
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_geotags_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_geotags_TagResource_RequestSyntax) **   <a name="location-geotags_TagResource-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource whose tags you want to update.
+ Format example: `arn:aws:geo:region:account-id:resourcetype/ExampleResource`
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`
Required: Yes

## Request Body
<a name="API_geotags_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_geotags_TagResource_RequestSyntax) **   <a name="location-geotags_TagResource-request-Tags"></a>
Applies one or more tags to specific resource. A tag is a key-value pair that helps you manage, identify, search, and filter your resources.
Format: `"key" : "value"`
Restrictions:
+ Maximum 50 tags per resource.
+ Each tag key must be unique and must have exactly one associated value.
+ Maximum key length: 128 Unicode characters in UTF-8.
+ Maximum value length: 256 Unicode characters in UTF-8.
+ Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: \+ - = . \_ : / @
+ Cannot use `"aws:"` as a prefix for a key.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Required: Yes

## Response Syntax
<a name="API_geotags_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_geotags_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_geotags_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

HTTP Status Code: 403

 ** InternalServerException **

HTTP Status Code: 500

 ** ResourceNotFoundException **

HTTP Status Code: 404

 ** ThrottlingException **

HTTP Status Code: 429

 ** ValidationException **

HTTP Status Code: 400

## See Also
<a name="API_geotags_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geotags-2020-11-19/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geotags-2020-11-19/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geotags-2020-11-19/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geotags-2020-11-19/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geotags-2020-11-19/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geotags-2020-11-19/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geotags-2020-11-19/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geotags-2020-11-19/TagResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/geotags-2020-11-19/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geotags-2020-11-19/TagResource)

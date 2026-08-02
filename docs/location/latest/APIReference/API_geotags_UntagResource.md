---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_UntagResource.html
---

# UntagResource
<a name="API_geotags_UntagResource"></a>

Removes one or more tags from the specified Amazon Location resource.

## Request Syntax
<a name="API_geotags_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{ResourceArn}}?tagKeys={{TagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geotags_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_geotags_UntagResource_RequestSyntax) **   <a name="location-geotags_UntagResource-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource from which you want to remove tags.
+ Format example: `arn:aws:geo:region:account-id:resourcetype/ExampleResource`
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`
Required: Yes

 ** [TagKeys](#API_geotags_UntagResource_RequestSyntax) **   <a name="location-geotags_UntagResource-request-uri-TagKeys"></a>
The list of tag keys to remove from the specified resource.
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Request Body
<a name="API_geotags_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geotags_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_geotags_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_geotags_UntagResource_Errors"></a>

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
<a name="API_geotags_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geotags-2020-11-19/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geotags-2020-11-19/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geotags-2020-11-19/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geotags-2020-11-19/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geotags-2020-11-19/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geotags-2020-11-19/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geotags-2020-11-19/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geotags-2020-11-19/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/geotags-2020-11-19/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geotags-2020-11-19/UntagResource)

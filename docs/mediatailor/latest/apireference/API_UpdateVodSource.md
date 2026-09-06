---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_UpdateVodSource.html
---

# UpdateVodSource
<a name="API_UpdateVodSource"></a>

Updates a VOD source's configuration.

## Request Syntax
<a name="API_UpdateVodSource_RequestSyntax"></a>

```
PUT /sourceLocation/{{SourceLocationName}}/vodSource/{{VodSourceName}} HTTP/1.1
Content-type: application/json

{
   "HttpPackageConfigurations": [
      {
         "Path": "{{string}}",
         "SourceGroup": "{{string}}",
         "Type": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateVodSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SourceLocationName](#API_UpdateVodSource_RequestSyntax) **   <a name="mediatailor-UpdateVodSource-request-uri-SourceLocationName"></a>
The name of the source location associated with this VOD Source.
Required: Yes

 ** [VodSourceName](#API_UpdateVodSource_RequestSyntax) **   <a name="mediatailor-UpdateVodSource-request-uri-VodSourceName"></a>
The name of the VOD source.
Required: Yes

## Request Body
<a name="API_UpdateVodSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [HttpPackageConfigurations](#API_UpdateVodSource_RequestSyntax) **   <a name="mediatailor-UpdateVodSource-request-HttpPackageConfigurations"></a>
A list of HTTP package configurations for the VOD source on this account.
Type: Array of [HttpPackageConfiguration](API_HttpPackageConfiguration.md) objects
Required: Yes

## Response Syntax
<a name="API_UpdateVodSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreationTime": number,
   "HttpPackageConfigurations": [
      {
         "Path": "string",
         "SourceGroup": "string",
         "Type": "string"
      }
   ],
   "LastModifiedTime": number,
   "SourceLocationName": "string",
   "tags": {
      "string" : "string"
   },
   "VodSourceName": "string"
}
```

## Response Elements
<a name="API_UpdateVodSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateVodSource_ResponseSyntax) **   <a name="mediatailor-UpdateVodSource-response-Arn"></a>
The Amazon Resource Name (ARN) associated with the VOD source.
Type: String

 ** [CreationTime](#API_UpdateVodSource_ResponseSyntax) **   <a name="mediatailor-UpdateVodSource-response-CreationTime"></a>
The timestamp that indicates when the VOD source was created.
Type: Timestamp

 ** [HttpPackageConfigurations](#API_UpdateVodSource_ResponseSyntax) **   <a name="mediatailor-UpdateVodSource-response-HttpPackageConfigurations"></a>
A list of HTTP package configurations for the VOD source on this account.
Type: Array of [HttpPackageConfiguration](API_HttpPackageConfiguration.md) objects

 ** [LastModifiedTime](#API_UpdateVodSource_ResponseSyntax) **   <a name="mediatailor-UpdateVodSource-response-LastModifiedTime"></a>
The timestamp that indicates when the VOD source was last modified.
Type: Timestamp

 ** [SourceLocationName](#API_UpdateVodSource_ResponseSyntax) **   <a name="mediatailor-UpdateVodSource-response-SourceLocationName"></a>
The name of the source location associated with the VOD source.
Type: String

 ** [tags](#API_UpdateVodSource_ResponseSyntax) **   <a name="mediatailor-UpdateVodSource-response-tags"></a>
The tags to assign to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

 ** [VodSourceName](#API_UpdateVodSource_ResponseSyntax) **   <a name="mediatailor-UpdateVodSource-response-VodSourceName"></a>
The name of the VOD source.
Type: String

## Errors
<a name="API_UpdateVodSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_UpdateVodSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/UpdateVodSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/UpdateVodSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/UpdateVodSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/UpdateVodSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/UpdateVodSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/UpdateVodSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/UpdateVodSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/UpdateVodSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/UpdateVodSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/UpdateVodSource)

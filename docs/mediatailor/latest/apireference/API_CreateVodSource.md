---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_CreateVodSource.html
---

# CreateVodSource
<a name="API_CreateVodSource"></a>

The VOD source configuration parameters.

## Request Syntax
<a name="API_CreateVodSource_RequestSyntax"></a>

```
POST /sourceLocation/{{SourceLocationName}}/vodSource/{{VodSourceName}} HTTP/1.1
Content-type: application/json

{
   "HttpPackageConfigurations": [
      {
         "Path": "{{string}}",
         "SourceGroup": "{{string}}",
         "Type": "{{string}}"
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateVodSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SourceLocationName](#API_CreateVodSource_RequestSyntax) **   <a name="mediatailor-CreateVodSource-request-uri-SourceLocationName"></a>
The name of the source location for this VOD source.
Required: Yes

 ** [VodSourceName](#API_CreateVodSource_RequestSyntax) **   <a name="mediatailor-CreateVodSource-request-uri-VodSourceName"></a>
The name associated with the VOD source.>
Required: Yes

## Request Body
<a name="API_CreateVodSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [HttpPackageConfigurations](#API_CreateVodSource_RequestSyntax) **   <a name="mediatailor-CreateVodSource-request-HttpPackageConfigurations"></a>
A list of HTTP package configuration parameters for this VOD source.
Type: Array of [HttpPackageConfiguration](API_HttpPackageConfiguration.md) objects
Required: Yes

 ** [tags](#API_CreateVodSource_RequestSyntax) **   <a name="mediatailor-CreateVodSource-request-tags"></a>
The tags to assign to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateVodSource_ResponseSyntax"></a>

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
<a name="API_CreateVodSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateVodSource_ResponseSyntax) **   <a name="mediatailor-CreateVodSource-response-Arn"></a>
The ARN to assign to this VOD source.
Type: String

 ** [CreationTime](#API_CreateVodSource_ResponseSyntax) **   <a name="mediatailor-CreateVodSource-response-CreationTime"></a>
The time the VOD source was created.
Type: Timestamp

 ** [HttpPackageConfigurations](#API_CreateVodSource_ResponseSyntax) **   <a name="mediatailor-CreateVodSource-response-HttpPackageConfigurations"></a>
A list of HTTP package configuration parameters for this VOD source.
Type: Array of [HttpPackageConfiguration](API_HttpPackageConfiguration.md) objects

 ** [LastModifiedTime](#API_CreateVodSource_ResponseSyntax) **   <a name="mediatailor-CreateVodSource-response-LastModifiedTime"></a>
The time the VOD source was last modified.
Type: Timestamp

 ** [SourceLocationName](#API_CreateVodSource_ResponseSyntax) **   <a name="mediatailor-CreateVodSource-response-SourceLocationName"></a>
The name to assign to the source location for this VOD source.
Type: String

 ** [tags](#API_CreateVodSource_ResponseSyntax) **   <a name="mediatailor-CreateVodSource-response-tags"></a>
The tags to assign to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

 ** [VodSourceName](#API_CreateVodSource_ResponseSyntax) **   <a name="mediatailor-CreateVodSource-response-VodSourceName"></a>
The name to assign to the VOD source.
Type: String

## Errors
<a name="API_CreateVodSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateVodSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/CreateVodSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/CreateVodSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/CreateVodSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/CreateVodSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/CreateVodSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/CreateVodSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/CreateVodSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/CreateVodSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/CreateVodSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/CreateVodSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

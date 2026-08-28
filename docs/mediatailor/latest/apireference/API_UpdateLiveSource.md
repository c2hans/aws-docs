---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_UpdateLiveSource.html
---

# UpdateLiveSource
<a name="API_UpdateLiveSource"></a>

Updates a live source's configuration.

## Request Syntax
<a name="API_UpdateLiveSource_RequestSyntax"></a>

```
PUT /sourceLocation/{{SourceLocationName}}/liveSource/{{LiveSourceName}} HTTP/1.1
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
<a name="API_UpdateLiveSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LiveSourceName](#API_UpdateLiveSource_RequestSyntax) **   <a name="mediatailor-UpdateLiveSource-request-uri-LiveSourceName"></a>
The name of the live source.
Required: Yes

 ** [SourceLocationName](#API_UpdateLiveSource_RequestSyntax) **   <a name="mediatailor-UpdateLiveSource-request-uri-SourceLocationName"></a>
The name of the source location associated with this Live Source.
Required: Yes

## Request Body
<a name="API_UpdateLiveSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [HttpPackageConfigurations](#API_UpdateLiveSource_RequestSyntax) **   <a name="mediatailor-UpdateLiveSource-request-HttpPackageConfigurations"></a>
A list of HTTP package configurations for the live source on this account.
Type: Array of [HttpPackageConfiguration](API_HttpPackageConfiguration.md) objects
Required: Yes

## Response Syntax
<a name="API_UpdateLiveSource_ResponseSyntax"></a>

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
   "LiveSourceName": "string",
   "SourceLocationName": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_UpdateLiveSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateLiveSource_ResponseSyntax) **   <a name="mediatailor-UpdateLiveSource-response-Arn"></a>
The Amazon Resource Name (ARN) associated with this live source.
Type: String

 ** [CreationTime](#API_UpdateLiveSource_ResponseSyntax) **   <a name="mediatailor-UpdateLiveSource-response-CreationTime"></a>
The timestamp that indicates when the live source was created.
Type: Timestamp

 ** [HttpPackageConfigurations](#API_UpdateLiveSource_ResponseSyntax) **   <a name="mediatailor-UpdateLiveSource-response-HttpPackageConfigurations"></a>
A list of HTTP package configurations for the live source on this account.
Type: Array of [HttpPackageConfiguration](API_HttpPackageConfiguration.md) objects

 ** [LastModifiedTime](#API_UpdateLiveSource_ResponseSyntax) **   <a name="mediatailor-UpdateLiveSource-response-LastModifiedTime"></a>
The timestamp that indicates when the live source was last modified.
Type: Timestamp

 ** [LiveSourceName](#API_UpdateLiveSource_ResponseSyntax) **   <a name="mediatailor-UpdateLiveSource-response-LiveSourceName"></a>
The name of the live source.
Type: String

 ** [SourceLocationName](#API_UpdateLiveSource_ResponseSyntax) **   <a name="mediatailor-UpdateLiveSource-response-SourceLocationName"></a>
The name of the source location associated with the live source.
Type: String

 ** [tags](#API_UpdateLiveSource_ResponseSyntax) **   <a name="mediatailor-UpdateLiveSource-response-tags"></a>
The tags to assign to the live source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

## Errors
<a name="API_UpdateLiveSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_UpdateLiveSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/UpdateLiveSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/UpdateLiveSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/UpdateLiveSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/UpdateLiveSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/UpdateLiveSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/UpdateLiveSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/UpdateLiveSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/UpdateLiveSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/UpdateLiveSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/UpdateLiveSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

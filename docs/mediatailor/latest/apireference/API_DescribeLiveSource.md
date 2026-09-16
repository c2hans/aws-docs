---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DescribeLiveSource.html
---

# DescribeLiveSource
<a name="API_DescribeLiveSource"></a>

The live source to describe.

## Request Syntax
<a name="API_DescribeLiveSource_RequestSyntax"></a>

```
GET /sourceLocation/{{SourceLocationName}}/liveSource/{{LiveSourceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeLiveSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LiveSourceName](#API_DescribeLiveSource_RequestSyntax) **   <a name="mediatailor-DescribeLiveSource-request-uri-LiveSourceName"></a>
The name of the live source.
Required: Yes

 ** [SourceLocationName](#API_DescribeLiveSource_RequestSyntax) **   <a name="mediatailor-DescribeLiveSource-request-uri-SourceLocationName"></a>
The name of the source location associated with this Live Source.
Required: Yes

## Request Body
<a name="API_DescribeLiveSource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeLiveSource_ResponseSyntax"></a>

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
<a name="API_DescribeLiveSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribeLiveSource_ResponseSyntax) **   <a name="mediatailor-DescribeLiveSource-response-Arn"></a>
The ARN of the live source.
Type: String

 ** [CreationTime](#API_DescribeLiveSource_ResponseSyntax) **   <a name="mediatailor-DescribeLiveSource-response-CreationTime"></a>
The timestamp that indicates when the live source was created.
Type: Timestamp

 ** [HttpPackageConfigurations](#API_DescribeLiveSource_ResponseSyntax) **   <a name="mediatailor-DescribeLiveSource-response-HttpPackageConfigurations"></a>
The HTTP package configurations.
Type: Array of [HttpPackageConfiguration](API_HttpPackageConfiguration.md) objects

 ** [LastModifiedTime](#API_DescribeLiveSource_ResponseSyntax) **   <a name="mediatailor-DescribeLiveSource-response-LastModifiedTime"></a>
The timestamp that indicates when the live source was modified.
Type: Timestamp

 ** [LiveSourceName](#API_DescribeLiveSource_ResponseSyntax) **   <a name="mediatailor-DescribeLiveSource-response-LiveSourceName"></a>
The name of the live source.
Type: String

 ** [SourceLocationName](#API_DescribeLiveSource_ResponseSyntax) **   <a name="mediatailor-DescribeLiveSource-response-SourceLocationName"></a>
The name of the source location associated with the live source.
Type: String

 ** [tags](#API_DescribeLiveSource_ResponseSyntax) **   <a name="mediatailor-DescribeLiveSource-response-tags"></a>
The tags assigned to the live source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

## Errors
<a name="API_DescribeLiveSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeLiveSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/DescribeLiveSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/DescribeLiveSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/DescribeLiveSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/DescribeLiveSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/DescribeLiveSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/DescribeLiveSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/DescribeLiveSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/DescribeLiveSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/DescribeLiveSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/DescribeLiveSource)

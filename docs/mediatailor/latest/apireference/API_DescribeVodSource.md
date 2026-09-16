---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DescribeVodSource.html
---

# DescribeVodSource
<a name="API_DescribeVodSource"></a>

Provides details about a specific video on demand (VOD) source in a specific source location.

## Request Syntax
<a name="API_DescribeVodSource_RequestSyntax"></a>

```
GET /sourceLocation/{{SourceLocationName}}/vodSource/{{VodSourceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeVodSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SourceLocationName](#API_DescribeVodSource_RequestSyntax) **   <a name="mediatailor-DescribeVodSource-request-uri-SourceLocationName"></a>
The name of the source location associated with this VOD Source.
Required: Yes

 ** [VodSourceName](#API_DescribeVodSource_RequestSyntax) **   <a name="mediatailor-DescribeVodSource-request-uri-VodSourceName"></a>
The name of the VOD Source.
Required: Yes

## Request Body
<a name="API_DescribeVodSource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeVodSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AdBreakOpportunities": [
      {
         "OffsetMillis": number
      }
   ],
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
<a name="API_DescribeVodSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdBreakOpportunities](#API_DescribeVodSource_ResponseSyntax) **   <a name="mediatailor-DescribeVodSource-response-AdBreakOpportunities"></a>
The ad break opportunities within the VOD source.
Type: Array of [AdBreakOpportunity](API_AdBreakOpportunity.md) objects

 ** [Arn](#API_DescribeVodSource_ResponseSyntax) **   <a name="mediatailor-DescribeVodSource-response-Arn"></a>
The ARN of the VOD source.
Type: String

 ** [CreationTime](#API_DescribeVodSource_ResponseSyntax) **   <a name="mediatailor-DescribeVodSource-response-CreationTime"></a>
The timestamp that indicates when the VOD source was created.
Type: Timestamp

 ** [HttpPackageConfigurations](#API_DescribeVodSource_ResponseSyntax) **   <a name="mediatailor-DescribeVodSource-response-HttpPackageConfigurations"></a>
The HTTP package configurations.
Type: Array of [HttpPackageConfiguration](API_HttpPackageConfiguration.md) objects

 ** [LastModifiedTime](#API_DescribeVodSource_ResponseSyntax) **   <a name="mediatailor-DescribeVodSource-response-LastModifiedTime"></a>
The last modified time of the VOD source.
Type: Timestamp

 ** [SourceLocationName](#API_DescribeVodSource_ResponseSyntax) **   <a name="mediatailor-DescribeVodSource-response-SourceLocationName"></a>
The name of the source location associated with the VOD source.
Type: String

 ** [tags](#API_DescribeVodSource_ResponseSyntax) **   <a name="mediatailor-DescribeVodSource-response-tags"></a>
The tags assigned to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

 ** [VodSourceName](#API_DescribeVodSource_ResponseSyntax) **   <a name="mediatailor-DescribeVodSource-response-VodSourceName"></a>
The name of the VOD source.
Type: String

## Errors
<a name="API_DescribeVodSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeVodSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/DescribeVodSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/DescribeVodSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/DescribeVodSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/DescribeVodSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/DescribeVodSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/DescribeVodSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/DescribeVodSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/DescribeVodSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/DescribeVodSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/DescribeVodSource)

---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DescribeSourceLocation.html
---

# DescribeSourceLocation
<a name="API_DescribeSourceLocation"></a>

Describes a source location. A source location is a container for sources. For more information about source locations, see [Working with source locations](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html) in the *MediaTailor User Guide*.

## Request Syntax
<a name="API_DescribeSourceLocation_RequestSyntax"></a>

```
GET /sourceLocation/{{SourceLocationName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeSourceLocation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SourceLocationName](#API_DescribeSourceLocation_RequestSyntax) **   <a name="mediatailor-DescribeSourceLocation-request-uri-SourceLocationName"></a>
The name of the source location.
Required: Yes

## Request Body
<a name="API_DescribeSourceLocation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeSourceLocation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccessConfiguration": {
      "AccessType": "string",
      "SecretsManagerAccessTokenConfiguration": {
         "HeaderName": "string",
         "SecretArn": "string",
         "SecretStringKey": "string"
      }
   },
   "Arn": "string",
   "CreationTime": number,
   "DefaultSegmentDeliveryConfiguration": {
      "BaseUrl": "string"
   },
   "HttpConfiguration": {
      "BaseUrl": "string"
   },
   "LastModifiedTime": number,
   "SegmentDeliveryConfigurations": [
      {
         "BaseUrl": "string",
         "Name": "string"
      }
   ],
   "SourceLocationName": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_DescribeSourceLocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessConfiguration](#API_DescribeSourceLocation_ResponseSyntax) **   <a name="mediatailor-DescribeSourceLocation-response-AccessConfiguration"></a>
The access configuration for the source location.
Type: [AccessConfiguration](API_AccessConfiguration.md) object

 ** [Arn](#API_DescribeSourceLocation_ResponseSyntax) **   <a name="mediatailor-DescribeSourceLocation-response-Arn"></a>
The ARN of the source location.
Type: String

 ** [CreationTime](#API_DescribeSourceLocation_ResponseSyntax) **   <a name="mediatailor-DescribeSourceLocation-response-CreationTime"></a>
The timestamp that indicates when the source location was created.
Type: Timestamp

 ** [DefaultSegmentDeliveryConfiguration](#API_DescribeSourceLocation_ResponseSyntax) **   <a name="mediatailor-DescribeSourceLocation-response-DefaultSegmentDeliveryConfiguration"></a>
The default segment delivery configuration settings.
Type: [DefaultSegmentDeliveryConfiguration](API_DefaultSegmentDeliveryConfiguration.md) object

 ** [HttpConfiguration](#API_DescribeSourceLocation_ResponseSyntax) **   <a name="mediatailor-DescribeSourceLocation-response-HttpConfiguration"></a>
The HTTP package configuration settings for the source location.
Type: [HttpConfiguration](API_HttpConfiguration.md) object

 ** [LastModifiedTime](#API_DescribeSourceLocation_ResponseSyntax) **   <a name="mediatailor-DescribeSourceLocation-response-LastModifiedTime"></a>
The timestamp that indicates when the source location was last modified.
Type: Timestamp

 ** [SegmentDeliveryConfigurations](#API_DescribeSourceLocation_ResponseSyntax) **   <a name="mediatailor-DescribeSourceLocation-response-SegmentDeliveryConfigurations"></a>
A list of the segment delivery configurations associated with this resource.
Type: Array of [SegmentDeliveryConfiguration](API_SegmentDeliveryConfiguration.md) objects

 ** [SourceLocationName](#API_DescribeSourceLocation_ResponseSyntax) **   <a name="mediatailor-DescribeSourceLocation-response-SourceLocationName"></a>
The name of the source location.
Type: String

 ** [tags](#API_DescribeSourceLocation_ResponseSyntax) **   <a name="mediatailor-DescribeSourceLocation-response-tags"></a>
The tags assigned to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

## Errors
<a name="API_DescribeSourceLocation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeSourceLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/DescribeSourceLocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/DescribeSourceLocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/DescribeSourceLocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/DescribeSourceLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/DescribeSourceLocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/DescribeSourceLocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/DescribeSourceLocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/DescribeSourceLocation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/DescribeSourceLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/DescribeSourceLocation)

---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_CreateSourceLocation.html
---

# CreateSourceLocation
<a name="API_CreateSourceLocation"></a>

Creates a source location. A source location is a container for sources. For more information about source locations, see [Working with source locations](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html) in the *MediaTailor User Guide*.

## Request Syntax
<a name="API_CreateSourceLocation_RequestSyntax"></a>

```
POST /sourceLocation/{{SourceLocationName}} HTTP/1.1
Content-type: application/json

{
   "AccessConfiguration": {
      "AccessType": "{{string}}",
      "SecretsManagerAccessTokenConfiguration": {
         "HeaderName": "{{string}}",
         "SecretArn": "{{string}}",
         "SecretStringKey": "{{string}}"
      }
   },
   "DefaultSegmentDeliveryConfiguration": {
      "BaseUrl": "{{string}}"
   },
   "HttpConfiguration": {
      "BaseUrl": "{{string}}"
   },
   "SegmentDeliveryConfigurations": [
      {
         "BaseUrl": "{{string}}",
         "Name": "{{string}}"
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSourceLocation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SourceLocationName](#API_CreateSourceLocation_RequestSyntax) **   <a name="mediatailor-CreateSourceLocation-request-uri-SourceLocationName"></a>
The name associated with the source location.
Required: Yes

## Request Body
<a name="API_CreateSourceLocation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccessConfiguration](#API_CreateSourceLocation_RequestSyntax) **   <a name="mediatailor-CreateSourceLocation-request-AccessConfiguration"></a>
Access configuration parameters. Configures the type of authentication used to access content from your source location.
Type: [AccessConfiguration](API_AccessConfiguration.md) object
Required: No

 ** [DefaultSegmentDeliveryConfiguration](#API_CreateSourceLocation_RequestSyntax) **   <a name="mediatailor-CreateSourceLocation-request-DefaultSegmentDeliveryConfiguration"></a>
The optional configuration for the server that serves segments.
Type: [DefaultSegmentDeliveryConfiguration](API_DefaultSegmentDeliveryConfiguration.md) object
Required: No

 ** [HttpConfiguration](#API_CreateSourceLocation_RequestSyntax) **   <a name="mediatailor-CreateSourceLocation-request-HttpConfiguration"></a>
The source's HTTP package configurations.
Type: [HttpConfiguration](API_HttpConfiguration.md) object
Required: Yes

 ** [SegmentDeliveryConfigurations](#API_CreateSourceLocation_RequestSyntax) **   <a name="mediatailor-CreateSourceLocation-request-SegmentDeliveryConfigurations"></a>
A list of the segment delivery configurations associated with this resource.
Type: Array of [SegmentDeliveryConfiguration](API_SegmentDeliveryConfiguration.md) objects
Required: No

 ** [tags](#API_CreateSourceLocation_RequestSyntax) **   <a name="mediatailor-CreateSourceLocation-request-tags"></a>
The tags to assign to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateSourceLocation_ResponseSyntax"></a>

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
<a name="API_CreateSourceLocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessConfiguration](#API_CreateSourceLocation_ResponseSyntax) **   <a name="mediatailor-CreateSourceLocation-response-AccessConfiguration"></a>
Access configuration parameters. Configures the type of authentication used to access content from your source location.
Type: [AccessConfiguration](API_AccessConfiguration.md) object

 ** [Arn](#API_CreateSourceLocation_ResponseSyntax) **   <a name="mediatailor-CreateSourceLocation-response-Arn"></a>
The ARN to assign to the source location.
Type: String

 ** [CreationTime](#API_CreateSourceLocation_ResponseSyntax) **   <a name="mediatailor-CreateSourceLocation-response-CreationTime"></a>
The time the source location was created.
Type: Timestamp

 ** [DefaultSegmentDeliveryConfiguration](#API_CreateSourceLocation_ResponseSyntax) **   <a name="mediatailor-CreateSourceLocation-response-DefaultSegmentDeliveryConfiguration"></a>
The optional configuration for the server that serves segments.
Type: [DefaultSegmentDeliveryConfiguration](API_DefaultSegmentDeliveryConfiguration.md) object

 ** [HttpConfiguration](#API_CreateSourceLocation_ResponseSyntax) **   <a name="mediatailor-CreateSourceLocation-response-HttpConfiguration"></a>
The source's HTTP package configurations.
Type: [HttpConfiguration](API_HttpConfiguration.md) object

 ** [LastModifiedTime](#API_CreateSourceLocation_ResponseSyntax) **   <a name="mediatailor-CreateSourceLocation-response-LastModifiedTime"></a>
The time the source location was last modified.
Type: Timestamp

 ** [SegmentDeliveryConfigurations](#API_CreateSourceLocation_ResponseSyntax) **   <a name="mediatailor-CreateSourceLocation-response-SegmentDeliveryConfigurations"></a>
The segment delivery configurations for the source location. For information about MediaTailor configurations, see [Working with configurations in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html).
Type: Array of [SegmentDeliveryConfiguration](API_SegmentDeliveryConfiguration.md) objects

 ** [SourceLocationName](#API_CreateSourceLocation_ResponseSyntax) **   <a name="mediatailor-CreateSourceLocation-response-SourceLocationName"></a>
The name to assign to the source location.
Type: String

 ** [tags](#API_CreateSourceLocation_ResponseSyntax) **   <a name="mediatailor-CreateSourceLocation-response-tags"></a>
The tags to assign to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

## Errors
<a name="API_CreateSourceLocation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateSourceLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/CreateSourceLocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/CreateSourceLocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/CreateSourceLocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/CreateSourceLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/CreateSourceLocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/CreateSourceLocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/CreateSourceLocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/CreateSourceLocation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/CreateSourceLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/CreateSourceLocation)

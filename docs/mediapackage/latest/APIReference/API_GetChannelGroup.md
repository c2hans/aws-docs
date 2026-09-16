---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetChannelGroup.html
---

# GetChannelGroup
<a name="API_GetChannelGroup"></a>

Retrieves the specified channel group that's configured in AWS Elemental MediaPackage.

## Request Syntax
<a name="API_GetChannelGroup_RequestSyntax"></a>

```
GET /channelGroup/{{ChannelGroupName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetChannelGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_GetChannelGroup_RequestSyntax) **   <a name="mediapackage-GetChannelGroup-request-uri-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_GetChannelGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetChannelGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "ChannelGroupName": "string",
   "CreatedAt": number,
   "Description": "string",
   "EgressDomain": "string",
   "ETag": "string",
   "ModifiedAt": number,
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetChannelGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetChannelGroup_ResponseSyntax) **   <a name="mediapackage-GetChannelGroup-response-Arn"></a>
The Amazon Resource Name (ARN) associated with the resource.
Type: String

 ** [ChannelGroupName](#API_GetChannelGroup_ResponseSyntax) **   <a name="mediapackage-GetChannelGroup-response-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Type: String

 ** [CreatedAt](#API_GetChannelGroup_ResponseSyntax) **   <a name="mediapackage-GetChannelGroup-response-CreatedAt"></a>
The date and time the channel group was created.
Type: Timestamp

 ** [Description](#API_GetChannelGroup_ResponseSyntax) **   <a name="mediapackage-GetChannelGroup-response-Description"></a>
The description for your channel group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [EgressDomain](#API_GetChannelGroup_ResponseSyntax) **   <a name="mediapackage-GetChannelGroup-response-EgressDomain"></a>
The output domain where the source stream should be sent. Integrate the domain with a downstream CDN (such as Amazon CloudFront) or playback device.
Type: String

 ** [ETag](#API_GetChannelGroup_ResponseSyntax) **   <a name="mediapackage-GetChannelGroup-response-ETag"></a>
The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

 ** [ModifiedAt](#API_GetChannelGroup_ResponseSyntax) **   <a name="mediapackage-GetChannelGroup-response-ModifiedAt"></a>
The date and time the channel group was modified.
Type: Timestamp

 ** [tags](#API_GetChannelGroup_ResponseSyntax) **   <a name="mediapackage-GetChannelGroup-response-tags"></a>
The comma-separated list of tag key:value pairs assigned to the channel group.
Type: String to string map

## Errors
<a name="API_GetChannelGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.
HTTP Status Code: 403

 ** InternalServerException **
Indicates that an error from the service occurred while trying to process a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceTypeNotFound **
The specified resource type wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The request throughput limit was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** ValidationExceptionType **
The type of ValidationException.
HTTP Status Code: 400

## See Also
<a name="API_GetChannelGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/GetChannelGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/GetChannelGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/GetChannelGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/GetChannelGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/GetChannelGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/GetChannelGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/GetChannelGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/GetChannelGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/GetChannelGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/GetChannelGroup)

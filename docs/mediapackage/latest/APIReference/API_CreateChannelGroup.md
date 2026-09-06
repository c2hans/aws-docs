---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateChannelGroup.html
---

# CreateChannelGroup
<a name="API_CreateChannelGroup"></a>

Create a channel group to group your channels and origin endpoints. A channel group is the top-level resource that consists of channels and origin endpoints that are associated with it and that provides predictable URLs for stream delivery. All channels and origin endpoints within the channel group are guaranteed to share the DNS. You can create only one channel group with each request.

## Request Syntax
<a name="API_CreateChannelGroup_RequestSyntax"></a>

```
POST /channelGroup HTTP/1.1
x-amzn-client-token: {{ClientToken}}
Content-type: application/json

{
   "ChannelGroupName": "{{string}}",
   "Description": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateChannelGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ClientToken](#API_CreateChannelGroup_RequestSyntax) **   <a name="mediapackage-CreateChannelGroup-request-ClientToken"></a>
A unique, case-sensitive token that you provide to ensure the idempotency of the request.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

## Request Body
<a name="API_CreateChannelGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChannelGroupName](#API_CreateChannelGroup_RequestSyntax) **   <a name="mediapackage-CreateChannelGroup-request-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. You can't use spaces in the name. You can't change the name after you create the channel group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [Description](#API_CreateChannelGroup_RequestSyntax) **   <a name="mediapackage-CreateChannelGroup-request-Description"></a>
Enter any descriptive text that helps you to identify the channel group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [tags](#API_CreateChannelGroup_RequestSyntax) **   <a name="mediapackage-CreateChannelGroup-request-tags"></a>
A comma-separated list of tag key:value pairs that you define. For example:
 `"Key1": "Value1",`
 `"Key2": "Value2"`
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateChannelGroup_ResponseSyntax"></a>

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
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateChannelGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateChannelGroup_ResponseSyntax) **   <a name="mediapackage-CreateChannelGroup-response-Arn"></a>
The Amazon Resource Name (ARN) associated with the resource.
Type: String

 ** [ChannelGroupName](#API_CreateChannelGroup_ResponseSyntax) **   <a name="mediapackage-CreateChannelGroup-response-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Type: String

 ** [CreatedAt](#API_CreateChannelGroup_ResponseSyntax) **   <a name="mediapackage-CreateChannelGroup-response-CreatedAt"></a>
The date and time the channel group was created.
Type: Timestamp

 ** [Description](#API_CreateChannelGroup_ResponseSyntax) **   <a name="mediapackage-CreateChannelGroup-response-Description"></a>
The description for your channel group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [EgressDomain](#API_CreateChannelGroup_ResponseSyntax) **   <a name="mediapackage-CreateChannelGroup-response-EgressDomain"></a>
The output domain where the source stream should be sent. Integrate the egress domain with a downstream CDN (such as Amazon CloudFront) or playback device.
Type: String

 ** [ETag](#API_CreateChannelGroup_ResponseSyntax) **   <a name="mediapackage-CreateChannelGroup-response-ETag"></a>
The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

 ** [ModifiedAt](#API_CreateChannelGroup_ResponseSyntax) **   <a name="mediapackage-CreateChannelGroup-response-ModifiedAt"></a>
The date and time the channel group was modified.
Type: Timestamp

 ** [Tags](#API_CreateChannelGroup_ResponseSyntax) **   <a name="mediapackage-CreateChannelGroup-response-Tags"></a>
The comma-separated list of tag key:value pairs assigned to the channel group.
Type: String to string map

## Errors
<a name="API_CreateChannelGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting this resource can cause an inconsistent state.
 ** ConflictExceptionType **
The type of ConflictException.
HTTP Status Code: 409

 ** InternalServerException **
Indicates that an error from the service occurred while trying to process a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceTypeNotFound **
The specified resource type wasn't found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request throughput limit was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** ValidationExceptionType **
The type of ValidationException.
HTTP Status Code: 400

## See Also
<a name="API_CreateChannelGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/CreateChannelGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/CreateChannelGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/CreateChannelGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/CreateChannelGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/CreateChannelGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/CreateChannelGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/CreateChannelGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/CreateChannelGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/CreateChannelGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/CreateChannelGroup)

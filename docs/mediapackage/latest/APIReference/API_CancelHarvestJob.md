---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CancelHarvestJob.html
---

# CancelHarvestJob
<a name="API_CancelHarvestJob"></a>

Cancels an in-progress harvest job.

## Request Syntax
<a name="API_CancelHarvestJob_RequestSyntax"></a>

```
PUT /channelGroup/{{ChannelGroupName}}/channel/{{ChannelName}}/originEndpoint/{{OriginEndpointName}}/harvestJob/{{HarvestJobName}} HTTP/1.1
x-amzn-update-if-match: {{ETag}}
```

## URI Request Parameters
<a name="API_CancelHarvestJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_CancelHarvestJob_RequestSyntax) **   <a name="mediapackage-CancelHarvestJob-request-uri-ChannelGroupName"></a>
The name of the channel group containing the channel from which the harvest job is running.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ChannelName](#API_CancelHarvestJob_RequestSyntax) **   <a name="mediapackage-CancelHarvestJob-request-uri-ChannelName"></a>
The name of the channel from which the harvest job is running.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ETag](#API_CancelHarvestJob_RequestSyntax) **   <a name="mediapackage-CancelHarvestJob-request-ETag"></a>
The current Entity Tag (ETag) associated with the harvest job. Used for concurrency control.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

 ** [HarvestJobName](#API_CancelHarvestJob_RequestSyntax) **   <a name="mediapackage-CancelHarvestJob-request-uri-HarvestJobName"></a>
The name of the harvest job to cancel. This name must be unique within the channel and cannot be changed after the harvest job is submitted.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [OriginEndpointName](#API_CancelHarvestJob_RequestSyntax) **   <a name="mediapackage-CancelHarvestJob-request-uri-OriginEndpointName"></a>
The name of the origin endpoint that the harvest job is harvesting from. This cannot be changed after the harvest job is submitted.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_CancelHarvestJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelHarvestJob_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CancelHarvestJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CancelHarvestJob_Errors"></a>

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

 ** ThrottlingException **
The request throughput limit was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** ValidationExceptionType **
The type of ValidationException.
HTTP Status Code: 400

## See Also
<a name="API_CancelHarvestJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/CancelHarvestJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/CancelHarvestJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/CancelHarvestJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/CancelHarvestJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/CancelHarvestJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/CancelHarvestJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/CancelHarvestJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/CancelHarvestJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/CancelHarvestJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/CancelHarvestJob)

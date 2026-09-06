---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_PutOriginEndpointPolicy.html
---

# PutOriginEndpointPolicy
<a name="API_PutOriginEndpointPolicy"></a>

Attaches an IAM policy to the specified origin endpoint. You can attach only one policy with each request.

## Request Syntax
<a name="API_PutOriginEndpointPolicy_RequestSyntax"></a>

```
POST /channelGroup/{{ChannelGroupName}}/channel/{{ChannelName}}/originEndpoint/{{OriginEndpointName}}/policy HTTP/1.1
Content-type: application/json

{
   "CdnAuthConfiguration": {
      "CdnIdentifierSecretArns": [ "{{string}}" ],
      "SecretsRoleArn": "{{string}}"
   },
   "Policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutOriginEndpointPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_PutOriginEndpointPolicy_RequestSyntax) **   <a name="mediapackage-PutOriginEndpointPolicy-request-uri-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ChannelName](#API_PutOriginEndpointPolicy_RequestSyntax) **   <a name="mediapackage-PutOriginEndpointPolicy-request-uri-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [OriginEndpointName](#API_PutOriginEndpointPolicy_RequestSyntax) **   <a name="mediapackage-PutOriginEndpointPolicy-request-uri-OriginEndpointName"></a>
The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_PutOriginEndpointPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CdnAuthConfiguration](#API_PutOriginEndpointPolicy_RequestSyntax) **   <a name="mediapackage-PutOriginEndpointPolicy-request-CdnAuthConfiguration"></a>
The settings for using authorization headers between the MediaPackage endpoint and your CDN.
For information about CDN authorization, see [CDN authorization in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/userguide/cdn-auth.html) in the MediaPackage user guide.
Type: [CdnAuthConfiguration](API_CdnAuthConfiguration.md) object
Required: No

 ** [Policy](#API_PutOriginEndpointPolicy_RequestSyntax) **   <a name="mediapackage-PutOriginEndpointPolicy-request-Policy"></a>
The policy to attach to the specified origin endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 6144.
Required: Yes

## Response Syntax
<a name="API_PutOriginEndpointPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutOriginEndpointPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutOriginEndpointPolicy_Errors"></a>

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
<a name="API_PutOriginEndpointPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/PutOriginEndpointPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/PutOriginEndpointPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/PutOriginEndpointPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/PutOriginEndpointPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/PutOriginEndpointPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/PutOriginEndpointPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/PutOriginEndpointPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/PutOriginEndpointPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/PutOriginEndpointPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/PutOriginEndpointPolicy)

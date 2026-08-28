---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetChannelPolicy.html
---

# GetChannelPolicy
<a name="API_GetChannelPolicy"></a>

Retrieves the specified channel policy that's configured in AWS Elemental MediaPackage. With policies, you can specify who has access to AWS resources and what actions they can perform on those resources.

## Request Syntax
<a name="API_GetChannelPolicy_RequestSyntax"></a>

```
GET /channelGroup/{{ChannelGroupName}}/channel/{{ChannelName}}/policy HTTP/1.1
```

## URI Request Parameters
<a name="API_GetChannelPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_GetChannelPolicy_RequestSyntax) **   <a name="mediapackage-GetChannelPolicy-request-uri-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ChannelName](#API_GetChannelPolicy_RequestSyntax) **   <a name="mediapackage-GetChannelPolicy-request-uri-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_GetChannelPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetChannelPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChannelGroupName": "string",
   "ChannelName": "string",
   "Policy": "string"
}
```

## Response Elements
<a name="API_GetChannelPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelGroupName](#API_GetChannelPolicy_ResponseSyntax) **   <a name="mediapackage-GetChannelPolicy-response-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Type: String

 ** [ChannelName](#API_GetChannelPolicy_ResponseSyntax) **   <a name="mediapackage-GetChannelPolicy-response-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Type: String

 ** [Policy](#API_GetChannelPolicy_ResponseSyntax) **   <a name="mediapackage-GetChannelPolicy-response-Policy"></a>
The policy assigned to the channel.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 6144.

## Errors
<a name="API_GetChannelPolicy_Errors"></a>

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
<a name="API_GetChannelPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/GetChannelPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/GetChannelPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/GetChannelPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/GetChannelPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/GetChannelPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/GetChannelPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/GetChannelPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/GetChannelPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/GetChannelPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/GetChannelPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

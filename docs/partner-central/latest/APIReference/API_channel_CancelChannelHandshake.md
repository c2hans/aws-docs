---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_CancelChannelHandshake.html
---

# CancelChannelHandshake
<a name="API_channel_CancelChannelHandshake"></a>

Cancels a pending channel handshake request.

## Request Syntax
<a name="API_channel_CancelChannelHandshake_RequestSyntax"></a>

```
{
   "catalog": "{{string}}",
   "identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_channel_CancelChannelHandshake_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [catalog](#API_channel_CancelChannelHandshake_RequestSyntax) **   <a name="AWSPartnerCentral-channel_CancelChannelHandshake-request-catalog"></a>
The catalog identifier for the handshake request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]*`
Required: Yes

 ** [identifier](#API_channel_CancelChannelHandshake_RequestSyntax) **   <a name="AWSPartnerCentral-channel_CancelChannelHandshake-request-identifier"></a>
The unique identifier of the channel handshake to cancel.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/channel-handshake/)?ch-[a-z0-9]{13}`
Required: Yes

## Response Syntax
<a name="API_channel_CancelChannelHandshake_ResponseSyntax"></a>

```
{
   "channelHandshakeDetail": {
      "arn": "string",
      "id": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_channel_CancelChannelHandshake_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [channelHandshakeDetail](#API_channel_CancelChannelHandshake_ResponseSyntax) **   <a name="AWSPartnerCentral-channel_CancelChannelHandshake-response-channelHandshakeDetail"></a>
Details of the canceled channel handshake.
Type: [CancelChannelHandshakeDetail](API_channel_CancelChannelHandshakeDetail.md) object

## Errors
<a name="API_channel_CancelChannelHandshake_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions.
 ** message **
A message describing the access denial.
 ** reason **
The reason for the access denial.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request.
 ** message **
A message describing the internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** message **
A message describing the resource not found error.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to too many requests being sent in a short period.
 ** message **
A message describing the throttling error.
 ** quotaCode **
The quota code associated with the throttling error.
 ** serviceCode **
The service code associated with the throttling error.
HTTP Status Code: 400

 ** ValidationException **
The request failed validation due to invalid input parameters.
 ** fieldList **
A list of fields that failed validation.
 ** message **
A message describing the validation error.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_channel_CancelChannelHandshake_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-channel-2024-03-18/CancelChannelHandshake)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-channel-2024-03-18/CancelChannelHandshake)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/CancelChannelHandshake)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-channel-2024-03-18/CancelChannelHandshake)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/CancelChannelHandshake)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-channel-2024-03-18/CancelChannelHandshake)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-channel-2024-03-18/CancelChannelHandshake)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-channel-2024-03-18/CancelChannelHandshake)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-channel-2024-03-18/CancelChannelHandshake)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/CancelChannelHandshake)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

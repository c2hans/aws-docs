---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_CreateChannelHandshake.html
---

# CreateChannelHandshake
<a name="API_channel_CreateChannelHandshake"></a>

Creates a new channel handshake request to establish a partnership with another AWS account.

## Request Syntax
<a name="API_channel_CreateChannelHandshake_RequestSyntax"></a>

```
{
   "associatedResourceIdentifier": "{{string}}",
   "catalog": "{{string}}",
   "clientToken": "{{string}}",
   "handshakeType": "{{string}}",
   "payload": { ... },
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_channel_CreateChannelHandshake_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [associatedResourceIdentifier](#API_channel_CreateChannelHandshake_RequestSyntax) **   <a name="AWSPartnerCentral-channel_CreateChannelHandshake-request-associatedResourceIdentifier"></a>
The identifier of the resource associated with this handshake.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `((arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/program-management-account/pma-[a-z0-9]{13}(/relationship/rs-[a-z0-9]{13})?)|(pma|rs)-[a-z0-9]{13})`
Required: Yes

 ** [catalog](#API_channel_CreateChannelHandshake_RequestSyntax) **   <a name="AWSPartnerCentral-channel_CreateChannelHandshake-request-catalog"></a>
The catalog identifier for the handshake request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]*`
Required: Yes

 ** [handshakeType](#API_channel_CreateChannelHandshake_RequestSyntax) **   <a name="AWSPartnerCentral-channel_CreateChannelHandshake-request-handshakeType"></a>
The type of handshake to create (e.g., start service period, revoke service period).
Type: String
Valid Values: `START_SERVICE_PERIOD | REVOKE_SERVICE_PERIOD | PROGRAM_MANAGEMENT_ACCOUNT`
Required: Yes

 ** [clientToken](#API_channel_CreateChannelHandshake_RequestSyntax) **   <a name="AWSPartnerCentral-channel_CreateChannelHandshake-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]*`
Required: No

 ** [payload](#API_channel_CreateChannelHandshake_RequestSyntax) **   <a name="AWSPartnerCentral-channel_CreateChannelHandshake-request-payload"></a>
The payload containing specific details for the handshake type.
Type: [ChannelHandshakePayload](API_channel_ChannelHandshakePayload.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [tags](#API_channel_CreateChannelHandshake_RequestSyntax) **   <a name="AWSPartnerCentral-channel_CreateChannelHandshake-request-tags"></a>
Key-value pairs to associate with the channel handshake.
Type: Array of [Tag](API_channel_Tag.md) objects
Required: No

## Response Syntax
<a name="API_channel_CreateChannelHandshake_ResponseSyntax"></a>

```
{
   "channelHandshakeDetail": {
      "arn": "string",
      "id": "string"
   }
}
```

## Response Elements
<a name="API_channel_CreateChannelHandshake_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [channelHandshakeDetail](#API_channel_CreateChannelHandshake_ResponseSyntax) **   <a name="AWSPartnerCentral-channel_CreateChannelHandshake-response-channelHandshakeDetail"></a>
Details of the created channel handshake.
Type: [CreateChannelHandshakeDetail](API_channel_CreateChannelHandshakeDetail.md) object

## Errors
<a name="API_channel_CreateChannelHandshake_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions.
 ** message **
A message describing the access denial.
 ** reason **
The reason for the access denial.
HTTP Status Code: 400

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
 ** message **
A message describing the conflict.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of the resource that caused the conflict.
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

 ** ServiceQuotaExceededException **
The request would exceed a service quota limit.
 ** message **
A message describing the service quota exceeded error.
 ** quotaCode **
The code identifying the specific quota that would be exceeded.
 ** resourceId **
The identifier of the resource that would exceed the quota.
 ** resourceType **
The type of the resource that would exceed the quota.
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
<a name="API_channel_CreateChannelHandshake_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-channel-2024-03-18/CreateChannelHandshake)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-channel-2024-03-18/CreateChannelHandshake)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/CreateChannelHandshake)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-channel-2024-03-18/CreateChannelHandshake)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/CreateChannelHandshake)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-channel-2024-03-18/CreateChannelHandshake)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-channel-2024-03-18/CreateChannelHandshake)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-channel-2024-03-18/CreateChannelHandshake)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-channel-2024-03-18/CreateChannelHandshake)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/CreateChannelHandshake)

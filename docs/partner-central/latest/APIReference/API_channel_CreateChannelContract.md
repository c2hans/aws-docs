---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_CreateChannelContract.html
---

# CreateChannelContract

Creates a new channel contract and sends it to the signatory for signature. In the Sandbox catalog, the channel contract is accepted automatically.

## Request Syntax
<a name="API_channel_CreateChannelContract_RequestSyntax"></a>

```
{
   "catalog": "{{string}}",
   "clientToken": "{{string}}",
   "contractType": "{{string}}",
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
<a name="API_channel_CreateChannelContract_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [catalog](#API_channel_CreateChannelContract_RequestSyntax) **   <a name="AWSPartnerCentral-channel_CreateChannelContract-request-catalog"></a>
The catalog identifier for the channel contract.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]*`
Required: Yes

 ** [contractType](#API_channel_CreateChannelContract_RequestSyntax) **   <a name="AWSPartnerCentral-channel_CreateChannelContract-request-contractType"></a>
The type of channel contract to create (for example, managed services attestation).
Type: String
Valid Values: `MANAGED_SERVICES_ATTESTATION`
Required: Yes

 ** [payload](#API_channel_CreateChannelContract_RequestSyntax) **   <a name="AWSPartnerCentral-channel_CreateChannelContract-request-payload"></a>
The payload containing specific details for the contract type.
Type: [ChannelContractPayload](API_channel_ChannelContractPayload.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [clientToken](#API_channel_CreateChannelContract_RequestSyntax) **   <a name="AWSPartnerCentral-channel_CreateChannelContract-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]*`
Required: No

 ** [tags](#API_channel_CreateChannelContract_RequestSyntax) **   <a name="AWSPartnerCentral-channel_CreateChannelContract-request-tags"></a>
Key-value pairs to associate with the channel contract.
Type: Array of [Tag](API_channel_Tag.md) objects
Required: No

## Response Syntax
<a name="API_channel_CreateChannelContract_ResponseSyntax"></a>

```
{
   "channelContractDetail": {
      "arn": "string",
      "id": "string"
   }
}
```

## Response Elements
<a name="API_channel_CreateChannelContract_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [channelContractDetail](#API_channel_CreateChannelContract_ResponseSyntax) **   <a name="AWSPartnerCentral-channel_CreateChannelContract-response-channelContractDetail"></a>
Details of the created channel contract.
Type: [CreateChannelContractDetail](API_channel_CreateChannelContractDetail.md) object

## Errors
<a name="API_channel_CreateChannelContract_Errors"></a>

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
<a name="API_channel_CreateChannelContract_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-channel-2024-03-18/CreateChannelContract)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-channel-2024-03-18/CreateChannelContract)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/CreateChannelContract)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-channel-2024-03-18/CreateChannelContract)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/CreateChannelContract)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-channel-2024-03-18/CreateChannelContract)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-channel-2024-03-18/CreateChannelContract)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-channel-2024-03-18/CreateChannelContract)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-channel-2024-03-18/CreateChannelContract)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/CreateChannelContract)

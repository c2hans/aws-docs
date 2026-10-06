---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_AcceptConnectionProposal.html
---

# AcceptConnectionProposal
<a name="API_AcceptConnectionProposal"></a>

Accepts a connection proposal which was generated at a supported partner's portal.

The proposal contains the [Environment](API_Environment.md) and bandwidth that were chosen on the partner's portal and cannot be modified.

Upon accepting the proposal a connection will be made between the AWS network as accessed via the selected [AttachPoint](API_AttachPoint.md) and the network previously selected network on the partner's portal.

## Request Syntax
<a name="API_AcceptConnectionProposal_RequestSyntax"></a>

```
{
   "activationKey": "{{string}}",
   "attachPoint": { ... },
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_AcceptConnectionProposal_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [activationKey](#API_AcceptConnectionProposal_RequestSyntax) **   <a name="interconnect-AcceptConnectionProposal-request-activationKey"></a>
An Activation Key that was generated on a supported partner's portal. This key captures the desired parameters from the initial creation request.
The details of this request can be described using with [DescribeConnectionProposal](API_DescribeConnectionProposal.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [attachPoint](#API_AcceptConnectionProposal_RequestSyntax) **   <a name="interconnect-AcceptConnectionProposal-request-attachPoint"></a>
The [AttachPoint](API_AttachPoint.md) to which the connection should be associated.
Type: [AttachPoint](API_AttachPoint.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [clientToken](#API_AcceptConnectionProposal_RequestSyntax) **   <a name="interconnect-AcceptConnectionProposal-request-clientToken"></a>
Idempotency token used for the request.
Type: String
Required: No

 ** [description](#API_AcceptConnectionProposal_RequestSyntax) **   <a name="interconnect-AcceptConnectionProposal-request-description"></a>
A description to distinguish this [Connection](API_Connection.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[-a-zA-Z0-9_ ]+`
Required: No

 ** [tags](#API_AcceptConnectionProposal_RequestSyntax) **   <a name="interconnect-AcceptConnectionProposal-request-tags"></a>
The tags to associate with the resulting [Connection](API_Connection.md).
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_AcceptConnectionProposal_ResponseSyntax"></a>

```
{
   "connection": {
      "activationKey": "string",
      "arn": "string",
      "attachPoint": { ... },
      "bandwidth": "string",
      "billingTier": number,
      "description": "string",
      "environmentId": "string",
      "id": "string",
      "location": "string",
      "ownerAccount": "string",
      "provider": { ... },
      "sharedId": "string",
      "state": "string",
      "tags": {
         "string" : "string"
      },
      "type": "string"
   }
}
```

## Response Elements
<a name="API_AcceptConnectionProposal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connection](#API_AcceptConnectionProposal_ResponseSyntax) **   <a name="interconnect-AcceptConnectionProposal-response-connection"></a>
The created [Connection](API_Connection.md) object.
Type: [Connection](API_Connection.md) object

## Errors
<a name="API_AcceptConnectionProposal_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The calling principal is not allowed to access the specified resource, or the resource does not exist.
HTTP Status Code: 403

 ** InterconnectClientException **
The request was denied due to incorrect client supplied parameters.
HTTP Status Code: 400

 ** InterconnectServerException **
The request resulted in an exception internal to the service.
HTTP Status Code: 500

 ** InterconnectValidationException **
The input fails to satisfy the constraints specified.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request specifies a resource that does not exist on the server.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The requested operation would result in the calling principal exceeding their allotted quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_AcceptConnectionProposal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/interconnect-2022-07-26/AcceptConnectionProposal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/interconnect-2022-07-26/AcceptConnectionProposal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/AcceptConnectionProposal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/interconnect-2022-07-26/AcceptConnectionProposal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/AcceptConnectionProposal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/interconnect-2022-07-26/AcceptConnectionProposal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/interconnect-2022-07-26/AcceptConnectionProposal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/interconnect-2022-07-26/AcceptConnectionProposal)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/interconnect-2022-07-26/AcceptConnectionProposal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/AcceptConnectionProposal)

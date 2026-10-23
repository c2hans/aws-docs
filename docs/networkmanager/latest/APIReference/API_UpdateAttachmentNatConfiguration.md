---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_UpdateAttachmentNatConfiguration.html
---

# UpdateAttachmentNatConfiguration
<a name="API_UpdateAttachmentNatConfiguration"></a>

Updates the NAT configuration of a core network attachment. You can enable or disable NAT gateway support, specify whether the core network installs system routes for the NAT CIDR blocks, and replace the NAT rules of the attachment. Specify at least one of `NatGatewaySupport`, `NatSystemRouteSupport`, or `NatGatewayRules`.

Only the core network owner can update the NAT configuration of an attachment. The attachment must be in the `AVAILABLE`, `PENDING_ATTACHMENT_ACCEPTANCE`, or `PENDING_TAG_ACCEPTANCE` state. Changes are applied asynchronously, and the attachment is in the `UPDATING` state while they are applied. If the attachment is pending acceptance, the NAT configuration is stored and is applied after the attachment is accepted.

## Request Syntax
<a name="API_UpdateAttachmentNatConfiguration_RequestSyntax"></a>

```
PATCH /attachments/{{attachmentId}}/nat-configuration HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "NatGatewayRules": [
      {
         "MatchSourceCidr": "{{string}}",
         "NatCidr": "{{string}}",
         "RuleNumber": {{number}}
      }
   ],
   "NatGatewaySupport": "{{string}}",
   "NatSystemRouteSupport": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateAttachmentNatConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [attachmentId](#API_UpdateAttachmentNatConfiguration_RequestSyntax) **   <a name="networkmanager-UpdateAttachmentNatConfiguration-request-uri-AttachmentId"></a>
The ID of the attachment to update the NAT configuration for.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`
Required: Yes

## Request Body
<a name="API_UpdateAttachmentNatConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateAttachmentNatConfiguration_RequestSyntax) **   <a name="networkmanager-UpdateAttachmentNatConfiguration-request-ClientToken"></a>
The client token associated with the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [NatGatewayRules](#API_UpdateAttachmentNatConfiguration_RequestSyntax) **   <a name="networkmanager-UpdateAttachmentNatConfiguration-request-NatGatewayRules"></a>
The complete set of NAT rules for the attachment, up to 50 rules. The rules that you specify replace the existing rules of the attachment, matched by rule number. Existing rules that aren't included in the request are deleted. To delete all NAT rules, specify an empty list. You can delete all NAT rules only when NAT gateway support is disabled, or when you disable it in the same request. If you omit this parameter, the existing rules are unchanged.
Type: Array of [NatRuleRequest](API_NatRuleRequest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [NatGatewaySupport](#API_UpdateAttachmentNatConfiguration_RequestSyntax) **   <a name="networkmanager-UpdateAttachmentNatConfiguration-request-NatGatewaySupport"></a>
Specifies whether to enable or disable NAT gateway support on the attachment. When you disable NAT gateway support, the attachment keeps its NAT rules but doesn't apply them. To enable NAT gateway support, the attachment must have at least one NAT rule, either specified in this request or already configured on the attachment. If you omit this parameter, NAT gateway support is unchanged.
Type: String
Valid Values: `ENABLE | DISABLE`
Required: No

 ** [NatSystemRouteSupport](#API_UpdateAttachmentNatConfiguration_RequestSyntax) **   <a name="networkmanager-UpdateAttachmentNatConfiguration-request-NatSystemRouteSupport"></a>
Specifies whether the core network installs system routes for the NAT CIDR blocks of the attachment's NAT rules. System routes have a route type of `SYSTEM`. NAT is applied to traffic whether or not this option is enabled. If you omit this parameter, the current value is unchanged.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateAttachmentNatConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AttachmentId": "string",
   "NatGatewayRules": [
      {
         "MatchSourceCidr": "string",
         "NatCidr": "string",
         "RuleNumber": number,
         "State": "string"
      }
   ],
   "NatGatewaySupport": "string",
   "NatSystemRouteSupport": boolean
}
```

## Response Elements
<a name="API_UpdateAttachmentNatConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachmentId](#API_UpdateAttachmentNatConfiguration_ResponseSyntax) **   <a name="networkmanager-UpdateAttachmentNatConfiguration-response-AttachmentId"></a>
The ID of the attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`

 ** [NatGatewayRules](#API_UpdateAttachmentNatConfiguration_ResponseSyntax) **   <a name="networkmanager-UpdateAttachmentNatConfiguration-response-NatGatewayRules"></a>
The NAT rules of the attachment, including rules that are being deleted.
Type: Array of [NatRule](API_NatRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [NatGatewaySupport](#API_UpdateAttachmentNatConfiguration_ResponseSyntax) **   <a name="networkmanager-UpdateAttachmentNatConfiguration-response-NatGatewaySupport"></a>
The state of NAT gateway support on the attachment. The transitional states `ENABLING` and `DISABLING` change to `ENABLED` or `DISABLED` after the update is applied. The state is `PENDING_ATTACHMENT_ACCEPTANCE` when NAT gateway support is enabled on an attachment that is pending acceptance.
Type: String
Valid Values: `ENABLED | ENABLING | DISABLED | DISABLING | PENDING_ATTACHMENT_ACCEPTANCE`

 ** [NatSystemRouteSupport](#API_UpdateAttachmentNatConfiguration_ResponseSyntax) **   <a name="networkmanager-UpdateAttachmentNatConfiguration-response-NatSystemRouteSupport"></a>
Indicates whether the core network installs system routes for the NAT CIDR blocks of the attachment's NAT rules.
Type: Boolean

## Errors
<a name="API_UpdateAttachmentNatConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed due to an internal error.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** Context **
The specified resource could not be found.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
A service limit was exceeded.
 ** LimitCode **
The limit code.
 ** Message **
The error message.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
 ** ServiceCode **
The service code.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason for the error.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAttachmentNatConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/UpdateAttachmentNatConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/UpdateAttachmentNatConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/UpdateAttachmentNatConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/UpdateAttachmentNatConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/UpdateAttachmentNatConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/UpdateAttachmentNatConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/UpdateAttachmentNatConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/UpdateAttachmentNatConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/UpdateAttachmentNatConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/UpdateAttachmentNatConfiguration)

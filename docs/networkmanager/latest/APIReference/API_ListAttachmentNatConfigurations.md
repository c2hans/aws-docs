---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListAttachmentNatConfigurations.html
---

# ListAttachmentNatConfigurations
<a name="API_ListAttachmentNatConfigurations"></a>

Returns the NAT configurations of core network attachments. You must specify either a core network ID or an attachment ID. Only the core network owner can list NAT configurations.

## Request Syntax
<a name="API_ListAttachmentNatConfigurations_RequestSyntax"></a>

```
POST /nat-configurations HTTP/1.1
Content-type: application/json

{
   "AttachmentId": "{{string}}",
   "CoreNetworkId": "{{string}}",
   "Filters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListAttachmentNatConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListAttachmentNatConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AttachmentId](#API_ListAttachmentNatConfigurations_RequestSyntax) **   <a name="networkmanager-ListAttachmentNatConfigurations-request-AttachmentId"></a>
The ID of an attachment. Returns the NAT configuration of the specified attachment. If you specify both an attachment ID and a core network ID, the attachment ID is used.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`
Required: No

 ** [CoreNetworkId](#API_ListAttachmentNatConfigurations_RequestSyntax) **   <a name="networkmanager-ListAttachmentNatConfigurations-request-CoreNetworkId"></a>
The ID of a core network. Returns the NAT configurations of attachments in the core network that support NAT.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: No

 ** [Filters](#API_ListAttachmentNatConfigurations_RequestSyntax) **   <a name="networkmanager-ListAttachmentNatConfigurations-request-Filters"></a>
The filters to apply to the results. Values for the same filter are joined with OR, and different filters are joined with AND. You can specify up to 10 filter values in total. The following filters are supported:
+  `nat-gateway-support`: The state of NAT gateway support on the attachment, for example `ENABLED`.
+  `nat-system-route-support`: Whether system routes are installed for the attachment, `true` or `false`.
+  `rule-number`: The rule number of a NAT rule.
+  `match-source-cidr`: The source CIDR block of a NAT rule. The value must exactly match the CIDR block of the rule.
+  `nat-cidr`: The NAT CIDR block of a NAT rule. The value must exactly match the CIDR block of the rule.
+  `nat-rule-state`: The state of a NAT rule, for example `ACTIVATED`.
Type: String to array of strings map
Key Length Constraints: Maximum length of 128.
Key Pattern: `^[0-9a-zA-Z\.-]*$`
Length Constraints: Maximum length of 255.
Pattern: `^[0-9a-zA-Z\*\.\\/\?-]*$`
Required: No

 ** [MaxResults](#API_ListAttachmentNatConfigurations_RequestSyntax) **   <a name="networkmanager-ListAttachmentNatConfigurations-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_ListAttachmentNatConfigurations_RequestSyntax) **   <a name="networkmanager-ListAttachmentNatConfigurations-request-NextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_ListAttachmentNatConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AttachmentNatConfigurations": [
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAttachmentNatConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachmentNatConfigurations](#API_ListAttachmentNatConfigurations_ResponseSyntax) **   <a name="networkmanager-ListAttachmentNatConfigurations-response-AttachmentNatConfigurations"></a>
The NAT configurations of the attachments.
Type: Array of [AttachmentNatConfiguration](API_AttachmentNatConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.

 ** [NextToken](#API_ListAttachmentNatConfigurations_ResponseSyntax) **   <a name="networkmanager-ListAttachmentNatConfigurations-response-NextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

## Errors
<a name="API_ListAttachmentNatConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_ListAttachmentNatConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/ListAttachmentNatConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/ListAttachmentNatConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ListAttachmentNatConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/ListAttachmentNatConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ListAttachmentNatConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/ListAttachmentNatConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/ListAttachmentNatConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/ListAttachmentNatConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/ListAttachmentNatConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ListAttachmentNatConfigurations)

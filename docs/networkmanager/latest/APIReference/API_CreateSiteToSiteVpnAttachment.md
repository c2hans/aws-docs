---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateSiteToSiteVpnAttachment.html
---

# CreateSiteToSiteVpnAttachment
<a name="API_CreateSiteToSiteVpnAttachment"></a>

Creates an Amazon Web Services site-to-site VPN attachment on an edge location of a core network.

## Request Syntax
<a name="API_CreateSiteToSiteVpnAttachment_RequestSyntax"></a>

```
POST /site-to-site-vpn-attachments HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "CoreNetworkId": "{{string}}",
   "RoutingPolicyLabel": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VpnConnectionArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateSiteToSiteVpnAttachment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSiteToSiteVpnAttachment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateSiteToSiteVpnAttachment_RequestSyntax) **   <a name="networkmanager-CreateSiteToSiteVpnAttachment-request-ClientToken"></a>
The client token associated with the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [CoreNetworkId](#API_CreateSiteToSiteVpnAttachment_RequestSyntax) **   <a name="networkmanager-CreateSiteToSiteVpnAttachment-request-CoreNetworkId"></a>
The ID of a core network where you're creating a site-to-site VPN attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: Yes

 ** [RoutingPolicyLabel](#API_CreateSiteToSiteVpnAttachment_RequestSyntax) **   <a name="networkmanager-CreateSiteToSiteVpnAttachment-request-RoutingPolicyLabel"></a>
The routing policy label to apply to the Site-to-Site VPN attachment for traffic routing decisions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [Tags](#API_CreateSiteToSiteVpnAttachment_RequestSyntax) **   <a name="networkmanager-CreateSiteToSiteVpnAttachment-request-Tags"></a>
The tags associated with the request.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [VpnConnectionArn](#API_CreateSiteToSiteVpnAttachment_RequestSyntax) **   <a name="networkmanager-CreateSiteToSiteVpnAttachment-request-VpnConnectionArn"></a>
The ARN identifying the VPN attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:vpn-connection\/vpn-[0-9a-f]{8,17}$`
Required: Yes

## Response Syntax
<a name="API_CreateSiteToSiteVpnAttachment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "SiteToSiteVpnAttachment": {
      "Attachment": {
         "AttachmentId": "string",
         "AttachmentPolicyRuleNumber": number,
         "AttachmentType": "string",
         "CoreNetworkArn": "string",
         "CoreNetworkId": "string",
         "CreatedAt": number,
         "EdgeLocation": "string",
         "EdgeLocations": [ "string" ],
         "LastModificationErrors": [
            {
               "Code": "string",
               "Message": "string",
               "RequestId": "string",
               "ResourceArn": "string"
            }
         ],
         "NetworkFunctionGroupName": "string",
         "OwnerAccountId": "string",
         "ProposedNetworkFunctionGroupChange": {
            "AttachmentPolicyRuleNumber": number,
            "NetworkFunctionGroupName": "string",
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ]
         },
         "ProposedSegmentChange": {
            "AttachmentPolicyRuleNumber": number,
            "SegmentName": "string",
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ]
         },
         "ResourceArn": "string",
         "SegmentName": "string",
         "State": "string",
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "UpdatedAt": number
      },
      "VpnConnectionArn": "string"
   }
}
```

## Response Elements
<a name="API_CreateSiteToSiteVpnAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SiteToSiteVpnAttachment](#API_CreateSiteToSiteVpnAttachment_ResponseSyntax) **   <a name="networkmanager-CreateSiteToSiteVpnAttachment-response-SiteToSiteVpnAttachment"></a>
Details about a site-to-site VPN attachment.
Type: [SiteToSiteVpnAttachment](API_SiteToSiteVpnAttachment.md) object

## Errors
<a name="API_CreateSiteToSiteVpnAttachment_Errors"></a>

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
<a name="API_CreateSiteToSiteVpnAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateSiteToSiteVpnAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/CreateSiteToSiteVpnAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateSiteToSiteVpnAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateSiteToSiteVpnAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateSiteToSiteVpnAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateSiteToSiteVpnAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateSiteToSiteVpnAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateSiteToSiteVpnAttachment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateSiteToSiteVpnAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateSiteToSiteVpnAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

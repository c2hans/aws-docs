---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateVpcAttachment.html
---

# CreateVpcAttachment
<a name="API_CreateVpcAttachment"></a>

Creates a VPC attachment on an edge location of a core network.

## Request Syntax
<a name="API_CreateVpcAttachment_RequestSyntax"></a>

```
POST /vpc-attachments HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "CoreNetworkId": "{{string}}",
   "Options": {
      "ApplianceModeSupport": {{boolean}},
      "DnsSupport": {{boolean}},
      "Ipv6Support": {{boolean}},
      "SecurityGroupReferencingSupport": {{boolean}}
   },
   "RoutingPolicyLabel": "{{string}}",
   "SubnetArns": [ "{{string}}" ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VpcArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateVpcAttachment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateVpcAttachment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateVpcAttachment_RequestSyntax) **   <a name="networkmanager-CreateVpcAttachment-request-ClientToken"></a>
The client token associated with the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [CoreNetworkId](#API_CreateVpcAttachment_RequestSyntax) **   <a name="networkmanager-CreateVpcAttachment-request-CoreNetworkId"></a>
The ID of a core network for the VPC attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: Yes

 ** [Options](#API_CreateVpcAttachment_RequestSyntax) **   <a name="networkmanager-CreateVpcAttachment-request-Options"></a>
Options for the VPC attachment.
Type: [VpcOptions](API_VpcOptions.md) object
Required: No

 ** [RoutingPolicyLabel](#API_CreateVpcAttachment_RequestSyntax) **   <a name="networkmanager-CreateVpcAttachment-request-RoutingPolicyLabel"></a>
The routing policy label to apply to the VPC attachment for traffic routing decisions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [SubnetArns](#API_CreateVpcAttachment_RequestSyntax) **   <a name="networkmanager-CreateVpcAttachment-request-SubnetArns"></a>
The subnet ARN of the VPC attachment.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:subnet\/subnet-[0-9a-f]{8,17}$|^$`
Required: Yes

 ** [Tags](#API_CreateVpcAttachment_RequestSyntax) **   <a name="networkmanager-CreateVpcAttachment-request-Tags"></a>
The key-value tags associated with the request.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [VpcArn](#API_CreateVpcAttachment_RequestSyntax) **   <a name="networkmanager-CreateVpcAttachment-request-VpcArn"></a>
The ARN of the VPC.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:vpc\/vpc-[0-9a-f]{8,17}$`
Required: Yes

## Response Syntax
<a name="API_CreateVpcAttachment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "VpcAttachment": {
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
      "Options": {
         "ApplianceModeSupport": boolean,
         "DnsSupport": boolean,
         "Ipv6Support": boolean,
         "SecurityGroupReferencingSupport": boolean
      },
      "SubnetArns": [ "string" ]
   }
}
```

## Response Elements
<a name="API_CreateVpcAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcAttachment](#API_CreateVpcAttachment_ResponseSyntax) **   <a name="networkmanager-CreateVpcAttachment-response-VpcAttachment"></a>
Provides details about the VPC attachment.
Type: [VpcAttachment](API_VpcAttachment.md) object

## Errors
<a name="API_CreateVpcAttachment_Errors"></a>

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
<a name="API_CreateVpcAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateVpcAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/CreateVpcAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateVpcAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateVpcAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateVpcAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateVpcAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateVpcAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateVpcAttachment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateVpcAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateVpcAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

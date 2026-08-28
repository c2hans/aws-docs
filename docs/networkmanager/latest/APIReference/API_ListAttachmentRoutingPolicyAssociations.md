---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListAttachmentRoutingPolicyAssociations.html
---

# ListAttachmentRoutingPolicyAssociations
<a name="API_ListAttachmentRoutingPolicyAssociations"></a>

Lists the routing policy associations for attachments in a core network.

## Request Syntax
<a name="API_ListAttachmentRoutingPolicyAssociations_RequestSyntax"></a>

```
GET /routing-policy-label/core-network/{{coreNetworkId}}?attachmentId={{AttachmentId}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAttachmentRoutingPolicyAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AttachmentId](#API_ListAttachmentRoutingPolicyAssociations_RequestSyntax) **   <a name="networkmanager-ListAttachmentRoutingPolicyAssociations-request-uri-AttachmentId"></a>
The ID of a specific attachment to filter the routing policy associations.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`

 ** [coreNetworkId](#API_ListAttachmentRoutingPolicyAssociations_RequestSyntax) **   <a name="networkmanager-ListAttachmentRoutingPolicyAssociations-request-uri-CoreNetworkId"></a>
The ID of the core network to list attachment routing policy associations for.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: Yes

 ** [MaxResults](#API_ListAttachmentRoutingPolicyAssociations_RequestSyntax) **   <a name="networkmanager-ListAttachmentRoutingPolicyAssociations-request-uri-MaxResults"></a>
The maximum number of results to return in a single page.
Valid Range: Minimum value of 1. Maximum value of 500.

 ** [NextToken](#API_ListAttachmentRoutingPolicyAssociations_RequestSyntax) **   <a name="networkmanager-ListAttachmentRoutingPolicyAssociations-request-uri-NextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

## Request Body
<a name="API_ListAttachmentRoutingPolicyAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAttachmentRoutingPolicyAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AttachmentRoutingPolicyAssociations": [
      {
         "AssociatedRoutingPolicies": [ "string" ],
         "AttachmentId": "string",
         "PendingRoutingPolicies": [ "string" ],
         "RoutingPolicyLabel": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAttachmentRoutingPolicyAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachmentRoutingPolicyAssociations](#API_ListAttachmentRoutingPolicyAssociations_ResponseSyntax) **   <a name="networkmanager-ListAttachmentRoutingPolicyAssociations-response-AttachmentRoutingPolicyAssociations"></a>
The list of attachment routing policy associations.
Type: Array of [AttachmentRoutingPolicyAssociationSummary](API_AttachmentRoutingPolicyAssociationSummary.md) objects

 ** [NextToken](#API_ListAttachmentRoutingPolicyAssociations_ResponseSyntax) **   <a name="networkmanager-ListAttachmentRoutingPolicyAssociations-response-NextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

## Errors
<a name="API_ListAttachmentRoutingPolicyAssociations_Errors"></a>

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
<a name="API_ListAttachmentRoutingPolicyAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/ListAttachmentRoutingPolicyAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/ListAttachmentRoutingPolicyAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ListAttachmentRoutingPolicyAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/ListAttachmentRoutingPolicyAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ListAttachmentRoutingPolicyAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/ListAttachmentRoutingPolicyAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/ListAttachmentRoutingPolicyAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/ListAttachmentRoutingPolicyAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/ListAttachmentRoutingPolicyAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ListAttachmentRoutingPolicyAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

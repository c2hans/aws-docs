---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DeleteLinkRoutingRule.html
---

# DeleteLinkRoutingRule
<a name="API_DeleteLinkRoutingRule"></a>

Deletes a routing rule from a link.

## Request Syntax
<a name="API_DeleteLinkRoutingRule_RequestSyntax"></a>

```
DELETE /responder-gateway/{{gatewayId}}/link/{{linkId}}/routing-rule/{{ruleId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteLinkRoutingRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_DeleteLinkRoutingRule_RequestSyntax) **   <a name="rtbfabric-DeleteLinkRoutingRule-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

 ** [linkId](#API_DeleteLinkRoutingRule_RequestSyntax) **   <a name="rtbfabric-DeleteLinkRoutingRule-request-uri-linkId"></a>
The unique identifier of the link.
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`
Required: Yes

 ** [ruleId](#API_DeleteLinkRoutingRule_RequestSyntax) **   <a name="rtbfabric-DeleteLinkRoutingRule-request-uri-ruleId"></a>
The unique identifier of the routing rule.
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `rule-[a-z0-9-]{1,25}`
Required: Yes

## Request Body
<a name="API_DeleteLinkRoutingRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteLinkRoutingRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ruleId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteLinkRoutingRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ruleId](#API_DeleteLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-DeleteLinkRoutingRule-response-ruleId"></a>
The unique identifier of the routing rule.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `rule-[a-z0-9-]{1,25}`

 ** [status](#API_DeleteLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-DeleteLinkRoutingRule-response-status"></a>
The status of the routing rule.
Type: String
Valid Values: `CREATION_IN_PROGRESS | ACTIVE | UPDATE_IN_PROGRESS | DELETION_IN_PROGRESS | DELETED | FAILED`

## Errors
<a name="API_DeleteLinkRoutingRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed because of a conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteLinkRoutingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/DeleteLinkRoutingRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/DeleteLinkRoutingRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/DeleteLinkRoutingRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/DeleteLinkRoutingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/DeleteLinkRoutingRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/DeleteLinkRoutingRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/DeleteLinkRoutingRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/DeleteLinkRoutingRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/DeleteLinkRoutingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/DeleteLinkRoutingRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RTB Fabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rtb-fabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

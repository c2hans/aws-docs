---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetLinkRoutingRule.html
---

# GetLinkRoutingRule
<a name="API_GetLinkRoutingRule"></a>

Retrieves the details of a routing rule for a link.

## Request Syntax
<a name="API_GetLinkRoutingRule_RequestSyntax"></a>

```
GET /responder-gateway/{{gatewayId}}/link/{{linkId}}/routing-rule/{{ruleId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLinkRoutingRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_GetLinkRoutingRule_RequestSyntax) **   <a name="rtbfabric-GetLinkRoutingRule-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

 ** [linkId](#API_GetLinkRoutingRule_RequestSyntax) **   <a name="rtbfabric-GetLinkRoutingRule-request-uri-linkId"></a>
The unique identifier of the link.
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`
Required: Yes

 ** [ruleId](#API_GetLinkRoutingRule_RequestSyntax) **   <a name="rtbfabric-GetLinkRoutingRule-request-uri-ruleId"></a>
The unique identifier of the routing rule.
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `rule-[a-z0-9-]{1,25}`
Required: Yes

## Request Body
<a name="API_GetLinkRoutingRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLinkRoutingRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "conditions": {
      "hostHeader": "string",
      "hostHeaderWildcard": "string",
      "pathExact": "string",
      "pathPrefix": "string",
      "queryStringEquals": {
         "key": "string",
         "value": "string"
      },
      "queryStringExists": "string"
   },
   "createdAt": number,
   "gatewayId": "string",
   "linkId": "string",
   "priority": number,
   "ruleId": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetLinkRoutingRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [conditions](#API_GetLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-GetLinkRoutingRule-response-conditions"></a>
The conditions for the routing rule.
Type: [RuleCondition](API_RuleCondition.md) object

 ** [createdAt](#API_GetLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-GetLinkRoutingRule-response-createdAt"></a>
The timestamp of when the routing rule was created.
Type: Timestamp

 ** [gatewayId](#API_GetLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-GetLinkRoutingRule-response-gatewayId"></a>
The unique identifier of the gateway.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`

 ** [linkId](#API_GetLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-GetLinkRoutingRule-response-linkId"></a>
The unique identifier of the link.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`

 ** [priority](#API_GetLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-GetLinkRoutingRule-response-priority"></a>
The priority of the routing rule.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [ruleId](#API_GetLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-GetLinkRoutingRule-response-ruleId"></a>
The unique identifier of the routing rule.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `rule-[a-z0-9-]{1,25}`

 ** [status](#API_GetLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-GetLinkRoutingRule-response-status"></a>
The status of the routing rule.
Type: String
Valid Values: `CREATION_IN_PROGRESS | ACTIVE | UPDATE_IN_PROGRESS | DELETION_IN_PROGRESS | DELETED | FAILED`

 ** [tags](#API_GetLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-GetLinkRoutingRule-response-tags"></a>
A map of the key-value pairs for the tag or tags assigned to the specified resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(resourceArn|internalId|[a-zA-Z0-9+\-=._:/@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 1600.

 ** [updatedAt](#API_GetLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-GetLinkRoutingRule-response-updatedAt"></a>
The timestamp of when the routing rule was last updated.
Type: Timestamp

## Errors
<a name="API_GetLinkRoutingRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetLinkRoutingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/GetLinkRoutingRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/GetLinkRoutingRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/GetLinkRoutingRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/GetLinkRoutingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/GetLinkRoutingRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/GetLinkRoutingRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/GetLinkRoutingRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/GetLinkRoutingRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/GetLinkRoutingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/GetLinkRoutingRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RTB Fabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rtb-fabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

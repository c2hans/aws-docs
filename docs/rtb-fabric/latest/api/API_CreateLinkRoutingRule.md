---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateLinkRoutingRule.html
---

# CreateLinkRoutingRule
<a name="API_CreateLinkRoutingRule"></a>

Creates a routing rule for a link.

Routing rules use priority-based evaluation where lower priority numbers are evaluated first. Each rule specifies conditions that must all match for the rule to apply.

## Request Syntax
<a name="API_CreateLinkRoutingRule_RequestSyntax"></a>

```
POST /responder-gateway/{{gatewayId}}/link/{{linkId}}/routing-rule HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "conditions": {
      "hostHeader": "{{string}}",
      "hostHeaderWildcard": "{{string}}",
      "pathExact": "{{string}}",
      "pathPrefix": "{{string}}",
      "queryStringEquals": {
         "key": "{{string}}",
         "value": "{{string}}"
      },
      "queryStringExists": "{{string}}"
   },
   "priority": {{number}},
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateLinkRoutingRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_CreateLinkRoutingRule_RequestSyntax) **   <a name="rtbfabric-CreateLinkRoutingRule-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

 ** [linkId](#API_CreateLinkRoutingRule_RequestSyntax) **   <a name="rtbfabric-CreateLinkRoutingRule-request-uri-linkId"></a>
The unique identifier of the link.
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`
Required: Yes

## Request Body
<a name="API_CreateLinkRoutingRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateLinkRoutingRule_RequestSyntax) **   <a name="rtbfabric-CreateLinkRoutingRule-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `clientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: Yes

 ** [conditions](#API_CreateLinkRoutingRule_RequestSyntax) **   <a name="rtbfabric-CreateLinkRoutingRule-request-conditions"></a>
The conditions for the routing rule. All specified fields must match for the rule to apply. At least one condition field must be set.
Type: [RuleCondition](API_RuleCondition.md) object
Required: Yes

 ** [priority](#API_CreateLinkRoutingRule_RequestSyntax) **   <a name="rtbfabric-CreateLinkRoutingRule-request-priority"></a>
The priority of the routing rule. Lower numbers are evaluated first. Valid values are 1 to 1000. Priority must be unique among non-deleted rules within a link.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** [tags](#API_CreateLinkRoutingRule_RequestSyntax) **   <a name="rtbfabric-CreateLinkRoutingRule-request-tags"></a>
A map of the key-value pairs of the tag or tags to assign to the resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(resourceArn|internalId|[a-zA-Z0-9+\-=._:/@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 1600.
Required: No

## Response Syntax
<a name="API_CreateLinkRoutingRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "ruleId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateLinkRoutingRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-CreateLinkRoutingRule-response-createdAt"></a>
The timestamp of when the routing rule was created.
Type: Timestamp

 ** [ruleId](#API_CreateLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-CreateLinkRoutingRule-response-ruleId"></a>
The unique identifier of the routing rule.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `rule-[a-z0-9-]{1,25}`

 ** [status](#API_CreateLinkRoutingRule_ResponseSyntax) **   <a name="rtbfabric-CreateLinkRoutingRule-response-status"></a>
The status of the routing rule.
Type: String
Valid Values: `CREATION_IN_PROGRESS | ACTIVE | UPDATE_IN_PROGRESS | DELETION_IN_PROGRESS | DELETED | FAILED`

## Errors
<a name="API_CreateLinkRoutingRule_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request could not be completed because you exceeded a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_CreateLinkRoutingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/CreateLinkRoutingRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/CreateLinkRoutingRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/CreateLinkRoutingRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/CreateLinkRoutingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/CreateLinkRoutingRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/CreateLinkRoutingRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/CreateLinkRoutingRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/CreateLinkRoutingRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/CreateLinkRoutingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/CreateLinkRoutingRule)

---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateRule.html
---

# CreateRule
<a name="API_CreateRule"></a>

Creates a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. For more information, see [Listener rules](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules) in the *Amazon VPC Lattice User Guide*.

## Request Syntax
<a name="API_CreateRule_RequestSyntax"></a>

```
POST /services/{{serviceIdentifier}}/listeners/{{listenerIdentifier}}/rules HTTP/1.1
Content-type: application/json

{
   "action": { ... },
   "clientToken": "{{string}}",
   "match": { ... },
   "name": "{{string}}",
   "priority": {{number}},
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [listenerIdentifier](#API_CreateRule_RequestSyntax) **   <a name="vpclattice-CreateRule-request-uri-listenerIdentifier"></a>
The ID or ARN of the listener.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((listener-[0-9a-z]{17})|(^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}$))`
Required: Yes

 ** [serviceIdentifier](#API_CreateRule_RequestSyntax) **   <a name="vpclattice-CreateRule-request-uri-serviceIdentifier"></a>
The ID or ARN of the service.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((svc-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_CreateRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_CreateRule_RequestSyntax) **   <a name="vpclattice-CreateRule-request-action"></a>
The action for the default rule.
Type: [RuleAction](API_RuleAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [clientToken](#API_CreateRule_RequestSyntax) **   <a name="vpclattice-CreateRule-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[!-~]+.*`
Required: No

 ** [match](#API_CreateRule_RequestSyntax) **   <a name="vpclattice-CreateRule-request-match"></a>
The rule match.
Type: [RuleMatch](API_RuleMatch.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [name](#API_CreateRule_RequestSyntax) **   <a name="vpclattice-CreateRule-request-name"></a>
The name of the rule. The name must be unique within the listener. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!rule-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: Yes

 ** [priority](#API_CreateRule_RequestSyntax) **   <a name="vpclattice-CreateRule-request-priority"></a>
The priority assigned to the rule. Each rule for a specific listener must have a unique priority. The lower the priority number the higher the priority.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2000.
Required: Yes

 ** [tags](#API_CreateRule_RequestSyntax) **   <a name="vpclattice-CreateRule-request-tags"></a>
The tags for the rule.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateRule_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "action": { ... },
   "arn": "string",
   "id": "string",
   "match": { ... },
   "name": "string",
   "priority": number
}
```

## Response Elements
<a name="API_CreateRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [action](#API_CreateRule_ResponseSyntax) **   <a name="vpclattice-CreateRule-response-action"></a>
The rule action.
Type: [RuleAction](API_RuleAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [arn](#API_CreateRule_ResponseSyntax) **   <a name="vpclattice-CreateRule-response-arn"></a>
The Amazon Resource Name (ARN) of the rule.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}/rule/rule-[0-9a-z]{17}`

 ** [id](#API_CreateRule_ResponseSyntax) **   <a name="vpclattice-CreateRule-response-id"></a>
The ID of the rule.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 22.
Pattern: `rule-[0-9a-z]{17}`

 ** [match](#API_CreateRule_ResponseSyntax) **   <a name="vpclattice-CreateRule-response-match"></a>
The rule match. The `RuleMatch` must be an `HttpMatch`. This means that the rule should be an exact match on HTTP constraints which are made up of the HTTP method, path, and header.
Type: [RuleMatch](API_RuleMatch.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [name](#API_CreateRule_ResponseSyntax) **   <a name="vpclattice-CreateRule-response-name"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!rule-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [priority](#API_CreateRule_ResponseSyntax) **   <a name="vpclattice-CreateRule-response-priority"></a>
The priority assigned to the rule. The lower the priority number the higher the priority.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2000.

## Errors
<a name="API_CreateRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
 ** serviceCode **
The service code.
HTTP Status Code: 402

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
 ** serviceCode **
The service code.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** fieldList **
The fields that failed validation.
 ** reason **
The reason.
HTTP Status Code: 400

## See Also
<a name="API_CreateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/CreateRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/CreateRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/CreateRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/CreateRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/CreateRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/CreateRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/CreateRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/CreateRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/CreateRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/CreateRule)

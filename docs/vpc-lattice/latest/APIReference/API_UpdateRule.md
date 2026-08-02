---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateRule.html
---

# UpdateRule
<a name="API_UpdateRule"></a>

Updates a specified rule for the listener. You can't modify a default listener rule. To modify a default listener rule, use `UpdateListener`.

## Request Syntax
<a name="API_UpdateRule_RequestSyntax"></a>

```
PATCH /services/{{serviceIdentifier}}/listeners/{{listenerIdentifier}}/rules/{{ruleIdentifier}} HTTP/1.1
Content-type: application/json

{
   "action": { ... },
   "match": { ... },
   "priority": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [listenerIdentifier](#API_UpdateRule_RequestSyntax) **   <a name="vpclattice-UpdateRule-request-uri-listenerIdentifier"></a>
The ID or ARN of the listener.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((listener-[0-9a-z]{17})|(^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}$))`
Required: Yes

 ** [ruleIdentifier](#API_UpdateRule_RequestSyntax) **   <a name="vpclattice-UpdateRule-request-uri-ruleIdentifier"></a>
The ID or ARN of the rule.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((rule-[0-9a-z]{17})|(^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}/rule/rule-[0-9a-z]{17}$))`
Required: Yes

 ** [serviceIdentifier](#API_UpdateRule_RequestSyntax) **   <a name="vpclattice-UpdateRule-request-uri-serviceIdentifier"></a>
The ID or ARN of the service.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((svc-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_UpdateRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_UpdateRule_RequestSyntax) **   <a name="vpclattice-UpdateRule-request-action"></a>
Information about the action for the specified listener rule.
Type: [RuleAction](API_RuleAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [match](#API_UpdateRule_RequestSyntax) **   <a name="vpclattice-UpdateRule-request-match"></a>
The rule match.
Type: [RuleMatch](API_RuleMatch.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [priority](#API_UpdateRule_RequestSyntax) **   <a name="vpclattice-UpdateRule-request-priority"></a>
The rule priority. A listener can't have multiple rules with the same priority.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2000.
Required: No

## Response Syntax
<a name="API_UpdateRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "action": { ... },
   "arn": "string",
   "id": "string",
   "isDefault": boolean,
   "match": { ... },
   "name": "string",
   "priority": number
}
```

## Response Elements
<a name="API_UpdateRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [action](#API_UpdateRule_ResponseSyntax) **   <a name="vpclattice-UpdateRule-response-action"></a>
Information about the action for the specified listener rule.
Type: [RuleAction](API_RuleAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [arn](#API_UpdateRule_ResponseSyntax) **   <a name="vpclattice-UpdateRule-response-arn"></a>
The Amazon Resource Name (ARN) of the listener.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}/rule/rule-[0-9a-z]{17}`

 ** [id](#API_UpdateRule_ResponseSyntax) **   <a name="vpclattice-UpdateRule-response-id"></a>
The ID of the listener.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 22.
Pattern: `rule-[0-9a-z]{17}`

 ** [isDefault](#API_UpdateRule_ResponseSyntax) **   <a name="vpclattice-UpdateRule-response-isDefault"></a>
Indicates whether this is the default rule.
Type: Boolean

 ** [match](#API_UpdateRule_ResponseSyntax) **   <a name="vpclattice-UpdateRule-response-match"></a>
The rule match.
Type: [RuleMatch](API_RuleMatch.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [name](#API_UpdateRule_ResponseSyntax) **   <a name="vpclattice-UpdateRule-response-name"></a>
The name of the listener.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!rule-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [priority](#API_UpdateRule_ResponseSyntax) **   <a name="vpclattice-UpdateRule-response-priority"></a>
The rule priority.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2000.

## Errors
<a name="API_UpdateRule_Errors"></a>

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
<a name="API_UpdateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/UpdateRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/UpdateRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/UpdateRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/UpdateRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/UpdateRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/UpdateRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/UpdateRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/UpdateRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/UpdateRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/UpdateRule)

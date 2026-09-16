---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetRule.html
---

# GetRule
<a name="API_GetRule"></a>

Retrieves information about the specified listener rules. You can also retrieve information about the default listener rule. For more information, see [Listener rules](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules) in the *Amazon VPC Lattice User Guide*.

## Request Syntax
<a name="API_GetRule_RequestSyntax"></a>

```
GET /services/{{serviceIdentifier}}/listeners/{{listenerIdentifier}}/rules/{{ruleIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [listenerIdentifier](#API_GetRule_RequestSyntax) **   <a name="vpclattice-GetRule-request-uri-listenerIdentifier"></a>
The ID or ARN of the listener.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((listener-[0-9a-z]{17})|(^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}$))`
Required: Yes

 ** [ruleIdentifier](#API_GetRule_RequestSyntax) **   <a name="vpclattice-GetRule-request-uri-ruleIdentifier"></a>
The ID or ARN of the listener rule.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((rule-[0-9a-z]{17})|(^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}/rule/rule-[0-9a-z]{17}$))`
Required: Yes

 ** [serviceIdentifier](#API_GetRule_RequestSyntax) **   <a name="vpclattice-GetRule-request-uri-serviceIdentifier"></a>
The ID or ARN of the service.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((svc-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_GetRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "action": { ... },
   "arn": "string",
   "createdAt": "string",
   "id": "string",
   "isDefault": boolean,
   "lastUpdatedAt": "string",
   "match": { ... },
   "name": "string",
   "priority": number
}
```

## Response Elements
<a name="API_GetRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [action](#API_GetRule_ResponseSyntax) **   <a name="vpclattice-GetRule-response-action"></a>
The action for the default rule.
Type: [RuleAction](API_RuleAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [arn](#API_GetRule_ResponseSyntax) **   <a name="vpclattice-GetRule-response-arn"></a>
The Amazon Resource Name (ARN) of the listener.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}/rule/rule-[0-9a-z]{17}`

 ** [createdAt](#API_GetRule_ResponseSyntax) **   <a name="vpclattice-GetRule-response-createdAt"></a>
The date and time that the listener rule was created, in ISO-8601 format.
Type: Timestamp

 ** [id](#API_GetRule_ResponseSyntax) **   <a name="vpclattice-GetRule-response-id"></a>
The ID of the listener.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 22.
Pattern: `rule-[0-9a-z]{17}`

 ** [isDefault](#API_GetRule_ResponseSyntax) **   <a name="vpclattice-GetRule-response-isDefault"></a>
Indicates whether this is the default rule.
Type: Boolean

 ** [lastUpdatedAt](#API_GetRule_ResponseSyntax) **   <a name="vpclattice-GetRule-response-lastUpdatedAt"></a>
The date and time that the listener rule was last updated, in ISO-8601 format.
Type: Timestamp

 ** [match](#API_GetRule_ResponseSyntax) **   <a name="vpclattice-GetRule-response-match"></a>
The rule match.
Type: [RuleMatch](API_RuleMatch.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [name](#API_GetRule_ResponseSyntax) **   <a name="vpclattice-GetRule-response-name"></a>
The name of the listener.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!rule-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [priority](#API_GetRule_ResponseSyntax) **   <a name="vpclattice-GetRule-response-priority"></a>
The priority level for the specified rule.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2000.

## Errors
<a name="API_GetRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/GetRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/GetRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/GetRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/GetRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/GetRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/GetRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/GetRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/GetRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/GetRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/GetRule)

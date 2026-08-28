---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_BatchUpdateRule.html
---

# BatchUpdateRule
<a name="API_BatchUpdateRule"></a>

Updates the listener rules in a batch. You can use this operation to change the priority of listener rules. This can be useful when bulk updating or swapping rule priority.

 **Required permissions:** `vpc-lattice:UpdateRule`

For more information, see [How Amazon VPC Lattice works with IAM](https://docs.aws.amazon.com/vpc-lattice/latest/ug/security_iam_service-with-iam.html) in the *Amazon VPC Lattice User Guide*.

## Request Syntax
<a name="API_BatchUpdateRule_RequestSyntax"></a>

```
PATCH /services/{{serviceIdentifier}}/listeners/{{listenerIdentifier}}/rules HTTP/1.1
Content-type: application/json

{
   "rules": [
      {
         "action": { ... },
         "match": { ... },
         "priority": {{number}},
         "ruleIdentifier": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchUpdateRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [listenerIdentifier](#API_BatchUpdateRule_RequestSyntax) **   <a name="vpclattice-BatchUpdateRule-request-uri-listenerIdentifier"></a>
The ID or ARN of the listener.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((listener-[0-9a-z]{17})|(^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}$))`
Required: Yes

 ** [serviceIdentifier](#API_BatchUpdateRule_RequestSyntax) **   <a name="vpclattice-BatchUpdateRule-request-uri-serviceIdentifier"></a>
The ID or ARN of the service.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((svc-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_BatchUpdateRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [rules](#API_BatchUpdateRule_RequestSyntax) **   <a name="vpclattice-BatchUpdateRule-request-rules"></a>
The rules for the specified listener.
Type: Array of [RuleUpdate](API_RuleUpdate.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_BatchUpdateRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "successful": [
      {
         "action": { ... },
         "arn": "string",
         "id": "string",
         "isDefault": boolean,
         "match": { ... },
         "name": "string",
         "priority": number
      }
   ],
   "unsuccessful": [
      {
         "failureCode": "string",
         "failureMessage": "string",
         "ruleIdentifier": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchUpdateRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [successful](#API_BatchUpdateRule_ResponseSyntax) **   <a name="vpclattice-BatchUpdateRule-response-successful"></a>
The rules that were successfully updated.
Type: Array of [RuleUpdateSuccess](API_RuleUpdateSuccess.md) objects

 ** [unsuccessful](#API_BatchUpdateRule_ResponseSyntax) **   <a name="vpclattice-BatchUpdateRule-response-unsuccessful"></a>
The rules that the operation couldn't update.
Type: Array of [RuleUpdateFailure](API_RuleUpdateFailure.md) objects

## Errors
<a name="API_BatchUpdateRule_Errors"></a>

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
<a name="API_BatchUpdateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/BatchUpdateRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/BatchUpdateRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/BatchUpdateRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/BatchUpdateRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/BatchUpdateRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/BatchUpdateRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/BatchUpdateRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/BatchUpdateRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/BatchUpdateRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/BatchUpdateRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

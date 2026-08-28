---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_AddPolicyStatement.html
---

# AddPolicyStatement
<a name="API_AddPolicyStatement"></a>

Adds a policy statement object. To retrieve a list of existing policy statements, use the `GetPolicy` API.

## Request Syntax
<a name="API_AddPolicyStatement_RequestSyntax"></a>

```
POST /policies/{{arn}}/{{statementId}} HTTP/1.1
Content-type: application/json

{
   "action": [ "{{string}}" ],
   "condition": "{{string}}",
   "effect": "{{string}}",
   "principal": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_AddPolicyStatement_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_AddPolicyStatement_RequestSyntax) **   <a name="API-AddPolicyStatement-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the resource that will be accessed by the principal.
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:((schemamapping|matchingworkflow|idmappingworkflow|idnamespace)/[a-zA-Z_0-9-]{1,255})`
Required: Yes

 ** [statementId](#API_AddPolicyStatement_RequestSyntax) **   <a name="API-AddPolicyStatement-request-uri-statementId"></a>
A statement identifier that differentiates the statement from others in the same policy.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9A-Za-z]+`
Required: Yes

## Request Body
<a name="API_AddPolicyStatement_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_AddPolicyStatement_RequestSyntax) **   <a name="API-AddPolicyStatement-request-action"></a>
The action that the principal can use on the resource.
For example, `entityresolution:GetIdMappingJob`, `entityresolution:GetMatchingJob`.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `(entityresolution:[a-zA-Z0-9]+)`
Required: Yes

 ** [condition](#API_AddPolicyStatement_RequestSyntax) **   <a name="API-AddPolicyStatement-request-condition"></a>
A set of condition keys that you can use in key policies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40960.
Required: No

 ** [effect](#API_AddPolicyStatement_RequestSyntax) **   <a name="API-AddPolicyStatement-request-effect"></a>
Determines whether the permissions specified in the policy are to be allowed (`Allow`) or denied (`Deny`).
 If you set the value of the `effect` parameter to `Deny` for the `AddPolicyStatement` operation, you must also set the value of the `effect` parameter in the `policy` to `Deny` for the `PutPolicy` operation.
Type: String
Valid Values: `Allow | Deny`
Required: Yes

 ** [principal](#API_AddPolicyStatement_RequestSyntax) **   <a name="API-AddPolicyStatement-request-principal"></a>
The AWS service or AWS account that can access the resource defined as ARN.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 12. Maximum length of 64.
Pattern: `((\d{12})|([a-z0-9\.]+))`
Required: Yes

## Response Syntax
<a name="API_AddPolicyStatement_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "policy": "string",
   "token": "string"
}
```

## Response Elements
<a name="API_AddPolicyStatement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_AddPolicyStatement_ResponseSyntax) **   <a name="API-AddPolicyStatement-response-arn"></a>
The Amazon Resource Name (ARN) of the resource that will be accessed by the principal.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:((schemamapping|matchingworkflow|idmappingworkflow|idnamespace)/[a-zA-Z_0-9-]{1,255})`

 ** [policy](#API_AddPolicyStatement_ResponseSyntax) **   <a name="API-AddPolicyStatement-response-policy"></a>
The resource-based policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40960.

 ** [token](#API_AddPolicyStatement_ResponseSyntax) **   <a name="API-AddPolicyStatement-response-token"></a>
A unique identifier for the current revision of the policy.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`

## Errors
<a name="API_AddPolicyStatement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc.
HTTP Status Code: 400

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_AddPolicyStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/AddPolicyStatement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/AddPolicyStatement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/AddPolicyStatement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/AddPolicyStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/AddPolicyStatement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/AddPolicyStatement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/AddPolicyStatement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/AddPolicyStatement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/AddPolicyStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/AddPolicyStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

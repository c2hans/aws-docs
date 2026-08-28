---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_PutPolicy.html
---

# PutPolicy
<a name="API_PutPolicy"></a>

Updates the resource-based policy.

## Request Syntax
<a name="API_PutPolicy_RequestSyntax"></a>

```
PUT /policies/{{arn}} HTTP/1.1
Content-type: application/json

{
   "policy": "{{string}}",
   "token": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_PutPolicy_RequestSyntax) **   <a name="API-PutPolicy-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the resource for which the policy needs to be updated.
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:((schemamapping|matchingworkflow|idmappingworkflow|idnamespace)/[a-zA-Z_0-9-]{1,255})`
Required: Yes

## Request Body
<a name="API_PutPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policy](#API_PutPolicy_RequestSyntax) **   <a name="API-PutPolicy-request-policy"></a>
The resource-based policy.
If you set the value of the `effect` parameter in the `policy` to `Deny` for the `PutPolicy` operation, you must also set the value of the `effect` parameter to `Deny` for the `AddPolicyStatement` operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40960.
Required: Yes

 ** [token](#API_PutPolicy_RequestSyntax) **   <a name="API-PutPolicy-request-token"></a>
A unique identifier for the current revision of the policy.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: No

## Response Syntax
<a name="API_PutPolicy_ResponseSyntax"></a>

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
<a name="API_PutPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_PutPolicy_ResponseSyntax) **   <a name="API-PutPolicy-response-arn"></a>
The AWS Entity Resolution resource ARN.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:((schemamapping|matchingworkflow|idmappingworkflow|idnamespace)/[a-zA-Z_0-9-]{1,255})`

 ** [policy](#API_PutPolicy_ResponseSyntax) **   <a name="API-PutPolicy-response-policy"></a>
The resource-based policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40960.

 ** [token](#API_PutPolicy_ResponseSyntax) **   <a name="API-PutPolicy-response-token"></a>
A unique identifier for the current revision of the policy.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`

## Errors
<a name="API_PutPolicy_Errors"></a>

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
<a name="API_PutPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/PutPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/PutPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/PutPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/PutPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/PutPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/PutPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/PutPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/PutPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/PutPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/PutPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

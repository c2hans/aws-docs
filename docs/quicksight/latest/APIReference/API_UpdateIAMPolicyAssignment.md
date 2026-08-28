---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateIAMPolicyAssignment.html
---

# UpdateIAMPolicyAssignment
<a name="API_UpdateIAMPolicyAssignment"></a>

Updates an existing IAM policy assignment. This operation updates only the optional parameter or parameters that are specified in the request. This overwrites all of the users included in `Identities`.

## Request Syntax
<a name="API_UpdateIAMPolicyAssignment_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/iam-policy-assignments/{{AssignmentName}} HTTP/1.1
Content-type: application/json

{
   "AssignmentStatus": "{{string}}",
   "Identities": {
      "{{string}}" : [ "{{string}}" ]
   },
   "PolicyArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateIAMPolicyAssignment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssignmentName](#API_UpdateIAMPolicyAssignment_RequestSyntax) **   <a name="QS-UpdateIAMPolicyAssignment-request-uri-AssignmentName"></a>
The name of the assignment, also called a rule. The name must be unique within the AWS account.
Length Constraints: Minimum length of 1.
Pattern: `(?=^.{2,256}$)(?!.*\s)[0-9a-zA-Z-_.:=+@]*$`
Required: Yes

 ** [AwsAccountId](#API_UpdateIAMPolicyAssignment_RequestSyntax) **   <a name="QS-UpdateIAMPolicyAssignment-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the IAM policy assignment.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [Namespace](#API_UpdateIAMPolicyAssignment_RequestSyntax) **   <a name="QS-UpdateIAMPolicyAssignment-request-uri-Namespace"></a>
The namespace of the assignment.
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: Yes

## Request Body
<a name="API_UpdateIAMPolicyAssignment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AssignmentStatus](#API_UpdateIAMPolicyAssignment_RequestSyntax) **   <a name="QS-UpdateIAMPolicyAssignment-request-AssignmentStatus"></a>
The status of the assignment. Possible values are as follows:
+  `ENABLED` - Anything specified in this assignment is used when creating the data source.
+  `DISABLED` - This assignment isn't used when creating the data source.
+  `DRAFT` - This assignment is an unfinished draft and isn't used when creating the data source.
Type: String
Valid Values: `ENABLED | DRAFT | DISABLED`
Required: No

 ** [Identities](#API_UpdateIAMPolicyAssignment_RequestSyntax) **   <a name="QS-UpdateIAMPolicyAssignment-request-Identities"></a>
The Amazon Quick Sight users, groups, or both that you want to assign the policy to.
Type: String to array of strings map
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [PolicyArn](#API_UpdateIAMPolicyAssignment_RequestSyntax) **   <a name="QS-UpdateIAMPolicyAssignment-request-PolicyArn"></a>
The ARN for the IAM policy to apply to the Amazon Quick Sight users and groups specified in this assignment.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateIAMPolicyAssignment_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AssignmentId": "string",
   "AssignmentName": "string",
   "AssignmentStatus": "string",
   "Identities": {
      "string" : [ "string" ]
   },
   "PolicyArn": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateIAMPolicyAssignment_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-UpdateIAMPolicyAssignment-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AssignmentId](#API_UpdateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-UpdateIAMPolicyAssignment-response-AssignmentId"></a>
The ID of the assignment.
Type: String

 ** [AssignmentName](#API_UpdateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-UpdateIAMPolicyAssignment-response-AssignmentName"></a>
The name of the assignment or rule.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `(?=^.{2,256}$)(?!.*\s)[0-9a-zA-Z-_.:=+@]*$`

 ** [AssignmentStatus](#API_UpdateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-UpdateIAMPolicyAssignment-response-AssignmentStatus"></a>
The status of the assignment. Possible values are as follows:
+  `ENABLED` - Anything specified in this assignment is used when creating the data source.
+  `DISABLED` - This assignment isn't used when creating the data source.
+  `DRAFT` - This assignment is an unfinished draft and isn't used when creating the data source.
Type: String
Valid Values: `ENABLED | DRAFT | DISABLED`

 ** [Identities](#API_UpdateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-UpdateIAMPolicyAssignment-response-Identities"></a>
The Amazon Quick Sight users, groups, or both that the IAM policy is assigned to.
Type: String to array of strings map
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`

 ** [PolicyArn](#API_UpdateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-UpdateIAMPolicyAssignment-response-PolicyArn"></a>
The ARN for the IAM policy applied to the Amazon Quick Sight users and groups specified in this assignment.
Type: String

 ** [RequestId](#API_UpdateIAMPolicyAssignment_ResponseSyntax) **   <a name="QS-UpdateIAMPolicyAssignment-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateIAMPolicyAssignment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConcurrentUpdatingException **
A resource is already in a state that indicates an operation is happening that must complete before a new update can be applied.
HTTP Status Code: 500

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceExistsException **
The resource specified already exists.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateIAMPolicyAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateIAMPolicyAssignment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateIAMPolicyAssignment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateIAMPolicyAssignment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateIAMPolicyAssignment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateIAMPolicyAssignment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateIAMPolicyAssignment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateIAMPolicyAssignment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateIAMPolicyAssignment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateIAMPolicyAssignment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateIAMPolicyAssignment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

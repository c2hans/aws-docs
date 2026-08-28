---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteAccountAssignment.html
---

# DeleteAccountAssignment
<a name="API_DeleteAccountAssignment"></a>

Deletes a principal's access from a specified AWS account using a specified permission set.

**Note**
After a successful response, call `DescribeAccountAssignmentDeletionStatus` to describe the status of an assignment deletion request.

## Request Syntax
<a name="API_DeleteAccountAssignment_RequestSyntax"></a>

```
{
   "InstanceArn": "{{string}}",
   "PermissionSetArn": "{{string}}",
   "PrincipalId": "{{string}}",
   "PrincipalType": "{{string}}",
   "TargetId": "{{string}}",
   "TargetType": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteAccountAssignment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceArn](#API_DeleteAccountAssignment_RequestSyntax) **   <a name="singlesignon-DeleteAccountAssignment-request-InstanceArn"></a>
The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** [PermissionSetArn](#API_DeleteAccountAssignment_RequestSyntax) **   <a name="singlesignon-DeleteAccountAssignment-request-PermissionSetArn"></a>
The ARN of the permission set that will be used to remove access.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::permissionSet/(sso)?ins-[a-zA-Z0-9-.]{16}/ps-[a-zA-Z0-9-./]{16}`
Required: Yes

 ** [PrincipalId](#API_DeleteAccountAssignment_RequestSyntax) **   <a name="singlesignon-DeleteAccountAssignment-request-PrincipalId"></a>
An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the [IAM Identity Center Identity Store API Reference](/singlesignon/latest/IdentityStoreAPIReference/welcome.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: Yes

 ** [PrincipalType](#API_DeleteAccountAssignment_RequestSyntax) **   <a name="singlesignon-DeleteAccountAssignment-request-PrincipalType"></a>
The entity type for which the assignment will be deleted.
Type: String
Valid Values: `USER | GROUP`
Required: Yes

 ** [TargetId](#API_DeleteAccountAssignment_RequestSyntax) **   <a name="singlesignon-DeleteAccountAssignment-request-TargetId"></a>
TargetID is an AWS account identifier, (For example, 123456789012).
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [TargetType](#API_DeleteAccountAssignment_RequestSyntax) **   <a name="singlesignon-DeleteAccountAssignment-request-TargetType"></a>
The entity type for which the assignment will be deleted.
Type: String
Valid Values: `AWS_ACCOUNT`
Required: Yes

## Response Syntax
<a name="API_DeleteAccountAssignment_ResponseSyntax"></a>

```
{
   "AccountAssignmentDeletionStatus": {
      "CreatedDate": number,
      "FailureReason": "string",
      "PermissionSetArn": "string",
      "PrincipalId": "string",
      "PrincipalType": "string",
      "RequestId": "string",
      "Status": "string",
      "TargetId": "string",
      "TargetType": "string"
   }
}
```

## Response Elements
<a name="API_DeleteAccountAssignment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountAssignmentDeletionStatus](#API_DeleteAccountAssignment_ResponseSyntax) **   <a name="singlesignon-DeleteAccountAssignment-response-AccountAssignmentDeletionStatus"></a>
The status object for the account assignment deletion operation.
Type: [AccountAssignmentOperationStatus](API_AccountAssignmentOperationStatus.md) object

## Errors
<a name="API_DeleteAccountAssignment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Indicates that a requested resource is not found.
 ** Reason **
The reason for the resource not found exception.
HTTP Status Code: 400

 ** ThrottlingException **
Indicates that the principal has crossed the throttling limits of the API operations.
 ** Reason **
The reason for the throttling exception.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
 ** Reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAccountAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/DeleteAccountAssignment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/DeleteAccountAssignment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/DeleteAccountAssignment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/DeleteAccountAssignment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/DeleteAccountAssignment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/DeleteAccountAssignment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/DeleteAccountAssignment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/DeleteAccountAssignment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/DeleteAccountAssignment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/DeleteAccountAssignment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

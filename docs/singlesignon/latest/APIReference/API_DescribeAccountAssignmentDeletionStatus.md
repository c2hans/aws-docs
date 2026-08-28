---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeAccountAssignmentDeletionStatus.html
---

# DescribeAccountAssignmentDeletionStatus
<a name="API_DescribeAccountAssignmentDeletionStatus"></a>

Describes the status of the assignment deletion request.

## Request Syntax
<a name="API_DescribeAccountAssignmentDeletionStatus_RequestSyntax"></a>

```
{
   "AccountAssignmentDeletionRequestId": "{{string}}",
   "InstanceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAccountAssignmentDeletionStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountAssignmentDeletionRequestId](#API_DescribeAccountAssignmentDeletionStatus_RequestSyntax) **   <a name="singlesignon-DescribeAccountAssignmentDeletionStatus-request-AccountAssignmentDeletionRequestId"></a>
The identifier that is used to track the request operation progress.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b`
Required: Yes

 ** [InstanceArn](#API_DescribeAccountAssignmentDeletionStatus_RequestSyntax) **   <a name="singlesignon-DescribeAccountAssignmentDeletionStatus-request-InstanceArn"></a>
The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

## Response Syntax
<a name="API_DescribeAccountAssignmentDeletionStatus_ResponseSyntax"></a>

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
<a name="API_DescribeAccountAssignmentDeletionStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountAssignmentDeletionStatus](#API_DescribeAccountAssignmentDeletionStatus_ResponseSyntax) **   <a name="singlesignon-DescribeAccountAssignmentDeletionStatus-response-AccountAssignmentDeletionStatus"></a>
The status object for the account assignment deletion operation.
Type: [AccountAssignmentOperationStatus](API_AccountAssignmentOperationStatus.md) object

## Errors
<a name="API_DescribeAccountAssignmentDeletionStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
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
<a name="API_DescribeAccountAssignmentDeletionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/DescribeAccountAssignmentDeletionStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/DescribeAccountAssignmentDeletionStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/DescribeAccountAssignmentDeletionStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/DescribeAccountAssignmentDeletionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/DescribeAccountAssignmentDeletionStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/DescribeAccountAssignmentDeletionStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/DescribeAccountAssignmentDeletionStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/DescribeAccountAssignmentDeletionStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/DescribeAccountAssignmentDeletionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/DescribeAccountAssignmentDeletionStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

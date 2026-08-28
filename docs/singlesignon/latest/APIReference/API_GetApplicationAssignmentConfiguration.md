---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationAssignmentConfiguration.html
---

# GetApplicationAssignmentConfiguration
<a name="API_GetApplicationAssignmentConfiguration"></a>

Retrieves the configuration of [PutApplicationAssignmentConfiguration](API_PutApplicationAssignmentConfiguration.md).

## Request Syntax
<a name="API_GetApplicationAssignmentConfiguration_RequestSyntax"></a>

```
{
   "ApplicationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetApplicationAssignmentConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationArn](#API_GetApplicationAssignmentConfiguration_RequestSyntax) **   <a name="singlesignon-GetApplicationAssignmentConfiguration-request-ApplicationArn"></a>
Specifies the ARN of the application. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: Yes

## Response Syntax
<a name="API_GetApplicationAssignmentConfiguration_ResponseSyntax"></a>

```
{
   "AssignmentRequired": boolean
}
```

## Response Elements
<a name="API_GetApplicationAssignmentConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssignmentRequired](#API_GetApplicationAssignmentConfiguration_ResponseSyntax) **   <a name="singlesignon-GetApplicationAssignmentConfiguration-response-AssignmentRequired"></a>
If `AssignmentsRequired` is `true` (default value), users don’t have access to the application unless an assignment is created using the [CreateApplicationAssignment API](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplicationAssignment.html). If `false`, all users have access to the application.
Type: Boolean

## Errors
<a name="API_GetApplicationAssignmentConfiguration_Errors"></a>

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
<a name="API_GetApplicationAssignmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/GetApplicationAssignmentConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/GetApplicationAssignmentConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/GetApplicationAssignmentConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/GetApplicationAssignmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/GetApplicationAssignmentConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/GetApplicationAssignmentConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/GetApplicationAssignmentConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/GetApplicationAssignmentConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/GetApplicationAssignmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/GetApplicationAssignmentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationSessionConfiguration.html
---

# GetApplicationSessionConfiguration
<a name="API_GetApplicationSessionConfiguration"></a>

Retrieves the session configuration for an application in IAM Identity Center.

The session configuration determines how users can access an application. This includes whether user background sessions are enabled. User background sessions allow users to start a job on a supported AWS managed application without having to remain signed in to an active session while the job runs.

## Request Syntax
<a name="API_GetApplicationSessionConfiguration_RequestSyntax"></a>

```
{
   "ApplicationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetApplicationSessionConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationArn](#API_GetApplicationSessionConfiguration_RequestSyntax) **   <a name="singlesignon-GetApplicationSessionConfiguration-request-ApplicationArn"></a>
The Amazon Resource Name (ARN) of the application for which to retrieve the session configuration.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: Yes

## Response Syntax
<a name="API_GetApplicationSessionConfiguration_ResponseSyntax"></a>

```
{
   "UserBackgroundSessionApplicationStatus": "string"
}
```

## Response Elements
<a name="API_GetApplicationSessionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserBackgroundSessionApplicationStatus](#API_GetApplicationSessionConfiguration_ResponseSyntax) **   <a name="singlesignon-GetApplicationSessionConfiguration-response-UserBackgroundSessionApplicationStatus"></a>
The status of user background sessions for the application.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_GetApplicationSessionConfiguration_Errors"></a>

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
<a name="API_GetApplicationSessionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/GetApplicationSessionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/GetApplicationSessionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/GetApplicationSessionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/GetApplicationSessionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/GetApplicationSessionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/GetApplicationSessionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/GetApplicationSessionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/GetApplicationSessionConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/GetApplicationSessionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/GetApplicationSessionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

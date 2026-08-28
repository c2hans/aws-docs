---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationAccessScope.html
---

# GetApplicationAccessScope
<a name="API_GetApplicationAccessScope"></a>

Retrieves the authorized targets for an IAM Identity Center access scope for an application.

## Request Syntax
<a name="API_GetApplicationAccessScope_RequestSyntax"></a>

```
{
   "ApplicationArn": "{{string}}",
   "Scope": "{{string}}"
}
```

## Request Parameters
<a name="API_GetApplicationAccessScope_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationArn](#API_GetApplicationAccessScope_RequestSyntax) **   <a name="singlesignon-GetApplicationAccessScope-request-ApplicationArn"></a>
Specifies the ARN of the application with the access scope that you want to retrieve.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: Yes

 ** [Scope](#API_GetApplicationAccessScope_RequestSyntax) **   <a name="singlesignon-GetApplicationAccessScope-request-Scope"></a>
Specifies the name of the access scope for which you want the authorized targets.
Type: String
Pattern: `([A-Za-z0-9_]{1,50})(:[A-Za-z0-9_]{1,50}){0,1}(:[A-Za-z0-9_]{1,50}){0,1}`
Required: Yes

## Response Syntax
<a name="API_GetApplicationAccessScope_ResponseSyntax"></a>

```
{
   "AuthorizedTargets": [ "string" ],
   "Scope": "string"
}
```

## Response Elements
<a name="API_GetApplicationAccessScope_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthorizedTargets](#API_GetApplicationAccessScope_ResponseSyntax) **   <a name="singlesignon-GetApplicationAccessScope-response-AuthorizedTargets"></a>
An array of authorized targets associated with this access scope.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::(\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}|:instance/(sso)?ins-[a-zA-Z0-9-.]{16})`

 ** [Scope](#API_GetApplicationAccessScope_ResponseSyntax) **   <a name="singlesignon-GetApplicationAccessScope-response-Scope"></a>
The name of the access scope that can be used with the authorized targets.
Type: String
Pattern: `([A-Za-z0-9_]{1,50})(:[A-Za-z0-9_]{1,50}){0,1}(:[A-Za-z0-9_]{1,50}){0,1}`

## Errors
<a name="API_GetApplicationAccessScope_Errors"></a>

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
<a name="API_GetApplicationAccessScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/GetApplicationAccessScope)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/GetApplicationAccessScope)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/GetApplicationAccessScope)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/GetApplicationAccessScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/GetApplicationAccessScope)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/GetApplicationAccessScope)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/GetApplicationAccessScope)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/GetApplicationAccessScope)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/GetApplicationAccessScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/GetApplicationAccessScope)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

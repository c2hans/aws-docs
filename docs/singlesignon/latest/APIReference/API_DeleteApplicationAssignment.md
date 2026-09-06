---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplicationAssignment.html
---

# DeleteApplicationAssignment
<a name="API_DeleteApplicationAssignment"></a>

Revoke application access to an application by deleting application assignments for a user or group.

## Request Syntax
<a name="API_DeleteApplicationAssignment_RequestSyntax"></a>

```
{
   "ApplicationArn": "{{string}}",
   "PrincipalId": "{{string}}",
   "PrincipalType": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteApplicationAssignment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationArn](#API_DeleteApplicationAssignment_RequestSyntax) **   <a name="singlesignon-DeleteApplicationAssignment-request-ApplicationArn"></a>
Specifies the ARN of the application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: Yes

 ** [PrincipalId](#API_DeleteApplicationAssignment_RequestSyntax) **   <a name="singlesignon-DeleteApplicationAssignment-request-PrincipalId"></a>
An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the [IAM Identity Center Identity Store API Reference](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: Yes

 ** [PrincipalType](#API_DeleteApplicationAssignment_RequestSyntax) **   <a name="singlesignon-DeleteApplicationAssignment-request-PrincipalType"></a>
The entity type for which the assignment will be deleted.
Type: String
Valid Values: `USER | GROUP`
Required: Yes

## Response Elements
<a name="API_DeleteApplicationAssignment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteApplicationAssignment_Errors"></a>

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
<a name="API_DeleteApplicationAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/DeleteApplicationAssignment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/DeleteApplicationAssignment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/DeleteApplicationAssignment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/DeleteApplicationAssignment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/DeleteApplicationAssignment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/DeleteApplicationAssignment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/DeleteApplicationAssignment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/DeleteApplicationAssignment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/DeleteApplicationAssignment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/DeleteApplicationAssignment)

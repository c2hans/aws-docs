---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetGlueIdentityCenterConfiguration.html
---

# GetGlueIdentityCenterConfiguration
<a name="API_GetGlueIdentityCenterConfiguration"></a>

Retrieves the current AWS Glue Identity Center configuration details, including the associated Identity Center instance and application information.

## Response Syntax
<a name="API_GetGlueIdentityCenterConfiguration_ResponseSyntax"></a>

```
{
   "ApplicationArn": "string",
   "InstanceArn": "string",
   "Scopes": [ "string" ],
   "UserBackgroundSessionsEnabled": boolean
}
```

## Response Elements
<a name="API_GetGlueIdentityCenterConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationArn](#API_GetGlueIdentityCenterConfiguration_ResponseSyntax) **   <a name="Glue-GetGlueIdentityCenterConfiguration-response-ApplicationArn"></a>
The Amazon Resource Name (ARN) of the Identity Center application associated with the AWS Glue configuration.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.

 ** [InstanceArn](#API_GetGlueIdentityCenterConfiguration_ResponseSyntax) **   <a name="Glue-GetGlueIdentityCenterConfiguration-response-InstanceArn"></a>
The Amazon Resource Name (ARN) of the Identity Center instance associated with the AWS Glue configuration.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.

 ** [Scopes](#API_GetGlueIdentityCenterConfiguration_ResponseSyntax) **   <a name="Glue-GetGlueIdentityCenterConfiguration-response-Scopes"></a>
A list of Identity Center scopes that define the permissions and access levels for the AWS Glue configuration.
Type: Array of strings

 ** [UserBackgroundSessionsEnabled](#API_GetGlueIdentityCenterConfiguration_ResponseSyntax) **   <a name="Glue-GetGlueIdentityCenterConfiguration-response-UserBackgroundSessionsEnabled"></a>
Indicates whether users can run background sessions when using Identity Center authentication with AWS Glue services.
Type: Boolean

## Errors
<a name="API_GetGlueIdentityCenterConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetGlueIdentityCenterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetGlueIdentityCenterConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetGlueIdentityCenterConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetGlueIdentityCenterConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetGlueIdentityCenterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetGlueIdentityCenterConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetGlueIdentityCenterConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetGlueIdentityCenterConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetGlueIdentityCenterConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetGlueIdentityCenterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetGlueIdentityCenterConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

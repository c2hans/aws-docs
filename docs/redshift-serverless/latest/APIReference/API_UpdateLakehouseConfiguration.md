---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateLakehouseConfiguration.html
---

# UpdateLakehouseConfiguration
<a name="API_UpdateLakehouseConfiguration"></a>

Modifies the lakehouse configuration for a namespace. This operation allows you to manage Amazon Redshift federated permissions and AWS IAM Identity Center trusted identity propagation.

## Request Syntax
<a name="API_UpdateLakehouseConfiguration_RequestSyntax"></a>

```
{
   "catalogName": "{{string}}",
   "dryRun": {{boolean}},
   "lakehouseIdcApplicationArn": "{{string}}",
   "lakehouseIdcRegistration": "{{string}}",
   "lakehouseRegistration": "{{string}}",
   "namespaceName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateLakehouseConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [catalogName](#API_UpdateLakehouseConfiguration_RequestSyntax) **   <a name="redshiftserverless-UpdateLakehouseConfiguration-request-catalogName"></a>
The name of the AWS Glue Data Catalog that will be associated with the namespace enabled with Amazon Redshift federated permissions.
Pattern: `^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9_-]*[a-z]+[a-z0-9_-]*`
Required: No

 ** [dryRun](#API_UpdateLakehouseConfiguration_RequestSyntax) **   <a name="redshiftserverless-UpdateLakehouseConfiguration-request-dryRun"></a>
A boolean value that, if `true`, validates the request without actually updating the lakehouse configuration. Use this to check for errors before making changes.
Type: Boolean
Required: No

 ** [lakehouseIdcApplicationArn](#API_UpdateLakehouseConfiguration_RequestSyntax) **   <a name="redshiftserverless-UpdateLakehouseConfiguration-request-lakehouseIdcApplicationArn"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling AWS IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions.
Type: String
Required: No

 ** [lakehouseIdcRegistration](#API_UpdateLakehouseConfiguration_RequestSyntax) **   <a name="redshiftserverless-UpdateLakehouseConfiguration-request-lakehouseIdcRegistration"></a>
Modifies the AWS IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions. Valid values are `Associate` or `Disassociate`.
Type: String
Valid Values: `Associate | Disassociate`
Required: No

 ** [lakehouseRegistration](#API_UpdateLakehouseConfiguration_RequestSyntax) **   <a name="redshiftserverless-UpdateLakehouseConfiguration-request-lakehouseRegistration"></a>
Specifies whether to register or deregister the namespace with Amazon Redshift federated permissions. Valid values are `Register` or `Deregister`.
Type: String
Valid Values: `Register | Deregister`
Required: No

 ** [namespaceName](#API_UpdateLakehouseConfiguration_RequestSyntax) **   <a name="redshiftserverless-UpdateLakehouseConfiguration-request-namespaceName"></a>
The name of the namespace whose lakehouse configuration you want to modify.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_UpdateLakehouseConfiguration_ResponseSyntax"></a>

```
{
   "catalogArn": "string",
   "lakehouseIdcApplicationArn": "string",
   "lakehouseRegistrationStatus": "string",
   "namespaceName": "string"
}
```

## Response Elements
<a name="API_UpdateLakehouseConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [catalogArn](#API_UpdateLakehouseConfiguration_ResponseSyntax) **   <a name="redshiftserverless-UpdateLakehouseConfiguration-response-catalogArn"></a>
The Amazon Resource Name (ARN) of the AWS Glue Data Catalog associated with the lakehouse configuration.
Type: String

 ** [lakehouseIdcApplicationArn](#API_UpdateLakehouseConfiguration_ResponseSyntax) **   <a name="redshiftserverless-UpdateLakehouseConfiguration-response-lakehouseIdcApplicationArn"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling AWS IAM Identity Center trusted identity propagation.
Type: String

 ** [lakehouseRegistrationStatus](#API_UpdateLakehouseConfiguration_ResponseSyntax) **   <a name="redshiftserverless-UpdateLakehouseConfiguration-response-lakehouseRegistrationStatus"></a>
The current status of the lakehouse registration. Indicates whether the namespace is successfully registered with Amazon Redshift federated permissions.
Type: String

 ** [namespaceName](#API_UpdateLakehouseConfiguration_ResponseSyntax) **   <a name="redshiftserverless-UpdateLakehouseConfiguration-response-namespaceName"></a>
The name of the namespace.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`

## Errors
<a name="API_UpdateLakehouseConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** DryRunException **
This exception is thrown when the request was successful, but dry run was enabled so no action was taken.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLakehouseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/UpdateLakehouseConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/UpdateLakehouseConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/UpdateLakehouseConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/UpdateLakehouseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/UpdateLakehouseConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/UpdateLakehouseConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/UpdateLakehouseConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/UpdateLakehouseConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/UpdateLakehouseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/UpdateLakehouseConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

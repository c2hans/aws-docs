---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateGlueIdentityCenterConfiguration.html
---

# CreateGlueIdentityCenterConfiguration
<a name="API_CreateGlueIdentityCenterConfiguration"></a>

Creates a new AWS Glue Identity Center configuration to enable integration between AWS Glue and AWS IAM Identity Center for authentication and authorization.

## Request Syntax
<a name="API_CreateGlueIdentityCenterConfiguration_RequestSyntax"></a>

```
{
   "InstanceArn": "{{string}}",
   "Scopes": [ "{{string}}" ],
   "UserBackgroundSessionsEnabled": {{boolean}}
}
```

## Request Parameters
<a name="API_CreateGlueIdentityCenterConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceArn](#API_CreateGlueIdentityCenterConfiguration_RequestSyntax) **   <a name="Glue-CreateGlueIdentityCenterConfiguration-request-InstanceArn"></a>
The Amazon Resource Name (ARN) of the Identity Center instance to be associated with the AWS Glue configuration.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Required: Yes

 ** [Scopes](#API_CreateGlueIdentityCenterConfiguration_RequestSyntax) **   <a name="Glue-CreateGlueIdentityCenterConfiguration-request-Scopes"></a>
A list of Identity Center scopes that define the permissions and access levels for the AWS Glue configuration.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Maximum length of 50.
Required: No

 ** [UserBackgroundSessionsEnabled](#API_CreateGlueIdentityCenterConfiguration_RequestSyntax) **   <a name="Glue-CreateGlueIdentityCenterConfiguration-request-UserBackgroundSessionsEnabled"></a>
Specifies whether users can run background sessions when using Identity Center authentication with AWS Glue services.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateGlueIdentityCenterConfiguration_ResponseSyntax"></a>

```
{
   "ApplicationArn": "string"
}
```

## Response Elements
<a name="API_CreateGlueIdentityCenterConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationArn](#API_CreateGlueIdentityCenterConfiguration_ResponseSyntax) **   <a name="Glue-CreateGlueIdentityCenterConfiguration-response-ApplicationArn"></a>
The Amazon Resource Name (ARN) of the Identity Center application that was created for the AWS Glue configuration.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.

## Errors
<a name="API_CreateGlueIdentityCenterConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
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
<a name="API_CreateGlueIdentityCenterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateGlueIdentityCenterConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateGlueIdentityCenterConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateGlueIdentityCenterConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateGlueIdentityCenterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateGlueIdentityCenterConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateGlueIdentityCenterConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateGlueIdentityCenterConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateGlueIdentityCenterConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateGlueIdentityCenterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateGlueIdentityCenterConfiguration)

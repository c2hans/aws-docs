---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateGlueIdentityCenterConfiguration.html
---

# UpdateGlueIdentityCenterConfiguration
<a name="API_UpdateGlueIdentityCenterConfiguration"></a>

Updates the existing AWS Glue Identity Center configuration, allowing modification of scopes and permissions for the integration.

## Request Syntax
<a name="API_UpdateGlueIdentityCenterConfiguration_RequestSyntax"></a>

```
{
   "Scopes": [ "{{string}}" ],
   "UserBackgroundSessionsEnabled": {{boolean}}
}
```

## Request Parameters
<a name="API_UpdateGlueIdentityCenterConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Scopes](#API_UpdateGlueIdentityCenterConfiguration_RequestSyntax) **   <a name="Glue-UpdateGlueIdentityCenterConfiguration-request-Scopes"></a>
A list of Identity Center scopes that define the updated permissions and access levels for the AWS Glue configuration.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Maximum length of 50.
Required: No

 ** [UserBackgroundSessionsEnabled](#API_UpdateGlueIdentityCenterConfiguration_RequestSyntax) **   <a name="Glue-UpdateGlueIdentityCenterConfiguration-request-UserBackgroundSessionsEnabled"></a>
Specifies whether users can run background sessions when using Identity Center authentication with AWS Glue services.
Type: Boolean
Required: No

## Response Elements
<a name="API_UpdateGlueIdentityCenterConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateGlueIdentityCenterConfiguration_Errors"></a>

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
<a name="API_UpdateGlueIdentityCenterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateGlueIdentityCenterConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateGlueIdentityCenterConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateGlueIdentityCenterConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateGlueIdentityCenterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateGlueIdentityCenterConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateGlueIdentityCenterConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateGlueIdentityCenterConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateGlueIdentityCenterConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateGlueIdentityCenterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateGlueIdentityCenterConfiguration)

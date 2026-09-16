---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteEnvironmentAccountConnection.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# DeleteEnvironmentAccountConnection
<a name="API_DeleteEnvironmentAccountConnection"></a>

In an environment account, delete an environment account connection.

After you delete an environment account connection that’s in use by an AWS Proton environment, AWS Proton *can’t* manage the environment infrastructure resources until a new environment account connection is accepted for the environment account and associated environment. You're responsible for cleaning up provisioned resources that remain without an environment connection.

For more information, see [Environment account connections](https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html) in the * AWS Proton User guide*.

## Request Syntax
<a name="API_DeleteEnvironmentAccountConnection_RequestSyntax"></a>

```
{
   "id": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteEnvironmentAccountConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [id](#API_DeleteEnvironmentAccountConnection_RequestSyntax) **   <a name="proton-DeleteEnvironmentAccountConnection-request-id"></a>
The ID of the environment account connection to delete.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_DeleteEnvironmentAccountConnection_ResponseSyntax"></a>

```
{
   "environmentAccountConnection": {
      "arn": "string",
      "codebuildRoleArn": "string",
      "componentRoleArn": "string",
      "environmentAccountId": "string",
      "environmentName": "string",
      "id": "string",
      "lastModifiedAt": number,
      "managementAccountId": "string",
      "requestedAt": number,
      "roleArn": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_DeleteEnvironmentAccountConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentAccountConnection](#API_DeleteEnvironmentAccountConnection_ResponseSyntax) **   <a name="proton-DeleteEnvironmentAccountConnection-response-environmentAccountConnection"></a>
The detailed data of the environment account connection being deleted.
Type: [EnvironmentAccountConnection](API_EnvironmentAccountConnection.md) object

## Errors
<a name="API_DeleteEnvironmentAccountConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** ConflictException **
The request *couldn't* be made due to a conflicting operation or resource.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource *wasn't* found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_DeleteEnvironmentAccountConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/DeleteEnvironmentAccountConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/DeleteEnvironmentAccountConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/DeleteEnvironmentAccountConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/DeleteEnvironmentAccountConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/DeleteEnvironmentAccountConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/DeleteEnvironmentAccountConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/DeleteEnvironmentAccountConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/DeleteEnvironmentAccountConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/DeleteEnvironmentAccountConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/DeleteEnvironmentAccountConnection)

---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_RejectEnvironmentAccountConnection.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# RejectEnvironmentAccountConnection
<a name="API_RejectEnvironmentAccountConnection"></a>

In a management account, reject an environment account connection from another environment account.

After you reject an environment account connection request, you *can't* accept or use the rejected environment account connection.

You *can’t* reject an environment account connection that's connected to an environment.

For more information, see [Environment account connections](https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html) in the * AWS Proton User guide*.

## Request Syntax
<a name="API_RejectEnvironmentAccountConnection_RequestSyntax"></a>

```
{
   "id": "{{string}}"
}
```

## Request Parameters
<a name="API_RejectEnvironmentAccountConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [id](#API_RejectEnvironmentAccountConnection_RequestSyntax) **   <a name="proton-RejectEnvironmentAccountConnection-request-id"></a>
The ID of the environment account connection to reject.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_RejectEnvironmentAccountConnection_ResponseSyntax"></a>

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
<a name="API_RejectEnvironmentAccountConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentAccountConnection](#API_RejectEnvironmentAccountConnection_ResponseSyntax) **   <a name="proton-RejectEnvironmentAccountConnection-response-environmentAccountConnection"></a>
The environment connection account detail data that's returned by AWS Proton.
Type: [EnvironmentAccountConnection](API_EnvironmentAccountConnection.md) object

## Errors
<a name="API_RejectEnvironmentAccountConnection_Errors"></a>

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
<a name="API_RejectEnvironmentAccountConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/RejectEnvironmentAccountConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/RejectEnvironmentAccountConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/RejectEnvironmentAccountConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/RejectEnvironmentAccountConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/RejectEnvironmentAccountConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/RejectEnvironmentAccountConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/RejectEnvironmentAccountConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/RejectEnvironmentAccountConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/RejectEnvironmentAccountConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/RejectEnvironmentAccountConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

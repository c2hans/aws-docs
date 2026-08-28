---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_CreateConnection.html
---

# CreateConnection
<a name="API_CreateConnection"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Create an AWS App Runner connection resource. App Runner requires a connection resource when you create App Runner services that access private repositories from certain third-party providers. You can share a connection across multiple services.

A connection resource is needed to access GitHub and Bitbucket repositories. Both require a user interface approval process through the App Runner console before you can use the connection.

## Request Syntax
<a name="API_CreateConnection_RequestSyntax"></a>

```
{
   "ConnectionName": "{{string}}",
   "ProviderType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectionName](#API_CreateConnection_RequestSyntax) **   <a name="apprunner-CreateConnection-request-ConnectionName"></a>
A name for the new connection. It must be unique across all App Runner connections for the AWS account in the AWS Region.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 32.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{3,31}`
Required: Yes

 ** [ProviderType](#API_CreateConnection_RequestSyntax) **   <a name="apprunner-CreateConnection-request-ProviderType"></a>
The source repository provider.
Type: String
Valid Values: `GITHUB | BITBUCKET`
Required: Yes

 ** [Tags](#API_CreateConnection_RequestSyntax) **   <a name="apprunner-CreateConnection-request-Tags"></a>
A list of metadata items that you can associate with your connection resource. A tag is a key-value pair.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateConnection_ResponseSyntax"></a>

```
{
   "Connection": {
      "ConnectionArn": "string",
      "ConnectionName": "string",
      "CreatedAt": number,
      "ProviderType": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_CreateConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connection](#API_CreateConnection_ResponseSyntax) **   <a name="apprunner-CreateConnection-response-Connection"></a>
A description of the App Runner connection that's created by this request.
Type: [Connection](API_Connection.md) object

## Errors
<a name="API_CreateConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
App Runner can't create this resource. You've reached your account quota for this resource type.
For App Runner per-resource quotas, see [AWS App Runner endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/apprunner.html) in the * AWS General Reference*.
HTTP Status Code: 400

## Examples
<a name="API_CreateConnection_Examples"></a>

### Create a GitHub connection
<a name="API_CreateConnection_Example_1"></a>

This example illustrates how to create a connection to a private GitHub code repository. The connection status after a successful call is `PENDING_HANDSHAKE`. This is because an authentication handshake with the provider still hasn't happened. Complete the handshake using the App Runner console. For more information, see [Managing App Runner connections](https://docs.aws.amazon.com/apprunner/latest/dg/manage-connections.html) in the * AWS App Runner Developer Guide*.

#### Sample Request
<a name="API_CreateConnection_Example_1_Request"></a>

```
$ aws apprunner create-connection --cli-input-json "`cat`"
{
  "ConnectionName": "my-github-connection",
  "ProviderType": "GITHUB"
}
```

#### Sample Response
<a name="API_CreateConnection_Example_1_Response"></a>

```
{
  "Connection": {
    "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection",
    "ConnectionName": "my-github-connection",
    "Status": "PENDING_HANDSHAKE",
    "CreatedAt": "2020-11-03T00:32:51Z",
    "ProviderType": "GITHUB"
  }
}
```

## See Also
<a name="API_CreateConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/CreateConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/CreateConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/CreateConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/CreateConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/CreateConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/CreateConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/CreateConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/CreateConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/CreateConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/CreateConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

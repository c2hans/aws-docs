---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_DeleteConnection.html
---

# DeleteConnection
<a name="API_DeleteConnection"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Delete an AWS App Runner connection. You must first ensure that there are no running App Runner services that use this connection. If there are any, the `DeleteConnection` action fails.

## Request Syntax
<a name="API_DeleteConnection_RequestSyntax"></a>

```
{
   "ConnectionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectionArn](#API_DeleteConnection_RequestSyntax) **   <a name="apprunner-DeleteConnection-request-ConnectionArn"></a>
The Amazon Resource Name (ARN) of the App Runner connection that you want to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

## Response Syntax
<a name="API_DeleteConnection_ResponseSyntax"></a>

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
<a name="API_DeleteConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connection](#API_DeleteConnection_ResponseSyntax) **   <a name="apprunner-DeleteConnection-response-Connection"></a>
A description of the App Runner connection that this request just deleted.
Type: [Connection](API_Connection.md) object

## Errors
<a name="API_DeleteConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource doesn't exist for the specified Amazon Resource Name (ARN) in your AWS account.
HTTP Status Code: 400

## Examples
<a name="API_DeleteConnection_Examples"></a>

### Delete a connection
<a name="API_DeleteConnection_Example_1"></a>

This example illustrates deleting an App Runner connection. The connection status after a successful call is `DELETED`. This is because the connection is no longer available.

#### Sample Request
<a name="API_DeleteConnection_Example_1_Request"></a>

```
$ aws apprunner delete-connection --cli-input-json "`cat`"
{
  "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection"
}
```

#### Sample Response
<a name="API_DeleteConnection_Example_1_Response"></a>

```
{
  "Connection": {
    "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection",
    "ConnectionName": "my-github-connection",
    "Status": "DELETED",
    "CreatedAt": "2020-11-03T00:32:51Z",
    "ProviderType": "GITHUB"
  }
}
```

## See Also
<a name="API_DeleteConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/DeleteConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/DeleteConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/DeleteConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/DeleteConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/DeleteConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/DeleteConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/DeleteConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/DeleteConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/DeleteConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/DeleteConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

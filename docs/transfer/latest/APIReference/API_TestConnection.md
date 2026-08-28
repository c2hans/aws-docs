---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_TestConnection.html
---

# TestConnection
<a name="API_TestConnection"></a>

Tests whether your SFTP connector is set up successfully. We highly recommend that you call this operation to test your ability to transfer files between local AWS storage and a trading partner's SFTP server.

## Request Syntax
<a name="API_TestConnection_RequestSyntax"></a>

```
{
   "ConnectorId": "{{string}}"
}
```

## Request Parameters
<a name="API_TestConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectorId](#API_TestConnection_RequestSyntax) **   <a name="TransferFamily-TestConnection-request-ConnectorId"></a>
The unique identifier for the connector.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `c-([0-9a-f]{17})`
Required: Yes

## Response Syntax
<a name="API_TestConnection_ResponseSyntax"></a>

```
{
   "ConnectorId": "string",
   "SftpConnectionDetails": {
      "HostKey": "string"
   },
   "Status": "string",
   "StatusMessage": "string"
}
```

## Response Elements
<a name="API_TestConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectorId](#API_TestConnection_ResponseSyntax) **   <a name="TransferFamily-TestConnection-response-ConnectorId"></a>
Returns the identifier of the connector object that you are testing.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `c-([0-9a-f]{17})`

 ** [SftpConnectionDetails](#API_TestConnection_ResponseSyntax) **   <a name="TransferFamily-TestConnection-response-SftpConnectionDetails"></a>
Structure that contains the SFTP connector host key.
Type: [SftpConnectorConnectionDetails](API_SftpConnectorConnectionDetails.md) object

 ** [Status](#API_TestConnection_ResponseSyntax) **   <a name="TransferFamily-TestConnection-response-Status"></a>
Returns `OK` for successful test, or `ERROR` if the test fails.
Type: String

 ** [StatusMessage](#API_TestConnection_ResponseSyntax) **   <a name="TransferFamily-TestConnection-response-StatusMessage"></a>
Returns `Connection succeeded` if the test is successful. Or, returns a descriptive error message if the test fails. The following list provides troubleshooting details, depending on the error message that you receive.
+ Verify that your secret name aligns with the one in Transfer Role permissions.
+ Verify the server URL in the connector configuration , and verify that the login credentials work successfully outside of the connector.
+ Verify that the secret exists and is formatted correctly.
+ Verify that the trusted host key in the connector configuration matches the `ssh-keyscan` output.
Type: String

## Errors
<a name="API_TestConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
This exception is thrown when an error occurs in the AWS Transfer Family service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when a resource is not found by the AWSTransfer Family service.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request has failed because the AWSTransfer Family service is not available.
HTTP Status Code: 500

## Examples
<a name="API_TestConnection_Examples"></a>

### Example
<a name="API_TestConnection_Example_1"></a>

The following example tests the connection to a remote server.

```
aws transfer test-connection --connector-id c-abcd1234567890fff
```

### Sample Response
<a name="API_TestConnection_Example_2"></a>

If successful the API call returns the following details.

```
{
    "Status": "OK",
    "StatusMessage": "Connection succeeded"
}
```

## See Also
<a name="API_TestConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/TestConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/TestConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/TestConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/TestConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/TestConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/TestConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/TestConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/TestConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/TestConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/TestConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

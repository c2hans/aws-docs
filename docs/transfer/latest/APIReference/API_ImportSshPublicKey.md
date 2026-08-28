---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_ImportSshPublicKey.html
---

# ImportSshPublicKey
<a name="API_ImportSshPublicKey"></a>

Adds a Secure Shell (SSH) public key to a Transfer Family user identified by a `UserName` value assigned to the specific file transfer protocol-enabled server, identified by `ServerId`.

The response returns the `UserName` value, the `ServerId` value, and the name of the `SshPublicKeyId`.

## Request Syntax
<a name="API_ImportSshPublicKey_RequestSyntax"></a>

```
{
   "ServerId": "{{string}}",
   "SshPublicKeyBody": "{{string}}",
   "UserName": "{{string}}"
}
```

## Request Parameters
<a name="API_ImportSshPublicKey_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ServerId](#API_ImportSshPublicKey_RequestSyntax) **   <a name="TransferFamily-ImportSshPublicKey-request-ServerId"></a>
A system-assigned unique identifier for a server.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-([0-9a-f]{17})`
Required: Yes

 ** [SshPublicKeyBody](#API_ImportSshPublicKey_RequestSyntax) **   <a name="TransferFamily-ImportSshPublicKey-request-SshPublicKeyBody"></a>
The public key portion of an SSH key pair.
 AWS Transfer Family accepts RSA, ECDSA, and ED25519 keys.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `\s*(ssh|ecdsa)-[a-z0-9-]+[ \t]+(([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{1,3})?(={0,3})?)(\s*|[ \t]+[\S \t]*\s*)`
Required: Yes

 ** [UserName](#API_ImportSshPublicKey_RequestSyntax) **   <a name="TransferFamily-ImportSshPublicKey-request-UserName"></a>
The name of the Transfer Family user that is assigned to one or more servers.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[\w][\w@.-]{2,99}`
Required: Yes

## Response Syntax
<a name="API_ImportSshPublicKey_ResponseSyntax"></a>

```
{
   "ServerId": "string",
   "SshPublicKeyId": "string",
   "UserName": "string"
}
```

## Response Elements
<a name="API_ImportSshPublicKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ServerId](#API_ImportSshPublicKey_ResponseSyntax) **   <a name="TransferFamily-ImportSshPublicKey-response-ServerId"></a>
A system-assigned unique identifier for a server.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-([0-9a-f]{17})`

 ** [SshPublicKeyId](#API_ImportSshPublicKey_ResponseSyntax) **   <a name="TransferFamily-ImportSshPublicKey-response-SshPublicKeyId"></a>
The name given to a public key by the system that was imported.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `key-[0-9a-f]{17}`

 ** [UserName](#API_ImportSshPublicKey_ResponseSyntax) **   <a name="TransferFamily-ImportSshPublicKey-response-UserName"></a>
A user name assigned to the `ServerID` value that you specified.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[\w][\w@.-]{2,99}`

## Errors
<a name="API_ImportSshPublicKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
This exception is thrown when an error occurs in the AWS Transfer Family service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

 ** ResourceExistsException **
The requested resource does not exist, or exists in a region other than the one specified for the command.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when a resource is not found by the AWSTransfer Family service.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request has failed because the AWSTransfer Family service is not available.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## Examples
<a name="API_ImportSshPublicKey_Examples"></a>

### Example
<a name="API_ImportSshPublicKey_Example_1"></a>

This command imports an ECDSA key stored in the `id_ecdsa.pub` file.

```
aws transfer import-ssh-public-key --server-id s-021345abcdef6789 --ssh-public-key-body file://id_ecdsa.pub --user-name jane-doe
```

### Example
<a name="API_ImportSshPublicKey_Example_2"></a>

If you run the previous command, the system returns the following information.

```
{
    "ServerId": "s-021345abcdef6789",
   "SshPublicKeyId": "key-1234567890abcdef0",
   "UserName": "jane-doe"
}
```

## See Also
<a name="API_ImportSshPublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/ImportSshPublicKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/ImportSshPublicKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/ImportSshPublicKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/ImportSshPublicKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/ImportSshPublicKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/ImportSshPublicKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/ImportSshPublicKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/ImportSshPublicKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/ImportSshPublicKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/ImportSshPublicKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_StartRemoteMove.html
---

# StartRemoteMove
<a name="API_StartRemoteMove"></a>

Moves or renames a file or directory on the remote SFTP server.

## Request Syntax
<a name="API_StartRemoteMove_RequestSyntax"></a>

```
{
   "ConnectorId": "{{string}}",
   "SourcePath": "{{string}}",
   "TargetPath": "{{string}}"
}
```

## Request Parameters
<a name="API_StartRemoteMove_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectorId](#API_StartRemoteMove_RequestSyntax) **   <a name="TransferFamily-StartRemoteMove-request-ConnectorId"></a>
The unique identifier for the connector.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `c-([0-9a-f]{17})`
Required: Yes

 ** [SourcePath](#API_StartRemoteMove_RequestSyntax) **   <a name="TransferFamily-StartRemoteMove-request-SourcePath"></a>
The absolute path of the file or directory to move or rename. You can only specify one path per call to this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(.)+`
Required: Yes

 ** [TargetPath](#API_StartRemoteMove_RequestSyntax) **   <a name="TransferFamily-StartRemoteMove-request-TargetPath"></a>
The absolute path for the target of the move/rename operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(.)+`
Required: Yes

## Response Syntax
<a name="API_StartRemoteMove_ResponseSyntax"></a>

```
{
   "MoveId": "string"
}
```

## Response Elements
<a name="API_StartRemoteMove_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MoveId](#API_StartRemoteMove_ResponseSyntax) **   <a name="TransferFamily-StartRemoteMove-response-MoveId"></a>
Returns a unique identifier for the move/rename operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[0-9a-zA-Z./-]+`

## Errors
<a name="API_StartRemoteMove_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## Examples
<a name="API_StartRemoteMove_Examples"></a>

### Example
<a name="API_StartRemoteMove_Example_1"></a>

The following example moves a file on the remote SFTP server from `/source/folder/sourceFile` to `/destination/targetFile`, and returns a unique identifier for the operation.

```
aws transfer --connector-id c-AAAA1111BBBB2222C start-remote-move \
   --source-path /source/folder/sourceFile --target-path /destination/targetFile
```

## See Also
<a name="API_StartRemoteMove_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/StartRemoteMove)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/StartRemoteMove)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/StartRemoteMove)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/StartRemoteMove)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/StartRemoteMove)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/StartRemoteMove)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/StartRemoteMove)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/StartRemoteMove)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/StartRemoteMove)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/StartRemoteMove)

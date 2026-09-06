---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_StartFileTransfer.html
---

# StartFileTransfer
<a name="API_StartFileTransfer"></a>

Begins a file transfer between local AWS storage and a remote AS2 or SFTP server.
+ For an AS2 connector, you specify the `ConnectorId` and one or more `SendFilePaths` to identify the files you want to transfer.
+ For an SFTP connector, the file transfer can be either outbound or inbound. In both cases, you specify the `ConnectorId`. Depending on the direction of the transfer, you also specify the following items:
  + If you are transferring file from a partner's SFTP server to Amazon Web Services storage, you specify one or more `RetrieveFilePaths` to identify the files you want to transfer, and a `LocalDirectoryPath` to specify the destination folder.
  + If you are transferring file to a partner's SFTP server from AWS storage, you specify one or more `SendFilePaths` to identify the files you want to transfer, and a `RemoteDirectoryPath` to specify the destination folder.

## Request Syntax
<a name="API_StartFileTransfer_RequestSyntax"></a>

```
{
   "ConnectorId": "{{string}}",
   "CustomHttpHeaders": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "LocalDirectoryPath": "{{string}}",
   "RemoteDirectoryPath": "{{string}}",
   "RetrieveFilePaths": [ "{{string}}" ],
   "SendFilePaths": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_StartFileTransfer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectorId](#API_StartFileTransfer_RequestSyntax) **   <a name="TransferFamily-StartFileTransfer-request-ConnectorId"></a>
The unique identifier for the connector.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `c-([0-9a-f]{17})`
Required: Yes

 ** [CustomHttpHeaders](#API_StartFileTransfer_RequestSyntax) **   <a name="TransferFamily-StartFileTransfer-request-CustomHttpHeaders"></a>
An array of key-value pairs that represent custom HTTP headers to include in AS2 messages. These headers are added to the AS2 message when sending files to your trading partner.
Type: Array of [CustomHttpHeader](API_CustomHttpHeader.md) objects
Required: No

 ** [LocalDirectoryPath](#API_StartFileTransfer_RequestSyntax) **   <a name="TransferFamily-StartFileTransfer-request-LocalDirectoryPath"></a>
For an inbound transfer, the `LocaDirectoryPath` specifies the destination for one or more files that are transferred from the partner's SFTP server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(.)+`
Required: No

 ** [RemoteDirectoryPath](#API_StartFileTransfer_RequestSyntax) **   <a name="TransferFamily-StartFileTransfer-request-RemoteDirectoryPath"></a>
For an outbound transfer, the `RemoteDirectoryPath` specifies the destination for one or more files that are transferred to the partner's SFTP server. If you don't specify a `RemoteDirectoryPath`, the destination for transferred files is the SFTP user's home directory.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(.)+`
Required: No

 ** [RetrieveFilePaths](#API_StartFileTransfer_RequestSyntax) **   <a name="TransferFamily-StartFileTransfer-request-RetrieveFilePaths"></a>
One or more source paths for the partner's SFTP server. Each string represents a source file path for one inbound file transfer.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(.)+`
Required: No

 ** [SendFilePaths](#API_StartFileTransfer_RequestSyntax) **   <a name="TransferFamily-StartFileTransfer-request-SendFilePaths"></a>
One or more source paths for the Amazon S3 storage. Each string represents a source file path for one outbound file transfer. For example, ` amzn-s3-demo-bucket/myfile.txt `.
Replace ` amzn-s3-demo-bucket ` with one of your actual buckets.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(.)+`
Required: No

## Response Syntax
<a name="API_StartFileTransfer_ResponseSyntax"></a>

```
{
   "TransferId": "string"
}
```

## Response Elements
<a name="API_StartFileTransfer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TransferId](#API_StartFileTransfer_ResponseSyntax) **   <a name="TransferFamily-StartFileTransfer-response-TransferId"></a>
Returns the unique identifier for the file transfer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[0-9a-zA-Z./-]+`

## Errors
<a name="API_StartFileTransfer_Errors"></a>

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
<a name="API_StartFileTransfer_Examples"></a>

### Example
<a name="API_StartFileTransfer_Example_1"></a>

The following example starts an AS2 file transfer from a Transfer Family server to a remote trading partner's endpoint. Replace ` amzn-s3-demo-bucket ` with one of your actual buckets.

#### Sample Request
<a name="API_StartFileTransfer_Example_1_Request"></a>

```
{
    "ConnectorId": "c-AAAA1111BBBB2222C",
    "SendFilePaths": [
        "/amzn-s3-demo-bucket/myfile-1.txt",
        "/amzn-s3-demo-bucket/myfile-2.txt",
        "/amzn-s3-demo-bucket/myfile-3.txt"
    ]
}
```

#### Sample Response
<a name="API_StartFileTransfer_Example_1_Response"></a>

```
{
   "TransferId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

### Example
<a name="API_StartFileTransfer_Example_2"></a>

The following example starts a file transfer from local AWS storage to a remote SFTP server.

#### Sample Request
<a name="API_StartFileTransfer_Example_2_Request"></a>

```
{
    "ConnectorId": "c-01234567890abcdef",
    "SendFilePaths": [
        "/amzn-s3-demo-bucket/myfile-1.txt",
        "/amzn-s3-demo-bucket/myfile-2.txt",
        "/amzn-s3-demo-bucket/myfile-3.txt"
    ],
    "RemoteDirectoryPath": "/MySFTPRootFolder/fromTranferFamilyServer"
}
```

#### Sample Response
<a name="API_StartFileTransfer_Example_2_Response"></a>

```
{
   "TransferId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
}
```

### Example
<a name="API_StartFileTransfer_Example_3"></a>

The following example starts a file transfer from a remote SFTP server to local AWS storage.

#### Sample Request
<a name="API_StartFileTransfer_Example_3_Request"></a>

```
{
    "ConnectorId": "c-111122223333AAAAA",
    "RetrieveFilePaths": [
        "/MySFTPFolder/toTranferFamily/myfile-1.txt",
        "/MySFTPFolder/toTranferFamily/myfile-2.txt",
        "/MySFTPFolder/toTranferFamily/myfile-3.txt"
    ],
    "LocalDirectoryPath": "/amzn-s3-demo-bucket/mySourceFiles"
}
```

#### Sample Response
<a name="API_StartFileTransfer_Example_3_Response"></a>

```
{
   "TransferId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa"
}
```

## See Also
<a name="API_StartFileTransfer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/StartFileTransfer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/StartFileTransfer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/StartFileTransfer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/StartFileTransfer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/StartFileTransfer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/StartFileTransfer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/StartFileTransfer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/StartFileTransfer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/StartFileTransfer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/StartFileTransfer)

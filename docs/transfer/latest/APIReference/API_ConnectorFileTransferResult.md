---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_ConnectorFileTransferResult.html
---

# ConnectorFileTransferResult
<a name="API_ConnectorFileTransferResult"></a>

A structure that contains the details for files transferred using an SFTP connector, during a single transfer.

## Contents
<a name="API_ConnectorFileTransferResult_Contents"></a>

 ** FilePath **   <a name="TransferFamily-Type-ConnectorFileTransferResult-FilePath"></a>
The filename and path to where the file was sent to or retrieved from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(.)+`
Required: Yes

 ** StatusCode **   <a name="TransferFamily-Type-ConnectorFileTransferResult-StatusCode"></a>
The current status for the transfer.
Type: String
Valid Values: `QUEUED | IN_PROGRESS | COMPLETED | FAILED`
Required: Yes

 ** FailureCode **   <a name="TransferFamily-Type-ConnectorFileTransferResult-FailureCode"></a>
For transfers that fail, this parameter contains a code indicating the reason. For example, `RETRIEVE_FILE_NOT_FOUND`
Type: String
Required: No

 ** FailureMessage **   <a name="TransferFamily-Type-ConnectorFileTransferResult-FailureMessage"></a>
For transfers that fail, this parameter describes the reason for the failure.
Type: String
Required: No

## See Also
<a name="API_ConnectorFileTransferResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/ConnectorFileTransferResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/ConnectorFileTransferResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/ConnectorFileTransferResult)

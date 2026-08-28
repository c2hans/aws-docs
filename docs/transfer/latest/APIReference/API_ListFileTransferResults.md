---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_ListFileTransferResults.html
---

# ListFileTransferResults
<a name="API_ListFileTransferResults"></a>

 Returns real-time updates and detailed information on the status of each individual file being transferred in a specific file transfer operation. You specify the file transfer by providing its `ConnectorId` and its `TransferId`.

**Note**
File transfer results are available up to 7 days after an operation has been requested.

## Request Syntax
<a name="API_ListFileTransferResults_RequestSyntax"></a>

```
{
   "ConnectorId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TransferId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListFileTransferResults_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectorId](#API_ListFileTransferResults_RequestSyntax) **   <a name="TransferFamily-ListFileTransferResults-request-ConnectorId"></a>
A unique identifier for a connector. This value should match the value supplied to the corresponding `StartFileTransfer` call.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `c-([0-9a-f]{17})`
Required: Yes

 ** [MaxResults](#API_ListFileTransferResults_RequestSyntax) **   <a name="TransferFamily-ListFileTransferResults-request-MaxResults"></a>
The maximum number of files to return in a single page. Note that currently you can specify a maximum of 10 file paths in a single [StartFileTransfer](https://docs.aws.amazon.com/transfer/latest/APIReference/API_StartFileTransfer.html) operation. Thus, the maximum number of file transfer results that can be returned in a single page is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListFileTransferResults_RequestSyntax) **   <a name="TransferFamily-ListFileTransferResults-request-NextToken"></a>
If there are more file details than returned in this call, use this value for a subsequent call to `ListFileTransferResults` to retrieve them.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.
Required: No

 ** [TransferId](#API_ListFileTransferResults_RequestSyntax) **   <a name="TransferFamily-ListFileTransferResults-request-TransferId"></a>
A unique identifier for a file transfer. This value should match the value supplied to the corresponding `StartFileTransfer` call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[0-9a-zA-Z./-]+`
Required: Yes

## Response Syntax
<a name="API_ListFileTransferResults_ResponseSyntax"></a>

```
{
   "FileTransferResults": [
      {
         "FailureCode": "string",
         "FailureMessage": "string",
         "FilePath": "string",
         "StatusCode": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFileTransferResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileTransferResults](#API_ListFileTransferResults_ResponseSyntax) **   <a name="TransferFamily-ListFileTransferResults-response-FileTransferResults"></a>
Returns the details for the files transferred in the transfer identified by the `TransferId` and `ConnectorId` specified.
+  `FilePath`: the filename and path to where the file was sent to or retrieved from.
+  `StatusCode`: current status for the transfer. The status returned is one of the following values:`QUEUED`, `IN_PROGRESS`, `COMPLETED`, or `FAILED`
+  `FailureCode`: for transfers that fail, this parameter contains a code indicating the reason. For example, `RETRIEVE_FILE_NOT_FOUND`
+  `FailureMessage`: for transfers that fail, this parameter describes the reason for the failure.
Type: Array of [ConnectorFileTransferResult](API_ConnectorFileTransferResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

 ** [NextToken](#API_ListFileTransferResults_ResponseSyntax) **   <a name="TransferFamily-ListFileTransferResults-response-NextToken"></a>
Returns a token that you can use to call `ListFileTransferResults` again and receive additional results, if there are any (against the same `TransferId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.

## Errors
<a name="API_ListFileTransferResults_Errors"></a>

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
<a name="API_ListFileTransferResults_Examples"></a>

### Example
<a name="API_ListFileTransferResults_Example_1"></a>

The following example returns a list of files for connector ID `a-11112222333344444` and transfer ID `aa1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.

#### Sample Request
<a name="API_ListFileTransferResults_Example_1_Request"></a>

```
aws transfer listFileTransferResults --connector-id a-11112222333344444 --transfer-id a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
```

### Example
<a name="API_ListFileTransferResults_Example_2"></a>

An example response looks like the following.

#### Sample Response
<a name="API_ListFileTransferResults_Example_2_Response"></a>

```
{
  "FileTransferResults": [
    {
      "FilePath" : "my-stuff/hello.txt",
      "StatusCode": "COMPLETED"
    },
    {
      "FilePath" : "my-stuff/texting.txt",
      "StatusCode": "FAILED",
      "FailureCode": "RETRIEVE_FILE_NOT_FOUND",
      "FailureMessage": "SFTP error (SSH_FX_NO_SUCH_FILE)"
    }
  ],
  "NextToken": "1111111"
}
```

## See Also
<a name="API_ListFileTransferResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/ListFileTransferResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/ListFileTransferResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/ListFileTransferResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/ListFileTransferResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/ListFileTransferResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/ListFileTransferResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/ListFileTransferResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/ListFileTransferResults)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/ListFileTransferResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/ListFileTransferResults)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

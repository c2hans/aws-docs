---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_StartDirectoryListing.html
---

# StartDirectoryListing
<a name="API_StartDirectoryListing"></a>

Retrieves a list of the contents of a directory from a remote SFTP server. You specify the connector ID, the output path, and the remote directory path. You can also specify the optional `MaxItems` value to control the maximum number of items that are listed from the remote directory. This API returns a list of all files and directories in the remote directory (up to the maximum value), but does not return files or folders in sub-directories. That is, it only returns a list of files and directories one-level deep.

After you receive the listing file, you can provide the files that you want to transfer to the `RetrieveFilePaths` parameter of the `StartFileTransfer` API call.

The naming convention for the output file is ` connector-ID-listing-ID.json`. The output file contains the following information:
+  `filePath`: the complete path of a remote file, relative to the directory of the listing request for your SFTP connector on the remote server.
+  `modifiedTimestamp`: the last time the file was modified, in UTC time format. This field is optional. If the remote file attributes don't contain a timestamp, it is omitted from the file listing.
+  `size`: the size of the file, in bytes. This field is optional. If the remote file attributes don't contain a file size, it is omitted from the file listing.
+  `path`: the complete path of a remote directory, relative to the directory of the listing request for your SFTP connector on the remote server.
+  `truncated`: a flag indicating whether the list output contains all of the items contained in the remote directory or not. If your `Truncated` output value is true, you can increase the value provided in the optional `max-items` input attribute to be able to list more items (up to the maximum allowed list size of 200,000 items).

## Request Syntax
<a name="API_StartDirectoryListing_RequestSyntax"></a>

```
{
   "ConnectorId": "{{string}}",
   "MaxItems": {{number}},
   "OutputDirectoryPath": "{{string}}",
   "RemoteDirectoryPath": "{{string}}"
}
```

## Request Parameters
<a name="API_StartDirectoryListing_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectorId](#API_StartDirectoryListing_RequestSyntax) **   <a name="TransferFamily-StartDirectoryListing-request-ConnectorId"></a>
The unique identifier for the connector.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `c-([0-9a-f]{17})`
Required: Yes

 ** [MaxItems](#API_StartDirectoryListing_RequestSyntax) **   <a name="TransferFamily-StartDirectoryListing-request-MaxItems"></a>
An optional parameter where you can specify the maximum number of file/directory names to retrieve. The default value is 1,000.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [OutputDirectoryPath](#API_StartDirectoryListing_RequestSyntax) **   <a name="TransferFamily-StartDirectoryListing-request-OutputDirectoryPath"></a>
Specifies the path (bucket and prefix) in Amazon S3 storage to store the results of the directory listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(.)+`
Required: Yes

 ** [RemoteDirectoryPath](#API_StartDirectoryListing_RequestSyntax) **   <a name="TransferFamily-StartDirectoryListing-request-RemoteDirectoryPath"></a>
Specifies the directory on the remote SFTP server for which you want to list its contents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(.)+`
Required: Yes

## Response Syntax
<a name="API_StartDirectoryListing_ResponseSyntax"></a>

```
{
   "ListingId": "string",
   "OutputFileName": "string"
}
```

## Response Elements
<a name="API_StartDirectoryListing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ListingId](#API_StartDirectoryListing_ResponseSyntax) **   <a name="TransferFamily-StartDirectoryListing-response-ListingId"></a>
Returns a unique identifier for the directory listing call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[0-9a-zA-Z./-]+`

 ** [OutputFileName](#API_StartDirectoryListing_ResponseSyntax) **   <a name="TransferFamily-StartDirectoryListing-response-OutputFileName"></a>
Returns the file name where the results are stored. This is a combination of the connector ID and the listing ID: `<connector-id>-<listing-id>.json`.
Type: String
Length Constraints: Minimum length of 26. Maximum length of 537.
Pattern: `c-([0-9a-f]{17})-[0-9a-zA-Z./-]+.json`

## Errors
<a name="API_StartDirectoryListing_Errors"></a>

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
<a name="API_StartDirectoryListing_Examples"></a>

### Example
<a name="API_StartDirectoryListing_Example_1"></a>

The following example lists the contents of the `home` folder on the remote SFTP server, which is identified by the specified connector. The results are placed into the Amazon S3 location `/amzn-s3-demo-bucket/connector-files`, and into a file named `c-AAAA1111BBBB2222C-6666abcd-11aa-22bb-cc33-0000aaaa3333.json`.

#### Sample Request
<a name="API_StartDirectoryListing_Example_1_Request"></a>

```
{
    "ConnectorId": "c-AAAA1111BBBB2222C",
    "MaxItems": "10",
    "OutputDirectoryPath": "/amzn-s3-demo-bucket/connector-files",
    "RemoteDirectoryPath": "/home"
}
```

#### Sample Response
<a name="API_StartDirectoryListing_Example_1_Response"></a>

```
{
    "ListingId": "6666abcd-11aa-22bb-cc33-0000aaaa3333",
    "OutputFileName": "c-AAAA1111BBBB2222C-6666abcd-11aa-22bb-cc33-0000aaaa3333.json"
}
```

```
// under bucket "amzn-s3-demo-bucket"
connector-files/c-AAAA1111BBBB2222C-6666abcd-11aa-22bb-cc33-0000aaaa3333.json
{
    "files": [
        {
            "filePath": "/home/what.txt",
            "modifiedTimestamp": "2024-01-30T20:34:54Z",
            "size" : 2323
        },
        {
            "filePath": "/home/how.pgp",
            "modifiedTimestamp": "2024-01-30T20:34:54Z",
            "size" : 51238
        }
    ],
    "paths": [
        {
            "path": "/home/magic"
        },
        {
            "path": "/home/aws"
        },
    ],
    "truncated": false
}
```

## See Also
<a name="API_StartDirectoryListing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/StartDirectoryListing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/StartDirectoryListing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/StartDirectoryListing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/StartDirectoryListing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/StartDirectoryListing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/StartDirectoryListing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/StartDirectoryListing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/StartDirectoryListing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/StartDirectoryListing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/StartDirectoryListing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

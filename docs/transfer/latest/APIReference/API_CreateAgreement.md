---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_CreateAgreement.html
---

# CreateAgreement
<a name="API_CreateAgreement"></a>

Creates an agreement. An agreement is a bilateral trading partner agreement, or partnership, between an AWS Transfer Family server and an AS2 process. The agreement defines the file and message transfer relationship between the server and the AS2 process. To define an agreement, Transfer Family combines a server, local profile, partner profile, certificate, and other attributes.

The partner is identified with the `PartnerProfileId`, and the AS2 process is identified with the `LocalProfileId`.

**Note**
Specify *either* `BaseDirectory` or `CustomDirectories`, but not both. Specifying both causes the command to fail.

## Request Syntax
<a name="API_CreateAgreement_RequestSyntax"></a>

```
{
   "AccessRole": "{{string}}",
   "BaseDirectory": "{{string}}",
   "CustomDirectories": {
      "FailedFilesDirectory": "{{string}}",
      "MdnFilesDirectory": "{{string}}",
      "PayloadFilesDirectory": "{{string}}",
      "StatusFilesDirectory": "{{string}}",
      "TemporaryFilesDirectory": "{{string}}"
   },
   "Description": "{{string}}",
   "EnforceMessageSigning": "{{string}}",
   "LocalProfileId": "{{string}}",
   "PartnerProfileId": "{{string}}",
   "PreserveFilename": "{{string}}",
   "ServerId": "{{string}}",
   "Status": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAgreement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessRole](#API_CreateAgreement_RequestSyntax) **   <a name="TransferFamily-CreateAgreement-request-AccessRole"></a>
Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the AWS Identity and Access Management role to use.
 **For AS2 connectors**
With AS2, you can send files by calling `StartFileTransfer` and specifying the file paths in the request parameter, `SendFilePaths`. We use the file’s parent directory (for example, for `--send-file-paths /bucket/dir/file.txt`, parent directory is `/bucket/dir/`) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the `AccessRole` needs to provide read and write access to the parent directory of the file location used in the `StartFileTransfer` request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with `StartFileTransfer`.
If you are using Basic authentication for your AS2 connector, the access role requires the `secretsmanager:GetSecretValue` permission for the secret. If the secret is encrypted using a customer-managed key instead of the AWS managed key in Secrets Manager, then the role also needs the `kms:Decrypt` permission for that key.
 **For SFTP connectors**
Make sure that the access role provides read and write access to the parent directory of the file location that's used in the `StartFileTransfer` request. Additionally, make sure that the role provides `secretsmanager:GetSecretValue` permission to AWS Secrets Manager.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*role/\S+`
Required: Yes

 ** [BaseDirectory](#API_CreateAgreement_RequestSyntax) **   <a name="TransferFamily-CreateAgreement-request-BaseDirectory"></a>
The landing directory (folder) for files transferred by using the AS2 protocol.
A `BaseDirectory` example is `/amzn-s3-demo-bucket/home/mydirectory`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(|/.*)`
Required: No

 ** [CustomDirectories](#API_CreateAgreement_RequestSyntax) **   <a name="TransferFamily-CreateAgreement-request-CustomDirectories"></a>
A `CustomDirectoriesType` structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.
+ Failed files
+ MDN files
+ Payload files
+ Status files
+ Temporary files
Type: [CustomDirectoriesType](API_CustomDirectoriesType.md) object
Required: No

 ** [Description](#API_CreateAgreement_RequestSyntax) **   <a name="TransferFamily-CreateAgreement-request-Description"></a>
A name or short description to identify the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\u0021-\u007E]+`
Required: No

 ** [EnforceMessageSigning](#API_CreateAgreement_RequestSyntax) **   <a name="TransferFamily-CreateAgreement-request-EnforceMessageSigning"></a>
 Determines whether or not unsigned messages from your trading partners will be accepted.
+  `ENABLED`: Transfer Family rejects unsigned messages from your trading partner.
+  `DISABLED` (default value): Transfer Family accepts unsigned messages from your trading partner.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [LocalProfileId](#API_CreateAgreement_RequestSyntax) **   <a name="TransferFamily-CreateAgreement-request-LocalProfileId"></a>
A unique identifier for the AS2 local profile.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `p-([0-9a-f]{17})`
Required: Yes

 ** [PartnerProfileId](#API_CreateAgreement_RequestSyntax) **   <a name="TransferFamily-CreateAgreement-request-PartnerProfileId"></a>
A unique identifier for the partner profile used in the agreement.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `p-([0-9a-f]{17})`
Required: Yes

 ** [PreserveFilename](#API_CreateAgreement_RequestSyntax) **   <a name="TransferFamily-CreateAgreement-request-PreserveFilename"></a>
 Determines whether or not Transfer Family appends a unique string of characters to the end of the AS2 message payload filename when saving it.
+  `ENABLED`: the filename provided by your trading parter is preserved when the file is saved.
+  `DISABLED` (default value): when Transfer Family saves the file, the filename is adjusted, as described in [File names and locations](https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html#file-names-as2).
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [ServerId](#API_CreateAgreement_RequestSyntax) **   <a name="TransferFamily-CreateAgreement-request-ServerId"></a>
A system-assigned unique identifier for a server instance. This is the specific server that the agreement uses.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-([0-9a-f]{17})`
Required: Yes

 ** [Status](#API_CreateAgreement_RequestSyntax) **   <a name="TransferFamily-CreateAgreement-request-Status"></a>
The status of the agreement. The agreement can be either `ACTIVE` or `INACTIVE`.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** [Tags](#API_CreateAgreement_RequestSyntax) **   <a name="TransferFamily-CreateAgreement-request-Tags"></a>
Key-value pairs that can be used to group and search for agreements.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateAgreement_ResponseSyntax"></a>

```
{
   "AgreementId": "string"
}
```

## Response Elements
<a name="API_CreateAgreement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AgreementId](#API_CreateAgreement_ResponseSyntax) **   <a name="TransferFamily-CreateAgreement-response-AgreementId"></a>
The unique identifier for the agreement. Use this ID for deleting, or updating an agreement, as well as in any other API calls that require that you specify the agreement ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `a-([0-9a-f]{17})`

## Errors
<a name="API_CreateAgreement_Errors"></a>

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
<a name="API_CreateAgreement_Examples"></a>

### Example
<a name="API_CreateAgreement_Example_1"></a>

The following example creates an agreement, and returns the agreement ID.

```
aws transfer create-agreement --server-id s-021345abcdef6789 --local-profile-id p-1234567890abcdef0 \
    --partner-profile-id p-abcdef01234567890 --base-directory/amzn-s3-demo-bucket/AS2-files \
    --access-role arn:aws:iam::111122223333:role/AS2-role
```

### Sample Response
<a name="API_CreateAgreement_Example_2"></a>

The API call returns the agreement ID for the new agreement.

```
{
    "AgreementId": "a-11112222333344444"
}
```

### Example
<a name="API_CreateAgreement_Example_3"></a>

The following example creates an agreement, using custom directories, and returns the agreement ID. Create a file that lists the custom directories to use for the agreement, and save it as `custom-directories.json`, then run the command that follows. (Replace the sample directories with your actual values.)

```
{
        "FailedFilesDirectory": "amzn-s3-demo-bucket/AS2-failed",
        "MdnFilesDirectory": "/amzn-s3-demo-bucket/AS2-mdn",
        "PayloadFilesDirectory": "amzn-s3-demo-bucket/AS2-payload",
        "StatusFilesDirectory": "/amzn-s3-demo-bucket/AS2-status",
        "TemporaryFilesDirectory": "amzn-s3-demo-bucket/AS2-temp"
}
```

```
aws transfer create-agreement --server-id s-021345abcdef6789 --local-profile-id p-1234567890abcdef0 \
    --partner-profile-id p-abcdef01234567890 --custom-directories file://custom-directories.json \
    --access-role arn:aws:iam::111122223333:role/AS2-role
```

### Sample Response
<a name="API_CreateAgreement_Example_4"></a>

The API call returns the agreement ID for the new agreement.

```
{
    "AgreementId": "a-11112222333344444"
}
```

## See Also
<a name="API_CreateAgreement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/CreateAgreement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/CreateAgreement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/CreateAgreement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/CreateAgreement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/CreateAgreement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/CreateAgreement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/CreateAgreement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/CreateAgreement)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/CreateAgreement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/CreateAgreement)

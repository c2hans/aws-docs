---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_UpdateAgreement.html
---

# UpdateAgreement
<a name="API_UpdateAgreement"></a>

Updates some of the parameters for an existing agreement. Provide the `AgreementId` and the `ServerId` for the agreement that you want to update, along with the new values for the parameters to update.

**Note**
Specify *either* `BaseDirectory` or `CustomDirectories`, but not both. Specifying both causes the command to fail.
If you update an agreement from using base directory to custom directories, the base directory is no longer used. Similarly, if you change from custom directories to a base directory, the custom directories are no longer used.

## Request Syntax
<a name="API_UpdateAgreement_RequestSyntax"></a>

```
{
   "AccessRole": "{{string}}",
   "AgreementId": "{{string}}",
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
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateAgreement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessRole](#API_UpdateAgreement_RequestSyntax) **   <a name="TransferFamily-UpdateAgreement-request-AccessRole"></a>
Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the AWS Identity and Access Management role to use.
 **For AS2 connectors**
With AS2, you can send files by calling `StartFileTransfer` and specifying the file paths in the request parameter, `SendFilePaths`. We use the file’s parent directory (for example, for `--send-file-paths /bucket/dir/file.txt`, parent directory is `/bucket/dir/`) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the `AccessRole` needs to provide read and write access to the parent directory of the file location used in the `StartFileTransfer` request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with `StartFileTransfer`.
If you are using Basic authentication for your AS2 connector, the access role requires the `secretsmanager:GetSecretValue` permission for the secret. If the secret is encrypted using a customer-managed key instead of the AWS managed key in Secrets Manager, then the role also needs the `kms:Decrypt` permission for that key.
 **For SFTP connectors**
Make sure that the access role provides read and write access to the parent directory of the file location that's used in the `StartFileTransfer` request. Additionally, make sure that the role provides `secretsmanager:GetSecretValue` permission to AWS Secrets Manager.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*role/\S+`
Required: No

 ** [AgreementId](#API_UpdateAgreement_RequestSyntax) **   <a name="TransferFamily-UpdateAgreement-request-AgreementId"></a>
A unique identifier for the agreement. This identifier is returned when you create an agreement.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `a-([0-9a-f]{17})`
Required: Yes

 ** [BaseDirectory](#API_UpdateAgreement_RequestSyntax) **   <a name="TransferFamily-UpdateAgreement-request-BaseDirectory"></a>
To change the landing directory (folder) for files that are transferred, provide the bucket folder that you want to use; for example, `/amzn-s3-demo-bucket/home/mydirectory `.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(|/.*)`
Required: No

 ** [CustomDirectories](#API_UpdateAgreement_RequestSyntax) **   <a name="TransferFamily-UpdateAgreement-request-CustomDirectories"></a>
A `CustomDirectoriesType` structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.
+ Failed files
+ MDN files
+ Payload files
+ Status files
+ Temporary files
Type: [CustomDirectoriesType](API_CustomDirectoriesType.md) object
Required: No

 ** [Description](#API_UpdateAgreement_RequestSyntax) **   <a name="TransferFamily-UpdateAgreement-request-Description"></a>
To replace the existing description, provide a short description for the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\u0021-\u007E]+`
Required: No

 ** [EnforceMessageSigning](#API_UpdateAgreement_RequestSyntax) **   <a name="TransferFamily-UpdateAgreement-request-EnforceMessageSigning"></a>
 Determines whether or not unsigned messages from your trading partners will be accepted.
+  `ENABLED`: Transfer Family rejects unsigned messages from your trading partner.
+  `DISABLED` (default value): Transfer Family accepts unsigned messages from your trading partner.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [LocalProfileId](#API_UpdateAgreement_RequestSyntax) **   <a name="TransferFamily-UpdateAgreement-request-LocalProfileId"></a>
A unique identifier for the AS2 local profile.
To change the local profile identifier, provide a new value here.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `p-([0-9a-f]{17})`
Required: No

 ** [PartnerProfileId](#API_UpdateAgreement_RequestSyntax) **   <a name="TransferFamily-UpdateAgreement-request-PartnerProfileId"></a>
A unique identifier for the partner profile. To change the partner profile identifier, provide a new value here.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `p-([0-9a-f]{17})`
Required: No

 ** [PreserveFilename](#API_UpdateAgreement_RequestSyntax) **   <a name="TransferFamily-UpdateAgreement-request-PreserveFilename"></a>
 Determines whether or not Transfer Family appends a unique string of characters to the end of the AS2 message payload filename when saving it.
+  `ENABLED`: the filename provided by your trading parter is preserved when the file is saved.
+  `DISABLED` (default value): when Transfer Family saves the file, the filename is adjusted, as described in [File names and locations](https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html#file-names-as2).
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [ServerId](#API_UpdateAgreement_RequestSyntax) **   <a name="TransferFamily-UpdateAgreement-request-ServerId"></a>
A system-assigned unique identifier for a server instance. This is the specific server that the agreement uses.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-([0-9a-f]{17})`
Required: Yes

 ** [Status](#API_UpdateAgreement_RequestSyntax) **   <a name="TransferFamily-UpdateAgreement-request-Status"></a>
You can update the status for the agreement, either activating an inactive agreement or the reverse.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## Response Syntax
<a name="API_UpdateAgreement_ResponseSyntax"></a>

```
{
   "AgreementId": "string"
}
```

## Response Elements
<a name="API_UpdateAgreement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AgreementId](#API_UpdateAgreement_ResponseSyntax) **   <a name="TransferFamily-UpdateAgreement-response-AgreementId"></a>
A unique identifier for the agreement. This identifier is returned when you create an agreement.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `a-([0-9a-f]{17})`

## Errors
<a name="API_UpdateAgreement_Errors"></a>

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

## See Also
<a name="API_UpdateAgreement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/UpdateAgreement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/UpdateAgreement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/UpdateAgreement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/UpdateAgreement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/UpdateAgreement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/UpdateAgreement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/UpdateAgreement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/UpdateAgreement)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/UpdateAgreement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/UpdateAgreement)

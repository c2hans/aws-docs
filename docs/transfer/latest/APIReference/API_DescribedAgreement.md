---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedAgreement.html
---

# DescribedAgreement
<a name="API_DescribedAgreement"></a>

Describes the properties of an agreement.

## Contents
<a name="API_DescribedAgreement_Contents"></a>

 ** Arn **   <a name="TransferFamily-Type-DescribedAgreement-Arn"></a>
The unique Amazon Resource Name (ARN) for the agreement.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1600.
Pattern: `arn:\S+`
Required: Yes

 ** AccessRole **   <a name="TransferFamily-Type-DescribedAgreement-AccessRole"></a>
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

 ** AgreementId **   <a name="TransferFamily-Type-DescribedAgreement-AgreementId"></a>
A unique identifier for the agreement. This identifier is returned when you create an agreement.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `a-([0-9a-f]{17})`
Required: No

 ** BaseDirectory **   <a name="TransferFamily-Type-DescribedAgreement-BaseDirectory"></a>
The landing directory (folder) for files that are transferred by using the AS2 protocol.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(|/.*)`
Required: No

 ** CustomDirectories **   <a name="TransferFamily-Type-DescribedAgreement-CustomDirectories"></a>
A `CustomDirectoriesType` structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.
+ Failed files
+ MDN files
+ Payload files
+ Status files
+ Temporary files
Type: [CustomDirectoriesType](API_CustomDirectoriesType.md) object
Required: No

 ** Description **   <a name="TransferFamily-Type-DescribedAgreement-Description"></a>
The name or short description that's used to identify the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\u0021-\u007E]+`
Required: No

 ** EnforceMessageSigning **   <a name="TransferFamily-Type-DescribedAgreement-EnforceMessageSigning"></a>
 Determines whether or not unsigned messages from your trading partners will be accepted.
+  `ENABLED`: Transfer Family rejects unsigned messages from your trading partner.
+  `DISABLED` (default value): Transfer Family accepts unsigned messages from your trading partner.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** LocalProfileId **   <a name="TransferFamily-Type-DescribedAgreement-LocalProfileId"></a>
A unique identifier for the AS2 local profile.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `p-([0-9a-f]{17})`
Required: No

 ** PartnerProfileId **   <a name="TransferFamily-Type-DescribedAgreement-PartnerProfileId"></a>
A unique identifier for the partner profile used in the agreement.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `p-([0-9a-f]{17})`
Required: No

 ** PreserveFilename **   <a name="TransferFamily-Type-DescribedAgreement-PreserveFilename"></a>
 Determines whether or not Transfer Family appends a unique string of characters to the end of the AS2 message payload filename when saving it.
+  `ENABLED`: the filename provided by your trading parter is preserved when the file is saved.
+  `DISABLED` (default value): when Transfer Family saves the file, the filename is adjusted, as described in [File names and locations](https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html#file-names-as2).
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** ServerId **   <a name="TransferFamily-Type-DescribedAgreement-ServerId"></a>
A system-assigned unique identifier for a server instance. This identifier indicates the specific server that the agreement uses.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-([0-9a-f]{17})`
Required: No

 ** Status **   <a name="TransferFamily-Type-DescribedAgreement-Status"></a>
The current status of the agreement, either `ACTIVE` or `INACTIVE`.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** Tags **   <a name="TransferFamily-Type-DescribedAgreement-Tags"></a>
Key-value pairs that can be used to group and search for agreements.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_DescribedAgreement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedAgreement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedAgreement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedAgreement)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-transfer-agreement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Agreement
<a name="aws-resource-transfer-agreement"></a>

Creates an agreement. An agreement is a bilateral trading partner agreement, or partnership, between an AWS Transfer Family server and an AS2 process. The agreement defines the file and message transfer relationship between the server and the AS2 process. To define an agreement, Transfer Family combines a server, local profile, partner profile, certificate, and other attributes.

The partner is identified with the `PartnerProfileId`, and the AS2 process is identified with the `LocalProfileId`.

**Note**
Specify *either*`BaseDirectory` or `CustomDirectories`, but not both. Specifying both causes the command to fail.

## Syntax
<a name="aws-resource-transfer-agreement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-transfer-agreement-syntax.json"></a>

```
{
  "Type" : "AWS::Transfer::Agreement",
  "Properties" : {
      "[AccessRole](#cfn-transfer-agreement-accessrole)" : {{String}},
      "[BaseDirectory](#cfn-transfer-agreement-basedirectory)" : {{String}},
      "[CustomDirectories](#cfn-transfer-agreement-customdirectories)" : {{CustomDirectories}},
      "[Description](#cfn-transfer-agreement-description)" : {{String}},
      "[EnforceMessageSigning](#cfn-transfer-agreement-enforcemessagesigning)" : {{String}},
      "[LocalProfileId](#cfn-transfer-agreement-localprofileid)" : {{String}},
      "[PartnerProfileId](#cfn-transfer-agreement-partnerprofileid)" : {{String}},
      "[PreserveFilename](#cfn-transfer-agreement-preservefilename)" : {{String}},
      "[ServerId](#cfn-transfer-agreement-serverid)" : {{String}},
      "[Status](#cfn-transfer-agreement-status)" : {{String}},
      "[Tags](#cfn-transfer-agreement-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-transfer-agreement-syntax.yaml"></a>

```
Type: AWS::Transfer::Agreement
Properties:
  [AccessRole](#cfn-transfer-agreement-accessrole): {{String}}
  [BaseDirectory](#cfn-transfer-agreement-basedirectory): {{String}}
  [CustomDirectories](#cfn-transfer-agreement-customdirectories): {{
    CustomDirectories}}
  [Description](#cfn-transfer-agreement-description): {{String}}
  [EnforceMessageSigning](#cfn-transfer-agreement-enforcemessagesigning): {{String}}
  [LocalProfileId](#cfn-transfer-agreement-localprofileid): {{String}}
  [PartnerProfileId](#cfn-transfer-agreement-partnerprofileid): {{String}}
  [PreserveFilename](#cfn-transfer-agreement-preservefilename): {{String}}
  [ServerId](#cfn-transfer-agreement-serverid): {{String}}
  [Status](#cfn-transfer-agreement-status): {{String}}
  [Tags](#cfn-transfer-agreement-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-transfer-agreement-properties"></a>

`AccessRole`  <a name="cfn-transfer-agreement-accessrole"></a>
Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the AWS Identity and Access Management role to use.
 **For AS2 connectors**
With AS2, you can send files by calling `StartFileTransfer` and specifying the file paths in the request parameter, `SendFilePaths`. We use the file’s parent directory (for example, for `--send-file-paths /bucket/dir/file.txt`, parent directory is `/bucket/dir/`) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the `AccessRole` needs to provide read and write access to the parent directory of the file location used in the `StartFileTransfer` request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with `StartFileTransfer`.
If you are using Basic authentication for your AS2 connector, the access role requires the `secretsmanager:GetSecretValue` permission for the secret. If the secret is encrypted using a customer-managed key instead of the AWS managed key in Secrets Manager, then the role also needs the `kms:Decrypt` permission for that key.
 **For SFTP connectors**
Make sure that the access role provides read and write access to the parent directory of the file location that's used in the `StartFileTransfer` request. Additionally, make sure that the role provides `secretsmanager:GetSecretValue` permission to AWS Secrets Manager.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*role/.*`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaseDirectory`  <a name="cfn-transfer-agreement-basedirectory"></a>
The landing directory (folder) for files that are transferred by using the AS2 protocol.
*Required*: No
*Type*: String
*Pattern*: `^(|/.*)$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomDirectories`  <a name="cfn-transfer-agreement-customdirectories"></a>
A `CustomDirectoriesType` structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.
+ Failed files
+ MDN files
+ Payload files
+ Status files
+ Temporary files
*Required*: No
*Type*: [CustomDirectories](aws-properties-transfer-agreement-customdirectories.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-transfer-agreement-description"></a>
The name or short description that's used to identify the agreement.
*Required*: No
*Type*: String
*Pattern*: `^[\u0021-\u007E]+$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnforceMessageSigning`  <a name="cfn-transfer-agreement-enforcemessagesigning"></a>
 Determines whether or not unsigned messages from your trading partners will be accepted.
+ `ENABLED`: Transfer Family rejects unsigned messages from your trading partner.
+ `DISABLED` (default value): Transfer Family accepts unsigned messages from your trading partner.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalProfileId`  <a name="cfn-transfer-agreement-localprofileid"></a>
A unique identifier for the AS2 local profile.
*Required*: Yes
*Type*: String
*Pattern*: `^p-([0-9a-f]{17})$`
*Minimum*: `19`
*Maximum*: `19`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartnerProfileId`  <a name="cfn-transfer-agreement-partnerprofileid"></a>
A unique identifier for the partner profile used in the agreement.
*Required*: Yes
*Type*: String
*Pattern*: `^p-([0-9a-f]{17})$`
*Minimum*: `19`
*Maximum*: `19`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreserveFilename`  <a name="cfn-transfer-agreement-preservefilename"></a>
 Determines whether or not Transfer Family appends a unique string of characters to the end of the AS2 message payload filename when saving it.
+ `ENABLED`: the filename provided by your trading parter is preserved when the file is saved.
+ `DISABLED` (default value): when Transfer Family saves the file, the filename is adjusted, as described in [File names and locations](https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html#file-names-as2).
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerId`  <a name="cfn-transfer-agreement-serverid"></a>
A system-assigned unique identifier for a server instance. This identifier indicates the specific server that the agreement uses.
*Required*: Yes
*Type*: String
*Pattern*: `^s-([0-9a-f]{17})$`
*Minimum*: `19`
*Maximum*: `19`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Status`  <a name="cfn-transfer-agreement-status"></a>
The current status of the agreement, either `ACTIVE` or `INACTIVE`.
*Required*: No
*Type*: String
*Allowed values*: `ACTIVE | INACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-transfer-agreement-tags"></a>
Key-value pairs that can be used to group and search for agreements.
*Required*: No
*Type*: Array of [Tag](aws-properties-transfer-agreement-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-transfer-agreement-return-values"></a>

### Ref
<a name="aws-resource-transfer-agreement-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-transfer-agreement-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-transfer-agreement-return-values-fn--getatt-fn--getatt"></a>

`AgreementId`  <a name="AgreementId-fn::getatt"></a>
The unique identifier for the AS2 agreement, returned after the API call succeeds.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

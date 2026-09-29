---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-agreement-customdirectories.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Agreement CustomDirectories
<a name="aws-properties-transfer-agreement-customdirectories"></a>

A `CustomDirectoriesType` structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.
+ Failed files
+ MDN files
+ Payload files
+ Status files
+ Temporary files

## Syntax
<a name="aws-properties-transfer-agreement-customdirectories-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-agreement-customdirectories-syntax.json"></a>

```
{
  "[FailedFilesDirectory](#cfn-transfer-agreement-customdirectories-failedfilesdirectory)" : {{String}},
  "[MdnFilesDirectory](#cfn-transfer-agreement-customdirectories-mdnfilesdirectory)" : {{String}},
  "[PayloadFilesDirectory](#cfn-transfer-agreement-customdirectories-payloadfilesdirectory)" : {{String}},
  "[StatusFilesDirectory](#cfn-transfer-agreement-customdirectories-statusfilesdirectory)" : {{String}},
  "[TemporaryFilesDirectory](#cfn-transfer-agreement-customdirectories-temporaryfilesdirectory)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-agreement-customdirectories-syntax.yaml"></a>

```
  [FailedFilesDirectory](#cfn-transfer-agreement-customdirectories-failedfilesdirectory): {{String}}
  [MdnFilesDirectory](#cfn-transfer-agreement-customdirectories-mdnfilesdirectory): {{String}}
  [PayloadFilesDirectory](#cfn-transfer-agreement-customdirectories-payloadfilesdirectory): {{String}}
  [StatusFilesDirectory](#cfn-transfer-agreement-customdirectories-statusfilesdirectory): {{String}}
  [TemporaryFilesDirectory](#cfn-transfer-agreement-customdirectories-temporaryfilesdirectory): {{String}}
```

## Properties
<a name="aws-properties-transfer-agreement-customdirectories-properties"></a>

`FailedFilesDirectory`  <a name="cfn-transfer-agreement-customdirectories-failedfilesdirectory"></a>
Specifies a location to store failed AS2 message files.
*Required*: Yes
*Type*: String
*Pattern*: `(|/.*)`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MdnFilesDirectory`  <a name="cfn-transfer-agreement-customdirectories-mdnfilesdirectory"></a>
Specifies a location to store MDN files.
*Required*: Yes
*Type*: String
*Pattern*: `(|/.*)`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PayloadFilesDirectory`  <a name="cfn-transfer-agreement-customdirectories-payloadfilesdirectory"></a>
Specifies a location to store the payload for AS2 message files.
*Required*: Yes
*Type*: String
*Pattern*: `(|/.*)`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusFilesDirectory`  <a name="cfn-transfer-agreement-customdirectories-statusfilesdirectory"></a>
Specifies a location to store AS2 status messages.
*Required*: Yes
*Type*: String
*Pattern*: `(|/.*)`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemporaryFilesDirectory`  <a name="cfn-transfer-agreement-customdirectories-temporaryfilesdirectory"></a>
Specifies a location to store temporary AS2 message files.
*Required*: Yes
*Type*: String
*Pattern*: `(|/.*)`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

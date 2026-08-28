---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Collaboration DataEncryptionMetadata
<a name="aws-properties-cleanrooms-collaboration-dataencryptionmetadata"></a>

The settings for client-side encryption for cryptographic computing.

## Syntax
<a name="aws-properties-cleanrooms-collaboration-dataencryptionmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-collaboration-dataencryptionmetadata-syntax.json"></a>

```
{
  "[AllowCleartext](#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowcleartext)" : {{Boolean}},
  "[AllowDuplicates](#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowduplicates)" : {{Boolean}},
  "[AllowJoinsOnColumnsWithDifferentNames](#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowjoinsoncolumnswithdifferentnames)" : {{Boolean}},
  "[PreserveNulls](#cfn-cleanrooms-collaboration-dataencryptionmetadata-preservenulls)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cleanrooms-collaboration-dataencryptionmetadata-syntax.yaml"></a>

```
  [AllowCleartext](#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowcleartext): {{Boolean}}
  [AllowDuplicates](#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowduplicates): {{Boolean}}
  [AllowJoinsOnColumnsWithDifferentNames](#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowjoinsoncolumnswithdifferentnames): {{Boolean}}
  [PreserveNulls](#cfn-cleanrooms-collaboration-dataencryptionmetadata-preservenulls): {{Boolean}}
```

## Properties
<a name="aws-properties-cleanrooms-collaboration-dataencryptionmetadata-properties"></a>

`AllowCleartext`  <a name="cfn-cleanrooms-collaboration-dataencryptionmetadata-allowcleartext"></a>
Indicates whether encrypted tables can contain cleartext data (`TRUE`) or are to cryptographically process every column (`FALSE`).
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AllowDuplicates`  <a name="cfn-cleanrooms-collaboration-dataencryptionmetadata-allowduplicates"></a>
Indicates whether Fingerprint columns can contain duplicate entries (`TRUE`) or are to contain only non-repeated values (`FALSE`).
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AllowJoinsOnColumnsWithDifferentNames`  <a name="cfn-cleanrooms-collaboration-dataencryptionmetadata-allowjoinsoncolumnswithdifferentnames"></a>
Indicates whether Fingerprint columns can be joined on any other Fingerprint column with a different name (`TRUE`) or can only be joined on Fingerprint columns of the same name (`FALSE`).
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreserveNulls`  <a name="cfn-cleanrooms-collaboration-dataencryptionmetadata-preservenulls"></a>
Indicates whether NULL values are to be copied as NULL to encrypted tables (`TRUE`) or cryptographically processed (`FALSE`).
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

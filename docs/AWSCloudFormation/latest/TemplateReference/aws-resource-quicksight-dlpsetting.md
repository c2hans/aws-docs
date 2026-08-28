---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-dlpsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DLPSetting
<a name="aws-resource-quicksight-dlpsetting"></a>

<a name="aws-resource-quicksight-dlpsetting-description"></a>The `AWS::QuickSight::DLPSetting` resource Property description not available. for QuickSight.

## Syntax
<a name="aws-resource-quicksight-dlpsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-dlpsetting-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::DLPSetting",
  "Properties" : {
      "[AwsAccountId](#cfn-quicksight-dlpsetting-awsaccountid)" : {{String}},
      "[DlpSettingId](#cfn-quicksight-dlpsetting-dlpsettingid)" : {{String}},
      "[Enabled](#cfn-quicksight-dlpsetting-enabled)" : {{Boolean}},
      "[Name](#cfn-quicksight-dlpsetting-name)" : {{String}},
      "[ProviderConfig](#cfn-quicksight-dlpsetting-providerconfig)" : {{ProviderConfig}},
      "[ProviderOutageAction](#cfn-quicksight-dlpsetting-provideroutageaction)" : {{String}},
      "[ProviderType](#cfn-quicksight-dlpsetting-providertype)" : {{String}},
      "[Tags](#cfn-quicksight-dlpsetting-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-dlpsetting-syntax.yaml"></a>

```
Type: AWS::QuickSight::DLPSetting
Properties:
  [AwsAccountId](#cfn-quicksight-dlpsetting-awsaccountid): {{String}}
  [DlpSettingId](#cfn-quicksight-dlpsetting-dlpsettingid): {{String}}
  [Enabled](#cfn-quicksight-dlpsetting-enabled): {{Boolean}}
  [Name](#cfn-quicksight-dlpsetting-name): {{String}}
  [ProviderConfig](#cfn-quicksight-dlpsetting-providerconfig): {{
    ProviderConfig}}
  [ProviderOutageAction](#cfn-quicksight-dlpsetting-provideroutageaction): {{String}}
  [ProviderType](#cfn-quicksight-dlpsetting-providertype): {{String}}
  [Tags](#cfn-quicksight-dlpsetting-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-quicksight-dlpsetting-properties"></a>

`AwsAccountId`  <a name="cfn-quicksight-dlpsetting-awsaccountid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DlpSettingId`  <a name="cfn-quicksight-dlpsetting-dlpsettingid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-_]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Enabled`  <a name="cfn-quicksight-dlpsetting-enabled"></a>
Property description not available.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dlpsetting-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9](?:[\w- &]*[A-Za-z0-9])?$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderConfig`  <a name="cfn-quicksight-dlpsetting-providerconfig"></a>
Property description not available.
*Required*: Yes
*Type*: [ProviderConfig](aws-properties-quicksight-dlpsetting-providerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderOutageAction`  <a name="cfn-quicksight-dlpsetting-provideroutageaction"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ALLOW | WARN | BLOCK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderType`  <a name="cfn-quicksight-dlpsetting-providertype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `MICROSOFT_PURVIEW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-quicksight-dlpsetting-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-dlpsetting-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-dlpsetting-return-values"></a>

### Ref
<a name="aws-resource-quicksight-dlpsetting-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-dlpsetting-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-dlpsetting-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

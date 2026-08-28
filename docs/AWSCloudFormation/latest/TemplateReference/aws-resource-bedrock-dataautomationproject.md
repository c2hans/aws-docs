---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-dataautomationproject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject
<a name="aws-resource-bedrock-dataautomationproject"></a>

A data automation project.

## Syntax
<a name="aws-resource-bedrock-dataautomationproject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-dataautomationproject-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::DataAutomationProject",
  "Properties" : {
      "[CustomOutputConfiguration](#cfn-bedrock-dataautomationproject-customoutputconfiguration)" : {{CustomOutputConfiguration}},
      "[KmsEncryptionContext](#cfn-bedrock-dataautomationproject-kmsencryptioncontext)" : {{{{{Key}}: {{Value}}, ...}}},
      "[KmsKeyId](#cfn-bedrock-dataautomationproject-kmskeyid)" : {{String}},
      "[OverrideConfiguration](#cfn-bedrock-dataautomationproject-overrideconfiguration)" : {{OverrideConfiguration}},
      "[ProjectDescription](#cfn-bedrock-dataautomationproject-projectdescription)" : {{String}},
      "[ProjectName](#cfn-bedrock-dataautomationproject-projectname)" : {{String}},
      "[ProjectType](#cfn-bedrock-dataautomationproject-projecttype)" : {{String}},
      "[StandardOutputConfiguration](#cfn-bedrock-dataautomationproject-standardoutputconfiguration)" : {{StandardOutputConfiguration}},
      "[Tags](#cfn-bedrock-dataautomationproject-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-dataautomationproject-syntax.yaml"></a>

```
Type: AWS::Bedrock::DataAutomationProject
Properties:
  [CustomOutputConfiguration](#cfn-bedrock-dataautomationproject-customoutputconfiguration): {{
    CustomOutputConfiguration}}
  [KmsEncryptionContext](#cfn-bedrock-dataautomationproject-kmsencryptioncontext): {{
    {{Key}}: {{Value}}}}
  [KmsKeyId](#cfn-bedrock-dataautomationproject-kmskeyid): {{String}}
  [OverrideConfiguration](#cfn-bedrock-dataautomationproject-overrideconfiguration): {{
    OverrideConfiguration}}
  [ProjectDescription](#cfn-bedrock-dataautomationproject-projectdescription): {{String}}
  [ProjectName](#cfn-bedrock-dataautomationproject-projectname): {{String}}
  [ProjectType](#cfn-bedrock-dataautomationproject-projecttype): {{String}}
  [StandardOutputConfiguration](#cfn-bedrock-dataautomationproject-standardoutputconfiguration): {{
    StandardOutputConfiguration}}
  [Tags](#cfn-bedrock-dataautomationproject-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrock-dataautomationproject-properties"></a>

`CustomOutputConfiguration`  <a name="cfn-bedrock-dataautomationproject-customoutputconfiguration"></a>
Blueprints to apply to objects processed by the project.
*Required*: No
*Type*: [CustomOutputConfiguration](aws-properties-bedrock-dataautomationproject-customoutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsEncryptionContext`  <a name="cfn-bedrock-dataautomationproject-kmsencryptioncontext"></a>
The AWS KMS encryption context to use for encryption.
*Required*: No
*Type*: Object of String
*Pattern*: `^.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-bedrock-dataautomationproject-kmskeyid"></a>
The AWS KMS key to use for encryption.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverrideConfiguration`  <a name="cfn-bedrock-dataautomationproject-overrideconfiguration"></a>
Additional settings for the project.
*Required*: No
*Type*: [OverrideConfiguration](aws-properties-bedrock-dataautomationproject-overrideconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectDescription`  <a name="cfn-bedrock-dataautomationproject-projectdescription"></a>
The project's description.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectName`  <a name="cfn-bedrock-dataautomationproject-projectname"></a>
The project's name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProjectType`  <a name="cfn-bedrock-dataautomationproject-projecttype"></a>
The type of bedrock data automation API that is compatible with this project.
*Required*: No
*Type*: String
*Allowed values*: `ASYNC | SYNC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StandardOutputConfiguration`  <a name="cfn-bedrock-dataautomationproject-standardoutputconfiguration"></a>
The project's standard output configuration.
*Required*: No
*Type*: [StandardOutputConfiguration](aws-properties-bedrock-dataautomationproject-standardoutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrock-dataautomationproject-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrock-dataautomationproject-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-dataautomationproject-return-values"></a>

### Ref
<a name="aws-resource-bedrock-dataautomationproject-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrock-dataautomationproject-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-dataautomationproject-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the project was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
When the project was last updated.

`ProjectArn`  <a name="ProjectArn-fn::getatt"></a>
The project's ARN.

`ProjectStage`  <a name="ProjectStage-fn::getatt"></a>
The project's stage.

`Status`  <a name="Status-fn::getatt"></a>
The project's status.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

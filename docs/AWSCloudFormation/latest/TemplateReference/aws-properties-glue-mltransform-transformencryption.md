---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-mltransform-transformencryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::MLTransform TransformEncryption
<a name="aws-properties-glue-mltransform-transformencryption"></a>

The encryption-at-rest settings of the transform that apply to accessing user data. Machine learning transforms can access user data encrypted in Amazon S3 using KMS.

Additionally, imported labels and trained transforms can now be encrypted using a customer provided KMS key.

## Syntax
<a name="aws-properties-glue-mltransform-transformencryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-mltransform-transformencryption-syntax.json"></a>

```
{
  "[MLUserDataEncryption](#cfn-glue-mltransform-transformencryption-mluserdataencryption)" : {{MLUserDataEncryption}},
  "[TaskRunSecurityConfigurationName](#cfn-glue-mltransform-transformencryption-taskrunsecurityconfigurationname)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-mltransform-transformencryption-syntax.yaml"></a>

```
  [MLUserDataEncryption](#cfn-glue-mltransform-transformencryption-mluserdataencryption): {{
    MLUserDataEncryption}}
  [TaskRunSecurityConfigurationName](#cfn-glue-mltransform-transformencryption-taskrunsecurityconfigurationname): {{String}}
```

## Properties
<a name="aws-properties-glue-mltransform-transformencryption-properties"></a>

`MLUserDataEncryption`  <a name="cfn-glue-mltransform-transformencryption-mluserdataencryption"></a>
The encryption-at-rest settings of the transform that apply to accessing user data.
*Required*: No
*Type*: [MLUserDataEncryption](aws-properties-glue-mltransform-mluserdataencryption.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TaskRunSecurityConfigurationName`  <a name="cfn-glue-mltransform-transformencryption-taskrunsecurityconfigurationname"></a>
The name of the security configuration.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-bootstrapactionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster BootstrapActionConfig
<a name="aws-properties-emr-cluster-bootstrapactionconfig"></a>

`BootstrapActionConfig` is a property of `AWS::EMR::Cluster` that can be used to run bootstrap actions on EMR clusters. You can use a bootstrap action to install software and configure EC2 instances for all cluster nodes before EMR installs and configures open-source big data applications on cluster instances. For more information, see [Create Bootstrap Actions to Install Additional Software](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-bootstrap.html) in the *Amazon EMR Management Guide*.

## Syntax
<a name="aws-properties-emr-cluster-bootstrapactionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-bootstrapactionconfig-syntax.json"></a>

```
{
  "[Name](#cfn-emr-cluster-bootstrapactionconfig-name)" : {{String}},
  "[ScriptBootstrapAction](#cfn-emr-cluster-bootstrapactionconfig-scriptbootstrapaction)" : {{ScriptBootstrapActionConfig}}
}
```

### YAML
<a name="aws-properties-emr-cluster-bootstrapactionconfig-syntax.yaml"></a>

```
  [Name](#cfn-emr-cluster-bootstrapactionconfig-name): {{String}}
  [ScriptBootstrapAction](#cfn-emr-cluster-bootstrapactionconfig-scriptbootstrapaction): {{
    ScriptBootstrapActionConfig}}
```

## Properties
<a name="aws-properties-emr-cluster-bootstrapactionconfig-properties"></a>

`Name`  <a name="cfn-emr-cluster-bootstrapactionconfig-name"></a>
The name of the bootstrap action.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScriptBootstrapAction`  <a name="cfn-emr-cluster-bootstrapactionconfig-scriptbootstrapaction"></a>
The script run by the bootstrap action.
*Required*: Yes
*Type*: [ScriptBootstrapActionConfig](aws-properties-emr-cluster-scriptbootstrapactionconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

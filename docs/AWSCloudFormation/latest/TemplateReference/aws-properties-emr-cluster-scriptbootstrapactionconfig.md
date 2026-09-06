---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-scriptbootstrapactionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster ScriptBootstrapActionConfig
<a name="aws-properties-emr-cluster-scriptbootstrapactionconfig"></a>

`ScriptBootstrapActionConfig` is a subproperty of the `BootstrapActionConfig` property type. `ScriptBootstrapActionConfig` specifies the arguments and location of the bootstrap script for EMR to run on all cluster nodes before it installs open-source big data applications on them.

## Syntax
<a name="aws-properties-emr-cluster-scriptbootstrapactionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-scriptbootstrapactionconfig-syntax.json"></a>

```
{
  "[Args](#cfn-emr-cluster-scriptbootstrapactionconfig-args)" : {{[ String, ... ]}},
  "[Path](#cfn-emr-cluster-scriptbootstrapactionconfig-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-cluster-scriptbootstrapactionconfig-syntax.yaml"></a>

```
  [Args](#cfn-emr-cluster-scriptbootstrapactionconfig-args): {{
    - String}}
  [Path](#cfn-emr-cluster-scriptbootstrapactionconfig-path): {{String}}
```

## Properties
<a name="aws-properties-emr-cluster-scriptbootstrapactionconfig-properties"></a>

`Args`  <a name="cfn-emr-cluster-scriptbootstrapactionconfig-args"></a>
A list of command line arguments to pass to the bootstrap action script.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Path`  <a name="cfn-emr-cluster-scriptbootstrapactionconfig-path"></a>
Location in Amazon S3 of the script to run during a bootstrap action.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-function-customoutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Function CustomOutputConfiguration
<a name="aws-properties-mediatailor-function-customoutputconfiguration"></a>

The configuration for a `CUSTOM_OUTPUT` function. MediaTailor evaluates the output expressions against the current session state and commits the results as output bindings. `CUSTOM_OUTPUT` functions do not make external calls. For more information, see [CUSTOM\_OUTPUT](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types-custom-output.html) in the *MediaTailor User Guide*.

## Syntax
<a name="aws-properties-mediatailor-function-customoutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-function-customoutputconfiguration-syntax.json"></a>

```
{
  "[Output](#cfn-mediatailor-function-customoutputconfiguration-output)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Runtime](#cfn-mediatailor-function-customoutputconfiguration-runtime)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-function-customoutputconfiguration-syntax.yaml"></a>

```
  [Output](#cfn-mediatailor-function-customoutputconfiguration-output): {{
    {{Key}}: {{Value}}}}
  [Runtime](#cfn-mediatailor-function-customoutputconfiguration-runtime): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-function-customoutputconfiguration-properties"></a>

`Output`  <a name="cfn-mediatailor-function-customoutputconfiguration-output"></a>
A map of output bindings. Each key is a namespaced output path (such as `player_params.device_type` or `temp.variant`), and each value is an expression that MediaTailor evaluates at runtime against the current session state. For more information about expression syntax, see [JSONata expression reference](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-jsonata.html) in the *MediaTailor User Guide*.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Runtime`  <a name="cfn-mediatailor-function-customoutputconfiguration-runtime"></a>
The expression language used to evaluate expressions in the function configuration. Set this to `JSONata`.
*Required*: Yes
*Type*: String
*Allowed values*: `JSONATA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

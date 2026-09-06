---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-function-sequentialexecutorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Function SequentialExecutorConfiguration
<a name="aws-properties-mediatailor-function-sequentialexecutorconfiguration"></a>

The configuration for a `SEQUENTIAL_EXECUTOR` function. A `SEQUENTIAL_EXECUTOR` runs a sequence of child functions in order, passing data between steps through temporary data. For more information, see [SEQUENTIAL\_EXECUTOR](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types-sequential-executor.html) in the *MediaTailor User Guide*.

## Syntax
<a name="aws-properties-mediatailor-function-sequentialexecutorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-function-sequentialexecutorconfiguration-syntax.json"></a>

```
{
  "[FunctionList](#cfn-mediatailor-function-sequentialexecutorconfiguration-functionlist)" : {{[ FunctionRef, ... ]}},
  "[Output](#cfn-mediatailor-function-sequentialexecutorconfiguration-output)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Runtime](#cfn-mediatailor-function-sequentialexecutorconfiguration-runtime)" : {{String}},
  "[TimeoutMilliseconds](#cfn-mediatailor-function-sequentialexecutorconfiguration-timeoutmilliseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediatailor-function-sequentialexecutorconfiguration-syntax.yaml"></a>

```
  [FunctionList](#cfn-mediatailor-function-sequentialexecutorconfiguration-functionlist): {{
    - FunctionRef}}
  [Output](#cfn-mediatailor-function-sequentialexecutorconfiguration-output): {{
    {{Key}}: {{Value}}}}
  [Runtime](#cfn-mediatailor-function-sequentialexecutorconfiguration-runtime): {{String}}
  [TimeoutMilliseconds](#cfn-mediatailor-function-sequentialexecutorconfiguration-timeoutmilliseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediatailor-function-sequentialexecutorconfiguration-properties"></a>

`FunctionList`  <a name="cfn-mediatailor-function-sequentialexecutorconfiguration-functionlist"></a>
An ordered list of 1 to 10 steps. Each step specifies a child function to execute and an optional run condition expression that controls whether the step runs. MediaTailor executes steps in order, passing data between steps through temporary data.
*Required*: Yes
*Type*: Array of [FunctionRef](aws-properties-mediatailor-function-functionref.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Output`  <a name="cfn-mediatailor-function-sequentialexecutorconfiguration-output"></a>
An optional map of output bindings that controls which bindings the sequence commits to the session state after all steps complete. If omitted, MediaTailor commits all accumulated output bindings from all child steps.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Runtime`  <a name="cfn-mediatailor-function-sequentialexecutorconfiguration-runtime"></a>
The expression language used to evaluate expressions in the function configuration. Set this to `JSONata`.
*Required*: Yes
*Type*: String
*Allowed values*: `JSONATA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMilliseconds`  <a name="cfn-mediatailor-function-sequentialexecutorconfiguration-timeoutmilliseconds"></a>
The maximum time, in milliseconds, for the entire sequence to complete. This timeout covers all steps, including any HTTP calls made by child functions. If the sequence exceeds this timeout, MediaTailor discards all output from the sequence and proceeds with default behavior.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

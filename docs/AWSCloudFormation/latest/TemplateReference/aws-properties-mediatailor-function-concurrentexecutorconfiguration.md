---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-function-concurrentexecutorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Function ConcurrentExecutorConfiguration
<a name="aws-properties-mediatailor-function-concurrentexecutorconfiguration"></a>

The configuration for a `CONCURRENT_EXECUTOR` function. A `CONCURRENT_EXECUTOR` runs a set of child functions in parallel, up to a maximum concurrency, and combines their output when all functions complete. For more information about functions, see [Working with functions](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the *MediaTailor User Guide*.

## Syntax
<a name="aws-properties-mediatailor-function-concurrentexecutorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-function-concurrentexecutorconfiguration-syntax.json"></a>

```
{
  "[FunctionList](#cfn-mediatailor-function-concurrentexecutorconfiguration-functionlist)" : {{[ FunctionRef, ... ]}},
  "[MaxConcurrency](#cfn-mediatailor-function-concurrentexecutorconfiguration-maxconcurrency)" : {{Integer}},
  "[Output](#cfn-mediatailor-function-concurrentexecutorconfiguration-output)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Runtime](#cfn-mediatailor-function-concurrentexecutorconfiguration-runtime)" : {{String}},
  "[TimeoutMilliseconds](#cfn-mediatailor-function-concurrentexecutorconfiguration-timeoutmilliseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediatailor-function-concurrentexecutorconfiguration-syntax.yaml"></a>

```
  [FunctionList](#cfn-mediatailor-function-concurrentexecutorconfiguration-functionlist): {{
    - FunctionRef}}
  [MaxConcurrency](#cfn-mediatailor-function-concurrentexecutorconfiguration-maxconcurrency): {{Integer}}
  [Output](#cfn-mediatailor-function-concurrentexecutorconfiguration-output): {{
    {{Key}}: {{Value}}}}
  [Runtime](#cfn-mediatailor-function-concurrentexecutorconfiguration-runtime): {{String}}
  [TimeoutMilliseconds](#cfn-mediatailor-function-concurrentexecutorconfiguration-timeoutmilliseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediatailor-function-concurrentexecutorconfiguration-properties"></a>

`FunctionList`  <a name="cfn-mediatailor-function-concurrentexecutorconfiguration-functionlist"></a>
The list of child functions that MediaTailor runs in parallel. Each entry specifies a child function to execute and an optional run condition expression that controls whether the function runs.
*Required*: Yes
*Type*: Array of [FunctionRef](aws-properties-mediatailor-function-functionref.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxConcurrency`  <a name="cfn-mediatailor-function-concurrentexecutorconfiguration-maxconcurrency"></a>
The maximum number of child functions that MediaTailor runs simultaneously. When the list contains more functions than `MaxConcurrency`, MediaTailor starts additional functions as running ones complete, so that no more than `MaxConcurrency` functions run at the same time.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Output`  <a name="cfn-mediatailor-function-concurrentexecutorconfiguration-output"></a>
A map of output bindings that controls which bindings the executor commits to the session state after all child functions complete. Each key is a namespaced output path, and each value is an expression that MediaTailor evaluates against the combined results of the child functions.
*Required*: Yes
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Runtime`  <a name="cfn-mediatailor-function-concurrentexecutorconfiguration-runtime"></a>
The expression language used to evaluate expressions in the function configuration. Set this to `JSONata`.
*Required*: Yes
*Type*: String
*Allowed values*: `JSONATA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMilliseconds`  <a name="cfn-mediatailor-function-concurrentexecutorconfiguration-timeoutmilliseconds"></a>
The maximum time, in milliseconds, for all child functions to complete. This timeout covers every function in the list, including any HTTP calls the child functions make. If the executor exceeds this timeout, MediaTailor discards all output from the executor and proceeds with default behavior.
*Required*: Yes
*Type*: Integer
*Minimum*: `100`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

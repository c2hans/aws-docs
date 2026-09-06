---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-computenodegroup-nodelifecyclescript.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::ComputeNodeGroup NodeLifecycleScript
<a name="aws-properties-pcs-computenodegroup-nodelifecyclescript"></a>

A script to run during a compute node lifecycle stage.

## Syntax
<a name="aws-properties-pcs-computenodegroup-nodelifecyclescript-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-computenodegroup-nodelifecyclescript-syntax.json"></a>

```
{
  "[Arguments](#cfn-pcs-computenodegroup-nodelifecyclescript-arguments)" : {{[ String, ... ]}},
  "[ExecutionPolicy](#cfn-pcs-computenodegroup-nodelifecyclescript-executionpolicy)" : {{String}},
  "[Name](#cfn-pcs-computenodegroup-nodelifecyclescript-name)" : {{String}},
  "[OnError](#cfn-pcs-computenodegroup-nodelifecyclescript-onerror)" : {{String}},
  "[ScriptSource](#cfn-pcs-computenodegroup-nodelifecyclescript-scriptsource)" : {{ScriptSource}}
}
```

### YAML
<a name="aws-properties-pcs-computenodegroup-nodelifecyclescript-syntax.yaml"></a>

```
  [Arguments](#cfn-pcs-computenodegroup-nodelifecyclescript-arguments): {{
    - String}}
  [ExecutionPolicy](#cfn-pcs-computenodegroup-nodelifecyclescript-executionpolicy): {{String}}
  [Name](#cfn-pcs-computenodegroup-nodelifecyclescript-name): {{String}}
  [OnError](#cfn-pcs-computenodegroup-nodelifecyclescript-onerror): {{String}}
  [ScriptSource](#cfn-pcs-computenodegroup-nodelifecyclescript-scriptsource): {{
    ScriptSource}}
```

## Properties
<a name="aws-properties-pcs-computenodegroup-nodelifecyclescript-properties"></a>

`Arguments`  <a name="cfn-pcs-computenodegroup-nodelifecyclescript-arguments"></a>
The command-line arguments to pass to the script. You can specify up to 20 arguments, and each argument can be up to 256 characters long.
*Required*: No
*Type*: Array of String
*Maximum*: `256 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionPolicy`  <a name="cfn-pcs-computenodegroup-nodelifecyclescript-executionpolicy"></a>
The policy that determines when the script runs. The default value is `FIRST_BOOT_ONLY`. Valid values:
+ `FIRST_BOOT_ONLY` – Runs the script only the first time the compute node boots.
+ `EVERY_BOOT` – Runs the script every time the compute node boots, including reboots.
*Required*: No
*Type*: String
*Allowed values*: `FIRST_BOOT_ONLY | EVERY_BOOT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-pcs-computenodegroup-nodelifecyclescript-name"></a>
A unique name for the script. The name can be up to 64 characters long. Valid characters are letters, numbers, spaces, underscores (`_`), and hyphens (`-`). The first character must be a letter or a number.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9 _-]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnError`  <a name="cfn-pcs-computenodegroup-nodelifecyclescript-onerror"></a>
The behavior when the script fails. The default value is `TERMINATE`. Valid values:
+ `TERMINATE` – Terminates the compute node.
+ `STOP_SEQUENCE` – Stops running subsequent scripts in the sequence but doesn't terminate the compute node.
+ `CONTINUE` – Ignores the error and continues running the next script.
*Required*: No
*Type*: String
*Allowed values*: `TERMINATE | STOP_SEQUENCE | CONTINUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScriptSource`  <a name="cfn-pcs-computenodegroup-nodelifecyclescript-scriptsource"></a>
The source location and integrity information for the script.
*Required*: Yes
*Type*: [ScriptSource](aws-properties-pcs-computenodegroup-scriptsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

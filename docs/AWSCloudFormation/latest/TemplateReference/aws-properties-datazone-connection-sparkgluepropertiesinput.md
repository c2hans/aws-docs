---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-sparkgluepropertiesinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection SparkGluePropertiesInput
<a name="aws-properties-datazone-connection-sparkgluepropertiesinput"></a>

The Spark AWS Glue properties.

## Syntax
<a name="aws-properties-datazone-connection-sparkgluepropertiesinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-sparkgluepropertiesinput-syntax.json"></a>

```
{
  "[AdditionalArgs](#cfn-datazone-connection-sparkgluepropertiesinput-additionalargs)" : {{SparkGlueArgs}},
  "[GlueConnectionName](#cfn-datazone-connection-sparkgluepropertiesinput-glueconnectionname)" : {{String}},
  "[GlueVersion](#cfn-datazone-connection-sparkgluepropertiesinput-glueversion)" : {{String}},
  "[IdleTimeout](#cfn-datazone-connection-sparkgluepropertiesinput-idletimeout)" : {{Number}},
  "[JavaVirtualEnv](#cfn-datazone-connection-sparkgluepropertiesinput-javavirtualenv)" : {{String}},
  "[NumberOfWorkers](#cfn-datazone-connection-sparkgluepropertiesinput-numberofworkers)" : {{Number}},
  "[PythonVirtualEnv](#cfn-datazone-connection-sparkgluepropertiesinput-pythonvirtualenv)" : {{String}},
  "[WorkerType](#cfn-datazone-connection-sparkgluepropertiesinput-workertype)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-sparkgluepropertiesinput-syntax.yaml"></a>

```
  [AdditionalArgs](#cfn-datazone-connection-sparkgluepropertiesinput-additionalargs): {{
    SparkGlueArgs}}
  [GlueConnectionName](#cfn-datazone-connection-sparkgluepropertiesinput-glueconnectionname): {{String}}
  [GlueVersion](#cfn-datazone-connection-sparkgluepropertiesinput-glueversion): {{String}}
  [IdleTimeout](#cfn-datazone-connection-sparkgluepropertiesinput-idletimeout): {{Number}}
  [JavaVirtualEnv](#cfn-datazone-connection-sparkgluepropertiesinput-javavirtualenv): {{String}}
  [NumberOfWorkers](#cfn-datazone-connection-sparkgluepropertiesinput-numberofworkers): {{
    Number}}
  [PythonVirtualEnv](#cfn-datazone-connection-sparkgluepropertiesinput-pythonvirtualenv): {{String}}
  [WorkerType](#cfn-datazone-connection-sparkgluepropertiesinput-workertype): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-sparkgluepropertiesinput-properties"></a>

`AdditionalArgs`  <a name="cfn-datazone-connection-sparkgluepropertiesinput-additionalargs"></a>
The additional args in the Spark AWS Glue properties.
*Required*: No
*Type*: [SparkGlueArgs](aws-properties-datazone-connection-sparkglueargs.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlueConnectionName`  <a name="cfn-datazone-connection-sparkgluepropertiesinput-glueconnectionname"></a>
The AWS Glue connection name in the Spark AWS Glue properties. Specify either `glueConnectionName` or `glueConnectionNames`, but not both.
*Required*: No
*Type*: String
*Pattern*: `^[\S]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlueVersion`  <a name="cfn-datazone-connection-sparkgluepropertiesinput-glueversion"></a>
The AWS Glue version in the Spark AWS Glue properties.
*Required*: No
*Type*: String
*Pattern*: `^\w+\.\w+$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdleTimeout`  <a name="cfn-datazone-connection-sparkgluepropertiesinput-idletimeout"></a>
The idle timeout in the Spark AWS Glue properties.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `3000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JavaVirtualEnv`  <a name="cfn-datazone-connection-sparkgluepropertiesinput-javavirtualenv"></a>
The Java virtual env in the Spark AWS Glue properties.
*Required*: No
*Type*: String
*Pattern*: `^[\S]*$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberOfWorkers`  <a name="cfn-datazone-connection-sparkgluepropertiesinput-numberofworkers"></a>
The number of workers in the Spark AWS Glue properties.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PythonVirtualEnv`  <a name="cfn-datazone-connection-sparkgluepropertiesinput-pythonvirtualenv"></a>
The Python virtual env in the Spark AWS Glue properties.
*Required*: No
*Type*: String
*Pattern*: `^[\S]*$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkerType`  <a name="cfn-datazone-connection-sparkgluepropertiesinput-workertype"></a>
The worker type in the Spark AWS Glue properties.
*Required*: No
*Type*: String
*Pattern*: `^[G|Z].*$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

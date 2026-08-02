---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-hadoopjarstepconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster HadoopJarStepConfig
<a name="aws-properties-emr-cluster-hadoopjarstepconfig"></a>

The `HadoopJarStepConfig` property type specifies a job flow step consisting of a JAR file whose main function will be executed. The main function submits a job for the cluster to execute as a step on the master node, and then waits for the job to finish or fail before executing subsequent steps.

## Syntax
<a name="aws-properties-emr-cluster-hadoopjarstepconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-hadoopjarstepconfig-syntax.json"></a>

```
{
  "[Args](#cfn-emr-cluster-hadoopjarstepconfig-args)" : {{[ String, ... ]}},
  "[Jar](#cfn-emr-cluster-hadoopjarstepconfig-jar)" : {{String}},
  "[MainClass](#cfn-emr-cluster-hadoopjarstepconfig-mainclass)" : {{String}},
  "[StepProperties](#cfn-emr-cluster-hadoopjarstepconfig-stepproperties)" : {{[ KeyValue, ... ]}}
}
```

### YAML
<a name="aws-properties-emr-cluster-hadoopjarstepconfig-syntax.yaml"></a>

```
  [Args](#cfn-emr-cluster-hadoopjarstepconfig-args): {{
    - String}}
  [Jar](#cfn-emr-cluster-hadoopjarstepconfig-jar): {{String}}
  [MainClass](#cfn-emr-cluster-hadoopjarstepconfig-mainclass): {{String}}
  [StepProperties](#cfn-emr-cluster-hadoopjarstepconfig-stepproperties): {{
    - KeyValue}}
```

## Properties
<a name="aws-properties-emr-cluster-hadoopjarstepconfig-properties"></a>

`Args`  <a name="cfn-emr-cluster-hadoopjarstepconfig-args"></a>
A list of command line arguments passed to the JAR file's main function when executed.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Jar`  <a name="cfn-emr-cluster-hadoopjarstepconfig-jar"></a>
A path to a JAR file run during the step.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MainClass`  <a name="cfn-emr-cluster-hadoopjarstepconfig-mainclass"></a>
The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StepProperties`  <a name="cfn-emr-cluster-hadoopjarstepconfig-stepproperties"></a>
A list of Java properties that are set when the step runs. You can use these properties to pass key-value pairs to your main function.
*Required*: No
*Type*: Array of [KeyValue](aws-properties-emr-cluster-keyvalue.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

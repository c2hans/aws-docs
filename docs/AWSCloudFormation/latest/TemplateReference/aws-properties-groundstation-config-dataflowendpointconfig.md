---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-config-dataflowendpointconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::Config DataflowEndpointConfig
<a name="aws-properties-groundstation-config-dataflowendpointconfig"></a>

 Provides information to AWS Ground Station about which IP endpoints to use during a contact.

## Syntax
<a name="aws-properties-groundstation-config-dataflowendpointconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-config-dataflowendpointconfig-syntax.json"></a>

```
{
  "[DataflowEndpointName](#cfn-groundstation-config-dataflowendpointconfig-dataflowendpointname)" : {{String}},
  "[DataflowEndpointRegion](#cfn-groundstation-config-dataflowendpointconfig-dataflowendpointregion)" : {{String}}
}
```

### YAML
<a name="aws-properties-groundstation-config-dataflowendpointconfig-syntax.yaml"></a>

```
  [DataflowEndpointName](#cfn-groundstation-config-dataflowendpointconfig-dataflowendpointname): {{String}}
  [DataflowEndpointRegion](#cfn-groundstation-config-dataflowendpointconfig-dataflowendpointregion): {{String}}
```

## Properties
<a name="aws-properties-groundstation-config-dataflowendpointconfig-properties"></a>

`DataflowEndpointName`  <a name="cfn-groundstation-config-dataflowendpointconfig-dataflowendpointname"></a>
 The name of the dataflow endpoint to use during contacts.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataflowEndpointRegion`  <a name="cfn-groundstation-config-dataflowendpointconfig-dataflowendpointregion"></a>
 The region of the dataflow endpoint to use during contacts. When omitted, Ground Station will use the region of the contact.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-groundstation-config-dataflowendpointconfig--examples"></a>

### Create a DataflowEndpointConfig
<a name="aws-properties-groundstation-config-dataflowendpointconfig--examples--Create_a_DataflowEndpointConfig"></a>

The following example creates a Ground Station `DataflowEndpointConfig`

#### JSON
<a name="aws-properties-groundstation-config-dataflowendpointconfig--examples--Create_a_DataflowEndpointConfig--json"></a>

```
{
  "DataflowEndpointConfig": {
    "DataflowEndpointName": "Downlink Demod Decode",
    "DataflowEndpointRegion": "us-east-2"
  }
}
```

#### YAML
<a name="aws-properties-groundstation-config-dataflowendpointconfig--examples--Create_a_DataflowEndpointConfig--yaml"></a>

```
DataflowEndpointConfig:
  DataflowEndpointName: "Downlink Demod Decode"
  DataflowEndpointRegion: "us-east-2"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

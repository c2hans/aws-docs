---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-glueconnectioninput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection GlueConnectionInput
<a name="aws-properties-datazone-connection-glueconnectioninput"></a>

The AWS Glue connecton input.

## Syntax
<a name="aws-properties-datazone-connection-glueconnectioninput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-glueconnectioninput-syntax.json"></a>

```
{
  "[AthenaProperties](#cfn-datazone-connection-glueconnectioninput-athenaproperties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[AuthenticationConfiguration](#cfn-datazone-connection-glueconnectioninput-authenticationconfiguration)" : {{AuthenticationConfigurationInput}},
  "[ConnectionProperties](#cfn-datazone-connection-glueconnectioninput-connectionproperties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ConnectionType](#cfn-datazone-connection-glueconnectioninput-connectiontype)" : {{String}},
  "[Description](#cfn-datazone-connection-glueconnectioninput-description)" : {{String}},
  "[MatchCriteria](#cfn-datazone-connection-glueconnectioninput-matchcriteria)" : {{String}},
  "[Name](#cfn-datazone-connection-glueconnectioninput-name)" : {{String}},
  "[PhysicalConnectionRequirements](#cfn-datazone-connection-glueconnectioninput-physicalconnectionrequirements)" : {{PhysicalConnectionRequirements}},
  "[PythonProperties](#cfn-datazone-connection-glueconnectioninput-pythonproperties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[SparkProperties](#cfn-datazone-connection-glueconnectioninput-sparkproperties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ValidateCredentials](#cfn-datazone-connection-glueconnectioninput-validatecredentials)" : {{Boolean}},
  "[ValidateForComputeEnvironments](#cfn-datazone-connection-glueconnectioninput-validateforcomputeenvironments)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-datazone-connection-glueconnectioninput-syntax.yaml"></a>

```
  [AthenaProperties](#cfn-datazone-connection-glueconnectioninput-athenaproperties): {{
    {{Key}}: {{Value}}}}
  [AuthenticationConfiguration](#cfn-datazone-connection-glueconnectioninput-authenticationconfiguration): {{
    AuthenticationConfigurationInput}}
  [ConnectionProperties](#cfn-datazone-connection-glueconnectioninput-connectionproperties): {{
    {{Key}}: {{Value}}}}
  [ConnectionType](#cfn-datazone-connection-glueconnectioninput-connectiontype): {{String}}
  [Description](#cfn-datazone-connection-glueconnectioninput-description): {{String}}
  [MatchCriteria](#cfn-datazone-connection-glueconnectioninput-matchcriteria): {{String}}
  [Name](#cfn-datazone-connection-glueconnectioninput-name): {{String}}
  [PhysicalConnectionRequirements](#cfn-datazone-connection-glueconnectioninput-physicalconnectionrequirements): {{
    PhysicalConnectionRequirements}}
  [PythonProperties](#cfn-datazone-connection-glueconnectioninput-pythonproperties): {{
    {{Key}}: {{Value}}}}
  [SparkProperties](#cfn-datazone-connection-glueconnectioninput-sparkproperties): {{
    {{Key}}: {{Value}}}}
  [ValidateCredentials](#cfn-datazone-connection-glueconnectioninput-validatecredentials): {{Boolean}}
  [ValidateForComputeEnvironments](#cfn-datazone-connection-glueconnectioninput-validateforcomputeenvironments): {{
    - String}}
```

## Properties
<a name="aws-properties-datazone-connection-glueconnectioninput-properties"></a>

`AthenaProperties`  <a name="cfn-datazone-connection-glueconnectioninput-athenaproperties"></a>
The Amazon Athena properties of the AWS Glue connection.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFF\t]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthenticationConfiguration`  <a name="cfn-datazone-connection-glueconnectioninput-authenticationconfiguration"></a>
The authentication configuration of the AWS Glue connection.
*Required*: No
*Type*: [AuthenticationConfigurationInput](aws-properties-datazone-connection-authenticationconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionProperties`  <a name="cfn-datazone-connection-glueconnectioninput-connectionproperties"></a>
The connection properties of the AWS Glue connection.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionType`  <a name="cfn-datazone-connection-glueconnectioninput-connectiontype"></a>
The connection type of the AWS Glue connection.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-datazone-connection-glueconnectioninput-description"></a>
The description of the AWS Glue connection.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFF\r\n\t]*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchCriteria`  <a name="cfn-datazone-connection-glueconnectioninput-matchcriteria"></a>
The match criteria of the AWS Glue connection.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-datazone-connection-glueconnectioninput-name"></a>
The name of the AWS Glue connection.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFF\t]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhysicalConnectionRequirements`  <a name="cfn-datazone-connection-glueconnectioninput-physicalconnectionrequirements"></a>
The physical connection requirements for the AWS Glue connection.
*Required*: No
*Type*: [PhysicalConnectionRequirements](aws-properties-datazone-connection-physicalconnectionrequirements.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PythonProperties`  <a name="cfn-datazone-connection-glueconnectioninput-pythonproperties"></a>
The Python properties of the AWS Glue connection.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFF\t]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SparkProperties`  <a name="cfn-datazone-connection-glueconnectioninput-sparkproperties"></a>
The Spark properties of the AWS Glue connection.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFF\t]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidateCredentials`  <a name="cfn-datazone-connection-glueconnectioninput-validatecredentials"></a>
Speciefies whether to validate credentials of the AWS Glue connection.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidateForComputeEnvironments`  <a name="cfn-datazone-connection-glueconnectioninput-validateforcomputeenvironments"></a>
Speciefies whether to validate for compute environments of the AWS Glue connection.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

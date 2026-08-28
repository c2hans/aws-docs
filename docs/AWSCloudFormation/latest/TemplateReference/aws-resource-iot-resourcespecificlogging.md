---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-resourcespecificlogging.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::ResourceSpecificLogging
<a name="aws-resource-iot-resourcespecificlogging"></a>

Configure resource-specific logging.

## Syntax
<a name="aws-resource-iot-resourcespecificlogging-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-resourcespecificlogging-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::ResourceSpecificLogging",
  "Properties" : {
      "[LogLevel](#cfn-iot-resourcespecificlogging-loglevel)" : {{String}},
      "[TargetName](#cfn-iot-resourcespecificlogging-targetname)" : {{String}},
      "[TargetType](#cfn-iot-resourcespecificlogging-targettype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iot-resourcespecificlogging-syntax.yaml"></a>

```
Type: AWS::IoT::ResourceSpecificLogging
Properties:
  [LogLevel](#cfn-iot-resourcespecificlogging-loglevel): {{String}}
  [TargetName](#cfn-iot-resourcespecificlogging-targetname): {{String}}
  [TargetType](#cfn-iot-resourcespecificlogging-targettype): {{String}}
```

## Properties
<a name="aws-resource-iot-resourcespecificlogging-properties"></a>

`LogLevel`  <a name="cfn-iot-resourcespecificlogging-loglevel"></a>
The default log level.Valid Values: `DEBUG | INFO | ERROR | WARN | DISABLED`
*Required*: Yes
*Type*: String
*Allowed values*: `ERROR | WARN | INFO | DEBUG | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetName`  <a name="cfn-iot-resourcespecificlogging-targetname"></a>
The target name.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9.:\s_\-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetType`  <a name="cfn-iot-resourcespecificlogging-targettype"></a>
The target type. Valid Values: `DEFAULT | THING_GROUP`
*Required*: Yes
*Type*: String
*Allowed values*: `THING_GROUP | CLIENT_ID | SOURCE_IP | PRINCIPAL_ID | EVENT_TYPE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iot-resourcespecificlogging-return-values"></a>

### Ref
<a name="aws-resource-iot-resourcespecificlogging-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource-specific log ID. For example:

 `{"Ref": "MyResourceLog-12345" }`

### Fn::GetAtt
<a name="aws-resource-iot-resourcespecificlogging-return-values-fn--getatt"></a>

####
<a name="aws-resource-iot-resourcespecificlogging-return-values-fn--getatt-fn--getatt"></a>

`TargetId`  <a name="TargetId-fn::getatt"></a>
The target Id.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-mitigationaction-enableiotloggingparams.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::MitigationAction EnableIoTLoggingParams
<a name="aws-properties-iot-mitigationaction-enableiotloggingparams"></a>

Parameters used when defining a mitigation action that enable AWS IoT Core logging.

## Syntax
<a name="aws-properties-iot-mitigationaction-enableiotloggingparams-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-mitigationaction-enableiotloggingparams-syntax.json"></a>

```
{
  "[LogLevel](#cfn-iot-mitigationaction-enableiotloggingparams-loglevel)" : {{String}},
  "[RoleArnForLogging](#cfn-iot-mitigationaction-enableiotloggingparams-rolearnforlogging)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-mitigationaction-enableiotloggingparams-syntax.yaml"></a>

```
  [LogLevel](#cfn-iot-mitigationaction-enableiotloggingparams-loglevel): {{String}}
  [RoleArnForLogging](#cfn-iot-mitigationaction-enableiotloggingparams-rolearnforlogging): {{String}}
```

## Properties
<a name="aws-properties-iot-mitigationaction-enableiotloggingparams-properties"></a>

`LogLevel`  <a name="cfn-iot-mitigationaction-enableiotloggingparams-loglevel"></a>
Specifies the type of information to be logged.
*Required*: Yes
*Type*: String
*Allowed values*: `DEBUG | INFO | ERROR | WARN | UNSET_VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArnForLogging`  <a name="cfn-iot-mitigationaction-enableiotloggingparams-rolearnforlogging"></a>
The Amazon Resource Name (ARN) of the IAM role used for logging.
*Required*: Yes
*Type*: String
*Minimum*: `11`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

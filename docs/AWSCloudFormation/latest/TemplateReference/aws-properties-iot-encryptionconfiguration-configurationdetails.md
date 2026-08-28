---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-encryptionconfiguration-configurationdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::EncryptionConfiguration ConfigurationDetails
<a name="aws-properties-iot-encryptionconfiguration-configurationdetails"></a>

The encryption configuration details that include the status information of the AWS Key Management Service (AWS KMS) key and the AWS KMS access role.

## Syntax
<a name="aws-properties-iot-encryptionconfiguration-configurationdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-encryptionconfiguration-configurationdetails-syntax.json"></a>

```
{
  "[ConfigurationStatus](#cfn-iot-encryptionconfiguration-configurationdetails-configurationstatus)" : {{String}},
  "[ErrorCode](#cfn-iot-encryptionconfiguration-configurationdetails-errorcode)" : {{String}},
  "[ErrorMessage](#cfn-iot-encryptionconfiguration-configurationdetails-errormessage)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-encryptionconfiguration-configurationdetails-syntax.yaml"></a>

```
  [ConfigurationStatus](#cfn-iot-encryptionconfiguration-configurationdetails-configurationstatus): {{String}}
  [ErrorCode](#cfn-iot-encryptionconfiguration-configurationdetails-errorcode): {{String}}
  [ErrorMessage](#cfn-iot-encryptionconfiguration-configurationdetails-errormessage): {{String}}
```

## Properties
<a name="aws-properties-iot-encryptionconfiguration-configurationdetails-properties"></a>

`ConfigurationStatus`  <a name="cfn-iot-encryptionconfiguration-configurationdetails-configurationstatus"></a>
The health status of KMS key and AWS KMS access role. If either KMS key or AWS KMS access role is `UNHEALTHY`, the return value will be `UNHEALTHY`. To use a customer managed KMS key, the value of `configurationStatus` must be `HEALTHY`.
*Required*: No
*Type*: String
*Allowed values*: `HEALTHY | UNHEALTHY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ErrorCode`  <a name="cfn-iot-encryptionconfiguration-configurationdetails-errorcode"></a>
The error code that indicates either the KMS key or the AWS KMS access role is `UNHEALTHY`. Valid values: `KMS_KEY_VALIDATION_ERROR` and `ROLE_VALIDATION_ERROR`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ErrorMessage`  <a name="cfn-iot-encryptionconfiguration-configurationdetails-errormessage"></a>
The detailed error message that corresponds to the `errorCode`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

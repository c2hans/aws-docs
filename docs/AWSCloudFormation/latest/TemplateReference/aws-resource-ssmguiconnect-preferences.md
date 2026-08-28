---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssmguiconnect-preferences.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMGuiConnect::Preferences
<a name="aws-resource-ssmguiconnect-preferences"></a>

Specify new or changed connection recording preferences for your AWS Systems Manager GUI Connect connections.

## Syntax
<a name="aws-resource-ssmguiconnect-preferences-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssmguiconnect-preferences-syntax.json"></a>

```
{
  "Type" : "AWS::SSMGuiConnect::Preferences",
  "Properties" : {
      "[ConnectionRecordingPreferences](#cfn-ssmguiconnect-preferences-connectionrecordingpreferences)" : {{ConnectionRecordingPreferences}}
    }
}
```

### YAML
<a name="aws-resource-ssmguiconnect-preferences-syntax.yaml"></a>

```
Type: AWS::SSMGuiConnect::Preferences
Properties:
  [ConnectionRecordingPreferences](#cfn-ssmguiconnect-preferences-connectionrecordingpreferences): {{
    ConnectionRecordingPreferences}}
```

## Properties
<a name="aws-resource-ssmguiconnect-preferences-properties"></a>

`ConnectionRecordingPreferences`  <a name="cfn-ssmguiconnect-preferences-connectionrecordingpreferences"></a>
The set of preferences used for recording RDP connections in the requesting AWS account and AWS Region. This includes details such as which S3 bucket recordings are stored in.
*Required*: No
*Type*: [ConnectionRecordingPreferences](aws-properties-ssmguiconnect-preferences-connectionrecordingpreferences.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ssmguiconnect-preferences-return-values"></a>

### Ref
<a name="aws-resource-ssmguiconnect-preferences-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ssmguiconnect-preferences-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ssmguiconnect-preferences-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
The primary identifier for the AWS CloudFormation resource.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

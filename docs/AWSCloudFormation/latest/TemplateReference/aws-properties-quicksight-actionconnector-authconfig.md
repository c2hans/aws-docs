---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-actionconnector-authconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ActionConnector AuthConfig
<a name="aws-properties-quicksight-actionconnector-authconfig"></a>

Authentication configuration for connecting to external services.

## Syntax
<a name="aws-properties-quicksight-actionconnector-authconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-actionconnector-authconfig-syntax.json"></a>

```
{
  "[AuthenticationMetadata](#cfn-quicksight-actionconnector-authconfig-authenticationmetadata)" : {{AuthenticationMetadata}},
  "[AuthenticationType](#cfn-quicksight-actionconnector-authconfig-authenticationtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-actionconnector-authconfig-syntax.yaml"></a>

```
  [AuthenticationMetadata](#cfn-quicksight-actionconnector-authconfig-authenticationmetadata): {{
    AuthenticationMetadata}}
  [AuthenticationType](#cfn-quicksight-actionconnector-authconfig-authenticationtype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-actionconnector-authconfig-properties"></a>

`AuthenticationMetadata`  <a name="cfn-quicksight-actionconnector-authconfig-authenticationmetadata"></a>
The authentication metadata containing the specific configuration for the chosen authentication type.
*Required*: Yes
*Type*: [AuthenticationMetadata](aws-properties-quicksight-actionconnector-authenticationmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthenticationType`  <a name="cfn-quicksight-actionconnector-authconfig-authenticationtype"></a>
The type of authentication method.
*Required*: Yes
*Type*: String
*Allowed values*: `BASIC | API_KEY | OAUTH2_CLIENT_CREDENTIALS | NONE | IAM | OAUTH2_AUTHORIZATION_CODE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-identitycenterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::IdentityCenterConfiguration
<a name="aws-resource-glue-identitycenterconfiguration"></a>

Creates a new AWS Glue Identity Center configuration to enable integration between AWS Glue and AWS IAM Identity Center for authentication and authorization.

## Syntax
<a name="aws-resource-glue-identitycenterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-identitycenterconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::IdentityCenterConfiguration",
  "Properties" : {
      "[InstanceArn](#cfn-glue-identitycenterconfiguration-instancearn)" : {{String}},
      "[Scopes](#cfn-glue-identitycenterconfiguration-scopes)" : {{[ String, ... ]}},
      "[UserBackgroundSessionsEnabled](#cfn-glue-identitycenterconfiguration-userbackgroundsessionsenabled)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-glue-identitycenterconfiguration-syntax.yaml"></a>

```
Type: AWS::Glue::IdentityCenterConfiguration
Properties:
  [InstanceArn](#cfn-glue-identitycenterconfiguration-instancearn): {{String}}
  [Scopes](#cfn-glue-identitycenterconfiguration-scopes): {{
    - String}}
  [UserBackgroundSessionsEnabled](#cfn-glue-identitycenterconfiguration-userbackgroundsessionsenabled): {{Boolean}}
```

## Properties
<a name="aws-resource-glue-identitycenterconfiguration-properties"></a>

`InstanceArn`  <a name="cfn-glue-identitycenterconfiguration-instancearn"></a>
The Amazon Resource Name (ARN) of the Identity Center instance associated with the AWS Glue configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`
*Minimum*: `10`
*Maximum*: `1224`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Scopes`  <a name="cfn-glue-identitycenterconfiguration-scopes"></a>
A list of Identity Center scopes that define the permissions and access levels for the AWS Glue configuration.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserBackgroundSessionsEnabled`  <a name="cfn-glue-identitycenterconfiguration-userbackgroundsessionsenabled"></a>
Indicates whether users can run background sessions when using Identity Center authentication with AWS Glue services.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-glue-identitycenterconfiguration-return-values"></a>

### Ref
<a name="aws-resource-glue-identitycenterconfiguration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-glue-identitycenterconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-glue-identitycenterconfiguration-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
Property description not available.

`ApplicationArn`  <a name="ApplicationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Identity Center application associated with the AWS Glue configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

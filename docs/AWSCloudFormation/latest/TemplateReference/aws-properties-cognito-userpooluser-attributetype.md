---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpooluser-attributetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolUser AttributeType
<a name="aws-properties-cognito-userpooluser-attributetype"></a>

The name and value of a user attribute.

## Syntax
<a name="aws-properties-cognito-userpooluser-attributetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpooluser-attributetype-syntax.json"></a>

```
{
  "[Name](#cfn-cognito-userpooluser-attributetype-name)" : {{String}},
  "[Value](#cfn-cognito-userpooluser-attributetype-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpooluser-attributetype-syntax.yaml"></a>

```
  [Name](#cfn-cognito-userpooluser-attributetype-name): {{String}}
  [Value](#cfn-cognito-userpooluser-attributetype-value): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpooluser-attributetype-properties"></a>

`Name`  <a name="cfn-cognito-userpooluser-attributetype-name"></a>
The name of the attribute, for example `email` or `custom:department`.
In some older user pools, the regex pattern for acceptable values of this parameter is `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`. Older pools will eventually be updated to use the new pattern. Affected user pools are those created before May 2024 in US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), Middle East (Bahrain), and South America (São Paulo).
*Required*: No
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r ]+`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-cognito-userpooluser-attributetype-value"></a>
The value of the attribute.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

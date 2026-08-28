---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-masteruseroptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain MasterUserOptions
<a name="aws-properties-opensearchservice-domain-masteruseroptions"></a>

Specifies information about the master user.

Required if `InternalUserDatabaseEnabled` is true in [AdvancedSecurityOptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html).

## Syntax
<a name="aws-properties-opensearchservice-domain-masteruseroptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-masteruseroptions-syntax.json"></a>

```
{
  "[MasterUserARN](#cfn-opensearchservice-domain-masteruseroptions-masteruserarn)" : {{String}},
  "[MasterUserName](#cfn-opensearchservice-domain-masteruseroptions-masterusername)" : {{String}},
  "[MasterUserPassword](#cfn-opensearchservice-domain-masteruseroptions-masteruserpassword)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-masteruseroptions-syntax.yaml"></a>

```
  [MasterUserARN](#cfn-opensearchservice-domain-masteruseroptions-masteruserarn): {{String}}
  [MasterUserName](#cfn-opensearchservice-domain-masteruseroptions-masterusername): {{String}}
  [MasterUserPassword](#cfn-opensearchservice-domain-masteruseroptions-masteruserpassword): {{String}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-masteruseroptions-properties"></a>

`MasterUserARN`  <a name="cfn-opensearchservice-domain-masteruseroptions-masteruserarn"></a>
Amazon Resource Name (ARN) for the master user. The ARN can point to an IAM user or role. This property is required for Amazon Cognito to work, and it must match the role configured for Cognito. Only specify if `InternalUserDatabaseEnabled` is false in [AdvancedSecurityOptionsInput](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MasterUserName`  <a name="cfn-opensearchservice-domain-masteruseroptions-masterusername"></a>
Username for the master user. Only specify if `InternalUserDatabaseEnabled` is true in [AdvancedSecurityOptionsInput](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html).
If you don't want to specify this value directly within the template, you can use a [dynamic reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html) instead.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MasterUserPassword`  <a name="cfn-opensearchservice-domain-masteruseroptions-masteruserpassword"></a>
Password for the master user. Only specify if `InternalUserDatabaseEnabled` is true in [AdvancedSecurityOptionsInput](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html).
If you don't want to specify this value directly within the template, you can use a [dynamic reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html) instead.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `8`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

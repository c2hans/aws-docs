---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-delegatedadmin.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::DelegatedAdmin
<a name="aws-resource-securityhub-delegatedadmin"></a>

The `AWS::SecurityHub::DelegatedAdmin` resource designates the delegated AWS Security Hub CSPM administrator account for an organization. You must enable the integration between Security Hub CSPM and AWS Organizations before you can designate a delegated Security Hub CSPM administrator. Only the management account for an organization can designate the delegated Security Hub CSPM administrator account. For more information, see [Designating the delegated Security Hub CSPM administrator](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html#designate-admin-instructions) in the *AWS Security Hub CSPM User Guide*.

To change the delegated administrator account, remove the current delegated administrator account, and then designate the new account.

To designate multiple delegated administrators in different organizations and AWS Regions, we recommend using [AWS CloudFormation mappings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html).

Tags aren't supported for this resource.

## Syntax
<a name="aws-resource-securityhub-delegatedadmin-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-delegatedadmin-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::DelegatedAdmin",
  "Properties" : {
      "[AdminAccountId](#cfn-securityhub-delegatedadmin-adminaccountid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-delegatedadmin-syntax.yaml"></a>

```
Type: AWS::SecurityHub::DelegatedAdmin
Properties:
  [AdminAccountId](#cfn-securityhub-delegatedadmin-adminaccountid): {{String}}
```

## Properties
<a name="aws-resource-securityhub-delegatedadmin-properties"></a>

`AdminAccountId`  <a name="cfn-securityhub-delegatedadmin-adminaccountid"></a>
The AWS account identifier of the account to designate as the Security Hub CSPM administrator account.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-securityhub-delegatedadmin-return-values"></a>

### Ref
<a name="aws-resource-securityhub-delegatedadmin-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the delegated Security Hub CSPM administrator account. The format is `accountID/Region`. For example, `123456789012/us-west-2`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityhub-delegatedadmin-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityhub-delegatedadmin-return-values-fn--getatt-fn--getatt"></a>

`DelegatedAdminIdentifier`  <a name="DelegatedAdminIdentifier-fn::getatt"></a>
The ID of the delegated Security Hub CSPM administrator account, in the format of `accountID/Region`.

`Status`  <a name="Status-fn::getatt"></a>
Whether the delegated Security Hub CSPM administrator is set for the organization.

## Examples
<a name="aws-resource-securityhub-delegatedadmin--examples"></a>

### Designating the delegated Security Hub CSPM administrator
<a name="aws-resource-securityhub-delegatedadmin--examples--Designating_the_delegated_administrator"></a>

The following example designates the specified AWS account as the delegated Security Hub CSPM administrator for an organization.

#### JSON
<a name="aws-resource-securityhub-delegatedadmin--examples--Designating_the_delegated_administrator--json"></a>

```
{
	"Description": "Example template to create the delegated Security Hub administrator",
	"Resources": {
		"SecurityHubDelegatedAdmin": {
			"Type": "AWS::SecurityHub::DelegatedAdmin",
			"Properties": {
				"AdminAccountId": "123456789012"
			}
		}
	}
}
```

#### YAML
<a name="aws-resource-securityhub-delegatedadmin--examples--Designating_the_delegated_administrator--yaml"></a>

```
Description: Example template to create the delegated Security Hub administrator
Resources:
  SecurityHubDelegatedAdmin:
    Type: 'AWS::SecurityHub::DelegatedAdmin'
    Properties:
      AdminAccountId: '123456789012'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

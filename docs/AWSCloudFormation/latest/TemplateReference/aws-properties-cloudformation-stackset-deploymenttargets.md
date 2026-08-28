---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-stackset-deploymenttargets.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::StackSet DeploymentTargets
<a name="aws-properties-cloudformation-stackset-deploymenttargets"></a>

The AWS Organizations accounts or AWS accounts to deploy stacks to in the specified Regions.

When deploying to AWS Organizations accounts with `SERVICE_MANAGED` permissions:
+ You must specify the `OrganizationalUnitIds` property.
+ If you specify organizational units (OUs) for `OrganizationalUnitIds` and use either the `Accounts` or `AccountsUrl` property, you must also specify the `AccountFilterType` property.

When deploying to AWS accounts with `SELF_MANAGED` permissions:
+ You must specify either the `Accounts` or `AccountsUrl` property, but not both.

## Syntax
<a name="aws-properties-cloudformation-stackset-deploymenttargets-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-stackset-deploymenttargets-syntax.json"></a>

```
{
  "[AccountFilterType](#cfn-cloudformation-stackset-deploymenttargets-accountfiltertype)" : {{String}},
  "[Accounts](#cfn-cloudformation-stackset-deploymenttargets-accounts)" : {{[ String, ... ]}},
  "[AccountsUrl](#cfn-cloudformation-stackset-deploymenttargets-accountsurl)" : {{String}},
  "[OrganizationalUnitIds](#cfn-cloudformation-stackset-deploymenttargets-organizationalunitids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudformation-stackset-deploymenttargets-syntax.yaml"></a>

```
  [AccountFilterType](#cfn-cloudformation-stackset-deploymenttargets-accountfiltertype): {{String}}
  [Accounts](#cfn-cloudformation-stackset-deploymenttargets-accounts): {{
    - String}}
  [AccountsUrl](#cfn-cloudformation-stackset-deploymenttargets-accountsurl): {{String}}
  [OrganizationalUnitIds](#cfn-cloudformation-stackset-deploymenttargets-organizationalunitids): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudformation-stackset-deploymenttargets-properties"></a>

`AccountFilterType`  <a name="cfn-cloudformation-stackset-deploymenttargets-accountfiltertype"></a>
Refines which accounts to deploy stacks to by specifying how to use the `Accounts` and `OrganizationalUnitIds` properties together.
The following values determine how CloudFormation selects target accounts:
+ `INTERSECTION`: StackSet deploys to the accounts specified in the `Accounts` property.
+ `DIFFERENCE`: StackSet deploys to the OU, excluding the accounts specified in the `Accounts` property.
+ `UNION`: StackSet deploys to the OU, and the accounts specified in the `Accounts` property. `UNION` is not supported for create operations when using StackSet as a resource or the `CreateStackInstances` API.
*Required*: No
*Type*: String
*Allowed values*: `NONE | UNION | INTERSECTION | DIFFERENCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Accounts`  <a name="cfn-cloudformation-stackset-deploymenttargets-accounts"></a>
The account IDs of the AWS accounts. If you have many account numbers, you can provide those accounts using the `AccountsUrl` property instead.
*Pattern*: `^[0-9]{12}$`
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AccountsUrl`  <a name="cfn-cloudformation-stackset-deploymenttargets-accountsurl"></a>
The Amazon S3 URL path to a file that contains a list of AWS account IDs. The file format must be either `.csv` or `.txt`, and the data can be comma-separated or new-line-separated. There is currently a 10MB limit for the data (approximately 800,000 accounts).
This property serves the same purpose as `Accounts` but allows you to specify a large number of accounts.
*Required*: No
*Type*: String
*Pattern*: `(s3://|http(s?)://).+`
*Minimum*: `1`
*Maximum*: `5120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrganizationalUnitIds`  <a name="cfn-cloudformation-stackset-deploymenttargets-organizationalunitids"></a>
The organization root ID or organizational unit (OU) IDs.
*Pattern*: `^(ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}|r-[a-z0-9]{4,32})$`
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fms-policy-iemap.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::Policy IEMap
<a name="aws-properties-fms-policy-iemap"></a>

Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to include in or exclude from the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.

This is used for the policy's `IncludeMap` and `ExcludeMap`.

You can specify account IDs, OUs, or a combination:
+ Specify account IDs by setting the key to `ACCOUNT`. For example, the following is a valid map: `{“ACCOUNT” : [“accountID1”, “accountID2”]}`.
+ Specify OUs by setting the key to `ORGUNIT`. For example, the following is a valid map: `{“ORGUNIT” : [“ouid111”, “ouid112”]}`.
+ Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: `{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`.

## Syntax
<a name="aws-properties-fms-policy-iemap-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fms-policy-iemap-syntax.json"></a>

```
{
  "[ACCOUNT](#cfn-fms-policy-iemap-account)" : {{[ String, ... ]}},
  "[ORGUNIT](#cfn-fms-policy-iemap-orgunit)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-fms-policy-iemap-syntax.yaml"></a>

```
  [ACCOUNT](#cfn-fms-policy-iemap-account): {{
    - String}}
  [ORGUNIT](#cfn-fms-policy-iemap-orgunit): {{
    - String}}
```

## Properties
<a name="aws-properties-fms-policy-iemap-properties"></a>

`ACCOUNT`  <a name="cfn-fms-policy-iemap-account"></a>
The account list for the map.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ORGUNIT`  <a name="cfn-fms-policy-iemap-orgunit"></a>
The organizational unit list for the map.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

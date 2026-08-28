---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Membership MembershipProtectedQueryResultConfiguration
<a name="aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration"></a>

Contains configurations for protected query results.

## Syntax
<a name="aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration-syntax.json"></a>

```
{
  "[OutputConfiguration](#cfn-cleanrooms-membership-membershipprotectedqueryresultconfiguration-outputconfiguration)" : {{MembershipProtectedQueryOutputConfiguration}},
  "[RoleArn](#cfn-cleanrooms-membership-membershipprotectedqueryresultconfiguration-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration-syntax.yaml"></a>

```
  [OutputConfiguration](#cfn-cleanrooms-membership-membershipprotectedqueryresultconfiguration-outputconfiguration): {{
    MembershipProtectedQueryOutputConfiguration}}
  [RoleArn](#cfn-cleanrooms-membership-membershipprotectedqueryresultconfiguration-rolearn): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration-properties"></a>

`OutputConfiguration`  <a name="cfn-cleanrooms-membership-membershipprotectedqueryresultconfiguration-outputconfiguration"></a>
Configuration for protected query results.
*Required*: Yes
*Type*: [MembershipProtectedQueryOutputConfiguration](aws-properties-cleanrooms-membership-membershipprotectedqueryoutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-cleanrooms-membership-membershipprotectedqueryresultconfiguration-rolearn"></a>
The unique ARN for an IAM role that is used by AWS Clean Rooms to write protected query results to the result location, given by the member who can receive results.
*Required*: No
*Type*: String
*Minimum*: `32`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

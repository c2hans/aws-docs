---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-organizations-root-policytypesummary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Organizations::Root PolicyTypeSummary
<a name="aws-properties-organizations-root-policytypesummary"></a>

Contains information about a policy type and its status in the associated root.

## Syntax
<a name="aws-properties-organizations-root-policytypesummary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-organizations-root-policytypesummary-syntax.json"></a>

```
{
  "[Status](#cfn-organizations-root-policytypesummary-status)" : {{String}},
  "[Type](#cfn-organizations-root-policytypesummary-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-organizations-root-policytypesummary-syntax.yaml"></a>

```
  [Status](#cfn-organizations-root-policytypesummary-status): {{String}}
  [Type](#cfn-organizations-root-policytypesummary-type): {{String}}
```

## Properties
<a name="aws-properties-organizations-root-policytypesummary-properties"></a>

`Status`  <a name="cfn-organizations-root-policytypesummary-status"></a>
The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | PENDING_ENABLE | PENDING_DISABLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-organizations-root-policytypesummary-type"></a>
The name of the policy type.
*Required*: No
*Type*: String
*Allowed values*: `SERVICE_CONTROL_POLICY | RESOURCE_CONTROL_POLICY | TAG_POLICY | BACKUP_POLICY | AISERVICES_OPT_OUT_POLICY | CHATBOT_POLICY | DECLARATIVE_POLICY_EC2 | SECURITYHUB_POLICY | INSPECTOR_POLICY | UPGRADE_ROLLOUT_POLICY | BEDROCK_POLICY | S3_POLICY | NETWORK_SECURITY_DIRECTOR_POLICY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

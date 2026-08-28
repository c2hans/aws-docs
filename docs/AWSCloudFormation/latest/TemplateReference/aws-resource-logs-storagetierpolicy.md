---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-storagetierpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::StorageTierPolicy
<a name="aws-resource-logs-storagetierpolicy"></a>

Sets the storage tier policy for the account. When you set the storage tier to `INTELLIGENT_TIERING`, the service automatically moves log data to the most cost-effective storage tier based on access frequency.

## Syntax
<a name="aws-resource-logs-storagetierpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-logs-storagetierpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::Logs::StorageTierPolicy",
  "Properties" : {
      "[StorageTier](#cfn-logs-storagetierpolicy-storagetier)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-logs-storagetierpolicy-syntax.yaml"></a>

```
Type: AWS::Logs::StorageTierPolicy
Properties:
  [StorageTier](#cfn-logs-storagetierpolicy-storagetier): {{String}}
```

## Properties
<a name="aws-resource-logs-storagetierpolicy-properties"></a>

`StorageTier`  <a name="cfn-logs-storagetierpolicy-storagetier"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `INTELLIGENT_TIERING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-logs-storagetierpolicy-return-values"></a>

### Ref
<a name="aws-resource-logs-storagetierpolicy-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-logs-storagetierpolicy-return-values-fn--getatt"></a>

####
<a name="aws-resource-logs-storagetierpolicy-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
Property description not available.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

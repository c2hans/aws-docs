---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rum-appmonitor-resourcepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RUM::AppMonitor ResourcePolicy
<a name="aws-properties-rum-appmonitor-resourcepolicy"></a>

Use this structure to assign a resource-based policy to a CloudWatch RUM app monitor to control access to it. Each app monitor can have one resource-based policy. The maximum size of the policy is 4 KB. To learn more about using resource policies with RUM, see [Using resource-based policies with CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html).

## Syntax
<a name="aws-properties-rum-appmonitor-resourcepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rum-appmonitor-resourcepolicy-syntax.json"></a>

```
{
  "[PolicyDocument](#cfn-rum-appmonitor-resourcepolicy-policydocument)" : {{String}},
  "[PolicyRevisionId](#cfn-rum-appmonitor-resourcepolicy-policyrevisionid)" : {{String}}
}
```

### YAML
<a name="aws-properties-rum-appmonitor-resourcepolicy-syntax.yaml"></a>

```
  [PolicyDocument](#cfn-rum-appmonitor-resourcepolicy-policydocument): {{String}}
  [PolicyRevisionId](#cfn-rum-appmonitor-resourcepolicy-policyrevisionid): {{String}}
```

## Properties
<a name="aws-properties-rum-appmonitor-resourcepolicy-properties"></a>

`PolicyDocument`  <a name="cfn-rum-appmonitor-resourcepolicy-policydocument"></a>
The JSON to use as the resource policy. The document can be up to 4 KB in size. For more information about the contents and syntax for this policy, see [Using resource-based policies with CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyRevisionId`  <a name="cfn-rum-appmonitor-resourcepolicy-policyrevisionid"></a>
A string value that you can use to conditionally update your policy. You can provide the revision ID of your existing policy to make mutating requests against that policy.
When you assign a policy revision ID, then later requests about that policy will be rejected with an `InvalidPolicyRevisionIdException` error if they don't provide the correct current revision ID.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-msk-batchscramsecret.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::BatchScramSecret
<a name="aws-resource-msk-batchscramsecret"></a>

Represents a secret stored in the AWS Secrets Manager that can be used to authenticate with a cluster using a user name and a password.

## Syntax
<a name="aws-resource-msk-batchscramsecret-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-msk-batchscramsecret-syntax.json"></a>

```
{
  "Type" : "AWS::MSK::BatchScramSecret",
  "Properties" : {
      "[ClusterArn](#cfn-msk-batchscramsecret-clusterarn)" : {{String}},
      "[SecretArnList](#cfn-msk-batchscramsecret-secretarnlist)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-msk-batchscramsecret-syntax.yaml"></a>

```
Type: AWS::MSK::BatchScramSecret
Properties:
  [ClusterArn](#cfn-msk-batchscramsecret-clusterarn): {{String}}
  [SecretArnList](#cfn-msk-batchscramsecret-secretarnlist): {{
    - String}}
```

## Properties
<a name="aws-resource-msk-batchscramsecret-properties"></a>

`ClusterArn`  <a name="cfn-msk-batchscramsecret-clusterarn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the cluster.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecretArnList`  <a name="cfn-msk-batchscramsecret-secretarnlist"></a>
List of Amazon Resource Name (ARN)s of Secrets Manager secrets.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-msk-batchscramsecret-return-values"></a>

### Ref
<a name="aws-resource-msk-batchscramsecret-return-values-ref"></a>

When you provide the logical ID of this resource to the `Ref` intrinsic function, `Ref` returns the secret stored in the Secrets Manager.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

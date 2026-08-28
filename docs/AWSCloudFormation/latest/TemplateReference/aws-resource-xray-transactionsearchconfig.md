---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-xray-transactionsearchconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::XRay::TransactionSearchConfig
<a name="aws-resource-xray-transactionsearchconfig"></a>

Use the `AWS::XRay::TransactionSearchConfig` resource to configure the percentage of traces indexed from CloudWatch Logs to X-Ray for transaction search.

For more information, see [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) in the *Amazon CloudWatch User Guide*.

## Syntax
<a name="aws-resource-xray-transactionsearchconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-xray-transactionsearchconfig-syntax.json"></a>

```
{
  "Type" : "AWS::XRay::TransactionSearchConfig",
  "Properties" : {
      "[IndexingPercentage](#cfn-xray-transactionsearchconfig-indexingpercentage)" : {{Number}}
    }
}
```

### YAML
<a name="aws-resource-xray-transactionsearchconfig-syntax.yaml"></a>

```
Type: AWS::XRay::TransactionSearchConfig
Properties:
  [IndexingPercentage](#cfn-xray-transactionsearchconfig-indexingpercentage): {{Number}}
```

## Properties
<a name="aws-resource-xray-transactionsearchconfig-properties"></a>

`IndexingPercentage`  <a name="cfn-xray-transactionsearchconfig-indexingpercentage"></a>
The percentage of spans to be indexed as trace summaries. The value can be set between 0 and 100.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-xray-transactionsearchconfig-return-values"></a>

### Ref
<a name="aws-resource-xray-transactionsearchconfig-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the AWS account ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-xray-transactionsearchconfig-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-xray-transactionsearchconfig-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
The AWS account ID associated with the transaction search configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancing-loadbalancer-accessloggingpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancing::LoadBalancer AccessLoggingPolicy
<a name="aws-properties-elasticloadbalancing-loadbalancer-accessloggingpolicy"></a>

Specifies where and how access logs are stored for your Classic Load Balancer.

## Syntax
<a name="aws-properties-elasticloadbalancing-loadbalancer-accessloggingpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancing-loadbalancer-accessloggingpolicy-syntax.json"></a>

```
{
  "[EmitInterval](#cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy-emitinterval)" : {{Integer}},
  "[Enabled](#cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy-enabled)" : {{Boolean}},
  "[S3BucketName](#cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy-s3bucketname)" : {{String}},
  "[S3BucketPrefix](#cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy-s3bucketprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancing-loadbalancer-accessloggingpolicy-syntax.yaml"></a>

```
  [EmitInterval](#cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy-emitinterval): {{Integer}}
  [Enabled](#cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy-enabled): {{Boolean}}
  [S3BucketName](#cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy-s3bucketname): {{String}}
  [S3BucketPrefix](#cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy-s3bucketprefix): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancing-loadbalancer-accessloggingpolicy-properties"></a>

`EmitInterval`  <a name="cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy-emitinterval"></a>
The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.
Default: 60 minutes
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy-enabled"></a>
Specifies whether access logs are enabled for the load balancer.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BucketName`  <a name="cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy-s3bucketname"></a>
The name of the Amazon S3 bucket where the access logs are stored.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BucketPrefix`  <a name="cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy-s3bucketprefix"></a>
The logical hierarchy you created for your Amazon S3 bucket, for example `my-bucket-prefix/prod`. If the prefix is not provided, the log is placed at the root level of the bucket.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-elasticloadbalancing-loadbalancer-accessloggingpolicy--seealso"></a>
+ [ModifyLoadBalancerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ModifyLoadBalancerAttributes.html) in the *Elastic Load Balancing API Reference (version 2012-06-01)*
+ [Access Logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html) in the *User Guide for Classic Load Balancers*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

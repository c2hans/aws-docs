---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-delegationset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::DelegationSet
<a name="aws-resource-route53-delegationset"></a>

A complex type that lists the name servers in a delegation set, as well as the `CallerReference` and the `ID` for the delegation set.

## Syntax
<a name="aws-resource-route53-delegationset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53-delegationset-syntax.json"></a>

```
{
  "Type" : "AWS::Route53::DelegationSet"
}
```

### YAML
<a name="aws-resource-route53-delegationset-syntax.yaml"></a>

```
Type: AWS::Route53::DelegationSet
```

## Return values
<a name="aws-resource-route53-delegationset-return-values"></a>

### Ref
<a name="aws-resource-route53-delegationset-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-route53-delegationset-return-values-fn--getatt"></a>

####
<a name="aws-resource-route53-delegationset-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CallerReference`  <a name="CallerReference-fn::getatt"></a>
The value that you specified for `CallerReference` when you created the reusable delegation set.

`Id`  <a name="Id-fn::getatt"></a>
The ID that Amazon Route 53 assigns to a reusable delegation set.

`NameServers`  <a name="NameServers-fn::getatt"></a>
A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

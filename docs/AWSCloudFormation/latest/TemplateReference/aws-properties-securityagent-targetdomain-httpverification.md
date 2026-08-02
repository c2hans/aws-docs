---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-targetdomain-httpverification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::TargetDomain HttpVerification
<a name="aws-properties-securityagent-targetdomain-httpverification"></a>

Contains HTTP route verification details for a target domain, including the route path and token to serve for domain ownership verification.

## Syntax
<a name="aws-properties-securityagent-targetdomain-httpverification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-targetdomain-httpverification-syntax.json"></a>

```
{
  "[RoutePath](#cfn-securityagent-targetdomain-httpverification-routepath)" : {{String}},
  "[Token](#cfn-securityagent-targetdomain-httpverification-token)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityagent-targetdomain-httpverification-syntax.yaml"></a>

```
  [RoutePath](#cfn-securityagent-targetdomain-httpverification-routepath): {{String}}
  [Token](#cfn-securityagent-targetdomain-httpverification-token): {{String}}
```

## Properties
<a name="aws-properties-securityagent-targetdomain-httpverification-properties"></a>

`RoutePath`  <a name="cfn-securityagent-targetdomain-httpverification-routepath"></a>
The HTTP route path where the verification token must be served.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Token`  <a name="cfn-securityagent-targetdomain-httpverification-token"></a>
The verification token to serve at the specified route path.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

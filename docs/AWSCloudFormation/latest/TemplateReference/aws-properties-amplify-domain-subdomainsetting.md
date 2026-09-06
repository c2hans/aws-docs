---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplify-domain-subdomainsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::Domain SubDomainSetting
<a name="aws-properties-amplify-domain-subdomainsetting"></a>

 The SubDomainSetting property type enables you to connect a subdomain (for example, example.exampledomain.com) to a specific branch.

## Syntax
<a name="aws-properties-amplify-domain-subdomainsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplify-domain-subdomainsetting-syntax.json"></a>

```
{
  "[BranchName](#cfn-amplify-domain-subdomainsetting-branchname)" : {{String}},
  "[Prefix](#cfn-amplify-domain-subdomainsetting-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplify-domain-subdomainsetting-syntax.yaml"></a>

```
  [BranchName](#cfn-amplify-domain-subdomainsetting-branchname): {{String}}
  [Prefix](#cfn-amplify-domain-subdomainsetting-prefix): {{String}}
```

## Properties
<a name="aws-properties-amplify-domain-subdomainsetting-properties"></a>

`BranchName`  <a name="cfn-amplify-domain-subdomainsetting-branchname"></a>
 The branch name setting for the subdomain.
*Length Constraints:* Minimum length of 1. Maximum length of 255.
*Pattern:* (?s).\+
*Required*: Yes
*Type*: String
*Pattern*: `(?s).+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-amplify-domain-subdomainsetting-prefix"></a>
 The prefix setting for the subdomain.
*Required*: Yes
*Type*: String
*Pattern*: `(?s).*`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

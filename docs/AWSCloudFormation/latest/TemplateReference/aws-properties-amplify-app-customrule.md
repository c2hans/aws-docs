---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplify-app-customrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::App CustomRule
<a name="aws-properties-amplify-app-customrule"></a>

 The CustomRule property type allows you to specify redirects, rewrites, and reverse proxies. Redirects enable a web app to reroute navigation from one URL to another.

## Syntax
<a name="aws-properties-amplify-app-customrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplify-app-customrule-syntax.json"></a>

```
{
  "[Condition](#cfn-amplify-app-customrule-condition)" : {{String}},
  "[Source](#cfn-amplify-app-customrule-source)" : {{String}},
  "[Status](#cfn-amplify-app-customrule-status)" : {{String}},
  "[Target](#cfn-amplify-app-customrule-target)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplify-app-customrule-syntax.yaml"></a>

```
  [Condition](#cfn-amplify-app-customrule-condition): {{String}}
  [Source](#cfn-amplify-app-customrule-source): {{String}}
  [Status](#cfn-amplify-app-customrule-status): {{String}}
  [Target](#cfn-amplify-app-customrule-target): {{String}}
```

## Properties
<a name="aws-properties-amplify-app-customrule-properties"></a>

`Condition`  <a name="cfn-amplify-app-customrule-condition"></a>
The condition for a URL rewrite or redirect rule, such as a country code.
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-amplify-app-customrule-source"></a>
 The source pattern for a URL rewrite or redirect rule.
*Required*: Yes
*Type*: String
*Pattern*: `(?s).+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-amplify-app-customrule-status"></a>
 The status code for a URL rewrite or redirect rule.
200
Represents a 200 rewrite rule.
301
Represents a 301 (moved pemanently) redirect rule. This and all future requests should be directed to the target URL.
302
Represents a 302 temporary redirect rule.
404
Represents a 404 redirect rule.
404-200
Represents a 404 rewrite rule.
*Required*: No
*Type*: String
*Pattern*: `.{3,7}`
*Minimum*: `3`
*Maximum*: `7`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Target`  <a name="cfn-amplify-app-customrule-target"></a>
 The target pattern for a URL rewrite or redirect rule.
*Required*: Yes
*Type*: String
*Pattern*: `(?s).+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

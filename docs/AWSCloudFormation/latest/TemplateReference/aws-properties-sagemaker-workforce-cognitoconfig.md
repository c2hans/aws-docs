---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-workforce-cognitoconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Workforce CognitoConfig
<a name="aws-properties-sagemaker-workforce-cognitoconfig"></a>

Use this parameter to configure your Amazon Cognito workforce. A single Cognito workforce is created using and corresponds to a single [ Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html).

## Syntax
<a name="aws-properties-sagemaker-workforce-cognitoconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-workforce-cognitoconfig-syntax.json"></a>

```
{
  "[ClientId](#cfn-sagemaker-workforce-cognitoconfig-clientid)" : {{String}},
  "[UserPool](#cfn-sagemaker-workforce-cognitoconfig-userpool)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-workforce-cognitoconfig-syntax.yaml"></a>

```
  [ClientId](#cfn-sagemaker-workforce-cognitoconfig-clientid): {{String}}
  [UserPool](#cfn-sagemaker-workforce-cognitoconfig-userpool): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-workforce-cognitoconfig-properties"></a>

`ClientId`  <a name="cfn-sagemaker-workforce-cognitoconfig-clientid"></a>
The client ID for your Amazon Cognito user pool.
*Required*: Yes
*Type*: String
*Pattern*: `[ -~]+`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserPool`  <a name="cfn-sagemaker-workforce-cognitoconfig-userpool"></a>
A [ user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) is a user directory in Amazon Cognito. With a user pool, your users can sign in to your web or mobile app through Amazon Cognito. Your users can also sign in through social identity providers like Google, Facebook, Amazon, or Apple, and through SAML identity providers.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]+_[0-9a-zA-Z]+`
*Minimum*: `1`
*Maximum*: `55`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

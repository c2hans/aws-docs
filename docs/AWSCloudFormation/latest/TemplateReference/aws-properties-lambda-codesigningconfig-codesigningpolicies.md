---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-codesigningconfig-codesigningpolicies.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::CodeSigningConfig CodeSigningPolicies
<a name="aws-properties-lambda-codesigningconfig-codesigningpolicies"></a>

Code signing configuration [policies](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html#config-codesigning-policies) specify the validation failure action for signature mismatch or expiry.

## Syntax
<a name="aws-properties-lambda-codesigningconfig-codesigningpolicies-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-codesigningconfig-codesigningpolicies-syntax.json"></a>

```
{
  "[UntrustedArtifactOnDeployment](#cfn-lambda-codesigningconfig-codesigningpolicies-untrustedartifactondeployment)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-codesigningconfig-codesigningpolicies-syntax.yaml"></a>

```
  [UntrustedArtifactOnDeployment](#cfn-lambda-codesigningconfig-codesigningpolicies-untrustedartifactondeployment): {{String}}
```

## Properties
<a name="aws-properties-lambda-codesigningconfig-codesigningpolicies-properties"></a>

`UntrustedArtifactOnDeployment`  <a name="cfn-lambda-codesigningconfig-codesigningpolicies-untrustedartifactondeployment"></a>
Code signing configuration policy for deployment validation failure. If you set the policy to `Enforce`, Lambda blocks the deployment request if signature validation checks fail. If you set the policy to `Warn`, Lambda allows the deployment and issues a new Amazon CloudWatch metric (`SignatureValidationErrors`) and also stores the warning in the CloudTrail log.
Default value: `Warn`
*Required*: Yes
*Type*: String
*Allowed values*: `Warn | Enforce`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

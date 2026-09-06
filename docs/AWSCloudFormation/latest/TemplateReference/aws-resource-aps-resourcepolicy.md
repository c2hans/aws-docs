---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-aps-resourcepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::ResourcePolicy
<a name="aws-resource-aps-resourcepolicy"></a>

Use resource-based policies to grant permissions to other AWS accounts or services to access your workspace.

Only Prometheus-compatible APIs can be used for workspace sharing. You can add non-Prometheus-compatible APIs to the policy, but they will be ignored. For more information, see [Prometheus-compatible APIs](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-Prometheus-Compatible-Apis.html) in the *Amazon Managed Service for Prometheus User Guide*.

If your workspace uses customer-managed AWS KMS keys for encryption, you must grant the principals in your resource-based policy access to those AWS KMS keys. You can do this by creating AWS KMS grants. For more information, see [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) in the *AWS KMS API Reference* and [Encryption at rest](https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html) in the *Amazon Managed Service for Prometheus User Guide*.

For more information about working with IAM, see [Using Amazon Managed Service for Prometheus with IAM](https://docs.aws.amazon.com/prometheus/latest/userguide/security_iam_service-with-iam.html) in the *Amazon Managed Service for Prometheus User Guide*.

## Syntax
<a name="aws-resource-aps-resourcepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-aps-resourcepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::APS::ResourcePolicy",
  "Properties" : {
      "[PolicyDocument](#cfn-aps-resourcepolicy-policydocument)" : {{String}},
      "[WorkspaceArn](#cfn-aps-resourcepolicy-workspacearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-aps-resourcepolicy-syntax.yaml"></a>

```
Type: AWS::APS::ResourcePolicy
Properties:
  [PolicyDocument](#cfn-aps-resourcepolicy-policydocument): {{String}}
  [WorkspaceArn](#cfn-aps-resourcepolicy-workspacearn): {{String}}
```

## Properties
<a name="aws-resource-aps-resourcepolicy-properties"></a>

`PolicyDocument`  <a name="cfn-aps-resourcepolicy-policydocument"></a>
The JSON to use as the Resource-based Policy.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceArn`  <a name="cfn-aps-resourcepolicy-workspacearn"></a>
An ARN identifying a Workspace.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):aps:[a-z0-9-]+:[0-9]+:workspace/[a-zA-Z0-9-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-aps-resourcepolicy-return-values"></a>

### Ref
<a name="aws-resource-aps-resourcepolicy-return-values-ref"></a>

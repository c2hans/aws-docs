---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-signer-signingjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Signer::SigningJob
<a name="aws-resource-signer-signingjob"></a>

Contains information about a signing job.

## Syntax
<a name="aws-resource-signer-signingjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-signer-signingjob-syntax.json"></a>

```
{
  "Type" : "AWS::Signer::SigningJob",
  "Properties" : {
      "[ProfileName](#cfn-signer-signingjob-profilename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-signer-signingjob-syntax.yaml"></a>

```
Type: AWS::Signer::SigningJob
Properties:
  [ProfileName](#cfn-signer-signingjob-profilename): {{String}}
```

## Properties
<a name="aws-resource-signer-signingjob-properties"></a>

`ProfileName`  <a name="cfn-signer-signingjob-profilename"></a>
The name of the signing profile that created a signing job.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_]{2,}$`
*Minimum*: `2`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-signer-signingjob-return-values"></a>

### Ref
<a name="aws-resource-signer-signingjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-signer-signingjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-signer-signingjob-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CompletedAt`  <a name="CompletedAt-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the signing job was created.

`JobId`  <a name="JobId-fn::getatt"></a>
The ID of the signing job.

`JobInvoker`  <a name="JobInvoker-fn::getatt"></a>
The AWS account ID of the job invoker.

`JobOwner`  <a name="JobOwner-fn::getatt"></a>
The AWS account ID of the job owner.

`PlatformDisplayName`  <a name="PlatformDisplayName-fn::getatt"></a>
The name of a signing platform.

`PlatformId`  <a name="PlatformId-fn::getatt"></a>
The unique identifier for a signing platform.

`ProfileVersion`  <a name="ProfileVersion-fn::getatt"></a>
The version of the signing profile that created a signing job.

`RequestedBy`  <a name="RequestedBy-fn::getatt"></a>
Property description not available.

`SignatureExpiresAt`  <a name="SignatureExpiresAt-fn::getatt"></a>
The time when the signature of a signing job expires.

`Status`  <a name="Status-fn::getatt"></a>
The status of the signing job.

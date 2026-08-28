---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpoolreplica.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolReplica
<a name="aws-resource-cognito-userpoolreplica"></a>

Creates a replica of an existing user pool in a specified AWS Region. The replica enables multi-region replication for high availability and disaster recovery. To create a replica, you must have permissions to create user pools in the target Region.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Syntax
<a name="aws-resource-cognito-userpoolreplica-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cognito-userpoolreplica-syntax.json"></a>

```
{
  "Type" : "AWS::Cognito::UserPoolReplica",
  "Properties" : {
      "[RegionName](#cfn-cognito-userpoolreplica-regionname)" : {{String}},
      "[UserPoolId](#cfn-cognito-userpoolreplica-userpoolid)" : {{String}},
      "[UserPoolTagsAtCreate](#cfn-cognito-userpoolreplica-userpooltagsatcreate)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-cognito-userpoolreplica-syntax.yaml"></a>

```
Type: AWS::Cognito::UserPoolReplica
Properties:
  [RegionName](#cfn-cognito-userpoolreplica-regionname): {{String}}
  [UserPoolId](#cfn-cognito-userpoolreplica-userpoolid): {{String}}
  [UserPoolTagsAtCreate](#cfn-cognito-userpoolreplica-userpooltagsatcreate): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-cognito-userpoolreplica-properties"></a>

`RegionName`  <a name="cfn-cognito-userpoolreplica-regionname"></a>
The AWS Region where the replica is located.
*Required*: Yes
*Type*: String
*Minimum*: `5`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserPoolId`  <a name="cfn-cognito-userpoolreplica-userpoolid"></a>
The ID of the user pool to replicate.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]+_[0-9a-zA-Z]+`
*Minimum*: `1`
*Maximum*: `55`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserPoolTagsAtCreate`  <a name="cfn-cognito-userpoolreplica-userpooltagsatcreate"></a>
A map of tags to assign to the replica user pool at creation. Each tag consists of a key and an optional value. You cannot modify tags through this resource after creation. To update tags on the replica, use the [UserPoolRegionalConfigurationAttachment](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolregionalconfigurationattachment.html) resource in the secondary Region.
*Required*: No
*Type*: Object of String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cognito-userpoolreplica-return-values"></a>

### Ref
<a name="aws-resource-cognito-userpoolreplica-return-values-ref"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

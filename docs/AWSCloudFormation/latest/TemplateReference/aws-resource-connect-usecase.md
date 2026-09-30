---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-usecase.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::UseCase
<a name="aws-resource-connect-usecase"></a>

Creates a use case for an integration association.

## Syntax
<a name="aws-resource-connect-usecase-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-usecase-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::UseCase",
  "Properties" : {
      "[InstanceId](#cfn-connect-usecase-instanceid)" : {{String}},
      "[IntegrationAssociationId](#cfn-connect-usecase-integrationassociationid)" : {{String}},
      "[Tags](#cfn-connect-usecase-tags)" : {{[ Tag, ... ]}},
      "[UseCaseType](#cfn-connect-usecase-usecasetype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-usecase-syntax.yaml"></a>

```
Type: AWS::Connect::UseCase
Properties:
  [InstanceId](#cfn-connect-usecase-instanceid): {{String}}
  [IntegrationAssociationId](#cfn-connect-usecase-integrationassociationid): {{String}}
  [Tags](#cfn-connect-usecase-tags): {{
    - Tag}}
  [UseCaseType](#cfn-connect-usecase-usecasetype): {{String}}
```

## Properties
<a name="aws-resource-connect-usecase-properties"></a>

`InstanceId`  <a name="cfn-connect-usecase-instanceid"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IntegrationAssociationId`  <a name="cfn-connect-usecase-integrationassociationid"></a>
The identifier for the integration association.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-connect-usecase-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-usecase-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseCaseType`  <a name="cfn-connect-usecase-usecasetype"></a>
The type of use case to associate to the integration association. Each integration association can have only one of each use case type.
*Required*: Yes
*Type*: String
*Allowed values*: `RULES_EVALUATION | CONNECT_CAMPAIGNS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-connect-usecase-return-values"></a>

### Ref
<a name="aws-resource-connect-usecase-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-connect-usecase-return-values-fn--getatt"></a>

####
<a name="aws-resource-connect-usecase-return-values-fn--getatt-fn--getatt"></a>

`UseCaseArn`  <a name="UseCaseArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the use case.

`UseCaseId`  <a name="UseCaseId-fn::getatt"></a>
The identifier for the use case.

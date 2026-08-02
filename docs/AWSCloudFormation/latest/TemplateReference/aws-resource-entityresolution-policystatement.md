---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-entityresolution-policystatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::PolicyStatement
<a name="aws-resource-entityresolution-policystatement"></a>

Adds a policy statement object. To retrieve a list of existing policy statements, use the `GetPolicy` API.

## Syntax
<a name="aws-resource-entityresolution-policystatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-entityresolution-policystatement-syntax.json"></a>

```
{
  "Type" : "AWS::EntityResolution::PolicyStatement",
  "Properties" : {
      "[Action](#cfn-entityresolution-policystatement-action)" : {{[ String, ... ]}},
      "[Arn](#cfn-entityresolution-policystatement-arn)" : {{String}},
      "[Condition](#cfn-entityresolution-policystatement-condition)" : {{String}},
      "[Effect](#cfn-entityresolution-policystatement-effect)" : {{String}},
      "[Principal](#cfn-entityresolution-policystatement-principal)" : {{[ String, ... ]}},
      "[StatementId](#cfn-entityresolution-policystatement-statementid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-entityresolution-policystatement-syntax.yaml"></a>

```
Type: AWS::EntityResolution::PolicyStatement
Properties:
  [Action](#cfn-entityresolution-policystatement-action): {{
    - String}}
  [Arn](#cfn-entityresolution-policystatement-arn): {{String}}
  [Condition](#cfn-entityresolution-policystatement-condition): {{String}}
  [Effect](#cfn-entityresolution-policystatement-effect): {{String}}
  [Principal](#cfn-entityresolution-policystatement-principal): {{
    - String}}
  [StatementId](#cfn-entityresolution-policystatement-statementid): {{String}}
```

## Properties
<a name="aws-resource-entityresolution-policystatement-properties"></a>

`Action`  <a name="cfn-entityresolution-policystatement-action"></a>
The action that the principal can use on the resource.
For example, `entityresolution:GetIdMappingJob`, `entityresolution:GetMatchingJob`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Arn`  <a name="cfn-entityresolution-policystatement-arn"></a>
The Amazon Resource Name (ARN) of the resource that will be accessed by the principal.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:((schemamapping|matchingworkflow|idmappingworkflow|idnamespace)/[a-zA-Z_0-9-]{1,255})$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Condition`  <a name="cfn-entityresolution-policystatement-condition"></a>
A set of condition keys that you can use in key policies.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `40960`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Effect`  <a name="cfn-entityresolution-policystatement-effect"></a>
Determines whether the permissions specified in the policy are to be allowed (`Allow`) or denied (`Deny`).
 If you set the value of the `effect` parameter to `Deny` for the `AddPolicyStatement` operation, you must also set the value of the `effect` parameter in the `policy` to `Deny` for the `PutPolicy` operation.
*Required*: No
*Type*: String
*Allowed values*: `Allow | Deny`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Principal`  <a name="cfn-entityresolution-policystatement-principal"></a>
The AWS service or AWS account that can access the resource defined as ARN.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatementId`  <a name="cfn-entityresolution-policystatement-statementid"></a>
A statement identifier that differentiates the statement from others in the same policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

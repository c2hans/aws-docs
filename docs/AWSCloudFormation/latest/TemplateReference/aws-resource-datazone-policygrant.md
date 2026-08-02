---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-policygrant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant
<a name="aws-resource-datazone-policygrant"></a>

Adds a policy grant (an authorization policy) to a specified entity, including domain units, environment blueprint configurations, or environment profiles.

## Syntax
<a name="aws-resource-datazone-policygrant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-policygrant-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::PolicyGrant",
  "Properties" : {
      "[Detail](#cfn-datazone-policygrant-detail)" : {{PolicyGrantDetail}},
      "[DomainIdentifier](#cfn-datazone-policygrant-domainidentifier)" : {{String}},
      "[EntityIdentifier](#cfn-datazone-policygrant-entityidentifier)" : {{String}},
      "[EntityType](#cfn-datazone-policygrant-entitytype)" : {{String}},
      "[PolicyType](#cfn-datazone-policygrant-policytype)" : {{String}},
      "[Principal](#cfn-datazone-policygrant-principal)" : {{PolicyGrantPrincipal}}
    }
}
```

### YAML
<a name="aws-resource-datazone-policygrant-syntax.yaml"></a>

```
Type: AWS::DataZone::PolicyGrant
Properties:
  [Detail](#cfn-datazone-policygrant-detail): {{
    PolicyGrantDetail}}
  [DomainIdentifier](#cfn-datazone-policygrant-domainidentifier): {{String}}
  [EntityIdentifier](#cfn-datazone-policygrant-entityidentifier): {{String}}
  [EntityType](#cfn-datazone-policygrant-entitytype): {{String}}
  [PolicyType](#cfn-datazone-policygrant-policytype): {{String}}
  [Principal](#cfn-datazone-policygrant-principal): {{
    PolicyGrantPrincipal}}
```

## Properties
<a name="aws-resource-datazone-policygrant-properties"></a>

`Detail`  <a name="cfn-datazone-policygrant-detail"></a>
The details of the policy grant member.
*Required*: No
*Type*: [PolicyGrantDetail](aws-properties-datazone-policygrant-policygrantdetail.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainIdentifier`  <a name="cfn-datazone-policygrant-domainidentifier"></a>
The ID of the domain where you want to add a policy grant.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EntityIdentifier`  <a name="cfn-datazone-policygrant-entityidentifier"></a>
The ID of the entity (resource) to which you want to add a policy grant.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EntityType`  <a name="cfn-datazone-policygrant-entitytype"></a>
The type of entity (resource) to which the grant is added.
*Required*: Yes
*Type*: String
*Allowed values*: `DOMAIN_UNIT | ENVIRONMENT_BLUEPRINT_CONFIGURATION | ENVIRONMENT_PROFILE | ASSET_TYPE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyType`  <a name="cfn-datazone-policygrant-policytype"></a>
The type of policy that you want to grant.
*Required*: Yes
*Type*: String
*Allowed values*: `CREATE_DOMAIN_UNIT | OVERRIDE_DOMAIN_UNIT_OWNERS | ADD_TO_PROJECT_MEMBER_POOL | OVERRIDE_PROJECT_OWNERS | CREATE_GLOSSARY | CREATE_FORM_TYPE | CREATE_ASSET_TYPE | CREATE_PROJECT | CREATE_ENVIRONMENT_PROFILE | DELEGATE_CREATE_ENVIRONMENT_PROFILE | CREATE_ENVIRONMENT | CREATE_ENVIRONMENT_FROM_BLUEPRINT | CREATE_PROJECT_FROM_PROJECT_PROFILE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Principal`  <a name="cfn-datazone-policygrant-principal"></a>
The principal of the policy grant member.
*Required*: No
*Type*: [PolicyGrantPrincipal](aws-properties-datazone-policygrant-policygrantprincipal.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-datazone-policygrant-return-values"></a>

### Ref
<a name="aws-resource-datazone-policygrant-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-datazone-policygrant-return-values-fn--getatt"></a>

####
<a name="aws-resource-datazone-policygrant-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Specifies the timestamp at which policy grant member was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
Specifies the user who created the policy grant member.

`GrantId`  <a name="GrantId-fn::getatt"></a>
The ID of the policy grant.

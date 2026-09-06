---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-policygrant-projectpolicygrantprincipal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant ProjectPolicyGrantPrincipal
<a name="aws-properties-datazone-policygrant-projectpolicygrantprincipal"></a>

The project policy grant principal.

## Syntax
<a name="aws-properties-datazone-policygrant-projectpolicygrantprincipal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-policygrant-projectpolicygrantprincipal-syntax.json"></a>

```
{
  "[ProjectDesignation](#cfn-datazone-policygrant-projectpolicygrantprincipal-projectdesignation)" : {{String}},
  "[ProjectGrantFilter](#cfn-datazone-policygrant-projectpolicygrantprincipal-projectgrantfilter)" : {{ProjectGrantFilter}},
  "[ProjectIdentifier](#cfn-datazone-policygrant-projectpolicygrantprincipal-projectidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-policygrant-projectpolicygrantprincipal-syntax.yaml"></a>

```
  [ProjectDesignation](#cfn-datazone-policygrant-projectpolicygrantprincipal-projectdesignation): {{String}}
  [ProjectGrantFilter](#cfn-datazone-policygrant-projectpolicygrantprincipal-projectgrantfilter): {{
    ProjectGrantFilter}}
  [ProjectIdentifier](#cfn-datazone-policygrant-projectpolicygrantprincipal-projectidentifier): {{String}}
```

## Properties
<a name="aws-properties-datazone-policygrant-projectpolicygrantprincipal-properties"></a>

`ProjectDesignation`  <a name="cfn-datazone-policygrant-projectpolicygrantprincipal-projectdesignation"></a>
The project designation of the project policy grant principal.
*Required*: No
*Type*: String
*Allowed values*: `OWNER | CONTRIBUTOR | PROJECT_CATALOG_STEWARD`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProjectGrantFilter`  <a name="cfn-datazone-policygrant-projectpolicygrantprincipal-projectgrantfilter"></a>
The project grant filter of the project policy grant principal.
*Required*: No
*Type*: [ProjectGrantFilter](aws-properties-datazone-policygrant-projectgrantfilter.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProjectIdentifier`  <a name="cfn-datazone-policygrant-projectpolicygrantprincipal-projectidentifier"></a>
The project ID of the project policy grant principal.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

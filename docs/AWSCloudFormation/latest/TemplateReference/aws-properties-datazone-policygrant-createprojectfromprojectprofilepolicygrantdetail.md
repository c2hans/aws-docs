---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-policygrant-createprojectfromprojectprofilepolicygrantdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant CreateProjectFromProjectProfilePolicyGrantDetail
<a name="aws-properties-datazone-policygrant-createprojectfromprojectprofilepolicygrantdetail"></a>

Specifies whether to create a project from project profile policy grant details.

## Syntax
<a name="aws-properties-datazone-policygrant-createprojectfromprojectprofilepolicygrantdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-policygrant-createprojectfromprojectprofilepolicygrantdetail-syntax.json"></a>

```
{
  "[IncludeChildDomainUnits](#cfn-datazone-policygrant-createprojectfromprojectprofilepolicygrantdetail-includechilddomainunits)" : {{Boolean}},
  "[ProjectProfiles](#cfn-datazone-policygrant-createprojectfromprojectprofilepolicygrantdetail-projectprofiles)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-datazone-policygrant-createprojectfromprojectprofilepolicygrantdetail-syntax.yaml"></a>

```
  [IncludeChildDomainUnits](#cfn-datazone-policygrant-createprojectfromprojectprofilepolicygrantdetail-includechilddomainunits): {{Boolean}}
  [ProjectProfiles](#cfn-datazone-policygrant-createprojectfromprojectprofilepolicygrantdetail-projectprofiles): {{
    - String}}
```

## Properties
<a name="aws-properties-datazone-policygrant-createprojectfromprojectprofilepolicygrantdetail-properties"></a>

`IncludeChildDomainUnits`  <a name="cfn-datazone-policygrant-createprojectfromprojectprofilepolicygrantdetail-includechilddomainunits"></a>
Specifies whether to include child domain units when creating a project from project profile policy grant details
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProjectProfiles`  <a name="cfn-datazone-policygrant-createprojectfromprojectprofilepolicygrantdetail-projectprofiles"></a>
Specifies project profiles when creating a project from project profile policy grant details
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

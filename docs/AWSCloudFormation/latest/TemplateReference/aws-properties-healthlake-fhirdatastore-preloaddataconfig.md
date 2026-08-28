---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::HealthLake::FHIRDatastore PreloadDataConfig
<a name="aws-properties-healthlake-fhirdatastore-preloaddataconfig"></a>

An optional parameter to preload (import) open source Synthea FHIR data upon creation of the data store.

## Syntax
<a name="aws-properties-healthlake-fhirdatastore-preloaddataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-healthlake-fhirdatastore-preloaddataconfig-syntax.json"></a>

```
{
  "[PreloadDataType](#cfn-healthlake-fhirdatastore-preloaddataconfig-preloaddatatype)" : {{String}}
}
```

### YAML
<a name="aws-properties-healthlake-fhirdatastore-preloaddataconfig-syntax.yaml"></a>

```
  [PreloadDataType](#cfn-healthlake-fhirdatastore-preloaddataconfig-preloaddatatype): {{String}}
```

## Properties
<a name="aws-properties-healthlake-fhirdatastore-preloaddataconfig-properties"></a>

`PreloadDataType`  <a name="cfn-healthlake-fhirdatastore-preloaddataconfig-preloaddatatype"></a>
The type of preloaded data. Only Synthea preloaded data is supported.
*Required*: Yes
*Type*: String
*Allowed values*: `SYNTHEA`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

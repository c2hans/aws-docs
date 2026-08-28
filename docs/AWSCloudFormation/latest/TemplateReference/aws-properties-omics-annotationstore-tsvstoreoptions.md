---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-annotationstore-tsvstoreoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::AnnotationStore TsvStoreOptions
<a name="aws-properties-omics-annotationstore-tsvstoreoptions"></a>

The store's parsing options.

## Syntax
<a name="aws-properties-omics-annotationstore-tsvstoreoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-annotationstore-tsvstoreoptions-syntax.json"></a>

```
{
  "[AnnotationType](#cfn-omics-annotationstore-tsvstoreoptions-annotationtype)" : {{String}},
  "[FormatToHeader](#cfn-omics-annotationstore-tsvstoreoptions-formattoheader)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Schema](#cfn-omics-annotationstore-tsvstoreoptions-schema)" : {{[ {{{Key}}: {{Value}}, ...}, ... ]}}
}
```

### YAML
<a name="aws-properties-omics-annotationstore-tsvstoreoptions-syntax.yaml"></a>

```
  [AnnotationType](#cfn-omics-annotationstore-tsvstoreoptions-annotationtype): {{String}}
  [FormatToHeader](#cfn-omics-annotationstore-tsvstoreoptions-formattoheader): {{
    {{Key}}: {{Value}}}}
  [Schema](#cfn-omics-annotationstore-tsvstoreoptions-schema): {{
    -
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-omics-annotationstore-tsvstoreoptions-properties"></a>

`AnnotationType`  <a name="cfn-omics-annotationstore-tsvstoreoptions-annotationtype"></a>
The store's annotation type.
*Required*: No
*Type*: String
*Allowed values*: `GENERIC | CHR_POS | CHR_POS_REF_ALT | CHR_START_END_ONE_BASE | CHR_START_END_REF_ALT_ONE_BASE | CHR_START_END_ZERO_BASE | CHR_START_END_REF_ALT_ZERO_BASE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FormatToHeader`  <a name="cfn-omics-annotationstore-tsvstoreoptions-formattoheader"></a>
The store's header key to column name mapping.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Schema`  <a name="cfn-omics-annotationstore-tsvstoreoptions-schema"></a>
The schema of an annotation store.
*Required*: No
*Type*: Array of Object
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

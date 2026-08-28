---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_IntArrayOptions.html
---

# IntArrayOptions
<a name="API_IntArrayOptions"></a>

## Description
<a name="API_IntArrayOptions_Description"></a>

Options for a field that contains an array of 64-bit signed integers. Present if `IndexFieldType` specifies the field is of type `int-array`. All options are enabled by default.

## Contents
<a name="API_IntArrayOptions_Contents"></a>

 **DefaultValue**
 A value to use for the field if the field isn't specified for a document.
Type: Long
 Required: No

 **FacetEnabled**
Whether facet information can be returned for the field.
Type: Boolean
 Required: No

 **ReturnEnabled**
Whether the contents of the field can be returned in the search results.
Type: Boolean
 Required: No

 **SearchEnabled**
Whether the contents of the field are searchable.
Type: Boolean
 Required: No

 **SourceFields**
A list of source fields to map to the field.
Type: String
 Required: No

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

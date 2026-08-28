---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_HITLayoutParameterArticle.html
---

# HITLayoutParameter
<a name="ApiReference_HITLayoutParameterArticle"></a>

## Description
<a name="ApiReference_HITLayoutParameterArticle-description"></a>

The `HITLayoutParameter` data structure defines parameter values used with a HITLayout. A HITLayout is a reusable Amazon Mechanical Turk project template used to provide Human Intelligence Task (HIT) question data for `CreateHIT`. For more information, see [HITLayout](ApiReference_HITLayoutArticle.md).

The `HITLayoutParameter` data structure is used in the results of the following operation:
+  [CreateHIT](ApiReference_CreateHITOperation.md)

**Tip**
The [HITLayout](ApiReference_HITLayoutArticle.md) is used to create an HTMLQuestion document. HITLayoutParameter values with reserved characters or invalid HTML markup may result in an invalid HTMLQuestion document.

## Elements
<a name="ApiReference_HITLayoutParameterArticle-the-HITLayoutParameter-data-structure"></a>

The `HITLayout` data structure has a root element of `HITLayoutParameter`.

The `HITLayoutParameter` element contains the following elements:

| Name | Description | Required |
| --- | --- | --- |
|  `Name`  | The name of the parameter in the HITLayout.<br />Type: String<br />Default: None<br />Constraints: Parameter names supplied in a HITLayoutParameter structure must be used in the referenced HITLayout. | Yes |
|  `Value`  | The value substituted for the parameter referenced in the HITLayout. <br />Type: String<br />Default: None | Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

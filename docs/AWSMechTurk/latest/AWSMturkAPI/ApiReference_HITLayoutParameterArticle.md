---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_HITLayoutParameterArticle.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

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

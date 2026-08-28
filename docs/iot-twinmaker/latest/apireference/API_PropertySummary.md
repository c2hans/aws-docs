---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertySummary.html
---

# PropertySummary
<a name="API_PropertySummary"></a>

This is an object that contains the information of a property.

## Contents
<a name="API_PropertySummary_Contents"></a>

 ** propertyName **   <a name="tm-Type-PropertySummary-propertyName"></a>
This is the name of the property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\-0-9]+`
Required: Yes

 ** areAllPropertyValuesReturned **   <a name="tm-Type-PropertySummary-areAllPropertyValuesReturned"></a>
This flag notes whether all values of a list or map type property are returned in the API response. The maximum number of values per property returned is 50.
Type: Boolean
Required: No

 ** definition **   <a name="tm-Type-PropertySummary-definition"></a>
This is the schema for the property.
Type: [PropertyDefinitionResponse](API_PropertyDefinitionResponse.md) object
Required: No

 ** value **   <a name="tm-Type-PropertySummary-value"></a>
This is the value for the property.
Type: [DataValue](API_DataValue.md) object
Required: No

## See Also
<a name="API_PropertySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/PropertySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/PropertySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/PropertySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

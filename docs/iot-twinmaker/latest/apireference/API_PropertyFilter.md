---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyFilter.html
---

# PropertyFilter
<a name="API_PropertyFilter"></a>

An object that filters items returned by a property request.

## Contents
<a name="API_PropertyFilter_Contents"></a>

 ** operator **   <a name="tm-Type-PropertyFilter-operator"></a>
The operator associated with this property filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** propertyName **   <a name="tm-Type-PropertyFilter-propertyName"></a>
The property name associated with this property filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** value **   <a name="tm-Type-PropertyFilter-value"></a>
The value associated with this property filter.
Type: [DataValue](API_DataValue.md) object
Required: No

## See Also
<a name="API_PropertyFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/PropertyFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/PropertyFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/PropertyFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyValueHistory.html
---

# PropertyValueHistory
<a name="API_PropertyValueHistory"></a>

The history of values for a time series property.

## Contents
<a name="API_PropertyValueHistory_Contents"></a>

 ** entityPropertyReference **   <a name="tm-Type-PropertyValueHistory-entityPropertyReference"></a>
An object that uniquely identifies an entity property.
Type: [EntityPropertyReference](API_EntityPropertyReference.md) object
Required: Yes

 ** values **   <a name="tm-Type-PropertyValueHistory-values"></a>
A list of objects that contain information about the values in the history of a time series property.
Type: Array of [PropertyValue](API_PropertyValue.md) objects
Required: No

## See Also
<a name="API_PropertyValueHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/PropertyValueHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/PropertyValueHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/PropertyValueHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

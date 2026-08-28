---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AssetPropertyValue.html
---

# AssetPropertyValue
<a name="API_AssetPropertyValue"></a>

An asset property value entry containing the following information.

## Contents
<a name="API_AssetPropertyValue_Contents"></a>

 ** timestamp **   <a name="iot-Type-AssetPropertyValue-timestamp"></a>
The asset property value timestamp.
Type: [AssetPropertyTimestamp](API_AssetPropertyTimestamp.md) object
Required: Yes

 ** value **   <a name="iot-Type-AssetPropertyValue-value"></a>
The value of the asset property.
Type: [AssetPropertyVariant](API_AssetPropertyVariant.md) object
Required: Yes

 ** quality **   <a name="iot-Type-AssetPropertyValue-quality"></a>
Optional. A string that describes the quality of the value. Accepts substitution templates. Must be `GOOD`, `BAD`, or `UNCERTAIN`.
Type: String
Required: No

## See Also
<a name="API_AssetPropertyValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AssetPropertyValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AssetPropertyValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AssetPropertyValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

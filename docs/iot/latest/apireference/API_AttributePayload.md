---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AttributePayload.html
---

# AttributePayload
<a name="API_AttributePayload"></a>

The attribute payload.

## Contents
<a name="API_AttributePayload_Contents"></a>

 ** attributes **   <a name="iot-Type-AttributePayload-attributes"></a>
A JSON string containing up to three key-value pair in JSON format. For example:
 `{\"attributes\":{\"string1\":\"string2\"}}`
Type: String to string map
Key Length Constraints: Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_.,@/:#-]+`
Value Length Constraints: Maximum length of 800.
Value Pattern: `[a-zA-Z0-9_.,@/:#=\[\]-]*`
Required: No

 ** merge **   <a name="iot-Type-AttributePayload-merge"></a>
Specifies whether the list of attributes provided in the `AttributePayload` is merged with the attributes stored in the registry, instead of overwriting them.
To remove an attribute, call `UpdateThing` with an empty attribute value.
The `merge` attribute is only valid when calling `UpdateThing` or `UpdateThingGroup`.
Type: Boolean
Required: No

## See Also
<a name="API_AttributePayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AttributePayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AttributePayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AttributePayload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

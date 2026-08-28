---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_CustomOutputConfiguration.html
---

# CustomOutputConfiguration
<a name="API_CustomOutputConfiguration"></a>

The configuration for a `CUSTOM_OUTPUT` function. MediaTailor evaluates the output expressions against the current session state and commits the results as output bindings. `CUSTOM_OUTPUT` functions do not make external calls. For more information, see [CUSTOM\_OUTPUT](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types-custom-output.html) in the *MediaTailor User Guide*.

## Contents
<a name="API_CustomOutputConfiguration_Contents"></a>

 ** Runtime **   <a name="mediatailor-Type-CustomOutputConfiguration-Runtime"></a>
The expression language used to evaluate expressions in the function configuration. Set this to `JSONata`.
Type: String
Valid Values: `JSONATA`
Required: Yes

 ** Output **   <a name="mediatailor-Type-CustomOutputConfiguration-Output"></a>
A map of output bindings. Each key is a namespaced output path (such as `player_params.device_type` or `temp.variant`), and each value is an expression that MediaTailor evaluates at runtime against the current session state. For more information about expression syntax, see [JSONata expression reference](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-jsonata.html) in the *MediaTailor User Guide*.
Type: String to string map
Required: No

## See Also
<a name="API_CustomOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/CustomOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/CustomOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/CustomOutputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

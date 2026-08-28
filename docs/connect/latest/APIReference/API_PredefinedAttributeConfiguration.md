---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PredefinedAttributeConfiguration.html
---

# PredefinedAttributeConfiguration
<a name="API_PredefinedAttributeConfiguration"></a>

Custom metadata that is associated to predefined attributes to control behavior in upstream services, such as controlling how a predefined attribute should be displayed in the Connect Customer admin website.

## Contents
<a name="API_PredefinedAttributeConfiguration_Contents"></a>

 ** EnableValueValidationOnAssociation **   <a name="connect-Type-PredefinedAttributeConfiguration-EnableValueValidationOnAssociation"></a>
When this parameter is set to true, Connect Customer enforces strict validation on the specific values, if the values are predefined in attributes. The contact will store only valid and predefined values for teh predefined attribute key.
Type: Boolean
Required: No

 ** IsReadOnly **   <a name="connect-Type-PredefinedAttributeConfiguration-IsReadOnly"></a>
A boolean flag used to indicate whether a predefined attribute should be displayed in the Connect Customer admin website.
Type: Boolean
Required: No

## See Also
<a name="API_PredefinedAttributeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PredefinedAttributeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PredefinedAttributeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PredefinedAttributeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

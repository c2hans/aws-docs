---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_StartCodegenJobData.html
---

# StartCodegenJobData
<a name="API_StartCodegenJobData"></a>

The code generation job resource configuration.

## Contents
<a name="API_StartCodegenJobData_Contents"></a>

 ** renderConfig **   <a name="amplifyuibuilder-Type-StartCodegenJobData-renderConfig"></a>
The code generation configuration for the codegen job.
Type: [CodegenJobRenderConfig](API_CodegenJobRenderConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** autoGenerateForms **   <a name="amplifyuibuilder-Type-StartCodegenJobData-autoGenerateForms"></a>
Specifies whether to autogenerate forms in the code generation job.
Type: Boolean
Required: No

 ** features **   <a name="amplifyuibuilder-Type-StartCodegenJobData-features"></a>
The feature flags for a code generation job.
Type: [CodegenFeatureFlags](API_CodegenFeatureFlags.md) object
Required: No

 ** genericDataSchema **   <a name="amplifyuibuilder-Type-StartCodegenJobData-genericDataSchema"></a>
The data schema to use for a code generation job.
Type: [CodegenJobGenericDataSchema](API_CodegenJobGenericDataSchema.md) object
Required: No

 ** tags **   <a name="amplifyuibuilder-Type-StartCodegenJobData-tags"></a>
One or more key-value pairs to use when tagging the code generation job data.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_StartCodegenJobData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/StartCodegenJobData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/StartCodegenJobData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/StartCodegenJobData)

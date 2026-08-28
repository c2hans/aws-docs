---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenJob.html
---

# CodegenJob
<a name="API_CodegenJob"></a>

Describes the configuration for a code generation job that is associated with an Amplify app.

## Contents
<a name="API_CodegenJob_Contents"></a>

 ** appId **   <a name="amplifyuibuilder-Type-CodegenJob-appId"></a>
The ID of the Amplify app associated with the code generation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `d[a-z0-9]+`
Required: Yes

 ** environmentName **   <a name="amplifyuibuilder-Type-CodegenJob-environmentName"></a>
The name of the backend environment associated with the code generation job.
Type: String
Required: Yes

 ** id **   <a name="amplifyuibuilder-Type-CodegenJob-id"></a>
The unique ID for the code generation job.
Type: String
Required: Yes

 ** asset **   <a name="amplifyuibuilder-Type-CodegenJob-asset"></a>
The `CodegenJobAsset` to use for the code generation job.
Type: [CodegenJobAsset](API_CodegenJobAsset.md) object
Required: No

 ** autoGenerateForms **   <a name="amplifyuibuilder-Type-CodegenJob-autoGenerateForms"></a>
Specifies whether to autogenerate forms in the code generation job.
Type: Boolean
Required: No

 ** createdAt **   <a name="amplifyuibuilder-Type-CodegenJob-createdAt"></a>
The time that the code generation job was created.
Type: Timestamp
Required: No

 ** dependencies **   <a name="amplifyuibuilder-Type-CodegenJob-dependencies"></a>
Lists the dependency packages that may be required for the project code to run.
Type: Array of [CodegenDependency](API_CodegenDependency.md) objects
Required: No

 ** features **   <a name="amplifyuibuilder-Type-CodegenJob-features"></a>
Describes the feature flags that you can specify for a code generation job.
Type: [CodegenFeatureFlags](API_CodegenFeatureFlags.md) object
Required: No

 ** genericDataSchema **   <a name="amplifyuibuilder-Type-CodegenJob-genericDataSchema"></a>
Describes the data schema for a code generation job.
Type: [CodegenJobGenericDataSchema](API_CodegenJobGenericDataSchema.md) object
Required: No

 ** modifiedAt **   <a name="amplifyuibuilder-Type-CodegenJob-modifiedAt"></a>
The time that the code generation job was modified.
Type: Timestamp
Required: No

 ** renderConfig **   <a name="amplifyuibuilder-Type-CodegenJob-renderConfig"></a>
Describes the configuration information for rendering the UI component associated with the code generation job.
Type: [CodegenJobRenderConfig](API_CodegenJobRenderConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** status **   <a name="amplifyuibuilder-Type-CodegenJob-status"></a>
The status of the code generation job.
Type: String
Valid Values: `in_progress | failed | succeeded`
Required: No

 ** statusMessage **   <a name="amplifyuibuilder-Type-CodegenJob-statusMessage"></a>
The customized status message for the code generation job.
Type: String
Required: No

 ** tags **   <a name="amplifyuibuilder-Type-CodegenJob-tags"></a>
One or more key-value pairs to use when tagging the code generation job.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_CodegenJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/CodegenJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/CodegenJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/CodegenJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

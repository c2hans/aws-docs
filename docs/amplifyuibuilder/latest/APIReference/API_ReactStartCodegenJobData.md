---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ReactStartCodegenJobData.html
---

# ReactStartCodegenJobData
<a name="API_ReactStartCodegenJobData"></a>

Describes the code generation job configuration for a React project.

## Contents
<a name="API_ReactStartCodegenJobData_Contents"></a>

 ** apiConfiguration **   <a name="amplifyuibuilder-Type-ReactStartCodegenJobData-apiConfiguration"></a>
The API configuration for the code generation job.
Type: [ApiConfiguration](API_ApiConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** dependencies **   <a name="amplifyuibuilder-Type-ReactStartCodegenJobData-dependencies"></a>
Lists the dependency packages that may be required for the project code to run.
Type: String to string map
Required: No

 ** inlineSourceMap **   <a name="amplifyuibuilder-Type-ReactStartCodegenJobData-inlineSourceMap"></a>
Specifies whether the code generation job should render inline source maps.
Type: Boolean
Required: No

 ** module **   <a name="amplifyuibuilder-Type-ReactStartCodegenJobData-module"></a>
The JavaScript module type.
Type: String
Valid Values: `es2020 | esnext`
Required: No

 ** renderTypeDeclarations **   <a name="amplifyuibuilder-Type-ReactStartCodegenJobData-renderTypeDeclarations"></a>
Specifies whether the code generation job should render type declaration files.
Type: Boolean
Required: No

 ** script **   <a name="amplifyuibuilder-Type-ReactStartCodegenJobData-script"></a>
The file type to use for a JavaScript project.
Type: String
Valid Values: `jsx | tsx | js`
Required: No

 ** target **   <a name="amplifyuibuilder-Type-ReactStartCodegenJobData-target"></a>
The ECMAScript specification to use.
Type: String
Valid Values: `es2015 | es2020`
Required: No

## See Also
<a name="API_ReactStartCodegenJobData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/ReactStartCodegenJobData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/ReactStartCodegenJobData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/ReactStartCodegenJobData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

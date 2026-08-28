---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_FormSummary.html
---

# FormSummary
<a name="API_FormSummary"></a>

Describes the basic information about a form.

## Contents
<a name="API_FormSummary_Contents"></a>

 ** appId **   <a name="amplifyuibuilder-Type-FormSummary-appId"></a>
The unique ID for the app associated with the form summary.
Type: String
Required: Yes

 ** dataType **   <a name="amplifyuibuilder-Type-FormSummary-dataType"></a>
The form's data source type.
Type: [FormDataTypeConfig](API_FormDataTypeConfig.md) object
Required: Yes

 ** environmentName **   <a name="amplifyuibuilder-Type-FormSummary-environmentName"></a>
The name of the backend environment that is part of the Amplify app.
Type: String
Required: Yes

 ** formActionType **   <a name="amplifyuibuilder-Type-FormSummary-formActionType"></a>
The type of operation to perform on the form.
Type: String
Valid Values: `create | update`
Required: Yes

 ** id **   <a name="amplifyuibuilder-Type-FormSummary-id"></a>
The ID of the form.
Type: String
Required: Yes

 ** name **   <a name="amplifyuibuilder-Type-FormSummary-name"></a>
The name of the form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_FormSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/FormSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/FormSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/FormSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

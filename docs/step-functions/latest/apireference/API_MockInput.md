---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_MockInput.html
---

# MockInput
<a name="API_MockInput"></a>

A JSON object that contains a mocked `result` or `errorOutput`.

## Contents
<a name="API_MockInput_Contents"></a>

 ** errorOutput **   <a name="StepFunctions-Type-MockInput-errorOutput"></a>
The mocked error output when calling TestState. When specified, the mocked response is returned as a JSON object that contains an `error` and `cause` field.
Type: [MockErrorOutput](API_MockErrorOutput.md) object
Required: No

 ** fieldValidationMode **   <a name="StepFunctions-Type-MockInput-fieldValidationMode"></a>
Determines the level of strictness when validating mocked results against their respective API models. Values include:
+  `STRICT`: All required fields must be present, and all present fields must conform to the API's schema.
+  `PRESENT`: All present fields must conform to the API's schema.
+  `NONE`: No validation is performed.
If no value is specified, the default value is `STRICT`.
Type: String
Valid Values: `STRICT | PRESENT | NONE`
Required: No

 ** result **   <a name="StepFunctions-Type-MockInput-result"></a>
A JSON string containing the mocked result of the state invocation.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

## See Also
<a name="API_MockInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/MockInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/MockInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/MockInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

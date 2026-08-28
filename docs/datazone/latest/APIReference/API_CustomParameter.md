---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CustomParameter.html
---

# CustomParameter
<a name="API_CustomParameter"></a>

The details of user parameters of an environment blueprint.

## Contents
<a name="API_CustomParameter_Contents"></a>

 ** fieldType **   <a name="datazone-Type-CustomParameter-fieldType"></a>
The filed type of the parameter.
Type: String
Required: Yes

 ** keyName **   <a name="datazone-Type-CustomParameter-keyName"></a>
The key name of the parameter.
Type: String
Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Required: Yes

 ** defaultValue **   <a name="datazone-Type-CustomParameter-defaultValue"></a>
The default value of the parameter.
Type: String
Required: No

 ** description **   <a name="datazone-Type-CustomParameter-description"></a>
The description of the parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** isEditable **   <a name="datazone-Type-CustomParameter-isEditable"></a>
Specifies whether the parameter is editable.
Type: Boolean
Required: No

 ** isOptional **   <a name="datazone-Type-CustomParameter-isOptional"></a>
Specifies whether the custom parameter is optional.
Type: Boolean
Required: No

 ** isUpdateSupported **   <a name="datazone-Type-CustomParameter-isUpdateSupported"></a>
Specifies whether a parameter value can be updated after creation.
Type: Boolean
Required: No

## See Also
<a name="API_CustomParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CustomParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CustomParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CustomParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

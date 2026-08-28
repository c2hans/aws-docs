---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_BatchGetAttributeOutput.html
---

# BatchGetAttributeOutput
<a name="API_BatchGetAttributeOutput"></a>

The results of the BatchGetAttribute action.

## Contents
<a name="API_BatchGetAttributeOutput_Contents"></a>

 ** attributeIdentifier **   <a name="datazone-Type-BatchGetAttributeOutput-attributeIdentifier"></a>
The attribute ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** forms **   <a name="datazone-Type-BatchGetAttributeOutput-forms"></a>
The metadata forms that are part of the results of the BatchGetAttribute action.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_BatchGetAttributeOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/BatchGetAttributeOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/BatchGetAttributeOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/BatchGetAttributeOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

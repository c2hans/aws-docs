---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_VeevaSourceProperties.html
---

# VeevaSourceProperties
<a name="API_VeevaSourceProperties"></a>

 The properties that are applied when using Veeva as a flow source.

## Contents
<a name="API_VeevaSourceProperties_Contents"></a>

 ** object **   <a name="appflow-Type-VeevaSourceProperties-object"></a>
 The object specified in the Veeva flow source.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** documentType **   <a name="appflow-Type-VeevaSourceProperties-documentType"></a>
The document type specified in the Veeva document extract flow.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\w_-]+`
Required: No

 ** includeAllVersions **   <a name="appflow-Type-VeevaSourceProperties-includeAllVersions"></a>
Boolean value to include All Versions of files in Veeva document extract flow.
Type: Boolean
Required: No

 ** includeRenditions **   <a name="appflow-Type-VeevaSourceProperties-includeRenditions"></a>
Boolean value to include file renditions in Veeva document extract flow.
Type: Boolean
Required: No

 ** includeSourceFiles **   <a name="appflow-Type-VeevaSourceProperties-includeSourceFiles"></a>
Boolean value to include source files in Veeva document extract flow.
Type: Boolean
Required: No

## See Also
<a name="API_VeevaSourceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/VeevaSourceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/VeevaSourceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/VeevaSourceProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

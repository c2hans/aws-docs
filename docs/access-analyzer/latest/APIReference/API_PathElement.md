---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_PathElement.html
---

# PathElement
<a name="API_PathElement"></a>

A single element in a path through the JSON representation of a policy.

## Contents
<a name="API_PathElement_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** index **   <a name="accessanalyzer-Type-PathElement-index"></a>
Refers to an index in a JSON array.
Type: Integer
Required: No

 ** key **   <a name="accessanalyzer-Type-PathElement-key"></a>
Refers to a key in a JSON object.
Type: String
Required: No

 ** substring **   <a name="accessanalyzer-Type-PathElement-substring"></a>
Refers to a substring of a literal string in a JSON object.
Type: [Substring](API_Substring.md) object
Required: No

 ** value **   <a name="accessanalyzer-Type-PathElement-value"></a>
Refers to the value associated with a given key in a JSON object.
Type: String
Required: No

## See Also
<a name="API_PathElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/PathElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/PathElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/PathElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

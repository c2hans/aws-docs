---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Location.html
---

# Location
<a name="API_Location"></a>

A location in a policy that is represented as a path through the JSON representation and a corresponding span.

## Contents
<a name="API_Location_Contents"></a>

 ** path **   <a name="accessanalyzer-Type-Location-path"></a>
A path in a policy, represented as a sequence of path elements.
Type: Array of [PathElement](API_PathElement.md) objects
Required: Yes

 ** span **   <a name="accessanalyzer-Type-Location-span"></a>
A span in a policy.
Type: [Span](API_Span.md) object
Required: Yes

## See Also
<a name="API_Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/Location)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

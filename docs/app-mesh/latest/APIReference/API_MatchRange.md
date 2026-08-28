---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_MatchRange.html
---

# MatchRange
<a name="API_MatchRange"></a>

An object that represents the range of values to match on. The first character of the range is included in the range, though the last character is not. For example, if the range specified were 1-100, only values 1-99 would be matched.

## Contents
<a name="API_MatchRange_Contents"></a>

 ** end **   <a name="appmesh-Type-MatchRange-end"></a>
The end of the range.
Type: Long
Required: Yes

 ** start **   <a name="appmesh-Type-MatchRange-start"></a>
The start of the range.
Type: Long
Required: Yes

## See Also
<a name="API_MatchRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/MatchRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/MatchRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/MatchRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_HttpMatch.html
---

# HttpMatch
<a name="API_HttpMatch"></a>

Describes criteria that can be applied to incoming requests.

## Contents
<a name="API_HttpMatch_Contents"></a>

 ** headerMatches **   <a name="vpclattice-Type-HttpMatch-headerMatches"></a>
The header matches. Matches incoming requests with rule based on request header value before applying rule action.
Type: Array of [HeaderMatch](API_HeaderMatch.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** method **   <a name="vpclattice-Type-HttpMatch-method"></a>
The HTTP method type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Required: No

 ** pathMatch **   <a name="vpclattice-Type-HttpMatch-pathMatch"></a>
The path match.
Type: [PathMatch](API_PathMatch.md) object
Required: No

## See Also
<a name="API_HttpMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/HttpMatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/HttpMatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/HttpMatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

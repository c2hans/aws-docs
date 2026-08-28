---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_PathMatchType.html
---

# PathMatchType
<a name="API_PathMatchType"></a>

Describes a path match type. Each rule can include only one of the following types of paths.

## Contents
<a name="API_PathMatchType_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** exact **   <a name="vpclattice-Type-PathMatchType-exact"></a>
An exact match of the path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `/[a-zA-Z0-9@:%_+.~#?&/=-]*`
Required: No

 ** prefix **   <a name="vpclattice-Type-PathMatchType-prefix"></a>
A prefix match of the path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `/[a-zA-Z0-9@:%_+.~#?&/=-]*`
Required: No

## See Also
<a name="API_PathMatchType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/PathMatchType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/PathMatchType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/PathMatchType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

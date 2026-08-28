---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GluePolicy.html
---

# GluePolicy
<a name="API_GluePolicy"></a>

A structure for returning a resource policy.

## Contents
<a name="API_GluePolicy_Contents"></a>

 ** CreateTime **   <a name="Glue-Type-GluePolicy-CreateTime"></a>
The date and time at which the policy was created.
Type: Timestamp
Required: No

 ** PolicyHash **   <a name="Glue-Type-GluePolicy-PolicyHash"></a>
Contains the hash value associated with this policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** PolicyInJson **   <a name="Glue-Type-GluePolicy-PolicyInJson"></a>
Contains the requested policy document, in JSON format.
Type: String
Length Constraints: Minimum length of 2.
Required: No

 ** UpdateTime **   <a name="Glue-Type-GluePolicy-UpdateTime"></a>
The date and time at which the policy was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_GluePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GluePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GluePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GluePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

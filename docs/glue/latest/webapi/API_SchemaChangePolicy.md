---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SchemaChangePolicy.html
---

# SchemaChangePolicy
<a name="API_SchemaChangePolicy"></a>

A policy that specifies update and deletion behaviors for the crawler.

## Contents
<a name="API_SchemaChangePolicy_Contents"></a>

 ** DeleteBehavior **   <a name="Glue-Type-SchemaChangePolicy-DeleteBehavior"></a>
The deletion behavior when the crawler finds a deleted object.
Type: String
Valid Values: `LOG | DELETE_FROM_DATABASE | DEPRECATE_IN_DATABASE`
Required: No

 ** UpdateBehavior **   <a name="Glue-Type-SchemaChangePolicy-UpdateBehavior"></a>
The update behavior when the crawler finds a changed schema.
Type: String
Valid Values: `LOG | UPDATE_IN_DATABASE`
Required: No

## See Also
<a name="API_SchemaChangePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SchemaChangePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SchemaChangePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SchemaChangePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UniqueTagResourceIdentifier.html
---

# UniqueTagResourceIdentifier
<a name="API_UniqueTagResourceIdentifier"></a>

 The unique key-value pair for a tag that identifies provisioned product resources.

## Contents
<a name="API_UniqueTagResourceIdentifier_Contents"></a>

 ** Key **   <a name="servicecatalog-Type-UniqueTagResourceIdentifier-Key"></a>
 A unique key that's attached to a resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Required: No

 ** Value **   <a name="servicecatalog-Type-UniqueTagResourceIdentifier-Value"></a>
 A unique value that's attached to a resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Required: No

## See Also
<a name="API_UniqueTagResourceIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/UniqueTagResourceIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/UniqueTagResourceIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/UniqueTagResourceIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

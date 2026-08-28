---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_TagQueryConfiguration.html
---

# TagQueryConfiguration
<a name="API_app-registry_TagQueryConfiguration"></a>

 The definition of `tagQuery`. Specifies which resources are associated with an application.

## Contents
<a name="API_app-registry_TagQueryConfiguration_Contents"></a>

 ** tagKey **   <a name="servicecatalog-Type-app-registry_TagQueryConfiguration-tagKey"></a>
 Condition in the IAM policy that associates resources to an application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^(?!\s+$)[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Required: No

## See Also
<a name="API_app-registry_TagQueryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/TagQueryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/TagQueryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/TagQueryConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

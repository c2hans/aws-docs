---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_FunctionConfig.html
---

# FunctionConfig
<a name="API_FunctionConfig"></a>

Contains configuration information about a CloudFront function.

## Contents
<a name="API_FunctionConfig_Contents"></a>

 ** Comment **   <a name="cloudfront-Type-FunctionConfig-Comment"></a>
A comment to describe the function. The comment cannot be longer than 128 characters.
Type: String
Required: Yes

 ** Runtime **   <a name="cloudfront-Type-FunctionConfig-Runtime"></a>
The function's runtime environment version.
Type: String
Valid Values: `cloudfront-js-1.0 | cloudfront-js-2.0`
Required: Yes

 ** KeyValueStoreAssociations **   <a name="cloudfront-Type-FunctionConfig-KeyValueStoreAssociations"></a>
The configuration for the key value store associations.
Type: [KeyValueStoreAssociations](API_KeyValueStoreAssociations.md) object
Required: No

## See Also
<a name="API_FunctionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FunctionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FunctionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FunctionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudfront_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Code examples for CloudFront using AWS SDKs
<a name="cloudfront_code_examples"></a>

The following code examples show you how to use Amazon CloudFront with an AWS software development kit (SDK).

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

**More resources**
+  **[ CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)** – More information about CloudFront.
+ **[CloudFront API Reference](https://docs.aws.amazon.com/cloudfront/latest/APIReference/Welcome.html)** – Details about all available CloudFront actions.
+ **[AWS Developer Center](https://aws.amazon.com/developer/code-examples/?awsf.sdk-code-examples-product=product%23cloudfront)** – Code examples that you can filter by category or full-text search.
+ **[AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)** – GitHub repo with complete code in preferred languages. Includes instructions for setting up and running the code.

**Contents**
+ [Basics](cloudfront_code_examples_basics.md)
  + [Actions](cloudfront_code_examples_actions.md)
    + [`CreateDistribution`](cloudfront_example_cloudfront_CreateDistribution_section.md)
    + [`CreateFunction`](cloudfront_example_cloudfront_CreateFunction_section.md)
    + [`CreateInvalidation`](cloudfront_example_cloudfront_CreateInvalidation_section.md)
    + [`CreateKeyGroup`](cloudfront_example_cloudfront_CreateKeyGroup_section.md)
    + [`CreatePublicKey`](cloudfront_example_cloudfront_CreatePublicKey_section.md)
    + [`DeleteDistribution`](cloudfront_example_cloudfront_DeleteDistribution_section.md)
    + [`GetCloudFrontOriginAccessIdentity`](cloudfront_example_cloudfront_GetCloudFrontOriginAccessIdentity_section.md)
    + [`GetCloudFrontOriginAccessIdentityConfig`](cloudfront_example_cloudfront_GetCloudFrontOriginAccessIdentityConfig_section.md)
    + [`GetDistribution`](cloudfront_example_cloudfront_GetDistribution_section.md)
    + [`GetDistributionConfig`](cloudfront_example_cloudfront_GetDistributionConfig_section.md)
    + [`ListCloudFrontOriginAccessIdentities`](cloudfront_example_cloudfront_ListCloudFrontOriginAccessIdentities_section.md)
    + [`ListDistributions`](cloudfront_example_cloudfront_ListDistributions_section.md)
    + [`UpdateDistribution`](cloudfront_example_cloudfront_UpdateDistribution_section.md)
+ [Scenarios](cloudfront_code_examples_scenarios.md)
  + [Create a multi-tenant distribution and distribution tenant](cloudfront_example_cloudfront_CreateSaasResources_section.md)
  + [Delete signing resources](cloudfront_example_cloudfront_DeleteSigningResources_section.md)
  + [Get started with a basic content distribution network](cloudfront_example_cloudfront_GettingStarted_section.md)
  + [Getting started with web application firewalls](cloudfront_example_wafv2_GettingStarted_052_section.md)
  + [Sign URLs and cookies](cloudfront_example_cloudfront_CloudFrontUtilities_section.md)
+ [CloudFront Functions examples](cloudfront_code_examples_cloudfront_functions_examples.md)
  + [Add HTTP security headers](cloudfront_example_cloudfront_functions_add_security_headers_section.md)
  + [Add a CORS header](cloudfront_example_cloudfront_functions_add_cors_header_section.md)
  + [Add a cache control header](cloudfront_example_cloudfront_functions_add_cache_control_header_section.md)
  + [Add a true client IP header](cloudfront_example_cloudfront_functions_add_true_client_ip_header_section.md)
  + [Add an origin header](cloudfront_example_cloudfront_functions_add_origin_header_section.md)
  + [Add index.html to request URLs](cloudfront_example_cloudfront_functions_url_rewrite_single_page_apps_section.md)
  + [Normalize query string parameters](cloudfront_example_cloudfront_functions_normalize_query_string_parameters_section.md)
  + [Redirect to a new URL](cloudfront_example_cloudfront_functions_redirect_based_on_country_section.md)
  + [Rewrite a request URI](cloudfront_example_cloudfront_functions_kvs_conditional_read_section.md)
  + [Select origin closer to the viewer](cloudfront_example_cloudfront_functions_select_origin_based_on_country_section.md)
  + [Use key-value pairs](cloudfront_example_cloudfront_functions_kvs_key_value_pairs_section.md)
  + [Validate a simple token](cloudfront_example_cloudfront_functions_kvs_jwt_verify_section.md)

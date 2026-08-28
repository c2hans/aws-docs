---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ProviderIntermediateDataAccessConfiguration.html
---

# ProviderIntermediateDataAccessConfiguration
<a name="API_ProviderIntermediateDataAccessConfiguration"></a>

The required configuration fields to give intermediate access to a provider service.

## Contents
<a name="API_ProviderIntermediateDataAccessConfiguration_Contents"></a>

 ** awsAccountIds **   <a name="API-Type-ProviderIntermediateDataAccessConfiguration-awsAccountIds"></a>
The AWS account that provider can use to read or write data into the customer's intermediate S3 bucket.
Type: Array of strings
Pattern: `\d{12}`
Required: No

 ** requiredBucketActions **   <a name="API-Type-ProviderIntermediateDataAccessConfiguration-requiredBucketActions"></a>
The S3 bucket actions that the provider requires permission for.
Type: Array of strings
Required: No

## See Also
<a name="API_ProviderIntermediateDataAccessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/ProviderIntermediateDataAccessConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/ProviderIntermediateDataAccessConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/ProviderIntermediateDataAccessConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CustomLogSourceConfiguration.html
---

# CustomLogSourceConfiguration
<a name="API_CustomLogSourceConfiguration"></a>

The configuration used for the third-party custom source.

## Contents
<a name="API_CustomLogSourceConfiguration_Contents"></a>

 ** crawlerConfiguration **   <a name="securitylake-Type-CustomLogSourceConfiguration-crawlerConfiguration"></a>
The configuration used for the Glue Crawler for a third-party custom source.
Type: [CustomLogSourceCrawlerConfiguration](API_CustomLogSourceCrawlerConfiguration.md) object
Required: Yes

 ** providerIdentity **   <a name="securitylake-Type-CustomLogSourceConfiguration-providerIdentity"></a>
The identity of the log provider for the third-party custom source.
Type: [AwsIdentity](API_AwsIdentity.md) object
Required: Yes

## See Also
<a name="API_CustomLogSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/CustomLogSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/CustomLogSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/CustomLogSourceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

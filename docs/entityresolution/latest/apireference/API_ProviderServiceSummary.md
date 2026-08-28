---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ProviderServiceSummary.html
---

# ProviderServiceSummary
<a name="API_ProviderServiceSummary"></a>

A list of `ProviderService` objects, each of which contain the fields `providerName`, `providerServiceArn`, `providerServiceName`, and `providerServiceType`.

## Contents
<a name="API_ProviderServiceSummary_Contents"></a>

 ** providerName **   <a name="API-Type-ProviderServiceSummary-providerName"></a>
The name of the provider. This name is typically the company name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

 ** providerServiceArn **   <a name="API-Type-ProviderServiceSummary-providerServiceArn"></a>
The ARN (Amazon Resource Name) that AWS Entity Resolution generated for the `providerService`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 255.
Pattern: `arn:(aws|aws-us-gov|aws-cn):(entityresolution):([a-z]{2}-[a-z]{1,10}-[0-9])::providerservice/([a-zA-Z0-9_-]{1,255})/([a-zA-Z0-9_-]{1,255})`
Required: Yes

 ** providerServiceDisplayName **   <a name="API-Type-ProviderServiceSummary-providerServiceDisplayName"></a>
The display name of the provider service.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: Yes

 ** providerServiceName **   <a name="API-Type-ProviderServiceSummary-providerServiceName"></a>
The name of the product that the provider service provides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

 ** providerServiceType **   <a name="API-Type-ProviderServiceSummary-providerServiceType"></a>
The type of provider service.
Type: String
Valid Values: `ASSIGNMENT | ID_MAPPING`
Required: Yes

## See Also
<a name="API_ProviderServiceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/ProviderServiceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/ProviderServiceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/ProviderServiceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

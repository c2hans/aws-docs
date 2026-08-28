---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationConformancePack.html
---

# OrganizationConformancePack
<a name="API_OrganizationConformancePack"></a>

An organization conformance pack that has information about conformance packs that AWS Config creates in member accounts.

## Contents
<a name="API_OrganizationConformancePack_Contents"></a>

 ** LastUpdateTime **   <a name="config-Type-OrganizationConformancePack-LastUpdateTime"></a>
Last time when organization conformation pack was updated.
Type: Timestamp
Required: Yes

 ** OrganizationConformancePackArn **   <a name="config-Type-OrganizationConformancePack-OrganizationConformancePackArn"></a>
Amazon Resource Name (ARN) of organization conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** OrganizationConformancePackName **   <a name="config-Type-OrganizationConformancePack-OrganizationConformancePackName"></a>
The name you assign to an organization conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: Yes

 ** ConformancePackInputParameters **   <a name="config-Type-OrganizationConformancePack-ConformancePackInputParameters"></a>
A list of `ConformancePackInputParameter` objects.
Type: Array of [ConformancePackInputParameter](API_ConformancePackInputParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 60 items.
Required: No

 ** DeliveryS3Bucket **   <a name="config-Type-OrganizationConformancePack-DeliveryS3Bucket"></a>
The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.
This field is optional.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Required: No

 ** DeliveryS3KeyPrefix **   <a name="config-Type-OrganizationConformancePack-DeliveryS3KeyPrefix"></a>
Any folder structure you want to add to an Amazon S3 bucket.
This field is optional.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ExcludedAccounts **   <a name="config-Type-OrganizationConformancePack-ExcludedAccounts"></a>
A comma-separated list of accounts excluded from organization conformance pack.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## See Also
<a name="API_OrganizationConformancePack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/OrganizationConformancePack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/OrganizationConformancePack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/OrganizationConformancePack)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

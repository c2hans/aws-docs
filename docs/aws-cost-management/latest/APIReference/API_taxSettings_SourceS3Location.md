---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_SourceS3Location.html
---

# SourceS3Location
<a name="API_taxSettings_SourceS3Location"></a>

The Amazon S3 bucket in your account where your tax document is located.

## Contents
<a name="API_taxSettings_SourceS3Location_Contents"></a>

 ** bucket **   <a name="awscostmanagement-Type-taxSettings_SourceS3Location-bucket"></a>
The name of your Amazon S3 bucket that your tax document is located.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?=^.{3,63}$)(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$)`
Required: Yes

 ** key **   <a name="awscostmanagement-Type-taxSettings_SourceS3Location-key"></a>
The object key of your tax document object in Amazon S3.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_taxSettings_SourceS3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/SourceS3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/SourceS3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/SourceS3Location)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

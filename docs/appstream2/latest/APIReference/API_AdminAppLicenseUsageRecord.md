---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AdminAppLicenseUsageRecord.html
---

# AdminAppLicenseUsageRecord
<a name="API_AdminAppLicenseUsageRecord"></a>

The collection of license usage records.

## Contents
<a name="API_AdminAppLicenseUsageRecord_Contents"></a>

 ** BillingPeriod **   <a name="WorkSpacesApplications-Type-AdminAppLicenseUsageRecord-BillingPeriod"></a>
The billing period for the license usage record.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** LicenseType **   <a name="WorkSpacesApplications-Type-AdminAppLicenseUsageRecord-LicenseType"></a>
The type of license (for example, Microsoft Office).
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** OwnerAWSAccountId **   <a name="WorkSpacesApplications-Type-AdminAppLicenseUsageRecord-OwnerAWSAccountId"></a>
The account ID of the owner of the license.
Type: String
Pattern: `^\d+$`
Required: Yes

 ** SubscriptionFirstUsedDate **   <a name="WorkSpacesApplications-Type-AdminAppLicenseUsageRecord-SubscriptionFirstUsedDate"></a>
The date and time when the license was first used.
Type: Timestamp
Required: Yes

 ** SubscriptionLastUsedDate **   <a name="WorkSpacesApplications-Type-AdminAppLicenseUsageRecord-SubscriptionLastUsedDate"></a>
The date and time when the license was last used.
Type: Timestamp
Required: Yes

 ** UserArn **   <a name="WorkSpacesApplications-Type-AdminAppLicenseUsageRecord-UserArn"></a>
The ARN of the user who used the license-included application.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** UserId **   <a name="WorkSpacesApplications-Type-AdminAppLicenseUsageRecord-UserId"></a>
The ID of the user who used the license-included application.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## See Also
<a name="API_AdminAppLicenseUsageRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/AdminAppLicenseUsageRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/AdminAppLicenseUsageRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/AdminAppLicenseUsageRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

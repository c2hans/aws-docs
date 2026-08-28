---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails.html
---

# AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails
<a name="API_AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails"></a>

Provides information about domain access control options.

## Contents
<a name="API_AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails_Contents"></a>

 ** Enabled **   <a name="securityhub-Type-AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails-Enabled"></a>
Enables fine-grained access control.
Type: Boolean
Required: No

 ** InternalUserDatabaseEnabled **   <a name="securityhub-Type-AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails-InternalUserDatabaseEnabled"></a>
Enables the internal user database.
Type: Boolean
Required: No

 ** MasterUserOptions **   <a name="securityhub-Type-AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails-MasterUserOptions"></a>
Specifies information about the master user of the domain.
Type: [AwsOpenSearchServiceDomainMasterUserOptionsDetails](API_AwsOpenSearchServiceDomainMasterUserOptionsDetails.md) object
Required: No

## See Also
<a name="API_AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAthenaWorkGroupConfigurationDetails.html
---

# AwsAthenaWorkGroupConfigurationDetails
<a name="API_AwsAthenaWorkGroupConfigurationDetails"></a>

 The configuration of the workgroup, which includes the location in Amazon Simple Storage Service (Amazon S3) where query results are stored, the encryption option, if any, used for query results, whether Amazon CloudWatch metrics are enabled for the workgroup, and the limit for the amount of bytes scanned (cutoff) per query, if it is specified.

## Contents
<a name="API_AwsAthenaWorkGroupConfigurationDetails_Contents"></a>

 ** ResultConfiguration **   <a name="securityhub-Type-AwsAthenaWorkGroupConfigurationDetails-ResultConfiguration"></a>
 The location in Amazon S3 where query and calculation results are stored and the encryption option, if any, used for query and calculation results. These are known as client-side settings. If workgroup settings override client-side settings, then the query uses the workgroup settings.
Type: [AwsAthenaWorkGroupConfigurationResultConfigurationDetails](API_AwsAthenaWorkGroupConfigurationResultConfigurationDetails.md) object
Required: No

## See Also
<a name="API_AwsAthenaWorkGroupConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAthenaWorkGroupConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAthenaWorkGroupConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAthenaWorkGroupConfigurationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

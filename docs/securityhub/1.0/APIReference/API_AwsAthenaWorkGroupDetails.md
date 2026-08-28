---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAthenaWorkGroupDetails.html
---

# AwsAthenaWorkGroupDetails
<a name="API_AwsAthenaWorkGroupDetails"></a>

 Provides information about an Amazon Athena workgroup.

## Contents
<a name="API_AwsAthenaWorkGroupDetails_Contents"></a>

 ** Configuration **   <a name="securityhub-Type-AwsAthenaWorkGroupDetails-Configuration"></a>
 The configuration of the workgroup, which includes the location in Amazon Simple Storage Service (Amazon S3) where query results are stored, the encryption option, if any, used for query results, whether Amazon CloudWatch metrics are enabled for the workgroup, and the limit for the amount of bytes scanned (cutoff) per query, if it is specified.
Type: [AwsAthenaWorkGroupConfigurationDetails](API_AwsAthenaWorkGroupConfigurationDetails.md) object
Required: No

 ** Description **   <a name="securityhub-Type-AwsAthenaWorkGroupDetails-Description"></a>
 The workgroup description.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsAthenaWorkGroupDetails-Name"></a>
 The workgroup name.
Type: String
Pattern: `.*\S.*`
Required: No

 ** State **   <a name="securityhub-Type-AwsAthenaWorkGroupDetails-State"></a>
 Whether the workgroup is enabled or disabled.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsAthenaWorkGroupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAthenaWorkGroupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAthenaWorkGroupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAthenaWorkGroupDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeclarativePoliciesReport.html
---

# DeclarativePoliciesReport
<a name="API_DeclarativePoliciesReport"></a>

Describes the metadata of the account status report.

## Contents
<a name="API_DeclarativePoliciesReport_Contents"></a>

 ** endTime **
The time when the report generation ended.
Type: Timestamp
Required: No

 ** reportId **
The ID of the report.
Type: String
Required: No

 ** s3Bucket **
The name of the Amazon S3 bucket where the report is located.
Type: String
Required: No

 ** s3Prefix **
The prefix for your S3 object.
Type: String
Required: No

 ** startTime **
The time when the report generation started.
Type: Timestamp
Required: No

 ** status **
The current status of the report.
Type: String
Valid Values: `running | cancelled | complete | error`
Required: No

 ** TagSet.N **
Any tags assigned to the report.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** targetId **
The root ID, organizational unit ID, or account ID.
Format:
+ For root: `r-ab12`
+ For OU: `ou-ab12-cdef1234`
+ For account: `123456789012`
Type: String
Required: No

## See Also
<a name="API_DeclarativePoliciesReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeclarativePoliciesReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeclarativePoliciesReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeclarativePoliciesReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

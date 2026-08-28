---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbStatusInfo.html
---

# AwsRdsDbStatusInfo
<a name="API_AwsRdsDbStatusInfo"></a>

Information about the status of a read replica.

## Contents
<a name="API_AwsRdsDbStatusInfo_Contents"></a>

 ** Message **   <a name="securityhub-Type-AwsRdsDbStatusInfo-Message"></a>
If the read replica is currently in an error state, provides the error details.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Normal **   <a name="securityhub-Type-AwsRdsDbStatusInfo-Normal"></a>
Whether the read replica instance is operating normally.
Type: Boolean
Required: No

 ** Status **   <a name="securityhub-Type-AwsRdsDbStatusInfo-Status"></a>
The status of the read replica instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StatusType **   <a name="securityhub-Type-AwsRdsDbStatusInfo-StatusType"></a>
The type of status. For a read replica, the status type is read replication.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRdsDbStatusInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbStatusInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbStatusInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbStatusInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ContinuousScanDetails.html
---

# ContinuousScanDetails
<a name="API_ContinuousScanDetails"></a>

Contains information about the time range within the continuous backup in AWS Backup to scan for a point-in-time recovery resource.

## Contents
<a name="API_ContinuousScanDetails_Contents"></a>

 ** endTime **   <a name="guardduty-Type-ContinuousScanDetails-endTime"></a>
The timestamp representing the end of the time range to scan.
Type: Timestamp
Required: Yes

 ** startTime **   <a name="guardduty-Type-ContinuousScanDetails-startTime"></a>
The timestamp representing the start of the time range to scan. Reserved for internal use.
Type: Timestamp
Required: No

## See Also
<a name="API_ContinuousScanDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ContinuousScanDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ContinuousScanDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ContinuousScanDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

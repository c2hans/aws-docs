---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_IncrementalScanDetails.html
---

# IncrementalScanDetails
<a name="API_IncrementalScanDetails"></a>

Contains information about the incremental scan configuration.

## Contents
<a name="API_IncrementalScanDetails_Contents"></a>

 ** baselineResourceArn **   <a name="guardduty-Type-IncrementalScanDetails-baselineResourceArn"></a>
Amazon Resource Name (ARN) of the baseline resource used for incremental scanning. The scan will only process changes since this baseline resource was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

## See Also
<a name="API_IncrementalScanDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/IncrementalScanDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/IncrementalScanDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/IncrementalScanDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

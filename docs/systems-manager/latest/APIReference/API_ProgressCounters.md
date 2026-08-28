---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ProgressCounters.html
---

# ProgressCounters
<a name="API_ProgressCounters"></a>

An aggregate of step execution statuses displayed in the AWS Systems Manager console for a multi-Region and multi-account Automation execution.

## Contents
<a name="API_ProgressCounters_Contents"></a>

 ** CancelledSteps **   <a name="systemsmanager-Type-ProgressCounters-CancelledSteps"></a>
The total number of steps that the system cancelled in all specified AWS Regions and AWS accounts for the current Automation execution.
Type: Integer
Required: No

 ** FailedSteps **   <a name="systemsmanager-Type-ProgressCounters-FailedSteps"></a>
The total number of steps that failed to run in all specified AWS Regions and AWS accounts for the current Automation execution.
Type: Integer
Required: No

 ** SuccessSteps **   <a name="systemsmanager-Type-ProgressCounters-SuccessSteps"></a>
The total number of steps that successfully completed in all specified AWS Regions and AWS accounts for the current Automation execution.
Type: Integer
Required: No

 ** TimedOutSteps **   <a name="systemsmanager-Type-ProgressCounters-TimedOutSteps"></a>
The total number of steps that timed out in all specified AWS Regions and AWS accounts for the current Automation execution.
Type: Integer
Required: No

 ** TotalSteps **   <a name="systemsmanager-Type-ProgressCounters-TotalSteps"></a>
The total number of steps run in all specified AWS Regions and AWS accounts for the current Automation execution.
Type: Integer
Required: No

## See Also
<a name="API_ProgressCounters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ProgressCounters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ProgressCounters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ProgressCounters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

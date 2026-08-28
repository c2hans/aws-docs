---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_SpendingLimitSummary.html
---

# SpendingLimitSummary
<a name="API_SpendingLimitSummary"></a>

Contains summary information about a spending limit, including current spending status and configuration details.

## Contents
<a name="API_SpendingLimitSummary_Contents"></a>

 ** createdAt **   <a name="braket-Type-SpendingLimitSummary-createdAt"></a>
The date and time when the spending limit was created, in epoch seconds.
Type: Timestamp
Required: Yes

 ** deviceArn **   <a name="braket-Type-SpendingLimitSummary-deviceArn"></a>
The Amazon Resource Name (ARN) of the quantum device associated with this spending limit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** queuedSpend **   <a name="braket-Type-SpendingLimitSummary-queuedSpend"></a>
The amount currently queued for spending on the device, in USD.
Type: String
Required: Yes

 ** spendingLimit **   <a name="braket-Type-SpendingLimitSummary-spendingLimit"></a>
The maximum spending amount allowed for the device during the specified time period, in USD.
Type: String
Required: Yes

 ** spendingLimitArn **   <a name="braket-Type-SpendingLimitSummary-spendingLimitArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the spending limit.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:braket:[a-z0-9\-]+:[0-9]{12}:spending-limit/.*`
Required: Yes

 ** timePeriod **   <a name="braket-Type-SpendingLimitSummary-timePeriod"></a>
The time period during which the spending limit is active.
Type: [TimePeriod](API_TimePeriod.md) object
Required: Yes

 ** totalSpend **   <a name="braket-Type-SpendingLimitSummary-totalSpend"></a>
The total amount spent on the device so far during the current time period, in USD.
Type: String
Required: Yes

 ** updatedAt **   <a name="braket-Type-SpendingLimitSummary-updatedAt"></a>
The date and time when the spending limit was last modified, in epoch seconds.
Type: Timestamp
Required: Yes

 ** tags **   <a name="braket-Type-SpendingLimitSummary-tags"></a>
The tags associated with the spending limit. Each tag consists of a key and an optional value.
Type: String to string map
Required: No

## See Also
<a name="API_SpendingLimitSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/SpendingLimitSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/SpendingLimitSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/SpendingLimitSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

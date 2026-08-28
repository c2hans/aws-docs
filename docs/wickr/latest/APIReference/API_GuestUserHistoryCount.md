---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_GuestUserHistoryCount.html
---

# GuestUserHistoryCount
<a name="API_GuestUserHistoryCount"></a>

Contains the count of guest users for a specific billing period, used for tracking historical guest user activity.

## Contents
<a name="API_GuestUserHistoryCount_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** count **   <a name="wickr-Type-GuestUserHistoryCount-count"></a>
The number of guest users who have communicated with your Wickr network during this billing period.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** month **   <a name="wickr-Type-GuestUserHistoryCount-month"></a>
The month and billing period in YYYY\_MM format (e.g., '2024\_01').
Type: String
Pattern: `[\S\s]*`
Required: Yes

## See Also
<a name="API_GuestUserHistoryCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/GuestUserHistoryCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/GuestUserHistoryCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/GuestUserHistoryCount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

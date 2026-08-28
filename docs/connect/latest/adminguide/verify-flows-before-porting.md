---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/verify-flows-before-porting.html
---

# Verify flows before porting numbers to Connect Customer
<a name="verify-flows-before-porting"></a>

We recommend that you test your call flows before the mutually agreed date and time of porting. If you would like to test your call flows, we recommend that you claim a direct inward dial (DID) or toll-free phone number available within Connect Customer and assign it to the call flow for testing.

When you are done testing, you can release the number from your instance so you will no longer be charged for it. For instructions, see [Release a phone number from Connect Customer back to inventory](release-phone-number.md).

Until you release the number, you are charged the daily rate associated with claiming a phone number and the per minute rate for telephony minutes used. For more information see the standard pricing for [Connect Customer service usage and associated telephony rates](https://aws.amazon.com/connect/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/journey-flow-block-distribute-by-percentage.html
---

# Distribute by percentage
<a name="journey-flow-block-distribute-by-percentage"></a>

## Description
<a name="journey-flow-block-distribute-by-percentage-description"></a>
+ This block is useful for doing A/B testing. It routes profiles randomly based on a percentage.
+ Profiles are distributed randomly, so exact percentage splits might or might not occur.

## How it works
<a name="journey-flow-block-distribute-by-percentage-works"></a>

This block creates static allocation rules based on how you configure it. Internal logic generates a random number between 1-100. This number identifies which branch to take. It doesn't use current or historical volume as part of it's logic.

For example, say a block is configure like this:
+ 20% = A
+ 40% = B
+ 40% remaining = Default

When a profile is being routed through a flow, Amazon Connect generates the random number.
+ If number is between 0-20, the contact is routed down the A branch.
+ Between 21-60 it's routed down the B branch.
+ Greater than 60 it's routed down the Default branch.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

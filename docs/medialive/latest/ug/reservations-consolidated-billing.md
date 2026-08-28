---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/reservations-consolidated-billing.html
---

# Reservations and AWS Organizations
<a name="reservations-consolidated-billing"></a>

MediaLive reservations work with AWS Organizations consolidated billing. If you purchase a reservation in the management (payer) account, the reservation applies to MediaLive usage across all member accounts in the organization. AWS applies the reservation to unreserved usage in the management account first, then to remaining unreserved usage in member accounts.

If you purchase a reservation in a member account, the reservation applies only to MediaLive usage in that member account.

For more information about how reservations work with consolidated billing, see [Reserved Instances](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-behavior.html) in the *AWS Billing User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

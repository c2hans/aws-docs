---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/overlay-ads-billing.html
---

# Billing for overlay ads in MediaTailor
<a name="overlay-ads-billing"></a>

MediaTailor bills customers based on the number of non-linear ads in the ADS response. This number includes non-linear ads that extend past the break duration. After MediaTailor fills the avail, it bills for the ads it filled.

For prefetch workflows, MediaTailor does not bill for ads when retrieving the prefetch, but rather, when it sees a compatible ad avail in the consumption window for that session.

For additional billing information, see [https://aws.amazon.com/mediatailor/pricing/](https://aws.amazon.com/mediatailor/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

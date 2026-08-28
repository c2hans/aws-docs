---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/disable-identity-resolution.html
---

# Disable Identity Resolution in Connect Customer Customer Profiles
<a name="disable-identity-resolution"></a>

## Disable machine learning-based
<a name="disable-identity-resolution-ml"></a>

You can disable machine learning-based matching when you no longer want it to automatically find similar profiles. If you have consolidation criteria, all your criteria will be deleted and your profiles will no longer be automatically consolidated. Profiles that have already been consolidated will remain consolidated.

## Disable rule-based matching
<a name="disable-identity-resolution-rb"></a>

You can disable rule-based matching when you no longer want it to automatically find similar profiles. If you have a custom matching rule, the matching rule will be deleted and your profiles will no longer be automatically consolidated. Profiles that have already been consolidated will remain consolidated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/how-keys-are-added-index.html
---

# How Customer Profiles adds keys to the index for lookups
<a name="how-keys-are-added-index"></a>

The following diagram shows how Customer Profiles processes the standard identifiers to determine whether to persist the key.

![A flowchart showing the decision process for persisting keys in Customer Profiles based on lookup and new object criteria.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-profiles-template2.png)

The flowchart shows the following steps:

1. Does the key have `LOOKUP_ONLY` specified?
   + If Yes, don't persist the key.

1. If No, does the key have `NEW_ONLY` specified?
   + If No, save the key in the index to allow it to be used for lookups.

1. If Yes, has ingesting the object results in creating a new profile?
   + If Yes, save the key in the index to allow it to be used for lookups.
   + If No, don't persist the key in the index for future lookups.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/doc-history.html
---

# Document History for Upgrade Guide
<a name="doc-history"></a>

The following table describes the documentation for this release of AWS Elemental Conductor Live.
+ **API version:** 3.22.0 and later
+ **Release notes: **[ current Release Notes](https://docs.aws.amazon.com/elemental-live/)

The following table describes the documentation for this release of Conductor Live. For notification about updates to this documentation, you can subscribe to an RSS feed.

| Change | Description | Date |
| --- |--- |--- |
| [Removed mention of prepare\_for\_downgrade script](downgrades-cl3-upg-dg-cond.md) | We have removed two mentions of this script. The script is no longer required for any of the supported versions of Conductor Live. Don't run the script, even if you have it available, because it will cause the node to be unusable. | March 14, 2025 |
| [Clarification about scope of the guide](about-cl3-upg.md) | This guide has been modified to clarify that it applies to AWS Elemental Conductor Live versions 3.25 and 3.26. | July 17, 2024 |
| [Rules for software versions](upgrades-version-rules.md) | This guide now contains information about the rules for combining different software versions on the nodes in a AWS Elemental Conductor Live cluster. | February 19, 2024 |
| [Cross-version release of the guide](about-cl3-upg.md) | This guide has been modified so that it isn't for a specific version of AWS Elemental Conductor Live. The upgrade and downgrade procedures don't change from version to version.  | November 11, 2021 |
| [Version 3.22 release](about-cl3-upg.md) | First release of the 3.22 software version. | February 6, 2021 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

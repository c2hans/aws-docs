---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/docdb-version-support-dates.html
---

# Amazon DocumentDB engine version support dates
<a name="docdb-version-support-dates"></a>

You can use the following dates to plan your testing and upgrade cycles.

## Release calendar for Amazon DocumentDB major versions
<a name="docdb-major-version-release-calendar"></a>

Amazon DocumentDB currently supports the following major versions. To upgrade your engine version, see [Upgrading a major engine version](docdb-mvu.md) or [Upgrading using AWS DMS](docdb-migration.versions.md).

| Engine version | Release date | End of standard support | Start of Extended Support (year 1 pricing) | Start of Extended Support (year 3 pricing) | End of Extended Support |
| --- | --- | --- | --- | --- | --- |
| Version 3.6 | 9 January 2019 | 30 March 2026 | 31 March 2026 | 31 March 2028 | 30 March 2029 |
| Version 4.0 | 9 November 2020 | N/A | N/A | N/A | N/A |
| Version 5.0 | 1 March 2023 | N/A | N/A | N/A | N/A |
| Version 8.0 | 14 November 2025 | N/A | N/A | N/A | N/A |

Amazon DocumentDB supports multiple engine versions under standard support. You can continue running a version past its end of standard support date for an Extended Support fee. For more information, see [Amazon DocumentDB Extended Support](extended-support.md) and [Amazon DocumentDB pricing](https://aws.amazon.com/documentdb/pricing/).

## Release calendar for Amazon DocumentDB minor versions
<a name="docdb-minor-version-release-calendar"></a>

Amazon DocumentDB currently supports the following minor versions. The release schedule will vary depending on additional features or fixes. Minor versions can reach end of standard support before corresponding major versions do. To upgrade your engine version, see [Upgrading a minor engine version](docdb-minor-version-upgrade.md).

**Note**
Minor versions are available starting on major version 5.0.

| Engine version | Release date |
| --- | --- |
| Version 5.0.0 (LTS) | 16 February 2026 |
| Version 5.0.1 | 8 June 2026 |

Amazon DocumentDB designates certain versions as Long-Term Support (LTS) releases. For more information, see [Using a long-term support (LTS) release](docdb-lts-release.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

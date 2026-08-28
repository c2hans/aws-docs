---
source_url: https://docs.aws.amazon.com/streams/latest/dev/kpl-version-lifecycle-policy.html
---

# KPL version lifecycle policy
<a name="kpl-version-lifecycle-policy"></a>

This topic outlines the version lifecycle policy for Amazon Kinesis Producer Library (KPL). AWS regularly provides new releases for KPL versions to support new features and enhancements, bug fixes, security patches, and dependency updates. We recommend that you stay up-to-date with KPL versions to keep up with the latest features, security updates, and underlying dependencies. We **don't** recommend continued use of an unsupported KPL version.

The lifecycle for major KPL versions consists of the following three phases:
+ **General availability (GA)** – During this phase, the major version is fully supported. AWS provides regular minor and patch version releases that include support for new features or API updates for Kinesis Data Streams, as well as bug and security fixes.
+ **Maintenance mode** – AWS limits patch version releases to address critical bug fixes and security issues only. The major version won't receive updates for new features or APIs of Kinesis Data Streams.
+ **End-of-support** – The major version will no longer receive updates or releases. Previously published releases will continue to be available through public package managers and the code will remain on GitHub. Use of a version which has reached end-of-support is done at the user’s discretion. We recommend that you upgrade to the latest major version.

| Major version | Current phase | Release date | Maintenance mode date | End-of-support date |
| --- | --- | --- | --- | --- |
| KPL 0.x | Maintenance mode | 2015-06-02 | 2025-04-17 | 2026-01-30 |
| KPL 1.x | General availability | 2024-12-15 | -- | -- |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

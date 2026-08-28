---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.20.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Infrastructure 6.20 release
<a name="infra-release-notes-6.20"></a>

The following release notes include information for infrastructure release 6.20. For information on the release timeline, see [Change log](#infra-release-notes-6.20-change-log).

**Platform version**

|  |  |
| --- | --- |
| Infrastructure | 6.20.0 (1732) |

**Changes, enhancements, and resolved issues**

The switchboard components were updated to:
+ the latest version of fast-xml-parser to address potential abuse for DoS attack.
+ the latest version jsonwebtoken to ensure signature validation cannot be bypassed and iOS push notifications are not broken; and ensure development dependencies used for testing are not included in production.

The schema components were updated to:
+ remove node-modules address request header exploit, regex DoS, and prototype pollution vulnerabilities.
+ ensure development dependencies used for testing are not included in production.

The crond was updated to ensure development dependencies used for testing are not included in production.

## Change log
<a name="infra-release-notes-6.20-change-log"></a>

**Change log for 6.20 release and release notes**

| Change | Description | Date |
| --- | --- | --- |
| Infrastructure update | Updates to address vulnerability scan results | August 11, 2023 |
| Initial release | Initial release of August release notes | August 11, 2023 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

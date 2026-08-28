---
source_url: https://docs.aws.amazon.com/linux/al2/ug/compare-with-al1.html
---

# Compare AL1 and AL2
<a name="compare-with-al1"></a>

The following topics describe key differences between AL1 and AL2. They also contain information about lifespan and support, and package changes.

**Topics**
+ [AL1 support and EOL](#al1-eol-date)
+ [Support for AWS Graviton processors](#al1-diff-graviton)
+ [`systemd` replaces `upstart` as `init` system](#al1-systemd)
+ [Python 2.6 and 2.7 were replaced with Python 3](#python2.6-no-more)
+ [Comparing packages installed on AL1 and AL2 AMIs](amzn1-amzn2-ami.md)
+ [Comparing packages installed on AL1 and AL2 base container images](amzn1-amzn2-container.md)

## AL1 support and EOL
<a name="al1-eol-date"></a>

 AL1 is now EOL. AL1 ended standard support as of December 31, 2020, and was in a maintenance support phase until December 31, 2023.

We recommend upgrading to the latest Amazon Linux version.

## Support for AWS Graviton processors
<a name="al1-diff-graviton"></a>

 AL2 introduced support for Graviton processors. AL2023 is further optimized for Graviton processors.

## `systemd` replaces `upstart` as `init` system
<a name="al1-systemd"></a>

 In AL2, `systemd` replaced `upstart` as the `init` system.

## Python 2.6 and 2.7 were replaced with Python 3
<a name="python2.6-no-more"></a>

 Although AL1 marked Python 2.6 as EOL with the 2018.03 release, the packages were still in the repositories to install. AL2 shipped with Python 2.7 as the earliest supported Python version.

 AL2023 completes the transition to Python 3, and no Python 2.x versions are included in the repositories.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/linux/al2/ug/prepare-for-al2023.html
---

# Prepare your migration to AL2023
<a name="prepare-for-al2023"></a>

 You can prepare your move to AL2023 while you continue to use AL2.

**Topics**
+ [Review the list of changes in AL2023](#review-al2-al2023-changes)
+ [Migrate to `systemd` timers from `cron` jobs](#systemd-timers)

## Review the list of changes in AL2023
<a name="review-al2-al2023-changes"></a>

 The AL2023 documentation contains a detailed list of changes that have been implemented since AL2. This information is located in the [Comparing AL2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html) section. There is also a comprehensive list of software package changes located in the [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html) section.

 AL2023 doesn't include `amazon-linux-extras`. Instead, it provides namespaced packages where multiple versions are provided. Because many packages are updated in AL2023, the base versions in AL2023 might be later than the versions that you are getting from `amazon-linux-extras`.

**Note**
 We recommend that you don't run `amazon-linux-extras`, because it is EOL.

 After you review these sections in the documentation, you can determine if there are changes in AL2023 that might require you to adapt your environment for the migration. For example, you might need to finally migrate a Python 2.7 script to Python 3.

## Migrate to `systemd` timers from `cron` jobs
<a name="systemd-timers"></a>

 By default, `cron` is not installed in AL2023. You can migrate your `cron` jobs to `systemd` timers in AL2 in preparation for migrating to AL2023. `systemd` has many advantages, such as more precise control over when timers are run and improved logging.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

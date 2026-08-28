---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/class-diagram-tracking.html
---

# Class diagram: S3 Transfer Manager tracking components
<a name="class-diagram-tracking"></a>

The following class diagram shows how the tracking components work together in the S3 Transfer Manager. Understanding these relationships helps you implement [custom listeners](s3-tm-transfer-listener.md) and [progress tracking](progress-tracking.md#customize-built-in-progress-tracker).

![AbstractTransferListener abstract class with four tracking methods, connected to SingleProgressTracker and MultiProgressTracker implementations, and ProgressBarFormat hierarchy for console display.](http://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/images/s3-tm-tracking-cls-diagram-drawio.drawio.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/class-diagram-tracking.html
---

# Class diagram: S3 Transfer Manager tracking components
<a name="class-diagram-tracking"></a>

The following class diagram shows how the tracking components work together in the S3 Transfer Manager. Understanding these relationships helps you implement [custom listeners](s3-tm-transfer-listener.md) and [progress tracking](progress-tracking.md#customize-built-in-progress-tracker).

![AbstractTransferListener abstract class with four tracking methods, connected to SingleProgressTracker and MultiProgressTracker implementations, and ProgressBarFormat hierarchy for console display.](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/images/s3-tm-tracking-cls-diagram-drawio.drawio.png)

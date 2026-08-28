---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/whats-new.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# What's new in the AWS Tools for PowerShell
<a name="whats-new"></a>

For high-level information about new developments related to the AWS Tools for PowerShell, see the product page at [https://aws.amazon.com/powershell/](https://aws.amazon.com/powershell/) and the [change logs](https://github.com/aws/aws-tools-for-powershell/tree/v4.1/changelogs).

The following is what's new in the Tools for PowerShell.

**September 17, 2025: Upcoming end-of-support for version 4 of the AWS Tools for PowerShell**

The end-of-support for this version (V4) of the AWS Tools for PowerShell has been announced. See the [V5 migration guide](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html) to migrate your V4 scripts and avoid disruptions. For more information, see the blog post [Announcing the end-of-support for AWS Tools for PowerShell v4](https://aws.amazon.com/blogs/devops/announcing-the-end-of-support-for-aws-tools-for-powershell-v4/).

**June 23, 2025: Version 5 of the AWS Tools for PowerShell**

Version 5 (V5) of the AWS Tools for PowerShell is generally available\! For more information, see the [AWS Tools for PowerShell User Guide (V5)](https://docs.aws.amazon.com/powershell/v5/userguide/), especially the topic for [Migrating to V5](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

**February 10, 2025: GA release for observability**

Observability is the extent to which a system's current state can be inferred from the data it emits. Observability has been added to the Tools for PowerShell, including an implementation of a telemetry provider. For more information, see [Observability](observability.md) in this guide and the blog post [Announcing the general availability of AWS .NET OpenTelemetry libraries](https://aws.amazon.com/blogs/dotnet/announcing-the-general-availability-of-aws-net-opentelemetry-libraries/).

**January 15, 2025: New default behavior for integrity protection**

Beginning with version 4.1.737 of the AWS Tools for PowerShell, the tools provide default integrity protections by automatically calculating a `CRC32` checksum for uploads. For more information, see the announcement on GitHub at [https://github.com/aws/aws-tools-for-powershell/issues/370](https://github.com/aws/aws-tools-for-powershell/issues/370). The Tools also provide global settings for data integrity protections that you can set externally, which you can read about in [Data Integrity Protections](https://docs.aws.amazon.com/sdkref/latest/guide/feature-dataintegrity.html) in the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/).

**November 18, 2024: Preview 1 release for version 5**

Preview 1 of the AWS Tools for PowerShell version 5 was released on November 18, 2024. For more information about this preview, see the blog post [Preview 1 of AWS Tools for PowerShell V5](https://aws.amazon.com/blogs/developer/preview-1-of-aws-tools-for-powershell-v5/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

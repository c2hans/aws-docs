---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/ips-collect-sources.html
---

# Identify the sources
<a name="ips-collect-sources"></a>

1. Identify all the sources that you will need through the lifetime of the MediaLive channel or at least until the next planned maintenance period.

1. Note which sources are push inputs and which are pull inputs. Make sure that you don't exceed the [limits](eml-limitations-and-rules.md#limits-inputs).

1. Note which sources are live sources and which are file sources. For information on whether a source is a live or file (VOD) source, see [Input types supported in MediaLive](inputs-supported-containers.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-emp-design.html
---

# Design the path for the output destination
<a name="hls-destinations-emp-design"></a>

Perform this step if you haven't yet designed the full destination path or paths. If you've already designed the paths, go to [Complete the fields on the console](hls-specify-destination-emp.md).

**To design the path**

1. Collect the information you [previously obtained](origin-server-hls-emp.md) from the MediaPackage user:
   + The two URLs (input endpoints is the MediaPackage terminology) for the channel. See the information after this procedure.
   + If you are using standard MediaPackage, obtain the user name and password. If you are using MediaPackage v2, you don't use user credentials.

1. You must design the portions of the destination paths that follow the URLs.

**Topics**
+ [Collect the information for standard MediaPackage](hls-destinations-emp-info.md)
+ [Collect the information for MediaPackage v2](hls-destinations-emp-info-v2.md)
+ [The syntax for the paths for the outputs](hls-syntax-emp.md)
+ [Designing the nameModifier](hls-nameModifier-design-emp.md)
+ [Designing the segmentModifier](hls-segmentModifier-design-emp.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

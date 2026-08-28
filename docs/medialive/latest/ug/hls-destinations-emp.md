---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-emp.html
---

# Fields for the output destination – sending to MediaPackage
<a name="hls-destinations-emp"></a>

When you [planned the output to MediaPackage](delivering-to-mediapackage.md), you might have decided to send the output by creating an HLS output group. (Or you might have decided to create a [MediaPackage output group](creating-mediapackage-output-group.md).)

You must design the destination path or paths for the output. You must then enter the different portions of the path into the appropriate fields on the console.

You can use an HLS output group to send to standard MediaPackage or toMediaPackage v2. The two versions use different protocols:
+ MediaPackage uses WebDAV.
+ MediaPackage v2 uses Basic PUT.

**Topics**
+ [Design the path for the output destination](hls-destinations-emp-design.md)
+ [Complete the fields on the console](hls-specify-destination-emp.md)
+ [Standard MediaPackage example](hls-example-mediapackage.md)
+ [MediaPackage v2 example](hls-example-mediapackage-v2.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

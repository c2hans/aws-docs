---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/FIPS-exceptions.html
---

# Exceptions
<a name="FIPS-exceptions"></a>

FIPS-compliant connections are not supported in the following scenarios:
+ Administration of WorkSpaces Applications through the WorkSpaces Applications console
+ Streaming sessions for users who authenticate using the WorkSpaces Applications user pool feature
+ Streaming using an interface VPC endpoint
+ Generating FIPS-compliant streaming URLs through the WorkSpaces Applications console
+ Connections to your Google Drive or OneDrive storage accounts where your storage provider does not provide a FIPS endpoint

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

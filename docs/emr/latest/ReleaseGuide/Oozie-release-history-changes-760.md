---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Oozie-release-history-changes-760.html
---

# Amazon EMR 7.6.0 - Oozie release notes
<a name="Oozie-release-history-changes-760"></a>

**Oozie known issues:**
+ Version Conflict in Oozie Sharelib:
  + Oozie sharelib contains multiple versions of commons-cli (versions 1.2 and 1.5).
  + If you encounter compatibility issues, consider either:
    + Removing commons-cli-1.2 JAR files.
    + Replacing commons-cli-1.2 with commons-cli-1.5.
+ Pig JAR Compatibility:
  + The Pig jar included by default in Oozie sharelib is the open-source jar. This differs from the Pig jar available elsewhere in the EMR cluster, on installing the Pig application, which includes additional EMR-specific enhancements and optimizations. Users should be aware of this difference when developing Pig workflows.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

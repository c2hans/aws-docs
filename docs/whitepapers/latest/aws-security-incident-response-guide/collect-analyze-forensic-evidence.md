---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/collect-analyze-forensic-evidence.html
---

# Collect and analyze forensic evidence
<a name="collect-analyze-forensic-evidence"></a>

 Forensics, as mentioned in the [Preparation](preparation.md) section of this document, is the process of collecting and analyzing artifacts during incident response. On AWS, it is applicable to infrastructure domain resources such as network traffic packet captures, operating system memory dump, and for service domain resources such as AWS CloudTrail logs.

 The forensics process has the following fundamental characteristics:
+  **Consistent** – It follows the exact steps documented, without deviations.
+  **Repeatable** – It produces the exact same results when repeated against the same artifact.
+  **Customary** – It’s publicly documented and widely adopted.

 It is important to maintain chain of custody for artifacts collected during incident response. Using automation and having automatic documentation of this collection generated can help, in addition to storing the artifacts in read-only repositories. Analysis should only be performed on exact replicas of the collected artifacts to maintain integrity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

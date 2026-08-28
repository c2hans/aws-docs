---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/certificate-based-authentication-manage-logging.html
---

# Logging and Monitoring
<a name="certificate-based-authentication-manage-logging"></a>

You can use CloudTrail to record API calls to a private CA by WorkSpaces Applications. For more information see [What Is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and [Using CloudTrail](https://docs.aws.amazon.com/privateca/latest/userguide/PcaCtIntro.html). In CloudTrail Event history you can view **GetCertificate** and **IssueCertificate** event names from **acm-pca.amazonaws.com** event source made by the WorkSpaces Applications**EcmAssumeRoleSession** user name. These events will be recorded for every WorkSpaces Applications certificate-based authentication request. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/workstations.html
---

# Secure artist workstations
<a name="workstations"></a>

Workstations with Deadline Cloud submitters installed hold credentials that can submit jobs to your farm, and jobs submitted from them run on your fleets at your expense. The following practices protect those credentials and the submission path:
+ Prefer temporary credentials for workstation access to Deadline Cloud. Users who sign in through the Deadline Cloud monitor receive temporary credentials automatically. If a workstation uses an AWS profile with long-lived IAM access keys, such as for the Deadline Cloud CLI, secure those keys. For more information, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#securing_access-keys) in the *IAM User Guide*.
+ When you install the Deadline Cloud submitters and adaptors, download them through the Deadline Cloud monitor and verify the installers before running them. For more information, see [Verify the authenticity of downloaded software](verify-installer.md). If you build your own submitters, see [Build a custom submitter for Deadline Cloud](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-custom-submitters.html) in the *Deadline Cloud Developer Guide*.
+ Use secure permissions on Deadline Cloud submitter program files to prevent tampering.
+ Restrict permissions to local DNS override configuration files (`/etc/hosts` and `/etc/resolv.conf` on Linux and macOS, and `C:\Windows\system32\etc\hosts` on Windows), and to route tables, so that workstation traffic to Deadline Cloud can't be redirected.
+ Regularly patch the operating system and the software used with Deadline Cloud, including submitters, adaptors, and OpenJD packages.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

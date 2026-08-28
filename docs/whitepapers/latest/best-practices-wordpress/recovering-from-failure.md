---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/recovering-from-failure.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Recovering from failure
<a name="recovering-from-failure"></a>

A single web server is a single point of failure, so you must ensure that your website data is backed up. The snapshot mechanism described earlier can also be used for this purpose. To recover from failure, you can restore a new instance from your most recent snapshot. To reduce the amount of data that could be lost during a restore, your snapshots must be as recent as possible.

To minimize the potential for data loss, ensure that snapshots are being taken on a regular basis. You can schedule automatic snapshots of your Lightsail Linux/Unix instances. For steps, refer to [Enabling or disabling automatic snapshots for instances or disks in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-configuring-automatic-snapshots).

AWS recommends that you use a static IP: a fixed, public IP address that is dedicated to your Lightsail account. If you need to replace your instance with another one, you can reassign the static IP to the new instance. In this way, you don’t have to reconfigure any external systems (such as DNS records) to point to a new IP address every time you want to replace your instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

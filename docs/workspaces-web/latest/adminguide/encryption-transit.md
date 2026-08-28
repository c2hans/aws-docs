---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/encryption-transit.html
---

# Encryption in transit for Amazon WorkSpaces Secure Browser
<a name="encryption-transit"></a>

WorkSpaces Secure Browser encrypts data in transit over HTTPS and TLS 1.2. You can send a request to WorkSpaces by using the console or direct API calls. The request data that is transferred is encrypted by sending everything through a HTTPS or TLS connection. Request data can be transferred from the AWS Console, AWS Command Line Interface, or AWS SDK to WorkSpaces Secure Browser.

Encryption in transit is configured by default, and secure connections (HTTPS, TLS) are configured by default.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

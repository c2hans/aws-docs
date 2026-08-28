---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/encryption-transit.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Encryption in transit
<a name="encryption-transit"></a>

WorkSpaces Thin Client encrypts data in transit over HTTPS and TLS 1.2. You can send a request to WorkSpaces Thin Client by using the console or direct API calls. The request data that is transferred is encrypted by sending it through an HTTPS or TLS connection. Request data can be transferred from the AWS Console, AWS Command Line Interface, or AWS SDK to WorkSpaces Thin Client. This also includes any software updates on the device.

Encryption in transit is configured by default, and secure connections (HTTPS, TLS) are configured by default.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/dcv/latest/userguide/set-certificate-validation-policy.html
---

# Set certificate validation policy
<a name="set-certificate-validation-policy"></a>

Amazon DCV uses a secure TLS connection for communication between the server and client. The certificate validation policy determines how the Amazon DCV client responds when a certificate can't be verified as trustworthy. Set one of the following options in the connection file:
+ `Strict`: Prohibits the connection if there is any problem validating the TLS certificate.
+ `Ask user`: Prompts the user to determine whether to trust the certificate when a certificate can't be verified.
+ `Accept untrusted`: Connects to the server even if the TLS certificate is self signed and can't be validated by the client.

For information about editing the connection file, see [Step 4: Create a connection file (optional)](using-connection-file.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

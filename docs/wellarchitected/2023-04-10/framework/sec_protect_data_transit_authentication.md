---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_protect_data_transit_authentication.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC09-BP04 Authenticate network communications
<a name="sec_protect_data_transit_authentication"></a>

 Verify the identity of communications by using protocols that support authentication, such as Transport Layer Security (TLS) or IPsec.

Using network protocols that support authentication, allows for trust to be established between the parties. This adds to the encryption used in the protocol to reduce the risk of communications being altered or intercepted. Common protocols that implement authentication include Transport Layer Security (TLS), which is used in many AWS services, and IPsec, which is used in [AWS Virtual Private Network (Site-to-Site VPN)](http://aws.amazon.com/vpn).

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement secure protocols: Use secure protocols that offer authentication and confidentiality, such as TLS or IPsec, to reduce the risk of data tampering or loss. Check the [AWS documentation](https://docs.aws.amazon.com/) for the protocols and security relevant to the services you are using.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Documentation](https://docs.aws.amazon.com/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

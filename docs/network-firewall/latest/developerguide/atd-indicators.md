---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/atd-indicators.html
---

# Understanding active threat defense managed rule group indicators
<a name="atd-indicators"></a>

A threat indicator is a unique identifier of potentially malicious infrastructure or threat activity. active threat defense managed rule groups match traffic for IP address, domain name, and URL indicators that are associated with known threats.

**Tip**
If you use Amazon GuardDuty, you can strengthen your security by using active threat defense managed rule group to automatically block the threats that Amazon GuardDuty detects. For information, see [Working with active threat defense indicators in Amazon GuardDuty](nwfw-atd-guardduty-use-case.md).

AWS groups threat indicators into categories based on observed attack patterns. The following table describes each indicator group available in the active threat defense managed rule group:

| Indicator group and description | Traffic direction | Indicator types |
| --- | --- | --- |
| **Command and control**<br />Infrastructure that malicious actors use to remotely control compromised systems. | Egress | IPs, domains |
| **Malware staging**<br />Infrastructure that facilitates the distribution of malware and attack tooling. | Ingress/Egress | URLs |
| **Sinkholes**<br />Previously abused infrastructure used for malicious purposes. | Egress | Domains |
| **Out-of-band application security testing**<br />A technique where injected payloads make an outbound connection to external infrastructure that validates the existence of a vulnerability. | Egress | IPs, domains |
| **Crypto-mining pool**<br />Infrastructure used by crypto-miners. | Egress | IPs, domains |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

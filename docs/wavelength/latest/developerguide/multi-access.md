---
source_url: https://docs.aws.amazon.com/wavelength/latest/developerguide/multi-access.html
---

# Multi-access AWS Wavelength
<a name="multi-access"></a>

TCP, UDP, and ICMP traffic from the device on the carrier network to an Amazon EC2 instance in the Wavelength Zone is supported. However, when a mobile subscriber connects to an external, non-cellular network offered by the communications service provider (CSP), such as a WiFi network, traffic is denied for most partners because traffic is characterized as *internet facing*.

With the proliferation of high-speed 5G networks, CSPs now offer new connectivity solutions to residential, small-business, and enterprise customers such as Fixed Wireless Access (FWA).

The following CSP partners that offer AWS Wavelength Zones have expanded the available ingress traffic flows:

| Communication service provider | Ingress from outside the carrier network | Ingress from 4G/5G-connected device | Ingress from Fixed Wireless Access |
| --- | --- | --- | --- |
| Orange | Yes | Yes | Yes |
| Verizon | No | Yes | Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wavelength. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wavelength` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/tcp-middlebox-reflection.html
---

# TCP middlebox reflection
<a name="tcp-middlebox-reflection"></a>

 This relatively new attack vector was first disclosed in an [academic whitepaper](https://www.usenix.org/system/files/sec21fall-bock.pdf) in August 2021 that explained how TCP non-compliance in network firewalls could result in these being tricked into becoming a TCP amplification vector. We've seen these attacks since early 2022 and continue to see them today. The amplification factor varies because of the different ways vendors have implemented this feature but can exceed Memcached UDP amplification.

 Memcached amplification can reach an [estimated 51,000 time](https://ubuntu.com/security/CVE-2018-1000115) the initial GET request by returning a large amount of UDP data, making it one of the highest known amplification factors—a 15-byte request can generate a response of up to 750 KB. This extreme amplification factor was exploited in February 2018 to launch attacks exceeding 1 Tbps. While the number of exposed memcached servers has decreased since then, it remains a significant amplification vector—and that TCP middlebox reflection can exceed this factor underscores the severity of this established and actively exploited attack vector.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

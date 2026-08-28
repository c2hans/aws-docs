---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp04.html
---

# HNSEC04-BP04 Implement DNS security controls
<a name="hnsec04-bp04"></a>

 DNS security control protects against DNS threats such as data exfiltration. You can create blocklists and allowlists to manage which domains your resources can query through DNS.

 **Desired outcome:** Prevent data exfiltration and block malicious domains at the DNS layer in hybrid networks.

 **Level of risk exposed if this best practice is not established:** Medium

 **Benefits of establishing this best practice:**
+  Blocks DNS-based attacks and data exfiltration
+  Provides centralized control over DNS traffic
+  Enables logging and reporting for compliance

## Implementation guidance
<a name="implementation-guidance-20"></a>
+  Define DNS firewall rule groups for blocklists and allowlists.
+  Associate DNS firewall rules with relevant networks.
+  Monitor DNS queries and refine rules based on findings.

## Resources
<a name="resources-19"></a>
+  [How Resolver DNS Firewall works](https://docs.aws.amazon.com/Route 53/latest/DeveloperGuide/resolver-dns-firewall-overview.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

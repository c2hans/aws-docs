---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-troubleshooting-dns-issues.html
---

# Troubleshooting DNS issues with Route 53 Global Resolver
<a name="gr-troubleshooting-dns-issues"></a>

Route 53 Global Resolver provides comprehensive DNS resolution capabilities, but occasionally you might need to troubleshoot connectivity, performance, or configuration issues. Use DNS logs, monitoring data, and diagnostic techniques to identify and resolve issues affecting client device DNS resolution with Route 53 Global Resolver. This chapter provides systematic approaches to troubleshooting common DNS problems and optimizing performance.

**Topics**
+ [Diagnose connectivity issues](gr-diagnose-connectivity-issues.md)
+ [Resolve performance issues](gr-resolve-performance-issues.md)
+ [Troubleshoot configuration](gr-troubleshoot-configuration-issues.md)
+ [Troubleshooting internal resource access](#gr-troubleshooting-internal-access)

## Troubleshooting internal resource access
<a name="gr-troubleshooting-internal-access"></a>

Common issues and solutions when managing internal resource access:

Client devices not resolving to private zone records
+ Verify the private hosted zone is associated with the correct DNS view
+ Check that the client device is authenticated to the correct DNS view
+ Ensure the domain name in the query exactly matches the zone name
+ Verify the DNS records exist in the private hosted zone

Intermittent resolution failures
+ Check the association status in the console
+ Review DNS query logs for error patterns
+ Verify network connectivity between Route 53 Global Resolver and Amazon Route 53

Unexpected public resolution
+ Confirm the private hosted zone contains the expected records
+ Check for firewall rules that might be blocking the query
+ Verify the query is coming from a client device associated with the DNS view

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

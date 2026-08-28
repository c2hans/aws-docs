---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/test-throughput.html
---

# Troubleshooting AWS Client VPN: Verify the bandwidth limit for a Client VPN endpoint
<a name="test-throughput"></a>

**Problem**
I need to verify the bandwidth limit for a Client VPN endpoint.

**Cause**
The throughput depends on multiple factors, such as the capacity of your connection from your location, and the network latency between your Client VPN desktop application on your computer and the VPC endpoint. A minimum bandwidth of 10 Mbps is supported per user connection.

**Solution**
Run the following commands to verify the bandwidth.

```
sudo iperf3 -s -V
```

On the client:

```
sudo iperf -c {{server IP address}} -p {{port}} -w 512k -P 60
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf06-bp01.html
---

# EUCPERF06-BP01 Minimize latency between end users and EUC services
<a name="eucperf06-bp01"></a>

 Like many other vendors, AWS EUC solutions deliver their services using a remote display protocol to stream the pixel information to the endpoint device, which is highly efficient and capable of tolerating a variety of network conditions. Low latency, low packet loss, and jitter are key to delivering the best service for end users.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-15"></a>

 Minimize latency between end user devices (like desktops, laptops, and thin clients) and the AWS EUC service endpoints by avoiding proxies, inspection appliances, and VPNs.

 Determine whether there are any conditions which might introduce latency between your end users and the AWS EUC service endpoints. Test connectivity under various conditions to identify the maximum latency that can be tolerated by the application set being deployed, and verify that your network can scale to reliably deliver the number of users being deployed.

 If end users will be working from home, try to establish a minimum level of network connectivity that should provide a good user experience. Most home broadband connections are more than capable of delivering low latency for home working, but problems with home networks can be difficult to diagnose.

 Verify that endpoint devices can run the local client application (WorkSpaces or AppStream Client) that processes and displays the encrypted pixel stream which flows between the end user and the AWS EUC service connection points (streaming gateways). If the workload delivers collaboration tools such as Microsoft TEAMs, Zoom, or Webex, optimization capabilities will try to offload processing to the local endpoint device, which must be capable of handling this additional load.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

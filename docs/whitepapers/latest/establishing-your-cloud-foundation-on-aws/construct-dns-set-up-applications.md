---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/construct-dns-set-up-applications.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Construct DNS set up for applications
<a name="construct-dns-set-up-applications"></a>

A Domain Name Service (DNS) is used by every application and organization to connect names to IP addresses. In cloud environments, DNS management becomes a critical element, since it allows for the discovery of each workload and service among themselves. Organizations usually manage their own DNS servers or leverage public DNS systems to make DNS queries. Within a cloud environment you can create DNS zones to publish your records, without having to configure and maintain your own DNS servers and software.

We recommend you manage your internal workloads and server domain names in a private DNS zone, limited to your network. For your public facing workloads and services, we recommend that you set up a different DNS, the DNS should be publicly accessible for clients over internet to connect.

Typical application architecture involves monolithic, virtual machines (VMs), or containerized version of jobs and services, Relational or key-value databases and other data sets, and front-end consisting API routing or Load Balancer. Each of these constructs need unique networking planning and designing. Domain Name Service (DNS) plays a key role in forwarding traffic to your applications irrespective of their structure. You should work with your application team to evaluate their needs for user experience and application monitoring. You can leverage DNS health checks provided by a cloud provider to test your applications or databases to ensure they are healthy in production environment. Similarly, DNS policies can be applied for your application traffic in cloud to influence routing. For example, you can use DNS routing policies to control which endpoints serve content to users based on the specific geographical location of your applications, users, or latency. You can also configure DNS records to achieve active/passive or load balancing between two endpoints.

For customers with hybrid workloads, which include on-premises and cloud-based resources, extra steps are necessary to configure DNS to work seamlessly across both environments. You can use different endpoints on AWS for DNS traffic to be routed in and out of your cloud and on-premises network. Further, centralizing DNS management for all your cloud network and on-premises domains should be considered for ease of management. Additionally, when you have hybrid connectivity between on-premises and cloud architecture of the DNS is one of the main players in the room as resources on-premises will need to resolve DNS names for resources in cloud and vice-versa.

Finally, to get insights into DNS traffic for auditing; DNS logging should be enabled and pushed to a monitoring system to get more insights into DNS data and perform necessary actions from that data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

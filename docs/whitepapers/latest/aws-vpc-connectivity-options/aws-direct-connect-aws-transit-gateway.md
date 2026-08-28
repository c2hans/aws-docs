---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-aws-transit-gateway.html
---

# AWS Direct Connect \+ AWS Transit Gateway
<a name="aws-direct-connect-aws-transit-gateway"></a>

 [AWS Direct Connect](https://aws.amazon.com/directconnect/) \+ [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html), using [transit VIF attachment to Direct Connect gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-dcg-attachments.html), enables your network to connect several regional centralized routers over a private dedicated connection. The following diagram shows connecting to two routers.

![Diagram that shows connecting to three routers.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/aws-direct-connect-and-aws-transit-gateway.png)

 Each AWS Transit Gateway is a network transit hub to interconnect VPCs in the same region, consolidating Amazon VPC routing configuration in one place. This solution simplifies management of connections between an Amazon VPC and your networks over a private connection that can reduce network costs, increase bandwidth throughput, and provide a more consistent network experience than internet-based connections.

## Additional resources
<a name="additional-resources-3"></a>
+  [AWS Direct Connect User Guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
+  [Link aggregation groups in AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/lags.html)
+  Blog post: [Integrating sub-1 Gbps hosted connections with AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-sub-1-gbps-hosted-connections-with-aws-transit-gateway/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

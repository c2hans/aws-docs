---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-perimeter-zone-apps-network-firewall/next-steps.html
---

# Next steps and resources
<a name="next-steps"></a>

To migrate your perimeter zone applications to the AWS Cloud, we recommend that you do the following:

1. Identify application components that reside in your on-premises perimeter zone. Then, document the security requirements for those application workloads.

1. Create an AWS account for hosting the application and [create a network firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-creating.html).

1. Migrate your application to the AWS account.

1. [Create a firewall policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policies.html) and associate it with the firewall. Optionally, you can create notifications for rule violations.

1. [Create route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) to ensure traffic is routed through the firewall.

1. Verify that the policy works as desired for incoming and outgoing connections.

## Related resources
<a name="related-resources"></a>
+ [What is AWS Network Firewall?](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
+ [What is a Gateway Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html)
+ [Deployment models for AWS Network Firewall](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/)
+ [AWS Transit Gateway](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway.html)
+ [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)

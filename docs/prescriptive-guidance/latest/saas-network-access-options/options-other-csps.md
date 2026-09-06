---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/options-other-csps.html
---

# SaaS consumers operating on other cloud service providers
<a name="options-other-csps"></a>

This scenario describes solutions for consumers on other cloud service providers (CSPs). This scenario shares some commonalities with connections to on-premises data centers. In fact, all connectivity options for on-premises environments are equally valid for consumers on other CSPs, even a private connection with AWS Direct Connect is possible with some CSPs. Most CSPs offer documentation and support about how to connect to the AWS Cloud through AWS Site-to-Site VPN or AWS Direct Connect.

When choosing Site-to-Site VPN, consumers can benefit from managed gateways or similar resources from their respective CSP. Consumers don't necessarily have to set them up themselves, as in the on-premises scenario. This influences some of the metrics for Site-to-Site VPN, such as improvements to time to repair and observability. This is because both ends of the connection are now managed.

The following networking value map summarizes how each of these options scores for each evaluation metric. It is very similar to the networking value map for on-premises connections, although the values for Site-to-Site VPN are different. For more information about the evaluation metrics, see [Evaluation metrics](evaluating.md#evaluating-metrics) in this guide. In the map, a five represents the best score, such as the lowest TCO, best network isolation, or lowest time to repair. For more information about how to read this radar chart, see [Networking value map](evaluating.md#evaluating-map) in this guide.

![Radar chart that shows scores for each evaluation metric.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/56756012-b77e-43f7-889b-aaba529d8621.png)

The radar chart shows the following values.

|
|
| **Evaluation metric** | **AWS Site-to-Site VPN** | **AWS Direct Connect** | **Consumer-managed transit VPC** | **Public internet access** |
| --- |--- |--- |--- |--- |
| **Ease of integration** | 3 | 1 | 4 | 5 |
| **TCO** | 3 | 1 | 5 | 4 |
| **Scalability** | 3 | 1 | 5 | 5 |
| **Adaptability** | 3 | 2 | 4 | 5 |
| **Network isolation** | 3 | 4 | 5 | 1 |
| **Observability** | 4 | 4 | 5 | 5 |
| **Time to repair** | 4 | 2 | 5 | 5 |

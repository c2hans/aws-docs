---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-eks-observability-best-practices/next-steps.html
---

# Next steps
<a name="next-steps"></a>

This guide provided a comprehensive framework for implementing robust observability in Amazon EKS environments, focusing on metrics collection, logging infrastructure, distributed tracing, and cost optimization. By understanding and applying these core components, you can build a highly observable, maintainable, and cost-effective container environment that provides deep insights into application and infrastructure behavior. The integration of AWS services such as [Amazon CloudWatch Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html) and [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html), combined with open-source solutions such as Prometheus and OpenTelemetry, creates a powerful foundation for monitoring and troubleshooting containerized applications.

Implementation success relies on a phased approach, starting with core metrics collection and gradually expanding to comprehensive logging and distributed tracing capabilities. We recommend that you begin by assessing your current monitoring capabilities, identifying gaps, and selecting appropriate tooling combinations that align with your operational requirements and team expertise. This methodical approach ensures that each component of the observability stack is properly implemented and integrated, while teams develop the necessary skills and processes to effectively use these tools.

The long-term sustainability of Amazon EKS observability depends on regular optimization of costs, resources, and processes. You should continuously review and adjust your observability infrastructure, including data retention policies, sampling rates, and resource allocation, to maintain the right balance between comprehensive monitoring and operational efficiency. This iterative approach to improvement, combined with ongoing team training and documentation updates, enables your organization to maintain effective observability while supporting business growth and adapting to evolving application architectures.

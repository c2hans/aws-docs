---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/access-proxy.html
---

# Access proxy
<a name="access-proxy"></a>

Centralized Logging with OpenSearch creates an [Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) together with an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html).

 **Centralized Logging with OpenSearch creates an Auto Scaling group together with an Application Load Balancer.**

![image15](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image15.png)

The workflow is as follows:

1. Users access the custom domain for the proxy, and the domain must be resolved via DNS service (for example, using Route 53 on AWS).

1. The DNS service routes the traffic to internet-facing Application Load Balancer.

1. The Application Load Balancer distributes traffic to a backend NGINX server running on Amazon EC2 within an Auto Scaling group.

1. (optional) VPC peering is required if the VPC for the proxy is not the same as the OpenSearch Service.

1. The NGINX server redirects the requests to OpenSearch Dashboards.

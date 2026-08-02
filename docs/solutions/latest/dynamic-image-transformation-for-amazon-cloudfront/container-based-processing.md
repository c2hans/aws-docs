---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/container-based-processing.html
---

# Container-based processing
<a name="container-based-processing"></a>

 **ECS tasks with AWS Fargate**

Containerized image processing applications running on AWS Fargate with automatic scaling based on CPU utilization and request volume. The architecture offers T-shirt sizing options (S, M, L, XL) for different performance requirements while requiring no server management as Fargate handles infrastructure provisioning.

 **Application Load Balancer**

Distributes requests across multiple ECS tasks for high availability with health checks ensuring traffic routes only to healthy container instances. The load balancer provides support for connection pooling and keep-alive connections, along with SSL termination and HTTP/2 support for optimal performance.

 **Scaling configuration**

The minimum task count ensures baseline capacity while the maximum task count prevents runaway scaling costs. Target CPU utilization triggers scale-out events, and scale-in cooldown periods prevent thrashing to maintain stable performance.

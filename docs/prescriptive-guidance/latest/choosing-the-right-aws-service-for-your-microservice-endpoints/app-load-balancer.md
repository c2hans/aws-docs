---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-the-right-aws-service-for-your-microservice-endpoints/app-load-balancer.html
---

# Application Load Balancer
<a name="app-load-balancer"></a>

[Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) is designed primarily for distributing incoming HTTP and HTTPS traffic across multiple targets, such as Amazon Elastic Compute Cloud (Amazon EC2) instances, containers, Lambda functions, and private IP addresses. For endpoint security, Application Load Balancer integrates with [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) and supports network security controls like security groups and network access control lists (ACLs).

Application Load Balancer offers [advanced request routing capabilities](https://exampleloadbalancer.com/advanced_request_routing_detail.html). With advanced request routing, developers can write rules (and route traffic) based on standard and custom HTTP headers and methods, the request path, the query string, and the source IP address. Its advanced request routing features makes Application Load Balancer well-suited for multiple use cases.

## Application Load Balancer use cases
<a name="alb-use-cases"></a>

Use cases for Application Load Balancer include the following:
+ **High availability and fault tolerance** – Distribute traffic across multiple targets in multiple Availability Zones. Application Load Balancer automatically routes traffic to healthy targets.
+ **Traffic segmentation and device-specific content** – Separate bot and crawler traffic from human traffic for improved security. Route customers or groups to distinct target groups for personalized experiences. Deliver tailored pages and user experiences for various device types and categories.
+ **Testing and release management** – Implement A/B testing for feature evaluation before global deployment. Perform canary and blue/green deployments with minimal disruptions.
+ **Access control and securing web applications** – Implement access restrictions based on IP addresses or content delivery network (CDN) providers to enhance security. With Application Load Balancer, you can offload SSL/TLS encryption and decryption, reducing the computational load on your backend servers.
+ **Hybrid cloud architecture and modernization** – Selectively route traffic between on-premises and cloud-based target groups for flexible deployments. For legacy applications hosted on EC2 instances or containers, gradually modernize the system by routing specific HTTP methods to specific microservice handlers. Examples of HTTP methods include PUTs and GETs.

The following diagram shows an Application Load Balancer that's configured to meet the routing requirements of multiple microservices supporting a web application. Requests for Service A are routed to a target group that's comprised of Amazon EC2 instances (a monolith). Service B has a new release that the developer wants to test with a small audience. The Application Load Balancer weighted target groups feature directs 90 percent of requests to the blue version of a blue/green deployment (Amazon EC2 with Service B). The weighted target groups feature directs 10 percent of requests to the green version (AWS Fargate with Service B).

![Application Load Balancer for HTTP endpoint with advanced request routing.](http://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-the-right-aws-service-for-your-microservice-endpoints/images/guide-img/45387eb1-39dc-4dd7-a6b2-e3cd572b2949/images/b512c3e1-002d-45e5-97a8-0e8b8b444216.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

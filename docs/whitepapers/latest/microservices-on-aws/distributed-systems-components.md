---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/distributed-systems-components.html
---

# Distributed systems components
<a name="distributed-systems-components"></a>

 In a microservices architecture, service discovery refers to the process of dynamically locating and identifying the network locations (IP addresses and ports) of individual microservices within a distributed system.

 When choosing an approach on AWS, consider factors such as:
+  **Code modification:** Can you get the benefits without modifying code?
+  **Cross-VPC or cross-account traffic:** If required, does your system need efficient management of communication across different VPCs or AWS accounts?
+  **Deployment strategies:** Does your system use or plan to use advanced deployment strategies such as blue-green or canary deployments?
+  **Performance considerations:** If your architecture frequently communicates with external services, what will be the impact on overall performance?

 AWS offers several methods for implementing service discovery in your microservices architecture:
+  **Amazon ECS Service Discovery:** Amazon ECS supports service discovery using its DNS-based method or by integrating with AWS Cloud Map (see [ECS Service discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html)). ECS Service Connect further improves connection management, which can be especially beneficial for larger applications with multiple interacting services.
+  **Amazon Route 53:** Route 53 integrates with ECS and other AWS services, such as EKS, to facilitate service discovery. In an ECS context, Route 53 can use the ECS Service Discovery feature, which leverages the Auto Naming API to automatically register and deregister services.
+  **AWS Cloud Map:** This option offers a dynamic API-based service discovery, which propagates changes across your services.

 For more advanced communication needs, **Amazon VPC Lattice** is an application networking service that consistently connects, monitors, and secures communications between your services, helping to improve productivity so that your developers can focus on building features that matter to your business. You can define policies for network traffic management, access, and monitoring to connect compute services in a simplified and consistent way across instances, containers, and serverless applications.

 In case you're already using third-party software, such as [HashiCorp Consul](https://www.consul.io/), or [Netflix Eureka](https://github.com/Netflix/eureka) for service discovery, you might prefer to continue using these as you migrate to AWS, enabling a smoother transition.

 The choice between these options should align with your specific needs. For simpler requirements, DNS-based solutions like Amazon ECS or AWS Cloud Map might be sufficient. For more complex or larger systems, service meshes like Amazon VPC Lattice might be more suitable.

 In conclusion, designing a microservices architecture on AWS is all about selecting the right tools to meet your specific needs. By keeping in mind the considerations discussed, you can make sure you're making informed decisions to optimize your system's service discovery and inter-service communication.

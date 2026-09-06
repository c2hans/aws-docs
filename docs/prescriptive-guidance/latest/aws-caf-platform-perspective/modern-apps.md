---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/modern-apps.html
---

# Modern application development
<a name="modern-apps"></a>

**Build well-architected, cloud-native applications.**

[Modern application](https://aws.amazon.com/modern-apps/) development practices are essential for organizations to build well-architected, cloud-native applications and remain competitive*.* Businesses can use cloud-native technologies such as [containers](https://aws.amazon.com/containers/) and [serverless](https://aws.amazon.com/serverless/) computing to create scalable and agile applications that adapt to changing market demands. These technologies enable organizations to optimize resource utilization, reduce costs, and improve the performance of their applications.

When you design your modern applications, develop agile solutions for operations and development. A modern application automatically reacts to changes in customer demand and is resilient to failure. Engineers can develop and deploy changes quickly and monitor application performance. A modern application is designed to be self-healing and capable of scaling to both large or small levels of traffic, including no traffic at zero cost, when needed.

Building well-architected, cloud-native applications requires a deep understanding of the underlying technologies and their best practices. Organizations should adopt a microservices architecture and design their applications to be modular and loosely coupled, allowing for independent deployment and scalability. This approach enables organizations to break down their applications into smaller, more manageable components that are developed, tested, and deployed quickly and independently.

## Start
<a name="modern-apps-start"></a>

### Explore modern approaches
<a name="explore-modern-approaches.222c3ae7-1984-548c-b6ab-c5bcde646462"></a>

Start by investigating containers, serverless technologies, and other approaches that enable the development of [microservices](https://aws.amazon.com/microservices/), which enhance resource efficiency, help improve security, and minimize infrastructure expenses. Choose to modernize your existing differentiating and enterprise applications to improve efficiency and maximize the value of your existing investments. Contemplate [replatforming](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-replatforming-cots-applications/welcome.html) (transitioning your self-managed containers, databases, or message brokers to managed cloud services) and [refactoring](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/welcome.html) (redeveloping your applications to adopt cloud-native architectures) based on value-led decision-making.

When you update your existing cloud-based application, a successful approach involves using the [strangler fig pattern](https://aws.amazon.com/blogs/architecture/seamlessly-migrate-on-premises-legacy-workloads-using-a-strangler-pattern/) to progressively decompose your architecture into microservices. This procedure aids in adopting a contemporary application methodology, so you can realize the inherent benefits and demonstrate its value to the larger organization. Consider constructing your applications as distinct microservices that harness [event-driven](https://aws.amazon.com/event-driven-architecture/) architectures where applicable. Ensure that your architecture takes into account unchangeable [service quotas](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/manage-service-quotas-and-constraints.html) and physical resources to avoid affecting workload performance or reliability.

### Adopt cloud-native compute capabilities
<a name="adopt-cloud-native-compute-capabilities.ece1d6e8-2a0c-5962-9026-69312019cbb1"></a>

Cloud-native computing capabilities are key for modern application development. This approach requires organizations to consider how they want their compute units to be hosted and identify the best option for each use case or service. For example, [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) offers a serverless mechanism for running your application code and plays a key role in event-driven architectures. Lambda functions are launched on demand and run in parallel up to a defined maximum concurrency, so they can scale to perform a variety of tasks.

### Use containerization
<a name="use-containerization.fc1f1879-54c7-5f69-9e00-05fa004de166"></a>

In modern software development, managing applications and their dependencies has become an increasingly complex task, especially when you consider the need to maintain consistency across various environments. To address these challenges, containerization technologies such as Docker have emerged as an effective solution for packaging applications and their dependencies. Containers ensure consistent and reproducible deployments regardless of your application's runtime environment, so development in your local environment behaves in the same manner as production development in the cloud environment. This approach reduces errors that might be caused by mismatches within the environment or its configurations.

### Use modern databases
<a name="use-modern-databases.be2f59e1-d2d7-5612-ad67-117e31f4d2b3"></a>

When you use modern databases, each microservice within your application can use the right purpose-built database that meets its requirements, which increases agility and performance while lowering costs. For example, one microservice might use a NoSQL database to achieve high throughput when storing session data, another microservice might use a relational database to do complex table joins, and yet another microservice might use a quantum ledger database to track changes to the blockchain.

Modern databases offer scalability and flexibility. They also help provide better security, compliance, and reliability than traditional databases. They enable organizations to store and manage their data more efficiently and ensure that applications can access the right data at the right time, leading to better performance and user experience.

Migrating to modern databases is a critical component of modern application development. By using the right data storage solutions, organizations can optimize their data management capabilities and deliver more efficient and reliable applications. By making each microservice independent and choosing the right technologies for each microservice, organizations can further optimize their data capabilities to achieve maximum efficiency and scalability while minimizing costs.

## Advance
<a name="modern-apps-advance"></a>

### Optimize your modern architecture
<a name="optimize-your-modern-architecture.73dc1802-7c1f-5b8c-8e49-25780ade5fb4"></a>

To achieve further optimizations, refine your implementation of serverless technologies and develop architectures that can be independently scaled and deployed by using AWS services such as [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) and [AWS Lambda.](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) Implement service discovery by using [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) and [AWS Cloud Map](https://docs.aws.amazon.com/cloud-map/latest/dg/what-is-cloud-map.html) to ensure seamless communication between components.

Adopt API versioning, caching, and rate limiting to maintain compatibility and performance across different application versions. Enhance security with [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) and resource policies. These help ensure that your infrastructure is protected and access is granted only to authorized entities.

If possible, use serverless services to run containers without having to manage the underlying infrastructure. This enables you to focus on developing your core applications and allows for better resource management and performance. It also helps you take full advantage of the benefits of scalability, flexibility, and cost efficiency.

By diving deeper into the intricacies of serverless architectures and incorporating these advanced practices, organizations can uncover opportunities for improvement and fine-tuning, and ultimately maximize the potential of their cloud-native applications. This pursuit facilitates the adoption of more sophisticated application patterns that further elevate the overall user experience. It also empowers organizations to become more agile and efficient in their software development processes.

### Use service mesh technologies
<a name="use-service-mesh-technologies.88cc8ea2-570c-57e7-8136-e518cf8a83fb"></a>

As organizations increasingly adopt a microservices architecture for building and deploying applications, managing the complexity, security, and communications among these services becomes critical. Service mesh technologies such as Istio, Linkerd, or Consul play a pivotal role in helping enhance the security, observability, and reliability of microservices.

### Ensure visibility and traceability
<a name="ensure-visibility-and-traceability.8e0cfa7f-d791-56d8-bec5-2783c2db4cb8"></a>

Modern practices provide greater visibility and traceability in the development process, and make it easier to comply with industry standards and best practices. Visibility and monitoring are essential for modern application development. Implementing monitoring and logging solutions to provide valuable insights into application performance enables organizations to identify areas for improvement and optimize their applications. We recommend that you work with your platform engineering teams to ensure that tools are available to provide end-to-end visibility and monitoring of application errors, performance, and compliance, so you can detect, diagnose, and resolve issues quickly.

## Excel
<a name="modern-apps-excel"></a>

### Embrace microservices
<a name="embrace-microservices.6b106075-53cc-5aa7-b07b-6137051b6531"></a>

For many organizations, modern application development is synonymous with business success. Microservices are at the heart of this transformation, and organizations can benefit from embracing these powerful architectural patterns.

Microservices offer a highly scalable, resilient, and agile application architecture. By breaking an application down into small, independently deployable services, organizations can choose to rapidly iterate on specific components without impacting other parts of the application. Advanced resiliency patterns, such as *circuit breakers* and *bulkheads*, play a crucial role in ensuring the high availability of these applications.

[Circuit breakers](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html) act as a safety mechanism that prevents cascading failures by temporarily halting or shifting communications from an unhealthy service, so it can recover. [Bulkheads](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_use_bulkhead.html), isolate resources and limit the scope of impact of potential failures. Together, these patterns create a robust architecture that withstands unforeseen disruptions and maintains optimal performance.

Another critical aspect of implementing microservices is the adoption of domain-driven design (DDD) principles. DDD focuses on creating a shared understanding of the business domain and translating it into a well-structured software design. This approach leads to more cohesive and maintainable microservices, and ensures that the application evolves in step with the organization's needs.

Optimizing inter-service communication is also vital in a microservices-based application. By implementing advanced protocols such as gRPC or GraphQL, organizations can significantly enhance communication efficiency between services. These protocols offer capabilities such as type safety, low latency, and flexibility, which help improve the overall performance and maintainability of the application.

An organization that adopts microservices provides an environment that fosters innovation, agility, and collaboration. The development teams are typically organized around business capabilities and have a strong focus on continuous integration and continuous delivery (CI/CD) practices. They are empowered to make decisions, experiment, and iterate quickly, and they embrace a culture of shared responsibility and accountability.

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/internal-developer-platform/principles.html
---

# Principles of building an internal developer platform
<a name="principles"></a>

## Adopt a product mindset
<a name="product-mindset"></a>

A key principle of success is to treat your internal developer platform as a regular application or a product that has a set of features and a roadmap. This helps you define the set of tools and processes that your internal developer platform will offer. Also, it helps you identify how to measure the success of adopting the platform capabilities, such as improving the software delivery cycle or reducing the quantity of operational incidents. By adopting a product mindset, you can quantify the value provided by the internal developer platform and make sure that it is achieving your original goals.

## Focus on your customers
<a name="customer-focus"></a>

Another important principle is identifying who are the customers of your internal developer platform. Basically, your customers are your developers. Understanding your customer is very important because the goal of the platform is to serve the need of the developers and meet them where they are. This means that the platform roadmap should be aligned. Prioritize features based on what your developers need.

## Provide self-service capabilities on demand and automatically
<a name="self-service"></a>

Another principle of success is that the platform should hide any complexity from developers by providing its capabilities through a self-service mechanism. Whether the team is using a cloud provider or a compute service such as Amazon Elastic Kubernetes Service (Amazon EKS), developers shouldn't care about these details. The internal developer platform needs to provide a simple interface, such as a graphical user interface (GUI), API, or a command-line interface (CLI) that helps developers deliver value. To provide a successful self-service mechanism, it is important to start with the right template design. The template should include the minimum parameters necessary to automate feature delivery. It should automate the testing processes that help developers meet quality gates and security requirements, and it should also provide feedback about key metrics after feature deployment.

A self-service mechanism helps reduce the cognitive load for developers. It reduces the number of services and tools that developers must use to deploy to production. Simplifying the user experience helps you market the platform to more teams. It is important to make sure that the internal developer platform is available on demand, whenever developers want to use it. Then, you must prepare to scale the internal developer platform as you onboard more teams.

## Make use optional and enable the use of specific capabilities
<a name="optional-use"></a>

Not every team can use the internal developer platform on the first day. For example, some teams are modernizing their workloads by using containers, and others use serverless solutions. The internal developer platform starts by supporting one journey, and more features are developed over time. Make use of the platform and its capabilities optional until the platform is scaled and more mature patterns are ready to serve your developers.

This doesn't mean that teams can't use the internal developer platform. Some teams can still manage their tools and processes and also adopt a specific capability of the internal developer platform. For example, teams might adopt a CI/CD pipeline to get infrastructure ready for them. The platform provides value by reducing the time it takes to manage infrastructure, helping developers focus on their application code.

## Define golden paths that align with your security standards
<a name="define-golden-paths"></a>

Golden paths are the most fundamental capability that the internal developer platform should provide. This is because golden paths include the best practices and the standards that help your developers get started in minutes. Golden paths simplify the software development lifecycle (SDLC) experience, from development to observability. They automate most of the capabilities used by the developers, such as source code repositories, testing, deployment, and observability.

However, golden paths are not only about providing automated patterns. They also provide governance to help developers deploy workloads in a secure way that follows organizational compliance requirements. One of the main challenges for developers is to address security early in the development lifecycle. Therefore, it is important to remove this challenge by including security scanning and policy-as-code tools as stages in the golden path. This can provide early feedback to developers and provide a governance framework for deployments.

When designing a golden path, don't make the process unnecessarily difficult. The goal is not to automate every stage in the SDLC at the beginning. The goal is to provide an abstraction layer that can hide all the complexities of using different tools or infrastructure. This helps developers get started quickly and focus on feature development instead of interacting with the underlying services. An example of a golden path is a template where a developer can provide some parameters that point to a source code repository. The internal developer platform automates all the other stages, such as testing, security, scanning, and deployment.

## Document and simplify the onboarding experience
<a name="documentation"></a>

Another important principle of success for the internal developer platform is documentation. The internal developer platform needs to include documentation that provides developers with an easy-to-follow onboarding guide. This guide should focus on how the developer can contribute to the project and not explain the hidden complexities of the interface or platform. For example, the onboarding guide should not describe that the platform is running on Amazon EKS or describe how the AWS account is baselined. The guide should explain service dependencies and the golden paths. For microservice architectures, it can also explain how services are connected.

Documentation and a simple onboarding experience minimize the amount of time that developers need to understand and use the internal developer platform. If you want to measure how effective the documentation was, the *code change volume metric *can be useful. This metric can provide data about who makes the greatest number of code changes and which repositories are the most active over time. You can collect the data at the developer or repository level.

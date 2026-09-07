---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/silo-compute-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Silo compute considerations
<a name="silo-compute-considerations"></a>

 As you look to silo the compute resources of your application (like the microservices shown above), you’ll want to think about how the isolation models of different compute services might influence your approach. The unique attributes of the various AWS compute services may also require you to take specific measures to ensure that your resources are adequately isolated.

![Diagram showing container silo isolation.](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/container-silo-isolation.png)

 Let’s start by looking at what it would mean to implement the silo model with containers. The challenge of isolating containers is that there are cases where malicious code or poorly configured environments can *escape* a container and assume permissions that would enable one tenant to access the resources of another tenant. Fortunately, containers offer constructs that, when used properly, can implement a robust isolation model. The mechanisms that are used to prevent cross-tenant access can vary across the different AWS container services. With Amazon Elastic Container Service (Amazon ECS), for example, you’ll need to create a separate cluster for each tenant to achieve silo isolation. Amazon Elastic Kubernetes Service (Amazon EKS) introduces some additional mechanisms that will let you silo resources within an EKS cluster. The diagram in Figure 10 provides a look at how you would achieve silo isolation within and EKS cluster.

 This example shows two separate groupings of tenants within an EKS cluster where an EKS namespace was used to isolate these compute resources. While namespace provides the foundation of your silo isolation here, namespaces alone don’t provide complete isolation. To get full isolation, you need to consider using one of the AWS or partner sidecar solutions that can be used to further lock down the flow between containers. AWS App Mesh and Tigera’s Calico represent two examples of solutions that could be used to achieve this added layer of isolation.

 AWS Lambda also adds a twist to the silo isolation model. When you think about a Lambda function, you’d presume that it’s already isolated since any one tenant can only be executing a function at a given moment in time. However, if a Lambda function is deployed with an execution role that supports all tenants, then there’s still the possibility that this function could access a resource that belongs to another tenant. While the pool

 (as we’ll see below) provides us a way around this, a fully siloed version of a Lambda function would mean that this function would not be executed by other tenants. The diagram in Figure 11 provides an example of how you might realize full isolation in a Lambda model.

![Diagram showing Lambda Silo Isolation.](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/lambda-silo-isolation.png)

 This diagram includes two separate tenants that have been deployed in a Lambda silo model. Because we want to ensure that tenant will remain within tenant boundaries, we have deployed separate functions for each tenant where these functions are configured and deployed with a tenant specific role that constrains their access to resources that are associated with that tenant.

 This approach has pros and cons. While it can be a compelling isolation story, it is unwieldy and may exceed limits for the Lambda service. Imagine managing and deploying separate functions for 1K tenants. That would become difficult to manage and would undermine the agility of your SaaS goals. At the same time, if you offered this option to a select collection of premium tenants and limited the broader expansion of this model, it would be more reasonable to manage and operate.

 The key takeaway here is that, as you consider how to implement your silo model, you’ll also need to be thinking about how the silo model is realized on the different AWS compute services. The strategy of silo isolation can change for each service.

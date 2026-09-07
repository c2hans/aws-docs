---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/soap.html
---

# SOAP-based ASP.NET web services
<a name="soap"></a>

When you modernize a legacy ASP.NET web service (ASMX) to a REST API on AWS, it might have dependent consumers that can't, and most likely shouldn't due to the associated risks, be upgraded at the same time. The following illustration depicts an ASMX web service that has three dependent consumers.

![Three service consumers dependent on a legacy, SOAP-based ASMX service.](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/images/guide-img/5e1df9e0-2643-4e7a-8b08-fc2f99f03ade/images/2f082dfe-e379-47ef-b266-c3c8aa78d0d5.png)

Because these consumers call the ASMX service by using the SOAP protocol, replacing the ASMX service with a REST API would cause these consumers to break. Furthermore, refactoring the ASMX service to a REST API while you convert the system from a monolithic architecture to microservices will most likely involve remodeling the system behavior and domain model. This is likely to create additional breaking changes for consumers.

To maintain backward compatibility with the old service so that the system can be incrementally modernized, you can implement the guidance of the strangler fig approach. In the strangler fig approach, risks associated with modernizing an important legacy system are, in part, managed by gradually replacing the legacy system with a new one.

Branch by abstraction is another approach introduced by Martin Fowler that is an effective technique for implementing the strangler fig pattern. As with the strangler fig approach, branch by abstraction helps engineers make incremental and gradual changes to systems when major pieces of functionality have to be replaced or modernized. In this approach, an abstraction layer is introduced between the code that implements specific functionality and the code that consumes that functionality (that is, client code). This abstraction layer doesn't have to be an abstract type that can be inherited by concrete classes. Instead, it can be any implementation that captures the functional contract between the consumer and the provider.

In the case of legacy SOAP-based ASP.NET web services, you can enable the gradual migration of service consumers from old to new by maintaining compatibility, through an approach that is inspired by the branch by abstraction technique. However, the approach for SOAP-based ASP.NET web services uses delegation instead of inheritance. Compatibility with ASMX consumers is achieved by refactoring the legacy ASMX service to delegate its implementation to the new REST API. The following illustration depicts the legacy ASMX service that is delegating its implementation to the new REST API. This delegation allows service consumer 3 to upgrade to the new REST API while service consumers 1 and 2 are upgraded independently.

![Refactoring of the ASMX web service to delegate its implementation to the new REST API.](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/images/guide-img/5e1df9e0-2643-4e7a-8b08-fc2f99f03ade/images/f9d6437a-c7ef-4efb-971c-814f7552da7e.png)

The nature of the ASMX service refactoring depends on the functional and non-functional (cross-functional) requirements of that service. In some cases, the refactoring might involve translating from the old to the new authentication and authorization mechanisms, transforming the service ASMX payload from XML to JSON, and then invoking the REST API with the transformed payload. In more complex scenarios, the refactored ASMX service might have to orchestrate calls to multiple REST APIs and maintain state.

The process of migrating service consumers from the legacy ASMX service to the modernized REST API continues incrementally until all service consumers have been updated to reference the new API. The following illustration depicts the fully modernized state, where all service consumers reference the REST API, and the ASMX service has been decommissioned because it is no longer needed.

![All service consumers reference the modern REST API, and the ASMX is decommissioned.](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/images/guide-img/5e1df9e0-2643-4e7a-8b08-fc2f99f03ade/images/0604e351-0b0b-47b3-854f-31bae8f69e55.png)

## Example architecture
<a name="architecture"></a>

The end-state architecture for the SOAP-based ASMX service shows all service consumers using the modernized REST API, leading to the decommissioning of the legacy ASMX web service. However, the focus of this pattern is not the end-state architecture, but the interim-state architecture needed during migration, while consumers are being upgraded. This interim state is illustrated in the following diagram. In this interim architecture, service consumers 1 and 2 are still using the legacy ASMX service, which has been refactored to delegate its implementation to the modernized REST API. The refactored Windows service is deployed as a Windows container in Amazon ECS, configured across three Availability Zones for high availability, and accessed through an Application Load Balancer. Service consumer 3 has been updated to use the new REST API directly through API Gateway.

![Modernized ASP.NET SOAP-based web service interim-state architecture.](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/images/guide-img/5e1df9e0-2643-4e7a-8b08-fc2f99f03ade/images/7bf81abb-0e6f-490d-bdb3-2981b739f503.png)

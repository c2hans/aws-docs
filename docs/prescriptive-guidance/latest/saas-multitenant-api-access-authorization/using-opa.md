---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/using-opa.html
---

# Design models for OPA
<a name="using-opa"></a>

## Using a centralized PDP with PEPs on APIs
<a name="using-opa-centralized-pdp"></a>

The centralized policy decision point (PDP) with policy enforcement points (PEPs) on APIs model follows industry best practices to create an effective and easily maintained system for API access control and authorization. This approach supports several key principles:
+ Authorization and API access control are applied at multiple points in the application.
+ Authorization logic is independent of the application.
+ Access control decisions are centralized.

This model uses a centralized PDP to make authorization decisions. PEPs are implemented at all APIs to make authorization requests to the PDP. The following diagram shows how you can implement this model in a hypothetical multi-tenant SaaS application.

![OPA design model with centralized PDP](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/17f68cd9-dc60-4588-a947-b33c1ecc7b64.png)

In this architecture, PEPs request authorization decisions at the service endpoints for Amazon CloudFront and Amazon API Gateway, and for each microservice. The authorization decision is made by an authorization service (the PDP) with an OPA sidecar. You can operate this authorization service as a container or as a traditional server instance. The OPA sidecar exposes its RESTful API locally so the API is accessible only to the authorization service. The authorization service exposes a separate API that is available to PEPs. Having the authorization service act as an intermediary between PEPs and OPA allows for the insertion of any transformation logic between PEPs and OPA that may be necessary—for example, when the authorization request from a PEP doesn't conform to the query input expected by OPA.

You can also use this architecture with custom policy engines. However, any advantages gained from OPA must be replaced with logic provided by the custom policy engine.

A centralized PDP with PEPs on APIs provides an easy option to create a robust authorization system for APIs. It's simple to implement and also provides an easy-to-use, repeatable interface for making authorization decisions for APIs, microservices, Backend for Frontend (BFF) layers, or other application components. However, this approach might create too much latency in your application, because authorization decisions require calling a separate API. If network latency is a problem, you might consider a distributed PDP.

## Using a distributed PDP with PEPs on APIs
<a name="using-opa-distributed-pdp"></a>

The distributed policy decision point (PDP) with policy enforcement points (PEPs) on APIs model follows industry best practices to create an effective system for API access control and authorization. As with the centralized PDP with PEPs on APIs model, this approach supports the following key principles:
+ Authorization and API access control are applied at multiple points in the application.
+ Authorization logic is independent of the application.
+ Access control decisions are centralized.

You might wonder why access control decisions are centralized when the PDP is distributed. Although the PDP might exist in multiple places in an application, it must use the same authorization logic to make access control decisions. All PDPs provide the same access control decisions given the same inputs. PEPs are implemented at all APIs to make authorization requests to the PDP. The following figure shows how this distributed model can be implemented in a hypothetical multi-tenant SaaS application.

In this approach, PDPs are implemented in multiple places in the application. For application components that have onboard compute capabilities that can run OPA and support a PDP, such as a containerized service with a sidecar or an Amazon Elastic Compute Cloud (Amazon EC2) instance, PDP decisions can be integrated directly into the application component without having to make a RESTful API call to a centralized PDP service. This has the benefit of reducing the latency that you might encounter in the centralized PDP model, because not every application component has to make additional API calls to obtain authorization decisions. However, a centralized PDP is still necessary in this model for application components that do not have onboard compute capabilities that enable direct integration of a PDP—such as the Amazon CloudFront or Amazon API Gateway service.

The following diagram shows how this combination of a centralized PDP and a distributed PDP can be implemented in a hypothetical multi-tenant SaaS application.

![OPA design model with distributed PDP](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/0c285b6d-1541-4f6b-92fe-5621cd87911a.png)

In this architecture, PEPs request authorization decisions at the service endpoints for CloudFront and API Gateway, and for each microservice. The authorization decision for microservices is made by an authorization service (the PDP) that operates as a sidecar with the application component. This model is possible for microservices (or services) that run on containers or Amazon Elastic Compute Cloud (Amazon EC2) instances. Authorization decisions for services such as API Gateway and CloudFront would still require contacting an external authorization service. Regardless, the authorization service exposes an API that is available to PEPs. Having the authorization service act as an intermediary between PEPs and OPA allows for the insertion of any transformation logic between PEPs and OPA that might be necessary—for example, when the authorization request from a PEP doesn't conform to the query input expected by OPA.

You can also use this architecture with custom policy engines. However, any advantages gained from OPA must be replaced with logic provided by the custom policy engine.

A distributed PDP with PEPs on APIs provides an option to create a robust authorization system for APIs. It's simple to implement and provides an easy-to-use, repeatable interface for making authorization decisions for APIs, microservices, Backend for Frontend (BFF) layers, or other application components. This approach also has the advantage of reducing the latency that you might encounter in the centralized PDP model.

## Using a distributed PDP as a library
<a name="using-opa-library"></a>

You can also request authorization decisions from a PDP that is made available as a library or package for use within an application. OPA can be used as a Go third-party library. For other programming languages, adopting this model generally means that you must create a custom policy engine.

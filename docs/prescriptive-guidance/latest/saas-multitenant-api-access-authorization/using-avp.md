---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/using-avp.html
---

# Design models for Amazon Verified Permissions
<a name="using-avp"></a>

## Using a centralized PDP with PEPs on APIs
<a name="using-avp-pdp"></a>

The centralized policy decision point (PDP) with policy enforcement points (PEPs) on APIs model follows industry best practices to create an effective and easily maintained system for API access control and authorization. This approach supports several key principles:
+ Authorization and API access control are applied at multiple points in the application.
+ Authorization logic is independent of the application.
+ Access control decisions are centralized.

![Using a centralized PDP with PEPs on APIs](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/82996376-fd1f-4369-92bf-820a383ef7d7.png)

This model uses a centralized PDP to make authorization decisions. PEPs are implemented at different points to make authorization requests to the PDP. The following diagram shows how you can implement this model in a hypothetical multi-tenant SaaS application.

In this architecture, PEPs request authorization decisions at the service endpoints for Amazon CloudFront and Amazon API Gateway and for each microservice. The authorization decision is made by the authorization service, Amazon Verified Permissions (the PDP). Because Verified Permissions is a fully managed service, you don't have to manage the underlying infrastructure. You can interact with Verified Permissions by using a RESTful API or the AWS SDK.

You can also use this architecture with custom policy engines. However, any advantages gained from Verified Permissions must be replaced with logic that's provided by the custom policy engine.

A centralized PDP with PEPs on APIs provides an easy option to create a robust authorization system for APIs. This simplifies the authorization process and also provides an easy-to-use, repeatable interface for making authorization decisions for APIs, microservices, Backend for Frontend (BFF) layers, or other application components.

## Using the Cedar SDK
<a name="using-avp-cedar"></a>

Amazon Verified Permissions uses the Cedar language to manage fine-grained permissions in your custom applications. With Verified Permissions, you can store Cedar policies in a central location, take advantage of low latency with millisecond processing, and audit permissions across different applications. You can also optionally integrate the Cedar SDK directly into your application to provide authorization decisions without using Verified Permissions. This option requires additional custom application development to manage and store policies for your use case. However, it can be a viable alternative, particularly in cases where access to Verified Permissions is intermittent or not possible because of inconsistent internet connectivity.

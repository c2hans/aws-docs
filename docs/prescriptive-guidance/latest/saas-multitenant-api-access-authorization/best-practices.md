---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/best-practices.html
---

# Best practices
<a name="best-practices"></a>

This section lists some of the high-level takeaways from this guide. For detailed discussions on each point, follow the links to the corresponding sections.

## Select an access control model that works for your application
<a name="selection"></a>

This guide discusses several [access control models](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/access-control-types.html). Depending on your application and business requirements, you should select a model that works for you. Consider how you can use these models to fulfill your access control needs, and how your access control needs might evolve, requiring changes to your selected approach.

## Implement a PDP
<a name="implement-pdp"></a>

The [policy decision point (PDP)](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/pdp.html) can be characterized as a policy or rules engine. This component is responsible for applying policies or rules and returning a decision on whether a particular access is permitted. A PDP allows authorization logic in application code to be offloaded to a separate system. This can simplify application code. It also provides an easy-to-use idempotent interface for making authorization decisions for APIs, microservices, Backend for Frontend (BFF) layers, or any other application component. A PDP can be used to enforce tenancy requirements consistently across an application.

## Implement PEPs for every API in your application
<a name="implement-pep"></a>

The implementation of a [policy enforcement point (PEP)](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/pep.html) requires determining where access control enforcement should occur in an application. As a first step, locate the points in your application where you can incorporate PEPs. Consider this principle when deciding where to add PEPs:

*If an application exposes an API, there should be authorization and access control on that API.*

## Consider using Amazon Verified Permissions or OPA as a policy engine for your PDP
<a name="use-avp-opa"></a>

Amazon Verified Permissions has advantages over custom policy engines. It is a scalable, fine-grained permissions management and authorization service for the applications that you build. It supports writing policies in the high-level declarative open-source language Cedar. As a result, implementing a policy engine by using Verified Permissions requires less development effort than implementing your own solution. In addition, Verified Permissions is fully managed, so you don't have to manage the underlying infrastructure.

The Open Policy Agent (OPA) has advantages over custom policy engines. OPA and its policy evaluation with Rego provide a flexible, pre-built policy engine that supports writing policies in a high-level declarative language. This makes the level of effort required for implementing a policy engine significantly less than building your own solution. Furthermore, OPA is quickly becoming a well-supported authorization standard.

## Implement a control plane for OPA for DevOps, monitoring, and logging
<a name="implement-control-plane"></a>

Because OPA doesn't provide a means to update and track changes to authorization logic through source control, we recommend that you [implement a control plane](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/considerations.html#monitoring) to perform these functions. This will allow for updates to be more easily distributed to OPA agents, particularly if OPA is operating in a distributed system, which will reduce the administrative burden of using OPA. Additionally, a control plane can be used to collect logs for aggregation and to monitor the status of OPA agents.

## Configure logging and observability features in Verified Permissions
<a name="configure-avp-logging"></a>

Verified Permissions provides easy access to observability features. You can configure the service to log all access attempts to AWS CloudTrail, Amazon CloudWatch log groups, S3 buckets, or Amazon Data Firehose delivery streams to enable a quick response to security incidents and audit requests. Additionally, you can monitor the health of the service through the AWS Health Dashboard. Because Verified Permissions is a managed service, its health is maintained by AWS, and you can configure its observability features by using other AWS managed services.

## Use a CI/CD pipeline to provision and update policy stores and policies in Verified Permissions
<a name="use-cd-cd-pipeline"></a>

Verified Permissions is a managed service, so you don't have to manage, configure, or maintain control planes or agents to perform updates. However, we still recommend that you use a continuous integration and continuous deployment (CI/CD) pipeline to administer the deployment of Verified Permissions policy stores and policy updates by using the AWSSDK. This effort can remove manual effort and reduce the likelihood of operator errors when you make changes to Verified Permissions resources.

## Determine whether external data is required for authorization decisions, and select a model to accommodate it
<a name="select-external-data-model"></a>

If a PDP can make authorization decisions based solely on data that is contained in a JSON Web Token (JWT), it is usually not necessary to import external data to assist in making these decisions. If you use Verified Permissions or OPA as a PDP, it can also accept additional input that is passed as part of the request, even if this data isn't included in a JWT. For Verified Permissions, you can use a context parameter for the additional data. For OPA, you can use JSON data as overload input. If you use a JWT, context or overload input methods are generally far easier than maintaining external data in another source. If more complex external data is required to make authorization decisions, [OPA offers several models for retrieving external data](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/considerations.html#external-data), and Verified Permissions can supplement data in its authorization requests by referencing external sources with an authorization service.

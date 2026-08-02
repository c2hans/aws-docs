---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/pep.html
---

# Implementing a PEP
<a name="pep"></a>

A policy enforcement point (PEP) is responsible for receiving authorization requests that are sent to the policy decision point (PDP) for evaluation. A PEP can be anywhere in an application where data and resources must be protected, or where authorization logic is applied. PEPs are relatively simple compared with PDPs. A PEP is responsible only for requesting and evaluating an authorization decision and doesn't require any authorization logic. PEPs, unlike PDPs, cannot be centralized in a SaaS application. This is because authorization and access control are required to be implemented throughout an application and its access points. PEPs can be applied to APIs, microservices, Backend for Frontend (BFF) layers, or any point in the application where access control is desired or required. Making PEPs pervasive in an application ensures that authorization is verified often and independently at multiple points.

To implement a PEP, the first step is to determine where access control enforcement should occur in an application. Consider this principle when deciding where PEPs should be integrated into your application:

*If an application exposes an API, there should be authorization and access control on that API.*

This is because in a microservices-oriented or service-oriented architecture, APIs serve as separators between different application functions. It makes sense to include access control as logical *checkpoints* between application functions. **We strongly recommend that you include PEPs as a prerequisite for access to each API in a SaaS application.** It is also possible to integrate authorization at other points in an application. In monolithic applications, it might be necessary to have PEPs integrated within the logic of the application itself. There is no single location where PEPs should be included, but consider using the API principle as a starting point.

## Requesting an authorization decision
<a name="request-decision"></a>

A PEP must request an authorization decision from the PDP. The request can take several forms. The easiest and most accessible method for requesting an authorization decision is to send an authorization request or query to a RESTful API that is exposed by the PDP (OPA or Verified Permissions). If you're using Verified Permissions, you can also call the **IsAuthorized** method by using the AWS SDK to retrieve an authorization decision. The only function of a PEP in this pattern is to forward the information that the authorization request or query needs. This can be as simple as forwarding a request received by an API as input to the PDP. There are other methods for creating PEPs. For example, you can integrate an OPA PDP locally with an application written in the Go programming language as a library instead of using an API.

## Evaluating an authorization decision
<a name="evaluate-decision"></a>

PEPs need to include logic to evaluate the results of an authorization decision. When PDPs are exposed as APIs, the authorization decision is likely in JSON format and returned by an API call. The PEP must evaluate this JSON code to determine whether the action being taken is authorized. For example, if a PDP is designed to provide a Boolean *allow* or *deny* authorization decision, the PEP might simply check this value, and then return HTTP status code 200 for *allow* and HTTP status code 403 for *deny*. This pattern of incorporating a PEP as a prerequisite for accessing an API is an easily implemented and highly effective pattern for implementing access control across a SaaS application. In more complicated scenarios, the PEP might be responsible for evaluating arbitrary JSON code returned by the PDP. The PEP must be written to include whatever logic is necessary to interpret the authorization decision that the PDP returns. Because a PEP is likely to be implemented in many different places in your application, we recommend that you package your PEP code as a reusable library or artifact in your programming language of choice. This way, your PEP can be easily integrated at any point in your application with minimal rework.

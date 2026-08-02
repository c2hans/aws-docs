---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/introduction.html
---

# Integrating microservices by using AWS serverless services
<a name="introduction"></a>

*Tabby Ward, Abhishek Agawane, and Matt Kahn, Amazon Web Services*

An important aspect of modernizing your organization's software is to select the right architectural patterns that enable agility and responsiveness to changing business needs. In some applications, a monolithic architecture is a common choice. However, for many organizations, [refactoring monoliths into microservices](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/welcome.html) can be an effective modernization strategy when the use case aligns with the benefits of microservices.

Microservices and monoliths aren't mutually exclusive—many successful organizations employ both patterns together, where modular monoliths serve some domains and microservices handle others.

When microservices are part of your architecture, several services might be called to fetch data for one business transaction. Implementing these integrations requires careful design to address potential challenges such as data consistency, latency, and operational complexity. When microservices are properly integrated, they can provide benefits such as independent scaling, improved development velocity, and potential cost optimizations.

The guide is part of a content series that covers the application modernization approach recommended by AWS. The series also includes:
+ [Phased approach to modernizing applications in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-phased-approach/)
+ [Evaluating modernization readiness for applications in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-assessing-applications/welcome.html)
+ [Decomposing monoliths into microservices](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/welcome.html)

## Intended audience
<a name="audience"></a>

This guide is for application owners, business owners, architects, technical leads, and project managers who have determined that microservices are appropriate for their specific use case. The guide introduces several patterns for synchronous and asynchronous communication between microservices by using serverless AWS services such as AWS Lambda and Amazon API Gateway for autonomy and scalability.

## Objectives
<a name="objectives"></a>

By using this guide to integrate your new microservices, you can efficiently transform your organization's architecture into a microservices architecture. This helps provide rapid adjustment to fluctuating business needs through high scalability, improved resiliency, continuous delivery, and failure isolation. A microservices architecture also speeds up innovation, because each microservice can be individually deployed and tested.

A microservices architecture can also help provide a shorter time to market for your products or services, because each microservice has an independent code base that makes it easier and faster to add new features and iterate on them.

## Security
<a name="security"></a>

You must secure your microservices properly to protect the integrity of your services and data, but ensure that security does not negatively impact the performance of your application.

In a microservices environment, you must consider how each service will authenticate and authorize requests it receives from an external client or another microservice. Also consider how each service will securely access other AWS services.

Access to AWS services should be granted through narrowly scoped [AWS Identity and Access Management (IAM) roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html). Assuming an IAM role provides the microservice with short-term IAM credentials in the form of an access key, an access secret, and a session token. These are used by the various software development kits (SDKs) to sign requests to AWS services by using [AWS Signature Version 4 (SigV4)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html).

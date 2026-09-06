---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/faq.html
---

# FAQ
<a name="faq"></a>

## Can you use multiple patterns to break down one monolith?
<a name="q1"></a>

Yes, you can use multiple patterns to decompose a monolith. The most common way is to decompose a monolith with the [decompose by business capability](decompose-business-capability.md) pattern and then use the [decompose by subdomain](decompose-subdomain.md) pattern to break it down more.

## How does decomposing a monolith into microservices affect the DevOps process?
<a name="q2"></a>

Because you do not have to redeploy everything after a change is made to the application, you must have support and ownership of newly created microservices that are added to the deployment process. This could make the DevOps process more complex.

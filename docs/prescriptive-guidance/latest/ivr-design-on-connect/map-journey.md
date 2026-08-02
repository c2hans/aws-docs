---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ivr-design-on-connect/map-journey.html
---

# Map the customer contact journey
<a name="map-journey"></a>

When your organization's goals have been defined, work back to build a customer journey map. This map helps identify typical engagement patterns and the data required to resolve customer queries.  It also helps define the experience presented to the customer, responses to unplanned events and emergencies, and the volume and scale of customer contacts necessary for deployment.

This step is critical to planning for three [AWS Well Architected](https://aws.amazon.com/architecture/well-architected/) pillars: [operational excellence](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html), [security](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html), and [reliability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).

Here are some questions** **to consider when you create the customer contact journey map:
+ **What is the customer's reason for contact?**

  The answer to this question helps identify frequently asked questions, such as balance inquiries, order status updates, and password resets.
+ **How do you validate the customer's identity?**

  Security is top priority, and validating the customer's identity is a critical step in the contact journey. Authentication options include voice biometrics, one-time passwords, and personal information such as credit card number and date of birth. This information also helps identify compliance requirements such as the Health Insurance Portability and Accountability Act (HIPAA), Payment Card Industry Data Security Standard (PCI DSS), and System and Organization Controls (SOC).
+ **What information do you already have about this customer?**

  After a customer has been identified, relevant customer data can help personalize their experience and solve issues proactively. This data could include the customer name, open cases, contact history and sentiment, and purchase behavior.
+ **What information is needed to resolve the customer's query?**

  Determining the information that is required to address the customer's queries helps define the customer data that should be gathered within the IVR system. For example, if a customer wants to check their balance, their account number and security PIN will be required, and the IVR application will have to integrate with the backend data stores that contain banking data. Checking the status of their order requires the order number.
+ **Are any integrations required to fulfill the customer's request?**

  Typically, self-service requests on the IVR require backend integrations for successful fulfillment. Depending on the use case, these integrations could be with databases, CRMs, or ticketing systems in the organization. For example, communicating the status of an order might require querying the information from an order management system. Purchases might require integrations with a payment gateway. It is crucial to identify these dependencies early, so you can plan for the availability of relevant APIs.
+ **What are the compliance requirements related to the customer's journey or data?**

  It's critical to define compliance objectives and incorporate them in the IVR design. Compliance programs are commonly enforced at an organizational level. We recommend that you engage the information security team in these discussions and planning sessions.

  For example, payment information on the IVR might require encryption and PCI DSS compliance. Personal identifiable information (PII) collected from any customer would require encryption. Your IVR system might involve additional information that you would have to protect.
+ **How do you respond to high call volumes or agent unavailability?**

  It's essential to identify scenarios where high call volume could lead to longer wait times. In these situations, the IVR system often acts as a gateway for effective redirection of customer contacts. Some common deflection strategies include offering callbacks during exceptionally long wait times, designing overflow scenarios that expand the pool of target agents, playing promotional messages, and redirecting a customer to another channel (SMS or chat). For more information about these strategies, see the blog post [How to handle unexpected contact spikes with Amazon Connect Customer](https://aws.amazon.com/blogs/contact-center/how-to-handle-unexpected-contact-spikes-with-amazon-connect/).
+ **What should the customer experience be during holidays or emergencies?**

  Unforeseen emergencies and unplanned events can impact your organization's ability to serve customers. Planning the customer experience during these events is a best practice for reliability. Additionally, holidays might limit staffing, and the IVR system can be an ideal place to keep customers informed and to set expectations.

  For example, you can design emergency placeholders and holiday messages in the IVR system, update them, and play relevant updates when needed.
+ **What should the customer experience be when you experience technical issues?**

  A customer's experience should always be complete and meaningful when they're following the IVR flow, even when application or backend integration errors occur. We recommend that you design the caller experience in the case of integration failures. Typically, you can implement retries and loops, or play a message that communicates the technical difficulty or transfers the customer to an agent. In either scenario, the caller experience should not lead to an abrupt and unexplained end to the communication, which would typically result in more calls.

After you outline the customer contact journey, look for repeatable processes or common patterns. These will be key points of focus when you design the foundation of your IVR architecture.

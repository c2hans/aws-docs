---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/problem-definition-and-approaches.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Problem definition and approaches
<a name="problem-definition-and-approaches"></a>

 This whitepaper and its reference architectures focus on the following data processing requirements that apply to most Operators:
+  [*The data residency principle*](req1-data-residency.md)
+  [*Protection of the data*](req2-measures-to-prevent-unauthorized-or-accidental-access.md)
+  [*Secure and reliable data transfer*](req3-data-access-controls.md)
+  [*Availability and durability of the solution*](req4-availability-and-durability.md)

 The *data residency* requirement may lead to customer considerations around hybrid architectures where some portions of the data and solution are located locally, whereas other portions are in AWS Cloud in Frankfurt or other EMEA Regions. To protect the data in transit between two locations (on-premises and AWS Cloud), the customer may apply certain measures to ensure that data is *securely and reliably transferred* to the AWS Cloud. After that, when persisting the data in AWS Cloud architectures, certain data protection techniques should be implemented to *protect the data* processed in the cloud, and provide for confidentiality and integrity of the relevant customer data. Additionally, the solution as a whole should provide sufficient levels of *availability* and *durability* at all layers, including network.

 This document describes some architectures that you may consider, design, and implement to address the Personal Data Protection requirements. AWS provides only suggestions for certain architectures. It is up to the customer to determine whether these architectures meet the local Data Protection Requirements in the customer’s specific use case, taking into account the scope of the data that the customer processes in the AWS services, and the purpose of the respective processing operations as determined by the customer or its end users.

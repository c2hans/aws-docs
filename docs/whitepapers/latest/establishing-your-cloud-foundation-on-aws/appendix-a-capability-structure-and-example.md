---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/appendix-a-capability-structure-and-example.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix A: Capability structure and example
<a name="appendix-a-capability-structure-and-example"></a>

## Capability structure
<a name="capability-structure"></a>

 **Definition**

 The definition includes a high-level description of what the capability will help you enable in your cloud environment.

 **Scenarios**

 Scenarios are a set of use cases that expand the capability definition, and detail what parts of your environment the guidance included in the capability solves. Each capability provides a baseline, which establishes the minimum requirement for the capability, and can be expanded and customized to add additional scenarios based on your requirements or as your business needs mature and your AWS presence grows.

 **Guidance**

 This section outlines prescriptive recommendations for how the capability should be built in your environment to implement the included scenarios. It also includes responsible stakeholders, and a description of how the capability will work in the overall environment. Additionally, this section includes the people and recommended skillsets necessary to successfully establish the capability in your environment.

 **Implementation guidance**

 Each capability provides prescriptive, opinionated AWS guidance to establish the capability in your environment. Runbooks are included to help you operate the capability efficiently in your environment using AWS services.

## Capability example - Log Storage
<a name="capability-example"></a>

 ****

### Definition
<a name="definition"></a>

 The Log Storage capability enables you to securely collect and store your environment logs centrally within an immutable storage. This will enable you to evaluate, monitor, alert, and audit access and actions performed on your AWS resources and objects.

### Scenarios
<a name="scenarios"></a>
+  Your cloud team wants to log *individual user access* to resources, and what systems are accessed and actions taken (*Individual user access* also includes access by system administrators and system operators).
+  Your cloud team wants to set controls to prevent modification of the related logs.
+  Your cloud team wants to set controls to prevent unauthorized access to logs.
+  Your cloud team wants to generate logs that can show if inappropriate or unusual activity has occurred.
+  Your cloud team wants to store logs in near real-time for resiliency during a determined period of time (matching your governance requirements).
+  Your cloud team wants the stored logs to be encrypted at rest.

### Guidance
<a name="guidance2"></a>

 The Log Storage capability primary mapping is to the **Security Functional Area**. This means the **Security team **should be responsible for implementing this capability.

 When establishing your capability, the builders owning the implementation will need to receive inputs from the owners of additional functional areas to ensure the proper interlock of the functions in the cloud environment. The list of secondary functional areas required are:
+  Operations
+  Central IT

Having a separated Log Storage allows you to establish a secure location where the logs become the source of truth to show what is happening in your environment related to security and operations. As your environment expands to accommodate your business needs, centrally aggregating the information will enable you to later build monitoring and observability capabilities, to monitor in near real-time what is happening across your environment.

The Log Storage must be secured, built for resilience, to avoid tampering with the logs, and only accessed by controlled, automated, and monitored mechanisms, based on least privilege access by role. The following controls need to be implemented around the Log Storage to protect the integrity and availability of the logs and their management process. The logs delivered to Log Storage should be encrypted, and the encryption key access and permissions should also be based on least privilege permissions.
+  **Detective controls** should be implemented to alert and remediate the collection of permissions used on the log storage, and to actively monitor access to the logs within the Log Storage.
+  **Preventive controls** should be implemented to protect from changes to your configuration and access in your Log Storage, and restricting permissions on your Log Storage.

 The Log Storage should also have retention policies, establishing a lifecycle for your logs based on your governance and data retention policy requirements (for example, automatically archiving infrequent access or delete the logs over time to reduce the cost while meeting retention requirements).

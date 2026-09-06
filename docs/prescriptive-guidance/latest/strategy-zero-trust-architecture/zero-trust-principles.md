---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-zero-trust-architecture/zero-trust-principles.html
---

# Understanding Zero Trust principles
<a name="zero-trust-principles"></a>

Zero trust architecture (ZTA) is based on a set of core principles that form the foundation of its security model. Understanding these principles is essential for organizations looking to adopt a ZTA strategy effectively. This section covers the core principles of ZTA.

## Verify and authenticate
<a name="verify-authenticate"></a>

The verify and authenticate principle emphasizes the importance of strong identification and authentication for principals of all types, including users, machines, and devices. ZTA requires continuous verification of identities and authentication status throughout a session, ideally on each request. It doesn't rely solely on traditional network location or controls. This includes implementing modern strong multi-factor authentication (MFA) and evaluating additional environmental and contextual signals during authentication processes. By adopting this principle, organizations can help ensure that resource authorization decisions have the best possible identity inputs.

## Least privilege access
<a name="least-privilege-access"></a>

The principle of least privilege involves granting principals the minimum level of access required to perform their tasks. By adopting the principle of least privilege access, organizations can enforce granular access controls, so that principals have access only to the resources necessary to fulfill their roles and responsibilities. This includes implementing just-in-time access provisioning, role-based access controls (RBAC), and regular access reviews to minimize the surface area and the risk of unauthorized access.

## Micro-segmentation
<a name="micro-segmentation"></a>

Micro-segmentation is a network security strategy that divides a network into smaller, isolated segments for authorizing specific traffic flows. You can achieve micro-segmentation by creating workload boundaries and enforcing strict access controls between different segments.

Micro-segmentation can be implemented through network virtualization, software-defined networking (SDN), host-based firewalls, network access control lists (NACLs), and AWS specific features such as Amazon Elastic Compute Cloud (Amazon EC2) security groups or AWS PrivateLink. Segmentation gateways control traffic between segments to explicitly authorize access. Micro-segmentation and segmentation gateways help organizations restrict unnecessary pathways through the network, particularly those that lead to critical systems and data.

## Continuous monitoring and analytics
<a name="continuous-monitoring-analytics"></a>

Continuous monitoring and analytics involve the collection, analysis, and correlation of security-related events and data across your organization's environment. By implementing robust monitoring and analytics tools, your organization can evaluate security data and telemetry in a converged way.

This principle emphasizes the importance of visibility into user behavior, network traffic, and system activities to identify anomalies and potential security events. Advanced technologies such as security information and event management (SIEM), user and entity behavior analytics (UEBA), and threat intelligence platforms play a vital role in achieving continuous monitoring and proactive threat detection.

## Automation and orchestration
<a name="automation-orchestration"></a>

Automation and orchestration help organizations to streamline security processes, reduce manual intervention, and enhance response times. By automating routine security tasks and using orchestration capabilities, your organization can enforce consistent security policies and rapidly respond to security events. This principle also includes automating access provisioning and deprovisioning processes to help ensure timely and accurate management of user permissions. By embracing automation and orchestration, your organization can improve operational efficiency, reduce human errors, and focus resources on more strategic security initiatives.

## Authorization
<a name="authorization"></a>

In a ZTA, each request to access a resource should be explicitly authorized by a gating enforcement point. In addition to the authenticated identity, authorization policies should consider additional context, such as device health and posture, behavior patterns, resource classification, and network factors. The authorization process should evaluate this converged context against the corresponding access policies that are relevant to the resource being accessed. Optimally, machine learning models can provide a dynamic supplement to the declarative policies. When utilized, these models should focus on additional restrictions only, and they should not grant access that wasn't explicitly specified.

## Section summary
<a name="core-principles-summary"></a>

By adhering to these core principles of ZTA, organizations can establish a robust security model that aligns with the diversity of the modern enterprise environment. Implementing these principles requires a comprehensive approach that combines technology, processes, and people to achieve a zero trust mindset and build a resilient security posture.

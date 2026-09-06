---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/well-architected-framework.html
---

# Well-Architected Framework
<a name="well-architected-framework"></a>

 [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) helps cloud architects build secure, high-performing, resilient, and efficient infrastructure for their applications and workloads. It describes the key concepts, design principles, and architectural best practices for designing and running workloads in the cloud. It is based on five key pillars:
+  Operational excellence
+  Security
+  Reliability
+  Performance efficiency
+  Cost optimization

 When architecting an Amazon WorkSpaces environment, it is important to evaluate these key pillars to determine the maturity deployment level, and discover additional features that can be used with the Amazon WorkSpaces. While there is overall guidance for the [AWS Well-Architect Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html), the following provides some key questions that can be included in the planning phase of your WorkSpaces deployment to ensure each of the five pillars are considered.

 **General**
+  What is the business driver for this project?

## Operational excellence
<a name="operational-excellence"></a>
+  How do you segregate access control between users and different admin groups?

## Security
<a name="wasecurity"></a>

1.  What are the security and compliance requirements to be considered for the WorkSpaces to operate in?

1.  Are there any restrictions on routing to external IP addresses?

1.  Are the required WorkSpaces ports allowed through the corporate firewall?

1.  Is or will multi-factor authentication be used with this deployment?

1.  How do you many user identities and authorization requests today?

## Reliability
<a name="reliability"></a>

1.  What is the data retention policy for desktops?

1.  What is the Recovery Point Objective (RPO) for end-user data?

1.  What is the Recovery Time Objective (RTO) for end-user data?

## Cost optimization
<a name="cost-optimization"></a>

1.  Have the WorkSpaces bundles been [right sized](https://aws.amazon.com/aws-cost-management/aws-cost-optimization/right-sizing/) for the user case and applications?

1.  Will the users consume WorkSpaces more than 82 hours per month?

 While the questions above do not constitute an exhaustive list of items that should be considered, they provide some overarching guidance to assist you with a Well-Architected Amazon WorkSpaces deployment.

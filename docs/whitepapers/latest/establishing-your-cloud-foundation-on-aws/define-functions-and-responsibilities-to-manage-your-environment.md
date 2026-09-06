---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/define-functions-and-responsibilities-to-manage-your-environment.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Define functions and responsibilities to manage your environment
<a name="define-functions-and-responsibilities-to-manage-your-environment"></a>

Federated access grants you the ability to efficiently manage the access to the environment, and should be established and operated centrally. The benefits of managing your identities and controlling access to your environment centrally, allows you to quickly create, update, and delete the permissions and policies you need to meet your business requirements. From granting or revoking permissions to specific users or roles, or by establishing preventative controls on your overall environment, your security teams can manage access to the environment from one place.

The responsibilities to perform certain actions of the environment need to be separated. Granting permissions to perform only the necessary actions to specific roles, and users, depending on the purpose of the service being established, achieving a least privileged access model. You also need to ensure that you group different users by their job family to access different tools with a different set of permissions, and that regardless of the user, there may be some preventative controls needed to set centrally to prevent access or modification to certain resources and areas of your environment.

We recommend that you establish Multi-Factor Authentication (MFA) for every role that has access to your environment, a minimum requirement is to establish MFA for administrator roles. This adds an extra layer of protection on top of your sign-in credentials. Additionally, it is very important that every ***root user user*** has MFA enabled. For access to your organizational account, the root user user MFA needs to be enabled, and the access key and password should be stored separately.

When establishing your environment, you need to set the following functions in your environment, these functions will enable you to manage your overall infrastructure:
+ The **Environment administrator role** manages the overall environment, creates isolated group of resources, sets guardrails, and delegates the administration of different services to the appropriate isolated group of resources and teams.
+ The **Network administrator **manages the network. This function will have access to create and configure network topologies, DNS, VPNs, and build network security across your environment. Network administrators are responsible for securing the network and distributing resources workloads.
+ The **Directory Services administrator **manages access to the environment. This function creates, updates, deletes, assigns, and removes access from different users to the environment.
+ The **Security administrator **manages security services and tools across your environment, ensuring all your services and workloads are running on a secured infrastructure. This function has access to the environment to remediate any possible security threat.
+ The **Billing administrator** manages the spend of your environment and creates budgets and alerts based on the forecasting of your expenses. This function is also responsible to pay the invoice for your environment.
+ The **Read Only Security** function is used to monitor the environment. Security administrators can use this function to oversee the environment in real time and interact with the different security tools, without having full access to the environment
+ The **Security Audit **is an exclusively read only function intended to grant access to external or internal auditors that need to examine the environment.
+  The **Log Storage administrator **manages the log storage in your environment. This function creates or updates the resources needed to security and immutably store your logs, and manages the environment when changes need to be applied.
+ The **Shared Services administrator **manages all the shared services across the environment. For example, this function is used to set up a central DNS or a central Template Management function.
+ The **Support** function will have access to read only permissions for the infrastructure and not the data within each of the isolated group of resources in the environment. This will allow the cloud team to help troubleshooting the environment, and the workload infrastructure when deployed, helping the team solve any issues with the environment or internal workflows. When necessary, it can be used to escalate to find resolution to your cloud service provider.

These functions with the appropriate permissions and boundaries should be assigned to the user groups which job family needs to perform tasks related to the roles above. This will allow them to access, monitor, operate, update, and secure the environment as needed to meet your business requirements. These functions represent responsibilities within your cloud environment, and multiple functions can be assumed by the same team or person.

To achieve this, you will need to build isolation boundaries to limit the access from each group to the services and tools needed to build, deploy, and operate. In some cases, these groups will need to work together to establish a connection to consume services between the boundaries isolating the resources, to create a cohesive environment that is secure and scalable, and provide access to these services to workloads or other foundational services within the environment.

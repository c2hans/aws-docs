---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/decommission-process-isolated-resource-environments.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Decommission process for isolated resource environments
<a name="decommission-process-isolated-resource-environments"></a>

There are various situations when your organization may need to decommission one or more isolated resource environments. For example, you may have a resource environment exclusively designed for and used by a single application that is being decommissioned, you may be using sandbox (disposable) environments, or you might have misconfigured a resource environment during your testing or development phases and determine that the best path is to delete the entire environment. For any situation that requires the decommissioning of isolated resource environments you will want to ensure a consistent termination workflow is in place to prevent unintended charges for resources no longer needed. Additionally, you will want to disable access to the resource environment during any interim waiting period while your resource environment is being terminated.

Similar to how you would approach provisioning isolated resource environments, you will want to have a request process in place for decommissioning isolated resource environments. You should ensure that any dependencies with other isolated resource environments are no longer needed before decommissioning. Internal policies and compliance needs should guide how persistent data within the environment is either deleted, or safely transitioned into a separate environment. We recommend that you carefully consider what assets from the environment should be retained, and how they should be retained. For example, consider retaining assets that could add value to your business in the future or that could augment future projects by transitioning them out of the resource environment prior to termination of the environment.

The decommissioning process should be documented and include guidance on the required steps in the workflow. This might include:
+ A method for determining if any assets or data within the environment should be retained.
+ Applying restrictive controls on the isolated resource environment for a period of time to prevent the use of the resources but allow a recovery process, if necessary.
+ A process or automation for disabling resources or deleting data.

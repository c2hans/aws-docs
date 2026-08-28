---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-use-shutdown.html
---

# Shut down Studio Lab resources
<a name="studio-lab-use-shutdown"></a>

**Note**
Amazon SageMaker Studio Lab is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Studio Lab, but we do not plan to introduce new features. For more information, see [Studio Lab availability change](studio-lab-availability-change.md).

You can view and shut down your running Amazon SageMaker Studio Lab resources from one location in your Studio Lab environment. The running resource types include terminals, and kernels. You can also shut down all resources of one resource type at the same time.

When you shut down all resources belonging to a resource type, the following occurs:
+ **KERNELS** – All kernels, notebooks, and consoles are shut down.
+ **TERMINALS** – All terminals are shut down.

**Shut down Studio Lab resources**

1. Start your Studio Lab project runtime. For more information on launching Studio Lab project runtime, see [Start your project runtime](studio-lab-manage-runtime.md#studio-lab-manage-runtime-start).

1. Choose the **Running Terminals and Kernels** icon (![Square icon with a white outline of a cloud on a dark blue background.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/Running_squid.png)) on the left navigation pane.

1. Choose the **X** symbol to the right of the resource you wish to shut down. You can view the **X** symbol by hovering your cursor over a resource.

1. (Optional) You can shut down all the resources of a given resource type by choosing **Shut Down All** to the right of the resource type name.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

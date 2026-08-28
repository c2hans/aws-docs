---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus05-bp01.html
---

# EUCSUS05-BP01 Optimize machine image creation, copying, and sharing to each environment (like development, testing, and production)
<a name="eucsus05-bp01"></a>

 Using automation with machine images facilitates scalability and elasticity, minimizing over-provisioning and associated energy consumption. Centralized management and compliance reporting further support sustainability initiatives. Overall, automation pipelines contribute to lower environmental impact and improved resource optimization.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance-99"></a>

 Use a dedicated and separate account to create your Amazon AppStream images to manage your changes and your image history. Push the image (copy or share) with other development or production AWS accounts. For more detail, see [UpdateImagePermissions](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateImagePermissions.html) and [UpdateWorkspaceImagePermission](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceImagePermission.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

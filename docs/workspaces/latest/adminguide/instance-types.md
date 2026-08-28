---
source_url: https://docs.aws.amazon.com/workspaces/latest/adminguide/instance-types.html
---

# WorkSpaces Pools Bundles
<a name="instance-types"></a>

A *WorkSpace bundle* is a combination of an operating system, and storage, compute, and software resources. When you launch a WorkSpace, you select the bundle that meets your needs. The default bundles available for WorkSpaces are called *public bundles*. For more information about the various public bundles available for WorkSpaces, see [Amazon WorkSpaces Bundles](https://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles).

The following table provides information about the licensing, streaming protocols, and bundles that are supported by each OS.

| Operating System | Licenses | Streaming protocols | Supported bundles |
| --- | --- | --- | --- |
| Windows Server 2019 | Included | DCV | Value, Standard, Performance, Power, PowerPro |
| Windows Server 2022 | Included | DCV | Standard, Performance, Power, PowerPro, Graphics.G4dn, GraphicsPro.G4dn |

**Note**
Operating system versions that are no longer supported by the vender are not guaranteed to work and are not supported by AWS support.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

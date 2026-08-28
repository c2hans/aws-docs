---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/smf-gpu-driver-lifecycle.html
---

# GPU driver lifecycle
<a name="smf-gpu-driver-lifecycle"></a>

Deadline Cloud supports NVIDIA Long-Term Support (LTS) branch drivers for service-managed fleets. Deadline Cloud plans to continue supporting LTS branches as NVIDIA releases them. For more information about the NVIDIA vGPU software lifecycle, see the [NVIDIA vGPU Software Lifecycle Policy](https://docs.nvidia.com/vgpu/news/vgpu-software-lifecycle-policy/) on the NVIDIA website.

When NVIDIA reaches end-of-life for a driver branch, Deadline Cloud deprecates that driver and eventually removes it. If you use a pinned driver version, migrate your fleets to `latest` or to a newer supported driver before the removal date.

The following table shows the current driver support status.

**GPU runtime driver lifecycle**

| Runtime driver | NVIDIA vGPU software | Branch type | Status | NVIDIA end-of-life |
| --- | --- | --- | --- | --- |
| grid:r580 | vGPU 19 | Long-Term Support | Active | July 2028 |
| grid:r570 | vGPU 18 | Production | Deprecating; scheduled for removal July 12, 2026 | March 2026 (reached) |
| grid:r535 | vGPU 16 | Long-Term Support | Deprecating; scheduled for removal August 5, 2026 | July 2026 |
| grid:r550 | vGPU 17 | Production | Deprecated | Not available |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/default-security-profiles.html
---

# Default security profiles in Connect Customer
<a name="default-security-profiles"></a>

Connect Customer includes default security profiles for general roles. You can review the permissions granted by these profiles and use them if they align with the permissions that your users need. Otherwise, create a security profile that grants your users only the permissions they need.

The following table lists the default security profiles.

| Security profile | Description |
| --- | --- |
| **Admin** | Grants administrators permission to perform a majority of actions. |
| **Agent** | Grants agents permission to access the CCP. |
| **CallCenterManager** | Grants managers permission to perform actions related to user management, metrics, and routing. |
| **QualityAnalyst** | Grants analysts permission to perform actions related to metrics. |

**Note**
New permissions are added on a regular basis. We recommend revisiting your permission configurations to ensure your users can access the latest Connect Customer features.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

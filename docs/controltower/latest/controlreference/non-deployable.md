---
source_url: https://docs.aws.amazon.com/controltower/latest/controlreference/non-deployable.html
---

# Controls that have non-deployable Regions
<a name="non-deployable"></a>

This section lists controls that are not activated when deployed in certain Regions, due to lack of underlying dependencies. This section presents summary information about these non-deployable Regions, for quick reference. You can find the most updated information about the deployable Regions for any control by calling the `ListControls` and `GetControl` APIs. You also can view the deployable Regions in the AWS Control Tower console.

When you activate a control on an OU that's governed by AWS Control Tower, the control's effective area is the intersection of your governed Regions with the control's deployable Regions, with a few minor caveats related to occasional states of mixed governance.

For example, a control can be enabled on an OU that operates in governed Regions X, Y and Z. But after it is enabled, the same control is deployed only on Regions X and Z, because the control itself does not support Region Y.

It's important to monitor the relationships among controls that you deploy and Regions where you operate workloads, so that you don't experience gaps in protection of your AWS resources.

**How to check your protected Regions**
+ In the AWS Control Tower console, you can view the enabled controls and Regions in the **Enabled controls** section.
+ If you call the `GetEnabledControl` API, the **targetRegions** parameter will show only those Regions where you can deploy the control effectively not the non-deployable Regions..

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

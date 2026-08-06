---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-vdi/vdi-operating-modes.html
---

# Large migration considerations for VDI operating modes
<a name="vdi-operating-modes"></a>

You can deploy VDIs in either persistent or non-persistent mode:
+ In *persistent* mode, a user can connect to the same virtual desktop every time. Changes from a previous session are saved for the next time the user connects. Persistent VDIs are typically faster to deploy, but you must manage patching and updating, and they require at least some storage capacity.
+ In *non-persistent* mode, the desktops are generic and identical, and changes are not typically saved for the next session. Non-persistent VDIs can be simpler to manage, more secure, and more cost-effective. Non-persistent VDIs are well suited for those who don't require personalization and who perform a routine, limited set of tasks.

In addition to the general pros and cons for these two deployment options, a few additional considerations apply when moving the VDI solution to the cloud.

The following table describes the benefits and drawbacks of non-persistent VDIs in the cloud.

|
|
| Benefits | Drawbacks |
| --- |--- |
| + *Simplified management* – Use Amazon Machine Images (AMIs) to manage VDIs in order to roll out changes to your entire environment.<br />+ *Improved availability* – You can deploy non-persistent VDIs in multiple Availability Zones, which allows users to access a VDI even when a specific Availability Zone is not accessible.<br />+ *Storage optimization* – You can reduce the storage requirements for non-persistent VDIs. User personalization layers can be moved to shared storage. Also, there is no requirement to back up VDIs.<br />+ *Flexible capacity* – Non-persistent VDIs do not require a one-to-one mapping of users to instances. | + *Complex personalization* – User profiles and applications have to be offloaded to shared storage devices. This can increase implementation effort, operational complexity, and scaling challenges. |

The following table describes the benefits and drawbacks of persistent VDIs in the cloud.

|
|
| Benefits | Drawbacks |
| --- |--- |
| + *Easy personalization* – Store user profiles and applications on the Amazon Elastic Block Store (Amazon EBS) volume for the instance. There is no requirement for shared storage.<br />+ *User customization* – The instance type and storage capacity can be adjusted on a per-user level. | + *Backup complexity* – Persistent VDIs require complex instance-level backup and restore capabilities and processes.<br />+ *Reduced availability* – Users are one-to-one mapped to instances and the corresponding Availability Zone. An Availability Zone failure results in the service being unavailable for the affected users. |

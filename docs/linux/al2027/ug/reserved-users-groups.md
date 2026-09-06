---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/reserved-users-groups.html
---

# AL2027 reserved users and groups
<a name="reserved-users-groups"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

AL2027 pre-allocates certain users and groups, both when an image is provisioned and when specific packages are installed. This section lists the user and group names with their associated UIDs and GIDs. Refer to this list to avoid conflicts when you create users and groups.

AL2027 packages declare their users and groups with `systemd-sysusers` configuration. Some users and groups have a static ID that is the same on every AL2027 instance. Others get a dynamic ID. `systemd-sysusers` allocates that ID from the system range (201-999) when you install the owning package. A name can have a reserved ID in one table and a dynamic ID in the other. For example, the `systemtap-runtime` package reserves its three group IDs and creates its users with dynamic IDs. For a dynamic user or group, the name is reserved but the numeric ID varies between instances. Regular user accounts start at UID and GID 1000. For example, the `ec2-user` account created when an Amazon EC2 instance is provisioned uses UID and GID 1000.

**Topics**
+ [List of AL2027 reserved users](reserved-users.md)
+ [List of AL2027 reserved groups](reserved-groups.md)

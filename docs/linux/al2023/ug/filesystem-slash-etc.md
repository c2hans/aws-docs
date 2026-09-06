---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-etc.html
---

# `/etc` (System Configuration)
<a name="filesystem-slash-etc"></a>

 The `/etc` directory on AL2023 contains system-specific configuration. By default, AL2023 images come with `/etc` on the root filesystem and writable by privileged users.

**Note**
 It is common for applications (including `systemd`) to keep default configuration under [`/usr` (System Resources)](filesystem-slash-usr.md) which can be overriden by placing configuration in [`/etc` (System Configuration)](#filesystem-slash-etc).
 For these applications, changing files in [`/usr` (System Resources)](filesystem-slash-usr.md) rather than overriding default configuration in `/etc` will likely result in the changes being overriden when the package is updated.

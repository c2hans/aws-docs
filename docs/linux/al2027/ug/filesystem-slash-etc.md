---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/filesystem-slash-etc.html
---

# `/etc` (system configuration)
<a name="filesystem-slash-etc"></a>

The `/etc` directory contains system-specific configuration. It is on the root file system and writable by privileged users.

**Note**
Many applications, including `systemd` and DNF, keep their default configuration under `/usr` and let you override it by placing configuration in `/etc`. Edit the override in `/etc` rather than the defaults in `/usr`: package updates overwrite files under `/usr`.

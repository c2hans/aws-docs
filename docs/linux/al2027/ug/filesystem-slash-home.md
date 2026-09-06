---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/filesystem-slash-home.html
---

# `/home` (user home directories)
<a name="filesystem-slash-home"></a>

Normal users have their home directories under `/home`. Software should always use the per-user `$HOME` environment variable rather than a pattern such as `/home/$USER`.

By default, AL2027 images have `/home` on the root file system, but software should not rely on this. The OS can be configured with `/home` as a separate file system that is mounted later during boot or only after a user authenticates.

**Note**
For `systemd` services that need at most read access to home directories, set `ProtectHome=read-only`, which makes `/home`, `/root`, and `/run/user` read-only for the service. For services that need no access, set `ProtectHome=tmpfs`, which replaces those paths with empty read-only `tmpfs` file systems in the service's sandbox. For more information, see the `systemd.exec(5)` man page.

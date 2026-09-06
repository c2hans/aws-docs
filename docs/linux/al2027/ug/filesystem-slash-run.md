---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/filesystem-slash-run.html
---

# `/run` (runtime data)
<a name="filesystem-slash-run"></a>

System components use the `/run` directory to store small amounts of runtime data, such as socket files. It is a `tmpfs` file system, writable only by privileged programs. The legacy `/var/run` path is a symbolic link to `/run`.

The `/run/log` directory can hold logs before they are written to `/var/log`, or before the `/var/log` file system is available.

The `/run/user/` path contains per-user runtime directories: individual `tmpfs` file systems that `systemd` mounts when a user logs in and removes when the user logs out. Reference them through the `$XDG_RUNTIME_DIR` environment variable, as described in the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/) on the freedesktop.org website, not by literal path.

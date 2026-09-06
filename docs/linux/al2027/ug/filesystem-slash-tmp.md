---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/filesystem-slash-tmp.html
---

# `/tmp` (small temporary files)
<a name="filesystem-slash-tmp"></a>

The `/tmp` directory is for small, size-bounded temporary files. As in AL2023, it is a `tmpfs` file system by default, with a size limit of 50% of RAM and a maximum of one million inodes. For larger temporary files, use [`/var/tmp`](filesystem-slash-var.md#filesystem-slash-var-tmp) instead.

Applications should prefer the path in the `$TMPDIR` environment variable over a hardcoded `/tmp`, so users can override the location.

The content of `/tmp` is cleaned at boot, and unused files are removed by a cleanup job that runs shortly after boot and then daily. To configure the cleanup, see the `tmpfiles.d(5)` and `systemd-tmpfiles(8)` man pages.

**Warning**
Because `/tmp` is shared, use safe methods to create temporary files. For details, see the upstream `systemd` documentation on [Using `/tmp` and `/var/tmp` safely](https://systemd.io/TEMPORARY_DIRECTORIES/) on the systemd.io website.

**Note**
We recommend setting the `PrivateTmp=` directive to `yes` or `disconnected` for `systemd` services, which gives the service private `/tmp` and `/var/tmp` directories that are not shared with the host or other services. See the `systemd.exec(5)` man page.

**Note**
In a container, the container runtime configuration dictates whether `/tmp` is `tmpfs` or a path on disk, and whether any cleanup process runs.

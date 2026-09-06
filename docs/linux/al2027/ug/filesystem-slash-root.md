---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/filesystem-slash-root.html
---

# `/root` (root user home directory)
<a name="filesystem-slash-root"></a>

The home directory of the root user is `/root`. It is deliberately separate from [`/home`](filesystem-slash-home.md) so that it is present even when the `/home` file system is not available. The `systemd` service best practice for `/home` applies to `/root` as well.

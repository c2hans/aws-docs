---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-root.html
---

# `/root` (root user home directory)
<a name="filesystem-slash-root"></a>

 The home directory of the root user is the `/root` directory, purposefully separate from [`/home` (User home directories)](filesystem-slash-home.md) so that it is present in the event that [`/home` (User home directories)](filesystem-slash-home.md) is on a file system which is not available.

 The best practice for configuring `systemd` services is the same for `/root` as it is for [`/home` (User home directories)](filesystem-slash-home.md).

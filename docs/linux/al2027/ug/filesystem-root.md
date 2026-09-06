---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/filesystem-root.html
---

# `/` (the root directory)
<a name="filesystem-root"></a>

By default, AL2027 images are configured with a writable `/`, allowing privileged users to create new files and directories.

The top-level `/bin`, `/sbin`, `/lib`, and `/lib64` paths are symbolic links to their counterparts under `/usr`, so commands and libraries resolve through either spelling.

**Note**
We recommend restricting what each `systemd` service can access. This can include the `ReadOnlyPaths=/` directive, which makes `/` read-only for that service. For more information, see the `systemd.exec(5)` man page.

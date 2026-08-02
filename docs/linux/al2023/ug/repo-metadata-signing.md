---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/repo-metadata-signing.html
---

# Repository metadata signing in AL2023
<a name="repo-metadata-signing"></a>

Starting with release `2023.11.20260406`, AL2023 repositories include cryptographic signatures for repository metadata. Each repository's `repomd.xml` file is accompanied by a detached GPG signature file (`repomd.xml.asc`) that you can use to verify the authenticity and integrity of the repository metadata before packages are downloaded.

This signing is in addition to the existing RPM package signing (`gpgcheck`), which verifies individual packages. Repository metadata signing verifies the metadata that describes the contents of the repository, such as the list of available packages and their checksums.

Package signing protects each package. The metadata index that lists those packages is otherwise trusted based only on TLS and checksums. Without a signature on the index, a compromised mirror or transport path could serve modified metadata that hides or blocks security updates. Repository metadata signing closes this gap and does not depend on mirror or transport trust.

## How repository metadata signing works
<a name="repo-metadata-signing-overview"></a>

When AL2023 repositories are published, the repository metadata (`repomd.xml`) is signed using an AWS KMS key. The resulting detached signature (`repomd.xml.asc`) is placed alongside the metadata in the repository.

When you enable `repo_gpgcheck` in your repository configuration, DNF verifies the `repomd.xml.asc` signature against the GPG public key before it uses the repository metadata. If verification fails, DNF rejects the metadata and does not run package operations from that repository.

The first time DNF verifies a repository's metadata, it prompts you to import that repository's signing key into a per-repository keyring. This prompt defaults to `No`. If you decline it, DNF skips the repository. For more information about `repo_gpgcheck`, see the [DNF Configuration Reference](https://dnf.readthedocs.io/en/latest/conf_ref.html).

This is the same key already used for package verification, but DNF stores it in a separate keyring for metadata checks. You are prompted to confirm it even though the key is already on disk. This is expected DNF behavior.

The following AL2023 repositories include signed metadata:
+ Core repository (`amazonlinux`)
+ Kernel Livepatch repository (`kernel-livepatch`)
+ NVIDIA repository (`amazonlinux-nvidia`)
+ Supplementary Packages for Amazon Linux repository (`amazonlinux-spal`)

## Difference between `gpgcheck` and `repo_gpgcheck`
<a name="repo-metadata-signing-gpgcheck-vs-repo-gpgcheck"></a>

| Setting | What it verifies | Default in AL2023 |
| --- | --- | --- |
| gpgcheck=1 | Verifies the GPG signature of individual RPM packages before installation. | Enabled |
| repo\_gpgcheck=1 | Verifies the GPG signature of the repository metadata (repomd.xml) before using the repository. | Disabled by default |

We recommend that you enable both `gpgcheck` and `repo_gpgcheck`, after you confirm that your automation is ready. This verifies both the repository metadata and the individual packages before use. Before you enable `repo_gpgcheck`, see [Use repository metadata verification in automation](#repo-metadata-signing-automation).

## Enabling repository metadata verification
<a name="repo-metadata-signing-enable"></a>

You can enable repository metadata verification for individual repositories by updating their configuration files.

**Important**
Repository metadata signature verification is not enabled by default. It stays disabled until you change it. Before you enable it, confirm that every unattended DNF command in your automation passes the `-y` option. For more information, see [Use repository metadata verification in automation](#repo-metadata-signing-automation).

### Enable for a specific repository
<a name="repo-metadata-signing-enable-per-repo"></a>

The AL2023 repository configuration files in `/etc/yum.repos.d/` set `repo_gpgcheck=0` by default. To enable repository metadata verification, change this value to `1` in the repository configuration. For example, to enable it for the core repository:

```
[amazonlinux]
name=Amazon Linux 2023 repository
...
gpgcheck=1
repo_gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-amazon-linux-2023
```

### Disable repository metadata verification
<a name="repo-metadata-signing-disable"></a>

To return to the previous behavior, set `repo_gpgcheck=0` in the repository configuration file. The next metadata refresh succeeds without verification.

```
[ec2-user ~]$ sudo sed -i 's/^repo_gpgcheck=1/repo_gpgcheck=0/' /etc/yum.repos.d/amazonlinux.repo
[ec2-user ~]$ sudo dnf -y makecache
```

## Verifying that repository metadata signing is working
<a name="repo-metadata-signing-verify"></a>

After enabling `repo_gpgcheck=1`, you can verify that metadata verification is working by clearing the DNF cache and refreshing the metadata:

```
[ec2-user ~]$ sudo dnf clean metadata
[ec2-user ~]$ sudo dnf makecache
```

The first time DNF verifies the metadata for a repository, it prompts you to import that repository's signing key. Enter `y` to confirm. After the key is imported, DNF creates the metadata cache without errors. You will see output similar to the following:

```
Amazon Linux 2023 repository                    1.7 MB/s | 1.8 kB     00:00
Importing GPG key 0xD832C631:
 Userid     : "Amazon Linux <amazon-linux@amazon.com>"
 Fingerprint: B21C 50FA 44A9 9720 EAA7 2F7F E951 904A D832 C631
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-amazon-linux-2023
Is this ok [y/N]: y
Amazon Linux 2023 repository                      18 MB/s |  55 MB     00:03
Metadata cache created.
```

The import prompt defaults to `No`. If you decline it, DNF skips the repository and reports `Ignoring repositories` in the output. If verification fails, DNF reports a GPG signature error and does not create the cache.

For unattended runs, see [Use repository metadata verification in automation](#repo-metadata-signing-automation).

## Use repository metadata verification in automation
<a name="repo-metadata-signing-automation"></a>

**Note**
The key import prompt defaults to `No`. An unattended DNF run cannot answer the prompt, so it declines the import and skips the repository. Because AL2023 sets `skip_if_unavailable=True`, the command still exits with status `0`. As a result, the automation reports success while the host receives no packages or updates. The sign of this is `Ignoring repositories` in the output.

To prevent this, pass the `-y` option to every unattended DNF command that refreshes metadata, including continuous integration jobs, image and container builds, `cloud-init`, configuration management, and cron jobs.

```
[ec2-user ~]$ sudo dnf -y makecache
[ec2-user ~]$ sudo dnf -y check-update
[ec2-user ~]$ sudo dnf -y upgrade
```

Commands that refresh metadata need `-y`. Commands that read only the local cache or the local RPM database, or that use the `-C` option, do not refresh metadata and do not prompt. For the full list, see [Commands that refresh repository metadata](#repo-metadata-signing-command-reference).

Keep `-y` in your automation permanently. The key is imported once per repository URL, not once per host. AL2023 builds each repository URL from the locked version (`releasever`) and the AWS Region, so an OS version upgrade or a Region change resolves to a new URL and prompts again. The signing key does not change; only its keyring location does. Do not pre-seed or pre-bake the key as a one-time fix, because the next version upgrade or Region uses a new keyring and prompts again.

Running `dnf clean all` clears cached metadata but does not remove the imported key within the same version. It does not re-trigger the prompt.

Container image builds need particular attention. Every `RUN dnf` step in an image build is unattended, and the keyring is part of the image filesystem, so it starts empty in every fresh image. The prompt appears during the build regardless of what your running hosts have already imported. Pass `-y` in image builds.

**Note**
If you drive DNF as a Python library (`import dnf`), the prompt does not apply. The library imports the key without prompting, so metadata loads without `-y`.

## Commands that refresh repository metadata
<a name="repo-metadata-signing-command-reference"></a>

Any command that downloads or refreshes repository metadata triggers the key import and the prompt. Commands that read only the local cache or the local RPM database do not. Options change the result: for example, `-v` makes `repolist` fetch, `--installed` keeps `list` and `info` local, `-C` or `--cacheonly` avoids fetching, and `--refresh` forces it. When in doubt, pass `-y`.

| Command | Refreshes metadata |
| --- | --- |
| dnf makecache | Yes |
| dnf check-update | Yes |
| dnf upgrade, dnf update | Yes |
| dnf upgrade-minimal | Yes |
| dnf distro-sync | Yes |
| dnf install | Yes |
| dnf reinstall | Yes |
| dnf downgrade | Yes |
| dnf autoremove | Yes |
| dnf swap | Yes |
| dnf list (default or --available) | Yes |
| dnf info (default or --available) | Yes |
| dnf search | Yes |
| dnf provides | Yes |
| dnf repoquery | Yes |
| dnf repoinfo | Yes |
| dnf deplist | Yes |
| dnf repository-packages | Yes |
| dnf updateinfo | Yes |
| dnf group (list, info, install) | Yes |
| dnf module (list, info) | Yes |
| dnf shell (if its subcommands fetch) | Yes |
| dnf builddep | Yes |
| dnf changelog | Yes |
| dnf debuginfo-install | Yes |
| dnf download | Yes |
| dnf repoclosure | Yes |
| dnf repograph | Yes |
| dnf reposync | Yes |
| dnf debug-dump | Yes |
| dnf repolist -v (verbose) | Yes |
| dnf repolist (plain or --all) | No |
| dnf list --installed, dnf info --installed | No |
| dnf remove, dnf erase | No |
| dnf mark | No |
| dnf history | No |
| dnf check | No |
| dnf clean | No |
| dnf config-manager | No |
| dnf needs-restarting | No |
| dnf alias | No |
| dnf help | No |
| dnf repomanage | No |
| dnf repodiff | No (errors unless two repositories are named) |
| dnf copr | No |
| dnf groups-manager | No |
| dnf playground | No |
| dnf debug-restore | No (acts on a saved dump) |
| Any command with -C or --cacheonly | No |

A repository skipped this way is reported as `Ignoring repositories` in the output, but most of these commands still exit with status `0` because AL2023 sets `skip_if_unavailable=True`. Do not rely on the exit code alone. Pass `-y` so the key import succeeds.

## Detect a skipped repository
<a name="repo-metadata-signing-detect"></a>

The exit code alone does not confirm that verification succeeded. A skipped repository exits `0`, and the signing key persists once any run imports it, so a later check can pass while an earlier step still fails. Use these two checks instead:
+ Audit your automation. Confirm that every metadata-fetching DNF command passes `-y`. This is what keeps you working on the next new repository URL.
+ Check the output for `Ignoring repositories`. The following command fails when the repository is skipped, which you can use to fail a pipeline:

```
[ec2-user ~]$ sudo dnf makecache 2>&1 | grep -q "Ignoring repositories" && { echo "repo skipped"; exit 1; }
```

## Pinned versions
<a name="repo-metadata-signing-pinned"></a>

If you pin `releasever` (with `--releasever`, `/etc/dnf/vars/releasever`, or `dnf.conf`) to a version released before `2023.11.20260406`, that version has no signature file, and `repo_gpgcheck=1` fails to refresh the repository:

```
Error: Failed to download metadata for repo 'amazonlinux':
GPG verification is enabled, but GPG signature is not available...
```

A pinned version does not receive updates beyond that version. If you pin, pin to version `2023.11.20260406` or later, or set `repo_gpgcheck=0`.

## GPG public keys for AL2023 repositories
<a name="repo-metadata-signing-gpg-keys"></a>

The GPG public keys used for repository metadata verification are installed by the corresponding repository configuration RPMs to `/etc/pki/rpm-gpg/`. The following table lists the public keys used by each repository.

| Repository | Package signing key | Repodata signing key | Distributed in |
| --- | --- | --- | --- |
| Core (amazonlinux) | RPM-GPG-KEY-amazon-linux-2023 | RPM-GPG-KEY-amazon-linux-2023 | system-release |
| Kernel Livepatch (kernel-livepatch) | RPM-GPG-KEY-amazon-linux-2023 | RPM-GPG-KEY-amazon-linux-2023 | system-release |
| NVIDIA (amazonlinux-nvidia) | RPM-GPG-KEY-NVIDIA-D42D0685 | RPM-GPG-KEY-amazon-linux-2023-nvidia | nvidia-release |
| SPAL (amazonlinux-spal) | RPM-GPG-KEY-amazonlinux-spal | RPM-GPG-KEY-amazonlinux-spal | spal-release |

These keys are automatically installed when you install the corresponding repository configuration RPM.

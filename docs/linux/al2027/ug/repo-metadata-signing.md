---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/repo-metadata-signing.html
---

# Repository metadata signing in AL2027
<a name="repo-metadata-signing"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

AL2027 repositories include cryptographic signatures for repository metadata. Each repository's `repomd.xml` file comes with a detached GPG signature file (`repomd.xml.asc`). DNF can use this signature to verify the authenticity and integrity of the repository metadata before downloading packages. AL2023 added this capability with release `2023.11.20260406`; AL2027 has it from the start.

Metadata signing is in addition to RPM package signing (`gpgcheck`), which verifies individual packages. Without a signature on the metadata index, that index is trusted based only on TLS and checksums, so a compromised mirror or transport path could serve modified metadata that hides or blocks security updates. Repository metadata signing closes this gap.

**Topics**
+ [How repository metadata signing works](#repo-metadata-signing-overview)
+ [Difference between `gpgcheck` and `repo_gpgcheck`](#repo-metadata-signing-gpgcheck-vs-repo-gpgcheck)
+ [Enabling repository metadata verification](#repo-metadata-signing-enable)
+ [Verifying that repository metadata signing is working](#repo-metadata-signing-verify)
+ [Use repository metadata verification in automation](#repo-metadata-signing-automation)
+ [Commands that refresh repository metadata](#repo-metadata-signing-command-reference)
+ [Detect a skipped repository](#repo-metadata-signing-detect)
+ [Pinned versions](#repo-metadata-signing-pinned)
+ [GPG public keys for AL2027 repositories](#repo-metadata-signing-gpg-keys)

## How repository metadata signing works
<a name="repo-metadata-signing-overview"></a>

When you enable `repo_gpgcheck` in a repository configuration, DNF verifies the `repomd.xml.asc` signature against the repository's GPG public key before it uses the metadata. If verification fails, DNF does not use the metadata. Because AL2027 repositories set `skip_if_unavailable=1`, DNF then skips the repository and continues. For how to catch this in automation, see [Detect a skipped repository](#repo-metadata-signing-detect).

The first time DNF verifies a repository's metadata, it prompts you to import the signing key into a separate keyring used for metadata checks. The prompt defaults to `No`, and declining it skips the repository.

The following AL2027 repositories include signed metadata:
+ Core repository (`amazonlinux`)
+ Source packages repository (`amazonlinux-source`)
+ Debug information repository (`amazonlinux-debuginfo`)

## Difference between `gpgcheck` and `repo_gpgcheck`
<a name="repo-metadata-signing-gpgcheck-vs-repo-gpgcheck"></a>

| Setting | What it verifies | Default in AL2027 |
| --- | --- | --- |
| gpgcheck=1 | Verifies the GPG signature of individual RPM packages before installation. | Enabled |
| repo\_gpgcheck=1 | Verifies the GPG signature of the repository metadata (repomd.xml) before using the repository. | Disabled |

We recommend enabling both settings after you confirm that your automation is ready. Before you enable `repo_gpgcheck`, see [Use repository metadata verification in automation](#repo-metadata-signing-automation).

## Enabling repository metadata verification
<a name="repo-metadata-signing-enable"></a>

**Important**
Repository metadata verification is not enabled by default. Before you enable it, confirm that every unattended DNF command in your automation passes the `-y` option. For more information, see [Use repository metadata verification in automation](#repo-metadata-signing-automation).
The NVIDIA repositories do not yet support repository metadata signing. Do not enable `repo_gpgcheck` for them. For more information, see [NVIDIA drivers](nvidia-drivers.md).

### Enable for a specific repository
<a name="repo-metadata-signing-enable-per-repo"></a>

The AL2027 repository configuration in `/etc/yum.repos.d/amazonlinux.repo` sets `repo_gpgcheck=0` by default. To enable metadata verification, change the value to `1` for each repository section:

```
[amazonlinux]
name=Amazon Linux 2027 repository
...
gpgcheck=1
repo_gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-amazon-linux-2027
```

The same key verifies both packages and repository metadata. The `system-release` package installs it at `/etc/pki/rpm-gpg/RPM-GPG-KEY-amazon-linux-2027`.

### Disable repository metadata verification
<a name="repo-metadata-signing-disable"></a>

To return to the default behavior, set `repo_gpgcheck=0` again. The next metadata refresh succeeds without verification:

```
sudo sed -i 's/^repo_gpgcheck=1/repo_gpgcheck=0/' /etc/yum.repos.d/amazonlinux.repo
sudo dnf -y makecache
```

## Verifying that repository metadata signing is working
<a name="repo-metadata-signing-verify"></a>

After enabling `repo_gpgcheck=1`, clear the DNF cache and refresh the metadata:

```
sudo dnf clean metadata
sudo dnf -y makecache
```

The first time DNF verifies a repository's metadata, it imports that repository's signing key into a separate keyring used for metadata checks, and asks for confirmation. This is the same key already used for package verification; the confirmation for the separate keyring is expected behavior. With `-y`, the key is imported and the cache is created without errors:

```
Updating and loading repositories:
 Amazon Linux 2027 repository           100% |  22.3 KiB/s |   4.5 KiB |  00m00s
>>> repomd.xml GPG signature verification error: Signing key not found
Importing OpenPGP key 0xB1E92E3D:
 UserID     : "Amazon Linux amazon-linux@amazon.com"
 Fingerprint: 37CE 7C38 33E5 A33C 4A1E 4B0D 5408 EAA4 B1E9 2E3D
 From       : file:///etc/pki/rpm-gpg/RPM-GPG-KEY-amazon-linux-2027
The key was successfully imported.
 Amazon Linux 2027 repository           100% |  10.8 MiB/s |   2.4 MiB |  00m00s
Repositories loaded.
Metadata cache created.
```

The `Signing key not found` line before the import is expected on the first run: verification is attempted, the key is imported, and verification then succeeds. If verification fails after the key is imported, DNF reports the `repomd.xml GPG signature verification error` and the metadata is not used.

## Use repository metadata verification in automation
<a name="repo-metadata-signing-automation"></a>

The key import prompt defaults to `No`. An unattended DNF run cannot answer the prompt, so it declines the import and metadata verification fails for the repository. The command can still exit with status `0`, so do not rely on the exit code alone. For how to catch this, see [Detect a skipped repository](#repo-metadata-signing-detect).

To prevent this, pass the `-y` option to every unattended DNF command that refreshes metadata, including CI jobs, image and container builds, `cloud-init`, configuration management, and scheduled jobs.

Keep `-y` in your automation permanently. The key is imported once per repository URL, and AL2027 builds each repository URL from the locked release version, so moving to a different release version resolves to a new URL and prompts again. Container image builds need particular attention. The keyring is part of the image file system and starts empty in every fresh image, so every `RUN dnf` build step is a first-time import.

## Commands that refresh repository metadata
<a name="repo-metadata-signing-command-reference"></a>

Any command that downloads repository metadata triggers verification, and with it the one-time key import. Commands that read only the local cache or the local RPM database do not. The table covers the commands that `dnf5 --help` lists on AL2027, including the preinstalled plugins and the `dnf5-plugins` package. Each behavior was measured against a cleaned cache. Command aliases, such as `dnf update` or `dnf rq`, behave like the command they map to. Options change the result: `--installed` keeps `list` and `info` local, and `-C` (`--cacheonly`) prevents any fetch. When in doubt, pass `-y`.

| Command | Refreshes metadata |
| --- | --- |
| dnf makecache | Yes |
| dnf check-update, dnf check-upgrade | Yes |
| dnf upgrade, dnf upgrade-minimal | Yes |
| dnf install, dnf reinstall | Yes |
| dnf downgrade, dnf swap | Yes |
| dnf distro-sync | Yes |
| dnf search, dnf list, dnf info | Yes |
| dnf provides, dnf repoquery | Yes |
| dnf advisory, dnf updateinfo | Yes |
| dnf group list | Yes |
| dnf download | Yes |
| dnf repoinfo | Yes |
| dnf needs-restarting | Yes |
| dnf changelog | Yes |
| dnf deplist | Yes |
| dnf builddep, dnf debuginfo-install | Yes |
| dnf repoclosure, dnf reposync | Yes |
| dnf supportinfo | Yes |
| dnf check-release-update | Yes |
| dnf group info, dnf environment list | Yes |
| dnf autoremove | No |
| dnf remove | No |
| dnf repolist (plain or --all) | No |
| dnf list --installed, dnf info --installed | No |
| dnf history | No |
| dnf leaves, dnf check | No |
| dnf versionlock | No |
| dnf offline status | No |
| dnf config-manager | No |
| dnf clean | No |
| Any command with -C or --cacheonly | No |

**Note**
Two behaviors changed from AL2023: `dnf autoremove` no longer refreshes metadata, and `dnf needs-restarting` now does.

## Detect a skipped repository
<a name="repo-metadata-signing-detect"></a>

The exit code alone does not confirm that verification succeeded. AL2027 repositories set `skip_if_unavailable=1`, so when metadata verification fails, DNF prints the error, skips the repository, and still exits with `0`:

```
sudo dnf upgrade
```

```
Updating and loading repositories:
 Amazon Linux 2027 repository           100% |  46.8 KiB/s |   4.5 KiB |  00m00s
>>> repomd.xml GPG signature verification error: Signing key not found
Repositories loaded.
Nothing to do.
```

On a system with pending updates, this looks like success. Use these two checks instead:
+ Audit your automation. Confirm that every metadata-fetching DNF command passes `-y`, so the one-time key import succeeds on each new repository URL.
+ Check the output for `GPG signature verification error`. The following command fails when the repository is skipped, which you can use to fail a pipeline:

```
if sudo dnf makecache 2>&1 | grep -q "GPG signature verification error"; then
  echo "repo skipped"
  exit 1
fi
```

After the key is imported, a healthy refresh prints no verification error, and the check passes.

## Pinned versions
<a name="repo-metadata-signing-pinned"></a>

All AL2027 releases carry signed repository metadata, so pinning `releasever` (with `--releasever` or `/etc/dnf/vars/releasever`) works with `repo_gpgcheck=1`. During the preview period, old preview releases can be removed from the repositories. A pinned version does not receive updates beyond that version, and a removed version stops resolving. Pin to a current release listed in the [AL2027 Release Notes](https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes.html).

## GPG public keys for AL2027 repositories
<a name="repo-metadata-signing-gpg-keys"></a>

The GPG public key used for repository metadata verification is installed to `/etc/pki/rpm-gpg/` by the `system-release` package. The following table lists the key used by each repository.

| Repository | Package signing key | Repodata signing key | Distributed in |
| --- | --- | --- | --- |
| Core (amazonlinux) | RPM-GPG-KEY-amazon-linux-2027 | RPM-GPG-KEY-amazon-linux-2027 | system-release |
| Source packages (amazonlinux-source) | RPM-GPG-KEY-amazon-linux-2027 | RPM-GPG-KEY-amazon-linux-2027 | system-release |
| Debug information (amazonlinux-debuginfo) | RPM-GPG-KEY-amazon-linux-2027 | RPM-GPG-KEY-amazon-linux-2027 | system-release |

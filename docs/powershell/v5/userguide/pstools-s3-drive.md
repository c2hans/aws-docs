---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/pstools-s3-drive.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Use Amazon S3 as a PowerShell drive
<a name="pstools-s3-drive"></a>

*Applies to: `AWS.Tools.S3` 5.0.288 and later. The S3 drive provider and its cmdlets ship in the `AWS.Tools.S3` module, which runs on Windows PowerShell 5.1 and PowerShell 7\+ (Windows, Linux, macOS).*

The S3 PowerShell drive lets you mount Amazon S3 storage as a drive and work with it the same way you work with a local disk. After you mount a drive, the provider presents buckets and prefixes as folders and objects as files. Common navigation commands work directly against S3, including `Set-Location`, `Get-ChildItem`, `Get-Content`, `Set-Content`, and `Remove-Item`.

This topic covers installing, mounting, navigating, transferring content, and unmounting, plus the credential, Region, and safety behavior for the S3 drive.

**Path separators differ by platform**
The examples in this topic use `/` as the path separator, which the drive accepts on every platform. On Windows the drive also accepts `\`, so `S3:\amzn-s3-demo-bucket\reports` and `S3:/amzn-s3-demo-bucket/reports` are equivalent there. On Linux and macOS only `/` is a separator, so use that form in scripts that run on more than one platform. The paths the drive hands back, such as `PSPath`, use the operating system's native separator: `\` on Windows and `/` on Linux and macOS.

## Prerequisites
<a name="pstools-s3-drive-prerequisites"></a>
+ The `AWS.Tools.S3` module, 5.0.288 or later. Install it directly from the PowerShell Gallery (this also pulls in its `AWS.Tools.Common` dependency):

  ```
  Install-Module -Name AWS.Tools.S3 -MinimumVersion 5.0.288
  ```

  Or, if you manage the modular tools with the `AWS.Tools.Installer` module, install that first and then use `Install-AWSToolsModule`:

  ```
  Install-Module -Name AWS.Tools.Installer  # provides Install-AWSToolsModule
  Install-AWSToolsModule AWS.Tools.S3
  ```

  The drive provider and its cmdlets ship inside `AWS.Tools.S3`. No additional installation is required.
+ AWS credentials configured the same way as for any S3 cmdlet (a named profile, environment variables, an IAM role, or SSO). For more information, see [Get started with the AWS Tools for PowerShell](pstools-getting-set-up.md).

Importing the module registers a PowerShell provider named `AWS.S3`. You can confirm that it is available:

```
Get-PSProvider AWS.S3
```

## Mount a drive
<a name="pstools-s3-drive-mount"></a>

Use `Mount-S3PSDrive` to create a drive. The `-Name` parameter becomes the drive name in every path (for example, `-Name S3` gives you paths like `S3:/amzn-s3-demo-bucket/reports/index.txt`).

```
# Mount an S3: drive using a named profile and Region
Mount-S3PSDrive -Name S3 -ProfileName my-profile -Region us-east-1
# List buckets
Get-ChildItem S3:/
```

Sample output:

```
   Type     LastModified              Size Name
   ----     ------------              ---- ----
   Bucket   2026-06-02 09:14:03            amzn-s3-demo-app-logs
   Bucket   2026-01-08 16:47:51            amzn-s3-demo-reports
```

If you have already set session defaults with `Set-AWSCredential` and `Set-DefaultAWSRegion`, you can mount with no other parameters:

```
Set-AWSCredential -ProfileName my-profile
Set-DefaultAWSRegion us-west-2
Mount-S3PSDrive -Name S3
```

`Mount-S3PSDrive` is a thin wrapper over the PowerShell built-in `New-PSDrive`. If you prefer, you can create the drive directly and pass the same credential and Region parameters:

```
New-PSDrive -Name S3 -PSProvider AWS.S3 -Root '' -Scope Global -ProfileName my-profile -Region us-east-1
```

**Using New-PSDrive directly**
Pass `-Scope Global` when you use `New-PSDrive` directly. Without it the drive is created in the current scope and disappears when that scope exits (for example, when the script or function that created it returns). `Mount-S3PSDrive` sets `-Scope Global` for you.

By default `Mount-S3PSDrive` produces no output. Add `-PassThru` if you want the `PSDriveInfo` object back.

**Credential parameter name**
The credential parameter is named `-AWSCredential`, not `-Credential`. `New-PSDrive` already defines `-Credential` as a `PSCredential`, which is a different type, so the S3 drive uses a distinct name to avoid a collision.

## How credentials and Region are resolved
<a name="pstools-s3-drive-credentials"></a>

An S3 drive authenticates and selects a Region exactly as the S3 cmdlets do: explicit parameters first, then the session defaults set by `Set-AWSCredential` and `Set-DefaultAWSRegion`, then the profile, environment, and instance-metadata sources of the SDK default chains. For the full resolution order, see [Using AWS Credentials](specifying-your-aws-credentials.md) and [Specify the AWS Region for the AWS Tools for PowerShell](pstools-installing-specifying-region.md).

If nothing supplies a Region, the drive falls back to `us-east-1`. The Region you mount with is only the *starting* Region: a single drive can reach buckets across Regions (see [Access buckets across Regions from one drive](#pstools-s3-drive-regions)).

A bad profile or a missing bucket or prefix fails at `Mount-S3PSDrive`. Some permission errors might not appear until you access an object.

## Navigate Amazon S3 like a local drive
<a name="pstools-s3-drive-browse"></a>

After you mount the drive, navigate with common PowerShell drive commands. S3 has no real folders, but the provider presents prefixes as folders so you can navigate them the same way.

```
# Change into a bucket, then a prefix
Set-Location S3:/amzn-s3-demo-reports/2026
# List the current location
Get-ChildItem
```

Sample output:

```
   Type     LastModified              Size Name
   ----     ------------              ---- ----
   Folder                                  q1
   Folder                                  q2
   Object   2026-03-31 18:02:11      48210 summary.txt
```

```
# List a path without changing location
Get-ChildItem S3:/amzn-s3-demo-bucket/reports/2026
```

Tab completion works for buckets, prefixes, and objects, so you can complete a path without entering full names.

`Get-ChildItem` returns each item as an object that exposes `Name`, `Type`, `Size`, and `LastModified` properties. These properties let listings pipe directly into commands such as `Where-Object` and `Sort-Object`. `Type` is one of `Bucket`, `Folder`, or `Object`. Folders and buckets carry no size.

```
# List the 10 largest objects with the prefix "2026"
Get-ChildItem S3:/amzn-s3-demo-app-logs/2026 -Recurse |
    Where-Object Type -eq 'Object' |
    Sort-Object Size -Descending |
    Select-Object -First 10 Name, Size, LastModified
```

Other navigation commands also work on the drive:

```
# Retrieve the single item at an exact path (no children)
Get-Item S3:/amzn-s3-demo-bucket/reports/index.txt
# Test whether a path exists and whether it is a folder or an object
Test-Path S3:/amzn-s3-demo-bucket/reports                              # -> True
Test-Path S3:/amzn-s3-demo-bucket/reports -PathType Container          # -> True (a prefix)
Test-Path S3:/amzn-s3-demo-bucket/reports/index.txt -PathType Leaf     # -> True (an object)
```

**Command aliases differ by operating system**
This is PowerShell behavior, not the drive. On Windows, the Unix-style aliases `ls`, `rm`, and `cat` map to the PowerShell cmdlets, so `ls S3:/amzn-s3-demo-bucket` works. On Linux and macOS, PowerShell leaves those names bound to the native tools (`/bin/ls`, `/bin/rm`, `/bin/cat`), which don't recognize an S3 path. As a result, `ls S3:/amzn-s3-demo-bucket` runs the system `ls` and fails. For scripts that run on every platform, use the full cmdlet names: `Get-ChildItem`, `Remove-Item`, and `Get-Content`. (`cd` and `dir` are aliased on all platforms, so those work everywhere.)

With `-Recurse`, an item's `Name` is its key *relative to the prefix* (so it can contain `/`), and the same leaf name can appear under different prefixes. When you need to identify a listed item unambiguously (for example, to pipe it onward), use its `PSPath` rather than `Name`.

**Piping listed objects with -AsByteStream on Windows PowerShell 5.1**
Piping `Get-ChildItem` into `Get-Content -AsByteStream` can fail on Windows PowerShell 5.1. The engine might bind `-AsByteStream` before it knows the piped input is an S3 path, and the FileSystem provider in 5.1 has no such parameter (see [Reading local file bytes differs by edition](#pstools-s3-drive-local-bytes)). Read each item by its explicit `PSPath` instead, which works on both editions:

```
# Read each listed object by explicit PSPath
Get-ChildItem S3:/amzn-s3-demo-bucket/prefix | ForEach-Object {
    Get-Content -LiteralPath $_.PSPath -AsByteStream -Raw
}
```
On PowerShell 7\+ the direct pipe works, but the per-item form is a safe default for scripts that run on both editions.

**Listings are safe to interrupt**
Listings stream as each page of results arrives from S3 and are safe to interrupt with Ctrl\+C. A prefix with a large number of objects begins producing output immediately instead of waiting for the full listing to finish.

**Wildcard characters in keys**
S3 keys can legally contain PowerShell wildcard characters (`[`, `]`, `*`, `?`). To address such a key literally, use `-LiteralPath` (supported by `Get-Item`, `Get-Content`, `Set-Content`, and `Remove-Item`), the same way you do on the file system provider:

```
Get-Content -LiteralPath 'S3:/amzn-s3-demo-bucket/data[2026].csv' -Raw
```

**Test-Path and objects you cannot read**
`Test-Path` returns `$true` for a path you can't read. It confirms the path resolves; it does not confirm that you have permission to read or write it.

## Read objects from S3
<a name="pstools-s3-drive-read"></a>

`Get-Content` downloads an object. By default it returns text line by line. Add `-Raw` to return the whole object as a single string. Both `Get-Content` and `Set-Content` support `-Encoding` for text and `-AsByteStream` for binary content.

```
# Read an object line by line
Get-Content S3:/amzn-s3-demo-reports/2026/summary.txt
# Read the whole object as one string
Get-Content S3:/amzn-s3-demo-reports/2026/summary.txt -Raw
```

For non-text objects, use `-AsByteStream` to get the raw bytes. On an S3 path this works on both PowerShell 7\+ and Windows PowerShell 5.1 because the S3 provider supplies the parameter. Only *local* files differ by edition (see [Reading local file bytes differs by edition](#pstools-s3-drive-local-bytes)). To control text decoding, add `-Encoding` with any of the standard PowerShell encoding names (`UTF8`, `UTF8BOM`, `Unicode`, `ASCII`, and so on). The default is UTF-8 without a BOM, on both `Get-Content` and `Set-Content`.

```
# Read raw bytes
Get-Content S3:/amzn-s3-demo-bucket/images/logo.png -AsByteStream -Raw
# Decode as a specific text encoding
Get-Content S3:/amzn-s3-demo-bucket/data/report.csv -Encoding UTF8
```

`Get-Content` also accepts `-PartSize` to set the multipart *download* part size, in bytes, between the S3 minimum of 5 MiB and the maximum of 5 GiB. It mirrors `-PartSize` on `Set-Content`, which sets the upload part size (see [Upload very large objects](#pstools-s3-drive-large-objects)).

**Reading raw bytes into a variable**
If you load an object's bytes into a variable (to hash, measure, or pass them to another API), flatten the `-AsByteStream` result first. Otherwise `.Length` and byte comparisons produce incorrect results:

```
$bytes = [byte[]]((Get-Content S3:/amzn-s3-demo-bucket/images/logo.png -AsByteStream -Raw) | ForEach-Object { $_ })
```
Piping to a file or another command (for example `Set-Content -AsByteStream`, as in [Copy objects between S3 and local disk](#pstools-s3-drive-copy)) needs no flattening.

## Write objects to S3
<a name="pstools-s3-drive-write"></a>

`Set-Content` uploads (and overwrites) an object.

```
# Write text
Set-Content S3:/amzn-s3-demo-reports/2026/notes.txt -Value 'Draft complete'
# Write several lines
Set-Content S3:/amzn-s3-demo-bucket/notes/list.txt -Value @('alpha', 'beta', 'gamma')
# Write raw bytes
Set-Content S3:/amzn-s3-demo-bucket/images/logo.png -AsByteStream -Value $bytes
```

Uploads have the following options:

| Parameter | Purpose |
| --- | --- |
| `-Encoding` | Text encoding for the on-the-wire bytes (default UTF-8, no BOM). |
| `-NoNewline` | Omit the trailing newline after each text value. |
| `-StorageClass` | Storage class for this object (for example `STANDARD_IA`, `GLACIER`). |
| `-PartSize` | Multipart part size for this upload, in bytes (between the S3 minimum of 5 MiB and maximum of 5 GiB). See [Upload very large objects](#pstools-s3-drive-large-objects). |

You can cancel an upload at any time with Ctrl\+C. Nothing is committed until the upload finishes, so cancelling does not leave a half-written object in place of the old one.

**Text uploads use LF line endings**
Text uploads use LF line endings, so an object written on Windows, Linux, or macOS is byte-identical. When you need exact control over the bytes, use `-AsByteStream`.

### Upload very large objects
<a name="pstools-s3-drive-large-objects"></a>

Every upload through the drive is a multipart upload, and S3 limits a multipart upload to 10,000 parts. With the default part size of 5 MiB that caps a single object at about 48 GiB, and an upload past the cap runs out of parts and fails. To upload something bigger, raise `-PartSize` so that it is at least `object size / 10,000`:

```
# Upload a ~200 GiB object with 64 MiB parts (200 GiB / 10,000 = 21 MiB, so 64 MiB is plenty)

# PowerShell 7+
Get-Content ./huge.bin -AsByteStream -ReadCount 8MB |
    Set-Content S3:/amzn-s3-demo-bucket/archive/huge.bin -AsByteStream -PartSize 64MB

# Windows PowerShell 5.1 (local read uses -Encoding Byte; the S3 write keeps -AsByteStream -PartSize)
Get-Content ./huge.bin -Encoding Byte -ReadCount 8MB |
    Set-Content S3:/amzn-s3-demo-bucket/archive/huge.bin -AsByteStream -PartSize 64MB
```

`-PartSize` and `-StorageClass` are S3 destination parameters. Use them with an explicit S3 destination path (as in the preceding example), not with a pipeline-bound destination object.

`-PartSize` accepts a value between the S3 minimum of 5 MiB and the maximum of 5 GiB. At the 5 GiB maximum, 10,000 parts covers the largest object that S3 supports (5 TiB).

**Choosing a part size**
A larger part size also means fewer round trips for a big upload, but each in-flight part is held in memory, so very large parts use more memory. 5 MiB to a few hundred MiB is a reasonable range. Only go higher when the object size requires it.

## Copy objects between S3 and local disk
<a name="pstools-s3-drive-copy"></a>

Copying *within* S3 with `Copy-Item` is not supported (see [Supported and unsupported operations](#pstools-s3-drive-supported)). To move data between your local disk and S3, pipe the content through `Get-Content` and `Set-Content`.

For binary data, read and write the bytes exactly. An **S3** path uses `-AsByteStream` on both PowerShell editions; only the *local* side differs, as described in [Reading local file bytes differs by edition](#pstools-s3-drive-local-bytes).

```
# Upload a local file (PowerShell 7+; on Windows PowerShell 5.1 the local read uses -Encoding Byte)
Get-Content ./report.csv -AsByteStream -ReadCount 8MB | Set-Content S3:/amzn-s3-demo-bucket/data/report.csv -AsByteStream

# Download to a local file (on Windows PowerShell 5.1 the local write uses -Encoding Byte)
Get-Content S3:/amzn-s3-demo-bucket/data/report.csv -AsByteStream | Set-Content ./report.csv -AsByteStream
```

**Use byte mode on both ends for binary data**
Read and write bytes on **both** ends when copying binary data. In text mode, content is decoded and re-encoded. A newline is normalized or appended for each line, which corrupts non-text data. Byte-mode on the read and the write copies the bytes exactly. For text files, plain `Get-Content | Set-Content` works, with one exception: text-mode `Set-Content` appends a trailing newline (LF) and normalizes line endings, so the copy is not byte-for-byte identical to the source. When you need an exact copy, use `-AsByteStream` on both ends.

### Reading local file bytes differs by edition
<a name="pstools-s3-drive-local-bytes"></a>

Targeting a local file uses PowerShell's built-in FileSystem provider, and that provider has no `-AsByteStream` in Windows PowerShell 5.1 (it arrived in PowerShell 6). Use `-Encoding Byte` there instead. This is a 5.1 limitation, not something the S3 drive controls; an S3 path takes `-AsByteStream` on both editions.

| Edition | Read local file bytes | Write local file bytes |
| --- | --- | --- |
| **PowerShell 7\+** | `Get-Content $f -AsByteStream -ReadCount 8MB` | `Set-Content $f -AsByteStream` |
| **Windows PowerShell 5.1** | `Get-Content $f -Encoding Byte -ReadCount 8MB` | `Set-Content $f -Encoding Byte` |

For server-side S3-to-S3 copies, use the [Copy-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Copy-S3Object.html) cmdlet.

## Delete objects and prefixes
<a name="pstools-s3-drive-delete"></a>

`Remove-Item` deletes a single object. Deleting a prefix (a folder with contents) requires `-Recurse`, which removes everything beneath it in batches.

```
# Delete a single object
Remove-Item S3:/amzn-s3-demo-bucket/notes/todo.txt
# Delete a prefix and everything under it
Remove-Item S3:/amzn-s3-demo-bucket/old-logs -Recurse
```

Whether `Remove-Item` prompts depends on what you target:
+ A single object, without `-Recurse`: no prompt. The object is deleted.
+ A prefix, with `-Recurse`: no prompt. Everything under the prefix is deleted.
+ A non-empty prefix, without `-Recurse`: PowerShell prompts for confirmation. This is the file system provider's container-has-children behavior. If you confirm, the delete recurses; if you decline, nothing is deleted. In a non-interactive host, that prompt blocks. Pass `-Recurse` to proceed without prompting.

Use the native PowerShell switches to preview or gate a delete:

```
# Preview without deleting
Remove-Item S3:/amzn-s3-demo-bucket/old-logs -Recurse -WhatIf
# Ask for confirmation
Remove-Item S3:/amzn-s3-demo-bucket/notes/todo.txt -Confirm
```

**Versioning-enabled buckets keep noncurrent versions**
On a bucket with Amazon S3 Versioning enabled, `Remove-Item` performs a standard delete. It adds a delete marker and hides the current version, but it does not remove noncurrent versions, which are retained and continue to incur storage cost. To remove versions permanently, use the S3 cmdlets (for example, [Remove-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Remove-S3Object.html) with a version ID) or an Amazon S3 Lifecycle rule.

**Remove-Item -Recurse deletes without prompting**
`Remove-Item -Recurse` deletes every object under the prefix with no prompt, the same as `rm -r`. On a bucket without versioning, the recursive delete is permanent. On a versioning-enabled bucket, it adds delete markers as described in the preceding note. Use `-WhatIf` first if you are unsure what it will remove.

You cannot delete a whole *bucket* through the drive because bucket lifecycle operations are out of scope. Use [Remove-S3Bucket](https://docs.aws.amazon.com/powershell/v5/reference/items/Remove-S3Bucket.html) instead.

## Scope a drive to one bucket or prefix
<a name="pstools-s3-drive-scoped-mount"></a>

Mount with `-Root` to confine a drive to a bucket, or a prefix within a bucket. The drive's root then *is* that location, and navigation is confined beneath it.

```
# Mount rooted at a bucket: the drive root lists the bucket's top-level entries
Mount-S3PSDrive -Name Data -Root amzn-s3-demo-bucket -ProfileName my-profile -Region us-east-1
Get-ChildItem Data:/                 # top-level keys in amzn-s3-demo-bucket
Get-Content Data:/reports/index.txt  # -> amzn-s3-demo-bucket/reports/index.txt

# Mount rooted at a bucket + prefix
Mount-S3PSDrive -Name Reports -Root amzn-s3-demo-reports/2026 -ProfileName my-profile -Region us-east-1
Get-ChildItem Reports:/              # contents of amzn-s3-demo-reports/2026/
```

The root must already exist. A nonexistent bucket or prefix fails the mount. Because relative paths cannot climb above the root (`..` is blocked by the engine), a scoped mount gives you a focused view of exactly one project's data.

## Access buckets across Regions from one drive
<a name="pstools-s3-drive-regions"></a>

A single mounted drive can reach buckets across Regions. The first time you touch a bucket, the provider looks up its Region and routes subsequent calls to the right endpoint automatically. You don't need a separate drive for each Region.

```
# Mounted in us-east-1, but this bucket is in us-west-2 and commands work without extra configuration
Mount-S3PSDrive -Name S3 -ProfileName my-profile -Region us-east-1
Get-ChildItem S3:/amzn-s3-demo-west-bucket
Get-Content   S3:/amzn-s3-demo-west-bucket/data/report.csv -Raw
```

## Set a default storage class
<a name="pstools-s3-drive-storage-class"></a>

Set a drive-wide default storage class at mount time with `-StorageClass`. Every upload through that drive uses the specified class unless a specific `Set-Content` overrides it with its own `-StorageClass`.

```
# Set all uploads to default to STANDARD_IA
Mount-S3PSDrive -Name Archive -ProfileName my-profile -Region us-east-1 -StorageClass STANDARD_IA
Set-Content Archive:/amzn-s3-demo-bucket/cold/data.txt -Value '...'                        # STANDARD_IA
Set-Content Archive:/amzn-s3-demo-bucket/hot/data.txt  -Value '...' -StorageClass STANDARD # overrides to STANDARD
```

## Unmount a drive
<a name="pstools-s3-drive-unmount"></a>

Use `Dismount-S3PSDrive` (a wrapper over `Remove-PSDrive`) to remove a drive. Change to another location first, because PowerShell won't remove a drive that is your current location.

```
Set-Location $HOME           # or C:\ on Windows
Dismount-S3PSDrive -Name S3
```

## Supported and unsupported operations
<a name="pstools-s3-drive-supported"></a>

Use the drive for browsing and moving object *content*. Bucket lifecycle and server-side copy operations stay with the dedicated S3 cmdlets.

### Supported
<a name="pstools-s3-drive-supported-list"></a>
+ Navigation and listing: `Set-Location`, `Get-ChildItem` (including `-Recurse`), `Get-Item`, `Test-Path`, tab-completion
+ Content: `Get-Content` (download), `Set-Content` (upload)
+ Deletion: `Remove-Item` (single object; prefixes with `-Recurse`)
+ Piping listed items into `Get-Content` and `Remove-Item`

### Not supported
<a name="pstools-s3-drive-not-supported"></a>

| Command | Why / what to use instead |
| --- | --- |
| `Copy-Item` | S3-to-S3 copy is not exposed through the drive. Use [Copy-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Copy-S3Object.html) for server-side copies. For local-to-S3 or S3-to-local transfers, pipe `Get-Content \| Set-Content`. |
| `Move-Item`, `Rename-Item` | S3 has no rename. Perform a copy \+ delete with the cmdlets. |
| `New-Item` (directory) | S3 has no real folders. A prefix appears when you write an object under it. |
| `Clear-Content`, `Add-Content` | Objects are written whole by `Set-Content`. There is no in-place append or clear. |
| `Get-ItemProperty`, `Set-ItemProperty`, `Clear-ItemProperty` | The drive doesn't implement the PowerShell property interface, so these commands fail with the PowerShell engine's own interface-not-supported error instead of the drive's message. The items that `Get-ChildItem` and `Get-Item` return carry only `Name`, `Type`, `Size`, and `LastModified`. To read or set S3 object metadata, use [Get-S3ObjectMetadata](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-S3ObjectMetadata.html) or [Write-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Write-S3Object.html). |
| Creating or deleting buckets | Use [New-S3Bucket](https://docs.aws.amazon.com/powershell/v5/reference/items/New-S3Bucket.html) / [Remove-S3Bucket](https://docs.aws.amazon.com/powershell/v5/reference/items/Remove-S3Bucket.html). |

Unsupported commands fail with a message that names the command and points to the alternative - for example, "Copy-Item is not supported by the S3 drive. Use Copy-S3Object, or pipe Get-Content to Set-Content." The `*-ItemProperty` commands are the exception, as described in the preceding table.

## Command reference
<a name="pstools-s3-drive-command-reference"></a>

For the full parameter list for [Mount-S3PSDrive](https://docs.aws.amazon.com/powershell/v5/reference/items/Mount-S3PSDrive.html) and [Dismount-S3PSDrive](https://docs.aws.amazon.com/powershell/v5/reference/items/Dismount-S3PSDrive.html), see the [AWS Tools for PowerShell Cmdlet Reference](https://docs.aws.amazon.com/powershell/v5/reference/).

On an S3 path, the drive also adds dynamic parameters to `Get-Content` and `Set-Content` that the PowerShell documentation for those cmdlets does not cover:

| Command | Parameters |
| --- | --- |
| `Get-Content` | `-AsByteStream`, `-Raw`, `-Encoding`, `-PartSize` |
| `Set-Content` | `-AsByteStream`, `-Encoding`, `-NoNewline`, `-StorageClass`, `-PartSize` (see [Upload very large objects](#pstools-s3-drive-large-objects)) |

## Troubleshooting
<a name="pstools-s3-drive-troubleshooting"></a>

### "Cannot dismount drive because it is in use."
<a name="pstools-s3-drive-ts-dismount"></a>

The S3 drive is the current location. Change to a location on another drive, such as `$HOME`, and then run `Dismount-S3PSDrive` again.

### The mount fails with "root was not found or is not reachable."
<a name="pstools-s3-drive-ts-root"></a>

The bucket or prefix in `-Root` does not exist. Check the name (and the Region, if the bucket is in one that your credentials don't default to). A *credential* failure produces a different error, not this "not reachable" message. A permission error on the root might not appear until you access an object, so a mount that succeeds does not guarantee that you can read every path under it.

### Deleting a non-empty prefix hangs in a script.
<a name="pstools-s3-drive-ts-delete-hangs"></a>

This happens when you delete a non-empty prefix *without* `-Recurse`. The PowerShell engine raises a confirmation prompt because the prefix has children (the file system provider's container-has-children behavior). A non-interactive host cannot answer the prompt, so the command blocks.

Pass `-Recurse` to delete the prefix's contents without prompting, or confirm interactively to proceed. (`-Force` is not consulted by the drive's delete path, so it has no effect here.)

### "An object I just changed outside the drive still shows the old listing."
<a name="pstools-s3-drive-ts-stale-listing"></a>

Listings are cached briefly (about a second) to keep navigation fast. Changes made *through* the drive appear immediately. Changes made by another tool appear after the short cache expires.

### "A key contains a backslash."
<a name="pstools-s3-drive-ts-backslash"></a>

Whether the drive can address a key that contains a backslash depends on the operating system, because the drive accepts the platform's native path separator:
+ **Windows** - `\` is a path separator, so the drive reads it as one and normalizes it to `/`. A key that contains a literal backslash can't be addressed through the drive. Use the S3 cmdlets instead, for example [Get-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-S3Object.html) or [Read-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Read-S3Object.html).
+ **Linux and macOS** - only `/` is a path separator. A backslash is an ordinary character in a key, so the drive addresses those keys normally.

**See also**
+  [What are the AWS Tools for PowerShell?](pstools-welcome.md)
+  [AWS Tools for PowerShell Cmdlet Reference](https://docs.aws.amazon.com/powershell/v5/reference/)
+  [Amazon S3 documentation](https://docs.aws.amazon.com/s3/)

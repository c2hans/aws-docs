---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/dotnet.html
---

# .NET in AL2023
<a name="dotnet"></a>

 AL2023 currently provides the [.NET](https://dotnet.microsoft.com/) runtime and SDK, versions 8.0, 9.0, and 10.0. .NET 6.0 reached end-of-life in November 2024 and is no longer supported. Each version is supported for the same period of time as upstream .NET. For more information, see [Package support statements](https://docs.aws.amazon.com/linux/al2023/release-notes/all-packages-AL2023.12.html).

## Migrating to newer .NET versions
<a name="dotnet-migration"></a>

**The upstream .NET community provides migration documentation for moving:**
+ [ to .NET 10](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-10/overview)
+ [ to .NET 9](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-9/overview)
+ [ to .NET 8](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-8/overview)

## Installing .NET on AL2023
<a name="dotnet-installation"></a>

 Multiple versions of the .NET runtime can be installed simultaneously on AL2023. However, the `dotnet` and `dotnet-host` packages are shared across SDK versions, so only one SDK version can own the `/usr/bin/dotnet` CLI entry point at a time. Installing a different SDK version will update the shared `dotnet` command to that version.

 To install a specific version of the .NET SDK, use the `dnf` command:

```
sudo dnf install dotnet-sdk-10.0
```

 Replace `10.0` with the desired version (8.0, 9.0, or 10.0).

 To install only the runtime without the SDK:

```
sudo dnf install dotnet-runtime-9.0
```

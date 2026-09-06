---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/dotnet.html
---

# .NET in AL2027
<a name="dotnet"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

 With AL2027, you can use the .NET runtime and SDK, version 10.0. .NET 6.0, 8.0, and 9.0 from AL2023 are not available in AL2027 at this time.

## Migrating to .NET 10
<a name="dotnet-migration"></a>

 If you are moving an application from AL2023 that targets .NET 8.0 or 9.0, for more information about upgrading, see the [.NET 10 migration guide](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-10/overview) on the Microsoft Learn website.

## Installing .NET on AL2027
<a name="dotnet-installation"></a>

 To install the .NET SDK, use the `dnf` command:

```
sudo dnf install dotnet-sdk-10.0
```

 To install only the runtime without the SDK, use the following command:

```
sudo dnf install dotnet-runtime-10.0
```

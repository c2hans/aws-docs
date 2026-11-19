---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-target-updates.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Annual .NET target updates for the AWS SDK for .NET

Starting with version 4.1, the AWS SDK for .NET updates its .NET build targets once a year in a minor version release. Each annual release adds builds for the .NET versions that Microsoft released during the year. It removes builds for .NET versions that are no longer supported according to the [Microsoft .NET lifecycle](https://learn.microsoft.com/en-us/lifecycle/products/microsoft-net-and-net-core) on the Microsoft Learn website. For background about this schedule, see [Annual .NET target updates for the AWS SDK for .NET](https://aws.amazon.com/blogs/developer/annual-net-target-updates-for-the-aws-sdk-for-net/) on the AWS Developer Blog.

If your project targets a version of .NET that Microsoft supports, you can expect to update to the latest version of the SDK with no code changes.

## Changes in version 4.1
<a name="net-dg-target-updates-4-1"></a>

AWS released version 4.1 of the AWS SDK for .NET on November 11, 2026, as the first release on the annual schedule. For the announcement, see [Announcing AWS SDK for .NET 4.1](https://aws.amazon.com/blogs/developer/announcing-aws-sdk-for-net-4-1/) on the AWS Developer Blog.

### Updated build targets
<a name="net-dg-target-updates-4-1-targets"></a>

Version 4.1 includes builds for .NET 11, .NET 10, and .NET 8, and for .NET Standard 2.0 and .NET Framework 4.7.2.

Version 4.1 removes the .NET Core 3.1 target. If your application targets .NET Core 3.1 or .NET 5, 6, or 7, it is out of support. Move it to a version of .NET that Microsoft supports. If you update the SDK without doing so, your project falls back to the .NET Standard 2.0 build of the SDK and you get a compile-time warning similar to the following:

```
warning : The target framework 'net6.0' is no longer supported by the AWS SDK for .NET. This project has fallen back to the .NET Standard 2.0 assemblies of the SDK, which do not include the features and optimizations available on supported targets.
```

The .NET Standard 2.0 build doesn't include target-specific features such as the Native AOT optimizations and bidirectional event stream APIs that are available in the .NET 8 and later builds.

**Note**
The .NET 8 target remains in version 4.1 even though .NET 8 is out of support from Microsoft. For information about how long it remains in the SDK, see [Announcing AWS SDK for .NET 4.1](https://aws.amazon.com/blogs/developer/announcing-aws-sdk-for-net-4-1/) on the AWS Developer Blog.

### AWS Common Runtime (CRT) is no longer needed
<a name="net-dg-target-updates-4-1-crt"></a>

Earlier versions of the SDK used .NET bindings to the native [AWS Common Runtime (CRT)](https://docs.aws.amazon.com/sdkref/latest/guide/common-runtime.html) for algorithms that .NET didn't provide. These algorithms included SigV4a signing for Amazon S3 multi-region access points and CRC64NVME checksums. If you used one of those features without the [AWSSDK.Extensions.CrtIntegration](https://www.nuget.org/packages/AWSSDK.Extensions.CrtIntegration) package from the NuGet website, you got a runtime exception.

Starting with version 4.1, the SDK doesn't need CRT. A managed SigV4a implementation is part of the `AWSSDK.Core` package, and checksums on all targets use the [System.IO.Hashing](https://www.nuget.org/packages/System.IO.Hashing) package from the NuGet website. If your project references `AWSSDK.Extensions.CrtIntegration`, you can remove the reference. Otherwise, the package is included in your deployment bundle and ignored.

Because .NET 8 and .NET 9 are out of support from Microsoft, projects that target them get a compile-time warning from `System.IO.Hashing` similar to the following:

```
warning : System.IO.Hashing 11.0.0 doesn't support net8.0 and has not been tested with it. Consider upgrading your TargetFramework to net10.0 or later.
```

The SDK's continuous integration tests exercise `System.IO.Hashing` for the ways in which the SDK uses it. Update to a version of .NET that Microsoft supports. Alternatively, you can suppress the warning by setting the `SuppressTfmSupportBuildWarnings` MSBuild property to `true` in your project file.

### Performance
<a name="net-dg-target-updates-4-1-performance"></a>

Checksum calculation, such as the CRC32 checksum that the SDK calculates by default for Amazon S3 uploads, now uses `System.IO.Hashing` instead of custom implementations in `AWSSDK.Core`. This avoids allocations and is hardware accelerated on newer targets such as .NET 10 and .NET 11. AWS services are adding support for Concise Binary Object Representation (CBOR). The SDK uses CBOR through the [System.Formats.Cbor](https://www.nuget.org/packages/System.Formats.Cbor) package from the NuGet website, which includes performance improvements for .NET 11. For more information, see [Performance best practices](net-dg-performance.md).

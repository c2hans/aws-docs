---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/sdk-from-pm.html
---

# Getting the AWS SDK for C\+\+ from a package manager
<a name="sdk-from-pm"></a>

**Important**
If you are using a package manager like homebrew or vcpkg:
After updating the SDK for C\+\+ to a new version, you must recompile any library or executable that depends on the SDK.

To set up the AWS SDK for C\+\+, you can either build the SDK yourself directly from the source or download the libraries using a package manager.

The SDK source is separated into individual packages by service. Installing the entire SDK can take up to an hour. Installing only the specific subset of services that your program uses decreases installation time and also reduces size on disk. To choose which services to install, you need to know the package name of each service your program uses. You can see the list of package directories at [https://github.com/aws/aws-sdk-cpp](https://github.com/aws/aws-sdk-cpp) on GitHub. The package name is the suffix of the directory name for the service.

```
aws-sdk-cpp\aws-cpp-sdk-{{<packageName>}}   # Repo directory name and packageName
aws-sdk-cpp\aws-cpp-sdk-s3              # Example: Package name is s3
```

## Prerequisites
<a name="prerequisites"></a>

You need a minimum of 4 GB of RAM to build some of the larger AWS clients. The SDK might fail to build on Amazon EC2 instance types *t2.micro*, *t2.small*, and other small instance types due to insufficient memory.

------
#### [ Linux/macOS ]

To use the AWS SDK for C\+\+ on Linux/macOS, you need one of the following:
+  GNU Compiler Collection (GCC) 4.9 or later, or
+  Clang 3.3 or later.

------
#### [ Windows ]

To use the AWS SDK for C\+\+ on Windows, you need one of the following:
+ Microsoft Visual Studio 2015 or later,
+  GNU Compiler Collection (GCC) 4.9 or later, or
+  Clang 3.3 or later.

------

## Get the SDK using vcpkg
<a name="setupwin-with-vcpkg"></a>

**Important**
The available vcpkg distribution is supported by external contributors and is not provided through AWS. The most recent version is always available through [installing from source](sdk-from-source.md).

[vcpkg](https://github.com/Microsoft/vcpkg) is a package manager updated and maintained by external contributors. Note that this package manager is not provided through AWS and may not reflect the latest available version for the AWS SDK for C\+\+. There is a delay between when a version is released by AWS and when it is available through an external package manager. The most recent version is always available through [installing from source](sdk-from-source.md).

You must install [vcpkg](https://github.com/Microsoft/vcpkg) on your system.
+ Download and bootstrap [vcpkg](https://github.com/Microsoft/vcpkg) by following the instructions on the vcpkg GitHub Readme, substituting the following options when prompted:
  +

    As part of those instructions, you are guided to enter:

    ```
    .\vcpkg\vcpkg install {{[packages to install]}}
    ```

    To install the entire SDK, enter `.\vcpkg\vcpkg install "aws-sdk-cpp[*]" --recurse` or indicate only specific services of the SDK to install by appending a package name in brackets, for example, `.\vcpkg\vcpkg install "aws-sdk-cpp[s3, ec2]" --recurse`

  The output displays a messages including the following:

  ```
  CMake projects should use: "-DCMAKE_TOOLCHAIN_FILE=C:/dev/vcpkg/vcpkg/scripts/buildsystems/vcpkg.cmake"
  ```
+ Copy the complete `-DCMAKE_TOOLCHAIN_FILE` command to use for CMake later. The vcpkg GitHub Readme also instructs on where to use this for your toolset.
+ You may also need to note the build configuration type that you installed via vcpkg. The console output shows the build configuration and the version of the SDK. The following example output indicates the build configuration is "x86-windows" and the AWS SDK for C\+\+ version installed is 1.8.

  ```
  The following packages will be built and installed:
      aws-sdk-cpp[core,dynamodb,kinesis,s3]:x86-windows -> 1.8.126#6
  ```

After you install the AWS SDK for C\+\+, you can develop your own application using the SDK. The example shown in [Creating a simple application](build-cmake.md) reports the Amazon S3 buckets you own.

---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cmake-params.html
---

# CMake parameters for building the AWS SDK for C\+\+
<a name="cmake-params"></a>

Use the [CMake](https://cmake.org/) parameters listed in this section to customize how your SDK builds.

You can set these options with CMake GUI tools or the command line by using *-D*. For example:

```
cmake -DENABLE_UNITY_BUILD=ON -DREGENERATE_CLIENTS=1
```

## General CMake Variables and Options
<a name="cmake-general-options"></a>

The following are general ** `cmake` ** variables and options that affect the build process of the SDK source code.

**Note**
Use these parameters when building the SDK source code for the SDK for C\+\+ itself.

**Topics**
+ [ADD\_CUSTOM\_CLIENTS](#cmake-add-custom-clients)
+ [AUTORUN\_UNIT\_TESTS](#cmake-AUTORUN_UNIT_TESTS)
+ [AWS\_AUTORUN\_LD\_LIBRARY\_PATH](#cmake-AWS_AUTORUN_LD_LIBRARY_PATH)
+ [AWS\_SDK\_WARNINGS\_ARE\_ERRORS](#cmake-AWS_SDK_WARNINGS_ARE_ERRORS)
+ [AWS\_USE\_CRYPTO\_SHARED\_LIBS](#cmake-use-crypto)
+ [AWS\_TEST\_REGION](#cmake-AWS_TEST_REGION)
+ [BUILD\_BENCHMARKS](#cmake-BUILD_BENCHMARKS)
+ [BUILD\_DEPS](#cmake-BUILD_DEPS)
+ [BUILD\_ONLY](#cmake-build-only)
+ [BUILD\_OPTEL](#cmake-BUILD_OPTEL)
+ [BUILD\_SHARED\_LIBS](#cmake-build-shared-libs)
+ [BYPASS\_DEFAULT\_PROXY](#cmake-BYPASS_DEFAULT_PROXY)
+ [CPP\_STANDARD](#cmake-cpp-standard)
+ [CURL\_INCLUDE\_DIR](#cmake-curl-include-dir)
+ [CURL\_LIBRARY](#cmake-curl-library)
+ [CUSTOM\_MEMORY\_MANAGEMENT](#cmake-custom-memory-management)
+ [DISABLE\_INTERNAL\_IMDSV1\_CALLS](#cmake-DISABLE_INTERNAL_IMDSV1_CALLS)
+ [ENABLE\_ADDRESS\_SANITIZER](#cmake-ENABLE_ADDRESS_SANITIZER)
+ [ENABLE\_CURL\_LOGGING](#cmake-enable-curl-logging)
+ [ENABLE\_HTTP\_CLIENT\_TESTING](#cmake-ENABLE_HTTP_CLIENT_TESTING)
+ [ENABLE\_RTTI](#cmake-enable-rtti)
+ [ENABLE\_TESTING](#cmake-enable-testing)
+ [ENABLE\_UNITY\_BUILD](#cmake-enable-unity-build)
+ [ENABLE\_VIRTUAL\_OPERATIONS](#cmake-virtual-op)
+ [ENABLE\_ZLIB\_REQUEST\_COMPRESSION](#cmake-ENABLE_ZLIB_REQUEST_COMPRESSION)
+ [FORCE\_CURL](#cmake-force-curl)
+ [FORCE\_SHARED\_CRT](#cmake-force-shared-crt)
+ [G](#cmake-g)
+ [MINIMIZE\_SIZE](#cmake-minimize-size)
+ [NO\_ENCRYPTION](#cmake-no-encryption)
+ [NO\_HTTP\_CLIENT](#cmake-no-http-client)
+ [REGENERATE\_CLIENTS](#cmake-regenerate-clients)
+ [REGENERATE\_DEFAULTS](#cmake-regenerate-defaults)
+ [SIMPLE\_INSTALL](#cmake-simple-install)
+ [TARGET\_ARCH](#cmake-target-arch)
+ [USE\_CRT\_HTTP\_CLIENT](#cmake-USE_CRT_HTTP_CLIENT)
+ [USE\_IXML\_HTTP\_REQUEST\_2](#cmake-USE_IXML_HTTP_REQUEST_2)
+ [USE\_OPENSSL](#cmake-use-openssl)
+ [USE\_TLS\_V1\_2](#cmake-USE_TLS_V1_2)
+ [USE\_TLS\_V1\_3](#cmake-USE_TLS_V1_3)

### ADD\_CUSTOM\_CLIENTS
<a name="cmake-add-custom-clients"></a>

Builds any arbitrary clients based on the API definition. Place your definition in the `code-generation/api-definitions` folder, and then pass this argument to ** `cmake` **. The ** `cmake` ** configure step generates your client and includes it as a subdirectory in your build. This is particularly useful to generate a C\+\+ client for using one of your [API Gateway](https://aws.amazon.com/api-gateway) services. For example:

```
-DADD_CUSTOM_CLIENTS="serviceName=myCustomService,version=2015-12-21;serviceName=someOtherService,version=2015-08-15"
```

**Note**
To use the `ADD_CUSTOM_CLIENTS` parameter, you must have [Python 2.7](https://www.python.org/downloads/), Java ([JDK 1.8\+](http://openjdk.java.net/install/)), and [Maven](https://maven.apache.org/) installed and in your `PATH`.

### AUTORUN\_UNIT\_TESTS
<a name="cmake-AUTORUN_UNIT_TESTS"></a>

If `ON`, run unit tests automatically after building.

Values
 *ON* \| *OFF*

Default
 *ON*

### AWS\_AUTORUN\_LD\_LIBRARY\_PATH
<a name="cmake-AWS_AUTORUN_LD_LIBRARY_PATH"></a>

The path to append into LD\_LIBRARY\_PATH for unit tests autorun by CMake. Set this path if custom runtime libraries are required for overridden dependencies.

Values
 *String.*

Default
 *N/A*

### AWS\_SDK\_WARNINGS\_ARE\_ERRORS
<a name="cmake-AWS_SDK_WARNINGS_ARE_ERRORS"></a>

If `ON`, treat compiler warnings as errors. Try turning this `OFF` if observing errors on a new or uncommon compiler.

Values
 *ON* \| *OFF*

Default
 *ON*

### AWS\_USE\_CRYPTO\_SHARED\_LIBS
<a name="cmake-use-crypto"></a>

Forces FindCrypto to use a shared crypto library if found. Turn this `OFF` to use [BUILD\_SHARED\_LIBS](#cmake-build-shared-libs)'s setting instead.

Values
 *ON* \| *OFF*

Default
 *OFF*

### AWS\_TEST\_REGION
<a name="cmake-AWS_TEST_REGION"></a>

The AWS Region to use for integration tests.

Values
 *String.*

Default
 *N/A*

### BUILD\_BENCHMARKS
<a name="cmake-BUILD_BENCHMARKS"></a>

If `ON`, build the benchmark executable.

Values
 *ON* \| *OFF*

Default
 *OFF*

### BUILD\_DEPS
<a name="cmake-BUILD_DEPS"></a>

If `ON`, build third-party dependencies.

Values
 *ON* \| *OFF*

Default
 *ON*

### BUILD\_ONLY
<a name="cmake-build-only"></a>

Builds only the clients you want to use. If set to a high-level SDK such as `aws-cpp-sdk-transfer`, *BUILD\_ONLY* resolves any low-level client dependencies. It also builds integration and unit tests related to the projects you select, if they exist. This is a list argument, with values separated by semicolon (`;`) characters. For example:

```
-DBUILD_ONLY="s3;cognito-identity"
```

**Note**
The core SDK module, `aws-sdk-cpp-core`, is *always* built, regardless of the value of the *BUILD\_ONLY* parameter.

### BUILD\_OPTEL
<a name="cmake-BUILD_OPTEL"></a>

If `ON`, builds the open telemetry implementation of tracing.

Values
 *ON* \| *OFF*

Default
 *OFF*

### BUILD\_SHARED\_LIBS
<a name="cmake-build-shared-libs"></a>

A built-in CMake option, re-exposed here for visibility. If `ON`, it builds shared libraries; otherwise, it builds only static libraries.

**Note**
To dynamically link to the SDK, you must define the `USE_IMPORT_EXPORT` symbol for all build targets using the SDK.

Values
 *ON* \| *OFF*

Default
 *ON*

### BYPASS\_DEFAULT\_PROXY
<a name="cmake-BYPASS_DEFAULT_PROXY"></a>

If `ON`, bypass the machine's default proxy settings when using IXmlHttpRequest2.

Values
 *ON* \| *OFF*

Default
 *ON*

### CPP\_STANDARD
<a name="cmake-cpp-standard"></a>

Specifies a custom C\+\+ standard for use with C\+\+ 14 and 17 code bases.

Values
 *11* \| *14* \| *17*

Default
 *11*

### CURL\_INCLUDE\_DIR
<a name="cmake-curl-include-dir"></a>

Path to curl include directory containing `libcurl` headers.

Values
 *String path to selected `include` directory. For example, `D:/path/to/dir/with/curl/include`.*

Default
 *N/A*

### CURL\_LIBRARY
<a name="cmake-curl-library"></a>

Path to curl library file to link against. This library can be a static library or an import library, depending on the needs of your application.

Values
 *String path to the curl library file. For example, `D:/path/to/static/libcur/file/ie/libcurl.lib.a`.*

Default
 *N/A*

### CUSTOM\_MEMORY\_MANAGEMENT
<a name="cmake-custom-memory-management"></a>

To use a custom memory manager, set the value to `1`. You can install a custom allocator so that all STL types use the custom allocation interface. If you set the value `0`, you still might want to use the STL template types to help with DLL safety on Windows.

If static linking is `ON`, custom memory management defaults to *off* (`0`). If dynamic linking is `ON`, custom memory management defaults to *on* (`1`) and avoids cross-DLL allocation and deallocation.

**Note**
To prevent linker mismatch errors, you must use the same value (`0` or `1`) throughout your build system.

To install your own memory manager to handle allocations made by the SDK, you must set `-DCUSTOM_MEMORY_MANAGEMENT` and define `USE_AWS_MEMORY_MANAGEMENT` for all build targets that depend on the SDK.

### DISABLE\_INTERNAL\_IMDSV1\_CALLS
<a name="cmake-DISABLE_INTERNAL_IMDSV1_CALLS"></a>

If `ON`, no internal calls are made to the V1 API of the [Instance Metadata Service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html). If `OFF`, IMDSv2 calls will fallback to using IMDSv1 if the IMDSv2 call fails. For more information on IMDSv1 and IMDSv2, see [Use the Instance Metadata Service to access instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) in the *Amazon EC2 User Guide*.

Values
 *ON* \| *OFF*

Default
 *OFF*

### ENABLE\_ADDRESS\_SANITIZER
<a name="cmake-ENABLE_ADDRESS_SANITIZER"></a>

If `ON`, turns on Address Sanitizer for gcc or clang.

Values
 *ON* \| *OFF*

Default
 *OFF*

### ENABLE\_CURL\_LOGGING
<a name="cmake-enable-curl-logging"></a>

If `ON`, pipe the internal log for curl to the SDK logger.

Values
 *ON* \| *OFF*

Default
 *OFF*

### ENABLE\_HTTP\_CLIENT\_TESTING
<a name="cmake-ENABLE_HTTP_CLIENT_TESTING"></a>

If `ON`, build and run corresponding HTTP client test suites.

Values
 *ON* \| *OFF*

Default
 *OFF*

### ENABLE\_RTTI
<a name="cmake-enable-rtti"></a>

Controls whether the SDK is built to enable run-time type information (RTTI).

Values
 *ON* \| *OFF*

Default
 *ON*

### ENABLE\_TESTING
<a name="cmake-enable-testing"></a>

Controls whether unit and integration test projects are built during the SDK build.

Values
 *ON* \| *OFF*

Default
 *ON*

### ENABLE\_UNITY\_BUILD
<a name="cmake-enable-unity-build"></a>

If `ON`, most SDK libraries are built as a single, generated `.cpp` file. This can significantly reduce static library size and speed up compilation time.

Values
 *ON* \| *OFF*

Default
 *OFF*

### ENABLE\_VIRTUAL\_OPERATIONS
<a name="cmake-virtual-op"></a>

This parameter usually works together with `REGENERATE_CLIENTS` for code generation.

If `ENABLE_VIRTUAL_OPERATIONS` is `ON` and `REGENERATE_CLIENTS` is `ON`, operation-related functions in service clients will be marked as `virtual`.

If `ENABLE_VIRTUAL_OPERATIONS` is `OFF` and `REGENERATE_CLIENTS` is `ON`, `virtual` won't be added to operation functions and service client classes will be marked as `final`.

If `ENABLE_VIRTUAL_OPERATIONS` is `OFF`, the SDK will also add `-ffunction-sections` and `-fdata-sections` compiler flags for gcc and clang when compiling.

For more information, see [CMake Parameters](https://github.com/aws/aws-sdk-cpp/blob/main/docs/CMake_Parameters.md#enable_virtual_operations) on GitHub.

Values
 *ON* \| *OFF*

Default
 *ON*

### ENABLE\_ZLIB\_REQUEST\_COMPRESSION
<a name="cmake-ENABLE_ZLIB_REQUEST_COMPRESSION"></a>

For services that support it, request content will be compressed. On by default if dependency is available.

Values
 *ON* \| *OFF*

Default
 *ON*

### FORCE\_CURL
<a name="cmake-force-curl"></a>

Windows only. If `ON`, forces usage of the curl client instead of the default [WinHTTP](https://msdn.microsoft.com/en-us/library/windows/desktop/aa382925%28v=vs.85%29.aspx) data transfer provider.

Values
 *ON* \| *OFF*

Default
 *OFF*

### FORCE\_SHARED\_CRT
<a name="cmake-force-shared-crt"></a>

If `ON`, the SDK links to the C runtime *dynamically*; otherwise, it uses the *BUILD\_SHARED\_LIBS* setting (sometimes necessary for backward compatibility with earlier versions of the SDK).

Values
 *ON* \| *OFF*

Default
 *ON*

### G
<a name="cmake-g"></a>

Generates build artifacts, such as Visual Studio solutions and Xcode projects.

For example, on Windows:

```
-G "Visual Studio 12 Win64"
```

For more information, see the CMake documentation for your platform.

### MINIMIZE\_SIZE
<a name="cmake-minimize-size"></a>

A superset of [ENABLE\_UNITY\_BUILD](#cmake-enable-unity-build). If `ON`, this option turns on *ENABLE\_UNITY\_BUILD* and additional binary size reduction settings.

Values
 *ON* \| *OFF*

Default
 *OFF*

### NO\_ENCRYPTION
<a name="cmake-no-encryption"></a>

If `ON`, prevents the default platform-specific cryptography implementation from being built into the library. Turn this *ON* to inject your own cryptography implementation.

Values
 *ON* \| *OFF*

Default
 *OFF*

### NO\_HTTP\_CLIENT
<a name="cmake-no-http-client"></a>

If `ON`, prevents the default platform-specific HTTP client from being built into the library. If *ON*, you will need to provide your own platform-specific HTTP client implementation.

Values
 *ON* \| *OFF*

Default
 *OFF*

### REGENERATE\_CLIENTS
<a name="cmake-regenerate-clients"></a>

If `ON`, this parameter deletes all generated code and generates the client directories from the `code-generation/api-definitions` folder. For example:

```
-DREGENERATE_CLIENTS=1
```

**Note**
To use the `REGENERATE_CLIENTS` parameter, you must have [Python 2.7](https://www.python.org/downloads/), Java ([JDK 1.8\+](http://openjdk.java.net/install/)), and [Maven](https://maven.apache.org/) installed and in your `PATH`.

### REGENERATE\_DEFAULTS
<a name="cmake-regenerate-defaults"></a>

If `ON`, this parameter deletes all generated defaults code and generates it again from the `code-generation/defaults` folder. For example:

```
-DREGENERATE_DEFAULTS=1
```

**Note**
To use the `REGENERATE_DEFAULTS` parameter, you must have [Python 2.7](https://www.python.org/downloads/), Java ([JDK 1.8\+](http://openjdk.java.net/install/)), and [Maven](https://maven.apache.org/) installed and in your `PATH`.

### SIMPLE\_INSTALL
<a name="cmake-simple-install"></a>

If `ON`, the install process does not insert platform-specific intermediate directories underneath `bin/` and `lib/`. Turn `OFF` if you need to make multiplatform releases under a single install directory.

Values
 *ON* \| *OFF*

Default
 *ON*

### TARGET\_ARCH
<a name="cmake-target-arch"></a>

To cross-compile or build for a mobile platform, you must specify the target platform. By default, the build detects the host operating system and builds for the detected operating system.

**Note**
When *TARGET\_ARCH* is *ANDROID*, additional options are available. See [Android CMake Variables and Options](#cmake-android-variables).

Values
 *WINDOWS* \| *LINUX* \| *APPLE* \| *ANDROID*

### USE\_CRT\_HTTP\_CLIENT
<a name="cmake-USE_CRT_HTTP_CLIENT"></a>

If `ON`, use the common runtime HTTP client, and the legacy systems such as WinHttp and libcurl are not built or included.

Values
 *ON* \| *OFF*

Default
 *OFF*

### USE\_IXML\_HTTP\_REQUEST\_2
<a name="cmake-USE_IXML_HTTP_REQUEST_2"></a>

Windows only. If `ON`, use the com object IXmlHttpRequest2 for the HTTP stack.

Values
 *ON* \| *OFF*

Default
 *OFF*

### USE\_OPENSSL
<a name="cmake-use-openssl"></a>

If `ON`, the SDK builds using OpenSSL; otherwise, it uses [`awslabs/aws-lc`](https://github.com/awslabs/aws-lc). `AWS-LC` is a general-purpose cryptographic library maintained by the AWS Cryptography team for AWS and their customers. Turning `OFF` the parameter installs `AWS-LC` as replacement of OpenSSL in the system default directory. Don't use if you already have an OpenSSL installation in your system.

Values
 *ON* \| *OFF*

Default
 *ON*

### USE\_TLS\_V1\_2
<a name="cmake-USE_TLS_V1_2"></a>

If `ON`, the HTTP client enforces TLS 1.2.

Values
 *ON* \| *OFF*

Default
 *ON*

### USE\_TLS\_V1\_3
<a name="cmake-USE_TLS_V1_3"></a>

If `ON`, the HTTP client enforces TLS 1.3.

Values
 *ON* \| *OFF*

Default
 *OFF*

## Android CMake Variables and Options
<a name="cmake-android-variables"></a>

Use the following variables when you are creating an Android build of the SDK (when [TARGET\_ARCH](#cmake-target-arch) is set to *ANDROID*).

**Topics**
+ [ANDROID\_ABI](#cmake-android-abi)
+ [ANDROID\_BUILD\_CURL](#cmake-ANDROID_BUILD_CURL)
+ [ANDROID\_BUILD\_OPENSSL](#cmake-ANDROID_BUILD_OPENSSL)
+ [ANDROID\_BUILD\_ZLIB](#cmake-ANDROID_BUILD_ZLIB)
+ [ANDROID\_NATIVE\_API\_LEVEL](#cmake-android-native-api-level)
+ [ANDROID\_STL](#cmake-android-stl)
+ [ANDROID\_TOOLCHAIN\_NAME](#cmake-android-toolchain-name)
+ [DISABLE\_ANDROID\_STANDALONE\_BUILD](#cmake-disable-android-standalone-build)
+ [NDK\_DIR](#cmake-ndk-dir)

### ANDROID\_ABI
<a name="cmake-android-abi"></a>

Android only. Controls which Application Binary Interface (ABI) to output code for.

**Note**
Not all valid Android ABI values are currently supported.

Values
 *arm64* \| *armeabi-v7a* \| *x86\_64* \| *x86* \| *mips64* \| *mips*

Default
 *armeabi-v7a*

### ANDROID\_BUILD\_CURL
<a name="cmake-ANDROID_BUILD_CURL"></a>

Android only. If `ON`, build curl also.

Values
 *ON* \| *OFF*

Default
 *ON*

### ANDROID\_BUILD\_OPENSSL
<a name="cmake-ANDROID_BUILD_OPENSSL"></a>

Android only. If `ON`, build Openssl also.

Values
 *ON* \| *OFF*

Default
 *ON*

### ANDROID\_BUILD\_ZLIB
<a name="cmake-ANDROID_BUILD_ZLIB"></a>

Android only. If `ON`, build Zlib also.

Values
 *ON* \| *OFF*

Default
 *ON*

### ANDROID\_NATIVE\_API\_LEVEL
<a name="cmake-android-native-api-level"></a>

Android only. Controls what API level the SDK builds against. If you set [ANDROID\_STL](#cmake-android-stl) to *gnustl*, you can choose any API level. If you use *libc\+\+*, you must use an API level of at least *21*.

Default
Varies by STL choice.

### ANDROID\_STL
<a name="cmake-android-stl"></a>

Android only. Controls what flavor of the C\+\+ standard library the SDK uses.

**Important**
Performance problems can occur within the SDK if the `gnustl` options are used; we strongly recommend using *libc\+\+\_shared* or *libc\+\+\_static*.

Values
 *libc\+\+\_shared* \| *libc\+\+\_static* \| *gnustl\_shared* \| *gnustl\_static*

Default
 *libc\+\+\_shared*

### ANDROID\_TOOLCHAIN\_NAME
<a name="cmake-android-toolchain-name"></a>

Android only. Controls which compiler is used to build the SDK.

**Note**
With GCC being deprecated by the Android NDK, we recommend using the default value.

Default
 *standalone-clang*

### DISABLE\_ANDROID\_STANDALONE\_BUILD
<a name="cmake-disable-android-standalone-build"></a>

Android only. By default, Android builds use a standalone clang-based toolchain constructed via NDK scripts. To use your own toolchain, turn this option *ON*.

Values
 *ON* \| *OFF*

Default
 *OFF*

### NDK\_DIR
<a name="cmake-ndk-dir"></a>

Android only. Specifies an override path where the build system should find the Android NDK. By default, the build system checks environment variables (`ANDROID_NDK`) if this variable is not set.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for C++. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-cpp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/swift.html
---

# Swift in AL2023
<a name="swift"></a>

 AL2023 currently provides the [https://https://www.swift.org](https://https://www.swift.org) runtime and SDK.

 In AL2023, the Swift SDK and runtime are split into separate packages. The `swiftlang-lib` package contains the runtime libraries, and the `swiftlang` package contains the full SDK. This allows users to run binaries compiled with the Swift SDK on production hosts without requiring the full SDK to be installed. At this time, different versions of Swift are not ABI compatible, so when updating Swift, applications will need to be rebuilt with the new version before they can be deployed.

**Note**
 Like Rust, Swift versions will follow the latest stable version from the Swift project. Packages will not be namespaced, and only one version will be supported at a time.

## Some notes on using Swift on AL2023
<a name="using-swift"></a>
+ **C\+\+ interoperability** – The system's package manager `clang` may not work with Swift. To resolve this, add `swift-clang` to your `PATH` or use alternatives to set `clang` to `swift-clang`.
+ **Debugging Swift code** – The system LLDB cannot debug Swift sources. Use the LLDB included with the Swift package instead by adding the Swift installation directory to your `PATH` or using alternatives to set `lldb` to `swift-lldb`.

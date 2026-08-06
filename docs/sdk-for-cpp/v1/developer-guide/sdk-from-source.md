---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/sdk-from-source.html
---

# Getting the AWS SDK for C\+\+ from source code
<a name="sdk-from-source"></a>

You can use the AWS SDK for C\+\+ from your code by first building the SDK from source and then installing it locally.

**Process overview**

| General process  | Detailed process |
| --- | --- |
|  1.  Use CMake to generate build files for the SDK. <br />2.  Build the SDK. <br />3.  Install the SDK.  | First build the SDK from source and install it. +  [Building on Windows](setup-windows.md) <br />+  [Building on Linux/macOS](setup-linux.md)   |
|  1.  Write your own code to use the SDK or use a sample application, and add the `AWSSDK` package to your cmake file. <br />2.  Use CMake to generate build files for your application. <br />3.  Build your application. <br />4.  Run your application.  | Then develop your own application using the SDK. +  [Creating a simple application](build-cmake.md)  |

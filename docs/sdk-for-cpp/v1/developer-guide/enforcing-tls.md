---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/enforcing-tls.html
---

# Enforcing a minimum TLS version in the AWS SDK for C\+\+
<a name="enforcing-tls"></a>

To increase security when communicating with AWS services, you should configure SDK for C\+\+ to use TLS 1.2 or later. We recommend using TLS 1.3.

The AWS SDK for C\+\+ is a cross-platform library. You can build and run your application on the platforms you want. Different platforms might depend on different underlying HTTP clients.

By default, macOS, Linux, Android and other non-Windows platforms use [libcurl](https://curl.haxx.se/libcurl/). If the libcurl version is later than 7.34.0, TLS 1.0 is the minimum version used by the underlying HTTP clients.

For Windows, the default library is [WinHttp](https://docs.microsoft.com/en-us/windows/win32/winhttp). Windows decides the actual protocol to use among the TLS 1.0, TLS 1.1, TLS 1.2, and TLS 1.3 protocols available. [WinINet](https://docs.microsoft.com/en-us/windows/win32/wininet) and [IXMLHttpRequest2](https://docs.microsoft.com/en-us/windows/win32/api/_ixhr2) are the other two options that are available on Windows. You can configure your application to replace the default library during CMake and at runtime. For these two HTTP clients, Windows also decides the secure protocol.

The AWS SDK for C\+\+ also provides the flexibility to override the default HTTP clients. For example, you can enforce libcurl or use whatever HTTP clients you want by using a custom HTTP client factory. So to use TLS 1.2 as the minimum version, you must be aware of the HTTP client library you’re using.

## Enforce specific TLS version with libcurl on all platforms
<a name="enforce-tls-1-2-with-libcurl-on-all-platforms"></a>

This section assumes that the AWS SDK for C\+\+ is using libcurl as a dependency for HTTP protocol support. To explicitly specify the TLS version, you will need a minimum libcurl version of 7.34.0. In addition, you might need to modify the source code of the AWS SDK for C\+\+ and then rebuild it.

The following procedure shows you how to perform these tasks.

### To enforce TLS 1.2 with libcurl
<a name="to-enforce-tls-1-2-with-libcurl"></a>

1. Verify that your installation of libcurl is at least version 7.34.0.

1. Download the source code for the AWS SDK for C\+\+ from [GitHub](http://github.com/aws/aws-sdk-cpp).

1. Open `aws-cpp-sdk-core/source/http/curl/CurlHttpClient.cpp` and find the following lines of code.

   ```
   #if LIBCURL_VERSION_MAJOR >= 7
   #if LIBCURL_VERSION_MINOR >= 34
   curl_easy_setopt(connectionHandle, CURLOPT_SSLVERSION, CURL_SSLVERSION_TLSv1);
   #endif //LIBCURL_VERSION_MINOR
   #endif //LIBCURL_VERSION_MAJOR
   ```

1. If necessary, change the last parameter in the function call as follows.

   ```
   #if LIBCURL_VERSION_MAJOR >= 7
   #if LIBCURL_VERSION_MINOR >= 34
   curl_easy_setopt(connectionHandle, CURLOPT_SSLVERSION, CURL_SSLVERSION_TLSv1_2);
   #endif //LIBCURL_VERSION_MINOR
   #endif //LIBCURL_VERSION_MAJOR
   ```

1. If you performed the preceding code changes, build and install the AWS SDK for C\+\+ according to the instructions at [https://github.com/aws/aws-sdk-cpp\#building-the-sdk](https://github.com/aws/aws-sdk-cpp#building-the-sdk).

1. For the service client in your application, enable `verifySSL` in its client configuration, if this option isn’t already enabled.

### To enforce TLS 1.3 with libcurl
<a name="to-enforce-tls-1-3-with-libcurl"></a>

To enforce TLS 1.3, follow the steps in the preceding section setting the `CURL_SSLVERSION_TLSv1_3` option instead of `CURL_SSLVERSION_TLSv1_2`.

## Enforce specific TLS version on Windows
<a name="enforce-tls-1-2-on-windows"></a>

The following procedures show you how to enforce TLS 1.2 or TLS 1.3 with WinHttp, WinINet, or IXMLHTTPRequest2.

### Prerequisite: Determine Windows TLS support
<a name="prerequisite-enable-tls-1-1-and-1-2-on-windows"></a>
+ Determine the TLS protocol version support available for your system as described at [https://docs.microsoft.com/en-us/windows/win32/secauthn/protocols-in-tls-ssl–schannel-ssp-](https://docs.microsoft.com/en-us/windows/win32/secauthn/protocols-in-tls-ssl--schannel-ssp-).
+ If you're running on Windows 7 SP1 or Windows Server 2008 R2 SP1, you need to ensure that TLS 1.2 support is enabled in the registry, as described at [https://docs.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings\#tls-12](https://docs.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings#tls-12). If you're running an earlier distribution, you must upgrade your operating system.

### To enforce TLS 1.2 or TLS 1.3 with WinHttp
<a name="to-enforce-tls-1-2-with-winhttp"></a>

WinHttp provides an API to explicitly set the acceptable secure protocols. However, to make this configurable at runtime, you need to modify the source code of the AWS SDK for C\+\+ and then rebuild it.

1. Download the source code for the AWS SDK for C\+\+ from [GitHub](http://github.com/aws/aws-sdk-cpp).

1. Open `aws-cpp-sdk-core/source/http/windows/WinHttpSyncHttpClient.cpp` and find the following lines of code.

   ```
   #if defined(WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_3)
       DWORD flags = WINHTTP_FLAG_SECURE_PROTOCOL_TLS1 | WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_1 |
               WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_2 | WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_3;
   #else
       DWORD flags = WINHTTP_FLAG_SECURE_PROTOCOL_TLS1 | WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_1 | WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_2;
   #endif

   if (!WinHttpSetOption(GetOpenHandle(), WINHTTP_OPTION_SECURE_PROTOCOLS, &flags, sizeof(flags)))
   {
       AWS_LOGSTREAM_FATAL(GetLogTag(), "Failed setting secure crypto protocols with error code: " << GetLastError());
   }
   ```

   The `WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_3` option flag is defined if TLS 1.3 is present on the current build system. For more information, see [WINHTTP\_OPTION\_SECURE\_PROTOCOLS](https://learn.microsoft.com/en-us/windows/win32/winhttp/option-flags#winhttp_option_secure_protocols) and [TLS protocol version support](https://learn.microsoft.com/en-us/windows/win32/secauthn/protocols-in-tls-ssl--schannel-ssp-#tls-protocol-version-support) on the Microsoft website.

1. Choose one of the following:
   + **To enforce TLS 1.2:**

     Under the `#else` directive, change the value of the `flags` variable, as follows.

     ```
     DWORD flags = WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_2;
     ```
   + **To enforce TLS 1.3:**

     Under the `#if defined(WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_3)` directive, change the value of the `flags` variable, as follows.

     ```
     DWORD flags = WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_3;
     ```

1. If you performed the preceding code changes, build and install the AWS SDK for C\+\+ according to the instructions at [https://github.com/aws/aws-sdk-cpp\#building-the-sdk](https://github.com/aws/aws-sdk-cpp#building-the-sdk).

1. For the service client in your application, enable `verifySSL` in its client configuration, if this option isn’t already enabled.

### To enforce TLS 1.2 with WinINet and IXMLHTTPRequest2
<a name="to-enforce-tls-1-2-with-wininet-and-ixmlhttprequest2"></a>

There is no API to specify the secure protocol for the WinINet and IXMLHTTPRequest2 libraries. So the AWS SDK for C\+\+ uses the default for the operating system. You can update the Windows registry to enforce the use of TLS 1.2, as shown in the following procedure. Be advised, however, that the result is a global change that impacts all applications that depend on Schannel.

1. Open Registry Editor and go to `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols`.

1. If they don’t already exist, create the following subkeys: `TLS 1.0,`, `TLS 1.1`, and `TLS 1.2`.

1. Under each of the subkeys, create a `Client` subkey and a `Server` subkey.

1. Create the following keys and values.

   ```
    Key name                          Key type   Value
    --------                          ---------  -----
    TLS 1.0\Client\DisabledByDefault  DWORD      0
    TLS 1.1\Client\DisabledByDefault  DWORD      0
    TLS 1.2\Client\DisabledByDefault  DWORD      0
    TLS 1.0\Client\Enabled            DWORD      0
    TLS 1.1\Client\Enabled            DWORD      0
    TLS 1.2\Client\Enabled            DWORD      1
   ```

   Notice that `TLS 1.2\Client\Enabled` is the only key that’s set to 1. Setting this key to 1 enforces TLS 1.2 as the only acceptable secure protocol.

### To enforce TLS 1.3 with WinINet and IXMLHTTPRequest2
<a name="to-enforce-tls-1-3-with-wininet-and-ixmlhttprequest2"></a>

There is no API to specify the secure protocol for the WinINet and IXMLHTTPRequest2 libraries. So the AWS SDK for C\+\+ uses the default for the operating system. You can update the Windows registry to enforce the use of TLS 1.3, as shown in the following procedure. Be advised, however, that the result is a global change that impacts all applications that depend on Schannel.

1. Open Registry Editor and go to `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols`.

1. If they don’t already exist, create the following subkeys: `TLS 1.0,`, `TLS 1.1`, `TLS 1.2` and `TLS 1.3`.

1. Under each of the subkeys, create a `Client` subkey and a `Server` subkey.

1. Create the following keys and values.

   ```
    Key name                          Key type   Value
    --------                          ---------  -----
    TLS 1.0\Client\DisabledByDefault  DWORD      0
    TLS 1.1\Client\DisabledByDefault  DWORD      0
    TLS 1.2\Client\DisabledByDefault  DWORD      0
    TLS 1.3\Client\DisabledByDefault  DWORD      0
    TLS 1.0\Client\Enabled            DWORD      0
    TLS 1.1\Client\Enabled            DWORD      0
    TLS 1.2\Client\Enabled            DWORD      0
    TLS 1.3\Client\Enabled            DWORD      1
   ```

   Notice that `TLS 1.3\Client\Enabled` is the only key that’s set to 1. Setting this key to 1 enforces TLS 1.3 as the only acceptable secure protocol.

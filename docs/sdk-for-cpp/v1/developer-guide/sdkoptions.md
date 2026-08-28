---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/sdkoptions.html
---

# General configuration using `Aws::SDKOptions` in the AWS SDK for C\+\+
<a name="sdkoptions"></a>

The [`Aws::SDKOptions`](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-core/html/struct_aws_1_1_s_d_k_options.html) struct contains SDK configuration options. `Aws::SDKOptions` focuses on general SDK configuration, whereas the [`ClientConfiguration`](client-config.md) struct focuses on configuration of communicating with AWS services.

An instance of [`Aws::SDKOptions`](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-core/html/struct_aws_1_1_s_d_k_options.html) is passed to the [`Aws::InitAPI` and `Aws::ShutdownAPI` methods](basic-use.md). The same instance should be sent to both methods.

The following samples demonstrate some of the available options.
+ Turn logging on using the default logger

  ```
  Aws::SDKOptions options;
  options.loggingOptions.logLevel = Aws::Utils::Logging::LogLevel::Info;
  Aws::InitAPI(options);
  {
      // make your SDK calls here.
  }
  Aws::ShutdownAPI(options);
  ```
+ Override the default HTTP client factory

  ```
  Aws::SDKOptions options;
  options.httpOptions.httpClientFactory_create_fn = [](){
          return Aws::MakeShared<MyCustomHttpClientFactory>(
              "ALLOC_TAG", arg1);
      };
  Aws::InitAPI(options);
  {
      // make your SDK calls here.
  }
  Aws::ShutdownAPI(options);
  ```
**Note**
 `httpOptions` takes a closure (also called an anonymous function or lambda expression) rather than a `std::shared_ptr`. Each of the SDK factory functions operates in this manner because at the time at which the factory memory allocation occurs, the memory manager has not yet been installed. By passing a closure to the method, the memory manager will be called to perform the memory allocation when it is safe to do so. A simple technique to accomplish this procedure is by using a Lambda expression.
+ Use a global `SIGPIPE` handler

  If you build the SDK for C\+\+ with curl and OpenSSL, you must specify a signal handler. If you don’t use your own custom signal handler, set `installSigPipeHandler` to `true`.

  ```
  Aws::SDKOptions options;
  options.httpOptions.installSigPipeHandler = true;
  Aws::InitAPI(options);
  {
      // make your SDK calls here.
  }
  Aws::ShutdownAPI(options);
  ```

  When `installSigPipeHandler` is `true`, the SDK for C\+\+ uses a handler that ignores `SIGPIPE` signals. For more information on `SIGPIPE`, see [Operation Error Signals](https://www.gnu.org/software/libc/manual/html_node/Operation-Error-Signals.html) on the GNU Operating System website. For more information on the curl handler, see [CURLOPT\_NOSIGNAL explained](https://curl.se/libcurl/c/CURLOPT_NOSIGNAL.html) on the curl website.

  The underlying libraries of curl and OpenSSL can send a `SIGPIPE` signal to notify when the remote side closes a connection. These signals must be handled by the application. For more information this curl functionality, see [libcurl thread safety](https://curl.se/libcurl/c/threadsafe.html) on the curl website. This behavior is not automatically built-in to the SDK because signal handlers are global for each application and the library is a dependency for the SDK.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for C++. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-cpp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

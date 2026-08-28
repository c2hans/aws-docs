---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/overriding-http-client.html
---

# Overriding your HTTP client in the AWS SDK for C\+\+
<a name="overriding-http-client"></a>

The default HTTP client for Windows is [WinHTTP](https://msdn.microsoft.com/en-us/library/windows/desktop/aa382925%28v=vs.85%29.aspx). The default HTTP client for all other platforms is [curl](https://curl.haxx.se/).

Optionally, you can override the HTTP client default by creating a custom `HttpClientFactory` to pass to any service client’s constructor. To override the HTTP client, the SDK must be built with curl support. Curl support is built by default in Linux and macOS, but additional steps are required to build on Windows. For more information about building the SDK on Windows with curl support, see [Building the AWS SDK for C\+\+ on Windows](setup-windows.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for C++. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-cpp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

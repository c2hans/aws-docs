---
source_url: https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-proxy-options.html
---

# Proxy options
<a name="odbc-v2-driver-proxy-options"></a>

## Proxy host
<a name="odbc-v2-driver-proxy-options-proxy-host"></a>

If you require users to go through a proxy, use this parameter to set the proxy host. This parameter corresponds to the `ClientConfiguration.proxyHost` parameter in the AWS SDK. For more information, see [AWS Client configuration](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html) in the *AWS SDK for C\+\+ Developer Guide*.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| --- | --- | --- | --- |
| ProxyHost | Optional | none | ProxyHost=127.0.0.1; |

## Proxy port
<a name="odbc-v2-driver-proxy-options-proxy-port"></a>

Use this parameter to set the proxy port. This parameter corresponds to the `ClientConfiguration.proxyPort` parameter in the AWS SDK. For more information, see [AWS Client configuration](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html) in the *AWS SDK for C\+\+ Developer Guide*.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| --- | --- | --- | --- |
| ProxyPort | Optional | none | ProxyPort=8888; |

## Proxy user name
<a name="odbc-v2-driver-proxy-options-proxy-username"></a>

Use this parameter to set the proxy user name. This parameter corresponds to the `ClientConfiguration.proxyUserName` parameter in the AWS SDK. For more information, see [AWS Client configuration](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html) in the *AWS SDK for C\+\+ Developer Guide*.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| --- | --- | --- | --- |
| ProxyUID | Optional | none | ProxyUID=username; |

## Proxy password
<a name="odbc-v2-driver-proxy-options-proxy-password"></a>

Use this parameter to set the proxy password. This parameter corresponds to the `ClientConfiguration.proxyPassword` parameter in the AWS SDK. For more information, see [AWS Client configuration](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html) in the *AWS SDK for C\+\+ Developer Guide*.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| --- | --- | --- | --- |
| ProxyPWD | Optional | none | ProxyPWD=password; |

## Non proxy host
<a name="odbc-v2-driver-proxy-options-non-proxy-host"></a>

Use this optional parameter to specify a host that the driver connects to without using a proxy. This parameter corresponds to the `ClientConfiguration.nonProxyHosts` parameter in the AWS SDK. For more information, see [AWS Client configuration](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html) in the *AWS SDK for C\+\+ Developer Guide*.

The `NonProxyHost` connection parameter is passed to the `CURLOPT_NOPROXY` curl option. For information about the `CURLOPT_NOPROXY` format, see [CURLOPT\_NOPROXY](https://curl.se/libcurl/c/CURLOPT_NOPROXY.html) in the curl documentation.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| --- | --- | --- | --- |
| NonProxyHost | Optional | none | NonProxyHost=.amazonaws.com,localhost,.example.net,.example.com; |

## Use proxy
<a name="odbc-v2-driver-proxy-options-use-proxy"></a>

Enables user traffic through the specified proxy.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| --- | --- | --- | --- |
| UseProxy | Optional | none | UseProxy=1; |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

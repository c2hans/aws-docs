---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/using-http-proxy.html
---

# Use an HTTP proxy
<a name="using-http-proxy"></a>

To access AWS through proxy servers using the AWS SDK for Kotlin, you can configure either JVM system properties or environment variables. If both are provided, the JVM system properties take precedence.

## Use JVM system properties
<a name="http-proxy-jvm-properties"></a>

The SDK looks for the JVM system properties `https.proxyHost`, `https.proxyPort`, and `http.nonProxyHosts`. For more information on these common JVM system properties, see [Networking and Proxies](https://docs.oracle.com/javase/8/docs/technotes/guides/net/proxies.html) in the Java documentation.

```
java -Dhttps.proxyHost=10.15.20.25 -Dhttps.proxyPort=1234 -Dhttp.nonProxyHosts=localhost|api.example.com MyApplication
```

## Use environment variables
<a name="http-proxy-environment-variables"></a>

The SDK looks for the `https_proxy`, `http_proxy`, and `no_proxy` environment variables (and capitalized versions of each).

```
export http_proxy=http://10.15.20.25:1234
export https_proxy=http://10.15.20.25:5678
export no_proxy=localhost,api.example.com
```

## Use a proxy on EC2 instances
<a name="http-proxy-ec2"></a>

If you configure a proxy on an EC2 instance launched with an attached IAM role, make sure to exempt the address that’s used to access the [instance metadata](/AWSEC2/latest/UserGuide/ec2-instance-metadata.html). To do this, set the `http.nonProxyHosts` JVM system property or `no_proxy` environment variable to the IP address of the Instance Metadata Service, which is `169.254.169.254`. This address does not vary.

```
export no_proxy=169.254.169.254
```

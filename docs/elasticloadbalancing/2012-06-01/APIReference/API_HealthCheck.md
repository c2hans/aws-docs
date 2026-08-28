---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_HealthCheck.html
---

# HealthCheck
<a name="API_HealthCheck"></a>

Information about a health check.

## Contents
<a name="API_HealthCheck_Contents"></a>

 ** HealthyThreshold **
The number of consecutive health checks successes required before moving the instance to the `Healthy` state.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: Yes

 ** Interval **
The approximate interval, in seconds, between health checks of an individual instance.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 300.
Required: Yes

 ** Target **
The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of valid ports is one (1) through 65535.
TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this case, a health check simply attempts to open a TCP connection to the instance on the specified port. Failure to connect within the configured timeout is considered unhealthy.
SSL is also specified as SSL: port pair, for example, SSL:5000.
For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this case, a HTTP GET request is issued to the instance on the given port and path. Any answer other than "200 OK" within the timeout period is considered unhealthy.
The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.
Type: String
Required: Yes

 ** Timeout **
The amount of time, in seconds, during which no response means a failed health check.
This value must be less than the `Interval` value.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 60.
Required: Yes

 ** UnhealthyThreshold **
The number of consecutive health check failures required before moving the instance to the `Unhealthy` state.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: Yes

## See Also
<a name="API_HealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/HealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/HealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/HealthCheck)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

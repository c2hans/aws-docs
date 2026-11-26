---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/monitoring-log-format.html
---

# Application log format

By default, ELB for Envoy writes Envoy application logs in a text format. You can switch to a JSON format in your Envoy bootstrap configuration.

The default text format uses the following pattern.

```
[%Y-%m-%d %T.%e][%t][%l][%n] [%g:%#] %v
```

The fields are the timestamp, thread ID, severity, component name, source file and line, and message. A log line in the default format looks like the following.

```
[2026-11-16 22:41:58.487][3105][critical][main] [external/envoy/source/server/config_validation/server.cc:76] error initializing configuration 'envoy.yaml'
```

To change the text pattern, set `application_log_config.log_format.text_format` in your bootstrap configuration. For the format flags, see [Envoy command line options](https://www.envoyproxy.io/docs/envoy/v1.40.0/operations/cli#cmdoption-log-format) in the Envoy documentation.

To get structured JSON logs instead, set `application_log_config.log_format.json_format` in the bootstrap configuration.

```yaml
application_log_config:
  log_format:
    json_format:
      timestamp: "%Y-%m-%dT%T.%e%z"
      thread_id: "%t"
      level: "%l"
      component: "%n"
      source: "%g:%#"
      message: "%j"
```

Use `%j` for the message so that special characters are escaped for JSON. The `%v` and `%_` message flags are not supported in `json_format`. For more information, see [Printing logs in JSON format](https://www.envoyproxy.io/docs/envoy/v1.40.0/configuration/observability/application_logging#printing-logs-in-json-format) in the Envoy documentation.

Include this block when you create the proxy (see [Create a proxy](create-proxy.md)), or apply it to an existing proxy with the **update-proxy-configuration** command.

```
aws elb-proxy update-proxy-configuration \
    --proxy-identifier <proxy-arn> \
    --configuration-file configurationBytes@=file:///tmp/envoy.yaml
```

ELB for Envoy supports global and per-component log levels. Fine-grained per-source-file logging is not supported. For more information about setting log levels, see [Set the Envoy log level](monitoring-log-level.md).

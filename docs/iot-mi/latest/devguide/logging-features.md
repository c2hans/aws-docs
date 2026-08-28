---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/logging-features.html
---

# Logging features
<a name="logging-features"></a>

Use these methods to implement logging features that managed integrations provides.

## Logger initialization
<a name="logging-initialization"></a>

```
void iotmi_devicesdk_log_init(const char* logger_name)
```

You must initialize the logger before you use any logging functionality.

Parameters
`logger_name` - The logger name you specify. Default value is: `MyApplication`

## Logging macros
<a name="logging-macros"></a>

`LOGGER_LOGD(...)`
Use this macro in your application for DEBUG level logging.

`LOGGER_LOGI(...)`
Use this macro in your application for INFO level logging.

`LOGGER_LOGW(...)`
Use this macro in your application for WARN level logging.

`LOGGER_LOGE(...)`
Use this macro in your application for ERROR level logging.

**Note**
For more information about logging features, see [Hub logging documentation](https://docs.aws.amazon.com/iot-mi/latest/devguide/hub-log.html). Custom protocol plugins fully support all logging features that managed integrations offers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

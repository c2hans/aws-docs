---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-demo.html
---

# FreeRTOS demo application
<a name="freertos-getting-started-demo"></a>

**Important**  <a name="deprecation-message-general"></a>
This page refers to the Amazon-FreeRTOS repository which is deprecated. We recommend that you [start here](freertos-getting-started-modular.md) when you create a new project. If you already have an existing FreeRTOS project based on the now deprecated Amazon-FreeRTOS repository, see the [Amazon-FreeRTOS Github Repository Migration Guide](github-repo-migration.md).

The demo application in this tutorial is the coreMQTT Agent demo defined in the `{{freertos}}/demos/coreMQTT_Agent/mqtt_agent_task.c` file. It uses the [coreMQTT library](coremqtt.md) to connect to the AWS Cloud and then periodically publish messages to an MQTT topic hosted by the [AWS IoT MQTT broker](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html).

Only a single FreeRTOS demo application can run at a time. When you build a FreeRTOS demo project, the first demo enabled in the `{{freertos}}/vendors/{{vendor}}/boards/{{board}}/aws_demos/config_files/aws_demo_config.h` header file is the application that runs. For this tutorial, you do not need to enable or disable any demos. The coreMQTT Agent demo is enabled by default.

For more information about the demo applications included with FreeRTOS, see [FreeRTOS demos](freertos-next-steps.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

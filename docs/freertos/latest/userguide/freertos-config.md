---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/freertos-config.html
---

# Configure the kernel (FreeRTOSConfig.h)
<a name="freertos-config"></a>

You can configure the FreeRTOS kernel for a specific board and application with the `FreeRTOSConfig.h` header file. Every application built on the kernel must have a `FreeRTOSConfig.h` header file in its preprocessor include path. `FreeRTOSConfig.h` is application-specific and should be placed under an application directory, and not in one of the FreeRTOS kernel source code directories.

The `FreeRTOSConfig.h` files for the FreeRTOS demo and test applications are located at `{{freertos}}/vendors/{{vendor}}/boards/{{board}}/aws_demos/config_files/FreeRTOSConfig.h` and `{{freertos}}/vendors/{{vendor}}/boards/{{board}}/aws_tests/config_files/FreeRTOSConfig.h`.

For a list of the available configuration parameters to specify in `FreeRTOSConfig.h`, see [FreeRTOS.org](https://www.freertos.org/a00110.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

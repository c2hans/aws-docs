---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/freertos-next-steps.html
---

# FreeRTOS demos
<a name="freertos-next-steps"></a>

FreeRTOS includes some demo applications in the `demos` folder, under the main FreeRTOS directory. All of the examples that can be executed by FreeRTOS appear in the `common` folder, under `demos`. There is also a folder for each FreeRTOS-qualified platform under the `demos` folder.

Before you try the demo applications, we recommend that you complete the tutorial in [Get Started with FreeRTOS](freertos-getting-started.md). It shows you how to set up and run the coreMQTT Agent demo.

## Running the FreeRTOS demos
<a name="running-demos"></a>

The following topics show you how to set up and run the FreeRTOS demos:
+ [Bluetooth Low Energy demo applications](ble-demo.md)
+ [Demo bootloader for the Microchip Curiosity PIC32MZEF](microchip-bootloader.md)
+ [AWS IoT Device Defender demo](dd-demo.md)
+ [AWS IoT Greengrass V1 discovery demo application](gg-demov1.md)
+ [AWS IoT Greengrass V2](gg-demov2.md)
+ [coreHTTP demos](core-http-demo.md)
+ [AWS IoT Jobs library demo](freertos-jobs-demo.md)
+ [coreMQTT demos](mqtt-demo.md)
+ [Over-the-air updates demo application](ota-demo.md)
+ [Secure Sockets echo client demo](secure-sockets-demo.md)
+ [AWS IoT Device Shadow demo application](shadow-demo.md)

The `DEMO_RUNNER_RunDemos` function, located in the `{{freertos}}/demos/demo_runner/iot_demo_runner.c` file, initializes a detached thread on which a single demo application runs. By default, `DEMO_RUNNER_RunDemos` only calls and starts the coreMQTT Agent demo. Depending on the configuration that you selected when you downloaded FreeRTOS, and where you downloaded FreeRTOS, the other example runner functions might start by default. To enable a demo application, open the `{{freertos}}/vendors/{{vendor}}/boards/{{board}}/aws_demos/config_files/aws_demo_config.h` file, and define the demo that you want to run.

**Note**
Not all combinations of examples work together. Depending on the combination, the software might not run on the selected target due to memory constraints. We recommend that you run one demo at a time.

## Configuring the demos
<a name="configuring-demos"></a>

The demos have been configured to get you started quickly. You might want to change some of the configurations for your project to create a version that runs on your platform. You can find configuration files at `vendors/{{vendor}}/boards/{{board}}/aws_demos/config_files`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

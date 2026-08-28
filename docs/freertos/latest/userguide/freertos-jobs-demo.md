---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/freertos-jobs-demo.html
---

# AWS IoT Jobs library demo
<a name="freertos-jobs-demo"></a>

**Important**  <a name="deprecation-message-demo"></a>
This demo is hosted on the Amazon-FreeRTOS repository which is deprecated. We recommend that you [start here](freertos-getting-started-modular.md) when you create a new project. If you already have an existing FreeRTOS project based on the now deprecated Amazon-FreeRTOS repository, see the [Amazon-FreeRTOS Github Repository Migration Guide](github-repo-migration.md).

## Introduction
<a name="freertos-jobs-demo-introduction"></a>

The AWS IoT Jobs library demo shows you how to connect to the [AWS IoT Jobs service](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html) through an MQTT connection, retrieve a job from AWS IoT, and process it on a device. The AWS IoT Jobs demo project uses the [ FreeRTOS Windows port](https://www.freertos.org/FreeRTOS-Windows-Simulator-Emulator-for-Visual-Studio-and-Eclipse-MingW.html), so it can be built and evaluated with the [Visual Studio Community](https://visualstudio.microsoft.com/vs/community/) version on Windows. No microcontroller hardware is needed. The demo establishes a secure connection to the AWS IoT MQTT broker using TLS in the same manner as the [coreMQTT mutual authentication demo](mqtt-demo-ma.md).

**Note**
To set up and run the FreeRTOS demos, follow the steps in [Get Started with FreeRTOS](freertos-getting-started.md).

## Source code organization
<a name="freertos-jobs-demo-source-code-org"></a>

The demo code is in the `jobs_demo.c` file and can be found on the [GitHub](https://github.com/aws/amazon-freertos/blob/main/demos/jobs_for_aws/jobs_demo.c) website or in the `{{freertos}}/demos/jobs_for_aws/` directory.

## Configure the AWS IoT MQTT broker connection
<a name="freertos-jobs-demo-configure-mqtt-broker"></a>

In this demo, you use an MQTT connection to the AWS IoT MQTT broker. This connection is configured in the same way as the [coreMQTT mutual authentication demo](mqtt-demo-ma.md).

## Functionality
<a name="freertos-jobs-demo-functionality"></a>

The demo shows the workflow used to receive jobs from AWS IoT and process them on a device. The demo is interactive and requires you to create jobs by using either the AWS IoT console or the AWS Command Line Interface (AWS CLI). For more information about creating a job, see [create-job](https://docs.aws.amazon.com/cli/latest/reference/iot/create-job.html) in the *AWS CLI Command Reference*. The demo requires the job document to have an `action` key set to `print` to print a message to the console.

See the following format for this job document.

```
{
    "action": "print",
    "message": "ADD_MESSAGE_HERE"
}
```

You can use the AWS CLI to create a job as in the following example command.

```
aws iot create-job \
    --job-id t12 \
    --targets arn:aws:iot:{{region}}:123456789012:thing/device1 \
    --document '{"action":"print","message":"hello world!"}'
```

The demo also uses a job document that has the `action` key set to `publish` to republish the message to a topic. See the following format for this job document.

```
{
    "action": "publish",
    "message": "ADD_MESSAGE_HERE",
    "topic": "topic/name/here"
}
```

The demo loops until it receives a job document with the `action` key set to `exit` to exit the demo. The format for the job document is as follows.

```
{
    "action: "exit"
}
```

### Entry point of the Jobs demo
<a name="freertos-jobs-demo-functionality-entry-point"></a>

The source code for the Jobs demo entry point function can be found on [ GitHub](https://github.com/aws/amazon-freertos/blob/main/demos/jobs_for_aws/jobs_demo.c#L773-L967). This function performs the following operations:

1. Establish an MQTT connection using the helper functions in `mqtt_demo_helpers.c`.

1. Subscribe to the MQTT topic for the `NextJobExecutionChanged` API, using helper functions in `mqtt_demo_helpers.c`. The topic string is assembled earlier, using macros defined by the AWS IoT Jobs library.

1. Publish to the MQTT topic for the `StartNextPendingJobExecution` API, using helper functions in `mqtt_demo_helpers.c`. The topic string is assembled earlier, using macros defined by the AWS IoT Jobs library.

1. Repeatedly call `MQTT_ProcessLoop` to receive incoming messages which are handed to `prvEventCallback` for processing.

1. After the demo receives the exit action, unsubscribe from the MQTT topic and disconnect, using the helper functions in the `mqtt_demo_helpers.c` file.

### Callback for received MQTT messages
<a name="freertos-jobs-demo-functionality-callback"></a>

The [ prvEventCallback](https://github.com/aws/amazon-freertos/blob/main/demos/jobs_for_aws/jobs_demo.c#L674-L769) function calls `Jobs_MatchTopic` from the AWS IoT Jobs library to classify the incoming MQTT message. If the message type corresponds to a new job, `prvNextJobHandler()` is called.

The [ prvNextJobHandler](https://github.com/aws/amazon-freertos/blob/main/demos/jobs_for_aws/jobs_demo.c#L601-L670) function, and the functions it calls, parse the job document from the JSON-formatted message, and run the action specified by the job. Of particular interest is the `prvSendUpdateForJob` function.

### Send an update for a running job
<a name="freertos-jobs-demo-functionality-send-update"></a>

The function [ prvSendUpdateForJob()](https://github.com/aws/amazon-freertos/blob/main/demos/jobs_for_aws/jobs_demo.c#L413-L457) calls `Jobs_Update()` from the Jobs library to populate the topic string used in the MQTT publish operation that immediately follows.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/lts-qual-steps.html
---

# First test of your microcontroller board
<a name="lts-qual-steps"></a>

You can use IDT for FreeRTOS to test your implementation of the FreeRTOS libraries. After you have ported the FreeRTOS libraries for your board’s device drivers, use AWS IoT Device Tester to run the qualification tests on your microcontroller board.

## Add library porting layers
<a name="lts-add-port-layer"></a>

To port FreeRTOS for your device, see the [FreeRTOS Porting Guide](https://docs.aws.amazon.com/freertos/latest/portingguide/porting-guide.html). When implementing the FreeRTOS tests repository and porting the FreeRTOS layers, you must provide a `manifest.yml` with paths to each library, including the tests repository. This file will be in the root directory of your source code. See [ manifest file instructions](https://docs.aws.amazon.com/freertos/latest/qualificationguide/afq-checklist-manifest-instr.html) for details.

## Configure your AWS credentials for AWS IoT Device Tester to communicate with the AWS Cloud
<a name="lts-cfg-aws-afr"></a>

You need to configure your AWS credentials for AWS IoT Device Tester to communicate with the AWS Cloud. For more information, see [Set up AWS Credentials and Region for Development](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html). Valid AWS credentials are specified in the `{{devicetester_extract_location}}/devicetester_freertos_{{[win|mac|linux]}}/configs/config.json` configuration file.

```
"auth": {
   "method": "environment"
}

"auth": {
    "method": "file",
    "credentials": {
        "profile": "<your-aws-profile>"
    }
}
```

The `auth` attribute of the `config.json` file has a method field that controls AWS authentication, and can be declared as either file or environment. Setting the field to environment pulls your AWS credentials from your host machine’s environment variables. Setting the field to file imports a specified profile from the `.aws/credentials` config file.

**Topics**
+ [Add library porting layers](#lts-add-port-layer)
+ [Configure your AWS credentials for AWS IoT Device Tester to communicate with the AWS Cloud](#lts-cfg-aws-afr)
+ [Create a device pool in IDT for FreeRTOS](lts-cfg-dt-dp.md)
+ [Configure build, flash, and test settings](lts-cfg-dt-ud.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

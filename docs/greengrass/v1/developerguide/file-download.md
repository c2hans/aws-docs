---
source_url: https://docs.aws.amazon.com/greengrass/v1/developerguide/file-download.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# Download required files
<a name="file-download"></a>

1. If you haven't already done so, install the AWS IoT Device SDK for Python. For instructions, see step 1 in [Install the AWS IoT Device SDK for Python](IoT-SDK.md).

   This SDK is used by client devices to communicate with AWS IoT and with AWS IoT Greengrass core devices.

1. From the [ TrafficLight](https://github.com/aws/aws-greengrass-core-sdk-python/tree/master/examples/TrafficLight) examples folder on GitHub, download the `lightController.py` and `trafficLight.py` files to your computer. Save them in the folder that contains the GG\_Switch and GG\_TrafficLight client device certificates and keys.

   The `lightController.py` script corresponds to the GG\_Switch client device, and the `trafficLight.py` script corresponds to the GG\_TrafficLight client device.
![Screenshot of files including the two Python scripts and the device certificates and keys.](http://docs.aws.amazon.com/greengrass/v1/developerguide/images/gg-get-started-082.png)
**Note**
The example Python files are stored in the AWS IoT Greengrass Core SDK for Python repository for convenience, but they don't use the AWS IoT Greengrass Core SDK.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

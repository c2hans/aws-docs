---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/add-idt-sdk.html
---

# Get the IDT client SDK
<a name="add-idt-sdk"></a>

You use the [IDT client SDK](test-executables.md#idt-client-sdk) to enable IDT to interact with the device under test and to report test results. For this tutorial, you will use the Python version of the SDK.

From the `{{<device-tester-extract-location>}}/sdks/python/` folder, copy the `idt_client` folder to your `MyTestSuite_1.0.0/suite/myTestGroup/myTestCase` folder.

To verify that the SDK was successfully copied, run the following command.

```
cd MyTestSuite_1.0.0/suite/myTestGroup/myTestCase
python3 -c 'import idt_client'
```

---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_Command.html
---

# Command
<a name="API_devicemanagement_Command"></a>

The command given to the device to execute.

## Contents
<a name="API_devicemanagement_Command_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** reboot **   <a name="Snowball-Type-devicemanagement_Command-reboot"></a>
Reboots the device.
Type: [Reboot](API_devicemanagement_Reboot.md) object
Required: No

 ** unlock **   <a name="Snowball-Type-devicemanagement_Command-unlock"></a>
Unlocks the device.
Type: [Unlock](API_devicemanagement_Unlock.md) object
Required: No

## See Also
<a name="API_devicemanagement_Command_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/Command)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/Command)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/Command)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

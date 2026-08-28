---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/api/API_AcceleratorEvent.html
---

# AcceleratorEvent
<a name="API_AcceleratorEvent"></a>

A complex type that contains a `Timestamp` value and `Message` for changes that you make to an accelerator in Global Accelerator. Messages stored here provide progress or error information when you update an accelerator from IPv4 to dual-stack, or from dual-stack to IPv4. Global Accelerator stores a maximum of ten event messages.

## Contents
<a name="API_AcceleratorEvent_Contents"></a>

 ** Message **   <a name="globalaccelerator-Type-AcceleratorEvent-Message"></a>
A string that contains an `Event` message describing changes or errors when you update an accelerator in Global Accelerator from IPv4 to dual-stack, or dual-stack to IPv4.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** Timestamp **   <a name="globalaccelerator-Type-AcceleratorEvent-Timestamp"></a>
A timestamp for when you update an accelerator in Global Accelerator from IPv4 to dual-stack, or dual-stack to IPv4.
Type: Timestamp
Required: No

## See Also
<a name="API_AcceleratorEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/AcceleratorEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/AcceleratorEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/AcceleratorEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

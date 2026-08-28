---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CPU.html
---

# CPU
<a name="API_CPU"></a>

Represents the amount of CPU that an app is using on a physical device. Does not represent system-wide CPU usage.

## Contents
<a name="API_CPU_Contents"></a>

 ** architecture **   <a name="devicefarm-Type-CPU-architecture"></a>
The CPU's architecture (for example, x86 or ARM).
Type: String
Required: No

 ** clock **   <a name="devicefarm-Type-CPU-clock"></a>
The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
Type: Double
Required: No

 ** frequency **   <a name="devicefarm-Type-CPU-frequency"></a>
The CPU's frequency.
Type: String
Required: No

## See Also
<a name="API_CPU_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/CPU)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/CPU)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/CPU)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

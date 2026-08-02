---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_NodeLifecycleScript.html
---

# NodeLifecycleScript
<a name="API_NodeLifecycleScript"></a>

A script to run during a compute node lifecycle stage.

## Contents
<a name="API_NodeLifecycleScript_Contents"></a>

 ** name **   <a name="PCS-Type-NodeLifecycleScript-name"></a>
A unique name for the script. The name can be up to 64 characters long. Valid characters are letters, numbers, spaces, underscores (`_`), and hyphens (`-`). The first character must be a letter or a number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9 _-]*`
Required: Yes

 ** scriptSource **   <a name="PCS-Type-NodeLifecycleScript-scriptSource"></a>
The source location and integrity information for the script.
Type: [ScriptSource](API_ScriptSource.md) object
Required: Yes

 ** arguments **   <a name="PCS-Type-NodeLifecycleScript-arguments"></a>
The command-line arguments to pass to the script. You can specify up to 20 arguments, and each argument can be up to 256 characters long.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** executionPolicy **   <a name="PCS-Type-NodeLifecycleScript-executionPolicy"></a>
The policy that determines when the script runs. The default value is `FIRST_BOOT_ONLY`. Valid values:
+  `FIRST_BOOT_ONLY` – Runs the script only the first time the compute node boots.
+  `EVERY_BOOT` – Runs the script every time the compute node boots, including reboots.
Type: String
Valid Values: `FIRST_BOOT_ONLY | EVERY_BOOT`
Required: No

 ** onError **   <a name="PCS-Type-NodeLifecycleScript-onError"></a>
The behavior when the script fails. The default value is `TERMINATE`. Valid values:
+  `TERMINATE` – Terminates the compute node.
+  `STOP_SEQUENCE` – Stops running subsequent scripts in the sequence but doesn't terminate the compute node.
+  `CONTINUE` – Ignores the error and continues running the next script.
Type: String
Valid Values: `TERMINATE | STOP_SEQUENCE | CONTINUE`
Required: No

## See Also
<a name="API_NodeLifecycleScript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/NodeLifecycleScript)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/NodeLifecycleScript)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/NodeLifecycleScript)

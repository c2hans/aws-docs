---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-configs-sdk3-compatibility-mode.html
---

# SDK3 compatibility mode for Key Storage Provider (KSP) for AWS CloudHSM
<a name="ksp-library-configs-sdk3-compatibility-mode"></a>

Key Storage Provider (KSP) implements different approaches for HSM key interaction:
+ Client SDK 5: Provides direct communication with keys stored in the HSM, eliminating the need for local reference files
+ Client SDK 3: Maintains local files on the Windows server that act as references to keys stored in the HSM, using these files to facilitate key operations

For customers migrating from Client SDK 3 to Client SDK 5, enabling SDK3 compatibility mode option supports operations using existing key reference files while preserving the underlying HSM key storage architecture.

## Enable SDK3 compatibility mode
<a name="ksp-library-configs-sdk3-compatibility-mode-on"></a>

------
#### [ Windows ]

**To enable SDK3 compatibility mode for Key Storage Provider (KSP) for Client SDK 5 in Windows**
+ You can use the following command to enable SDK3 compatibility mode:

  ```
  PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" --enable-sdk3-compatibility-mode
  ```

------

## Disable SDK3 compatibility mode
<a name="ksp-library-configs-sdk3-compatibility-mode-off"></a>

------
#### [ Windows ]

**To disable SDK3 compatibility mode for Key Storage Provider (KSP) for Client SDK 5 in Windows**
+ You can use the following command to disable SDK3 compatibility mode:

  ```
  PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" --disable-sdk3-compatibility-mode
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

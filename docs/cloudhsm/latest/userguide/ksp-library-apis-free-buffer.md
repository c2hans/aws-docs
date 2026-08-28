---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-free-buffer.html
---

# NCryptFreeBuffer with Key storage provider (KSP)
<a name="ksp-library-apis-free-buffer"></a>

The `NCryptFreeBuffer` function releases a block of memory that was allocated by the Key Storage Provider (KSP).

## Parameters
<a name="ksp-library-apis-free-buffer-parameters"></a>

 `pvInput` [in]
 The address of the memory to released.

## Return Value
<a name="ksp-library-apis-free-buffer-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:

| Return code | Description |
| --- | --- |
| ERROR\_SUCCESS | The operation completed successfully. |
| NTE\_FAIL | The operation couldn't complete. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

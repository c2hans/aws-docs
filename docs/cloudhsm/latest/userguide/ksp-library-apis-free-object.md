---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-free-object.html
---

# NCryptFreeObject with Key storage provider (KSP)
<a name="ksp-library-apis-free-object"></a>

The `NCryptFreeObject` function releases provider or key handle from the Key Storage Provider (KSP).

## Parameters
<a name="ksp-library-apis-free-object-parameters"></a>

 `hObject` [in]
 The handle of the object to release. You can use:
+ A provider handle (`NCRYPT_PROV_HANDLE`)
+ A key handle (`NCRYPT_KEY_HANDLE`)

## Return Value
<a name="ksp-library-apis-free-object-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:

| Return code | Description |
| --- | --- |
| ERROR\_SUCCESS | The operation completed successfully. |
| NTE\_INVALID\_HANDLE | The handle in `hObject` is not valid. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

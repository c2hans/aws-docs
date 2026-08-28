---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-open-key.html
---

# NCryptOpenKey with Key storage provider (KSP)
<a name="ksp-library-apis-open-key"></a>

The `NCryptOpenKey` function opens a key that exists in the Key Storage Provider (KSP).

## Parameters
<a name="ksp-library-apis-open-key-parameters"></a>

 `hProvider` [in]
The KSP handle that contains the key. Use [`NCryptOpenStorageProvider`](ksp-library-apis-open-provider.md) to get the handle.

 `phKey` [out]
A pointer to a `NCRYPT_KEY_HANDLE` variable that stores the key handle.

`pszKeyName` [in]
A pointer to a null-terminated Unicode string containing the key name.

`dwLegacyKeySpec` [in, unused]
AWS CloudHSM Key Storage Provider (KSP) doesn't use this parameter.

`dwFlags` [in]
Flags that modify function's behavior. No flags are defined for this function.

## Return Value
<a name="ksp-library-apis-open-key-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:

| Return code | Description |
| --- | --- |
| ERROR\_SUCCESS | The operation completed successfully. |
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. |
| NTE\_FAIL | The operation couldn't complete. |
| NTE\_INVALID\_HANDLE | The handle in `hProvider` is not valid. |
| NTE\_BAD\_KEYSET | The key name provided did not return unique result. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-is-alg-supported.html
---

# NCryptIsAlgSupported with Key storage provider (KSP)
<a name="ksp-library-apis-is-alg-supported"></a>

NCryptIsAlgSupported function determines if Key Storage Provider (KSP) supports a specific cryptographic algorithm.

## Parameters
<a name="ksp-library-apis-is-alg-supported-parameters"></a>

 `hProvider` [in]
 The handle of the key storage provider. Use [`NCryptOpenStorageProvider`](ksp-library-apis-open-provider.md) to get the handle.

 `pszAlgId` [in]
 A pointer to a null-terminated Unicode string that contains the identifier of the cryptographic algorithm to create the key. AWS CloudHSM Key Storage Provider (KSP) supports the following algorithms:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-is-alg-supported.html)

`dwFlags` [in]
Flags that modify function behavior. This can be zero or the following value:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-apis-is-alg-supported.html)

## Return Value
<a name="ksp-library-apis-is-alg-supported-return-value"></a>

The function returns a status code to indicate success or failure.

Common return codes include:

| Return code | Description |
| --- | --- |
| ERROR\_SUCCESS | The operation completed successfully. |
| NTE\_INVALID\_PARAMETER | One or more parameters are not valid. |
| NTE\_BAD\_FLAGS | The `dwFlags` parameter contains an invalid value. |
| NTE\_NOT\_SUPPORTED | The `pszAlgId` parameter contains an unsupported value. |
| NTE\_INVALID\_HANDLE | The handle in `hProvider` is not valid. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

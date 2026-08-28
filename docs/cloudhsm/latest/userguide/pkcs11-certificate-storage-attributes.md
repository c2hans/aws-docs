---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-certificate-storage-attributes.html
---

# Certificate storage attributes
<a name="pkcs11-certificate-storage-attributes"></a>

 The following table lists the supported certificate object attributes and their values:

| Attribute | Default value | Description |
| --- | --- | --- |
| `CKA_CLASS` | Required | Must be `CKO_CERTIFICATE`. |
| `CKA_TOKEN` | True | Must be `True`. |
| `CKA_MODIFIABLE` | True | Must be `True`. |
| `CKA_PRIVATE` | False | Must be `False`. |
| `CKA_LABEL` | Empty | Limit 127 characters. |
| `CKA_COPYABLE` | False | Must be `False`. |
| `CKA_DESTROYABLE` | True | Must be `True`. |
| `CKA_CERTIFICATE_TYPE` | Required | Must be `CKC_X_509`. |
| `CKA_TRUSTED` | False | Must be `False`. |
| `CKA_CERTIFICATE_CATEGORY` | `CK_CERTIFICATE_CATEGORY_UNSPECIFIED` | Must be `CK_CERTIFICATE_CATEGORY_UNSPECIFIED`. |
| `CKA_CHECK_VALUE` | Derived from `CKA_VALUE` | Automatically set based on `CKA_VALUE`. |
| `CKA_START_DATE` | Empty | The certificate 'not before' date. |
| `CKA_END_DATE` | Empty | The certificate 'not after' date. |
| `CKA_PUBLIC_KEY_INFO` | Empty | Maximum size is 16 kilobytes. |
| `CKA_SUBJECT` | Required | The certificate subject. |
| `CKA_ID` | Empty | Maximum size is 128 bytes. Uniqueness isn't enforced. |
| `CKA_ISSUER` | Empty | The certificate issuer. |
| `CKA_SERIAL_NUMBER` | Empty | The certificate serial number. |
| `CKA_VALUE` | Required | Maximum size is 32 kilobytes. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

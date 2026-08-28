---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/unwrap_keys_using_trusted.html
---

# How to unwrap a data key with a trusted key for AWS CloudHSM
<a name="unwrap_keys_using_trusted"></a>

To unwrap a data key in AWS CloudHSM, you need a trusted key that has `CKA_UNWRAP` set to true. To be such a key, it must also meet the following criteria:
+ The key’s `CKA_TRUSTED` attribute must be set to true.
+ The key must use `CKA_UNWRAP_TEMPLATE` and related attributes to specify what actions data keys can perform once they are unwrapped. If, for example, you want an unwrapped key to be non-exportable, you set `CKA_EXPORTABLE = FALSE` as part of the `CKA_UNWRAP_TEMPLATE`.

**Note**
`CKA_UNWRAP_TEMPLATE` is only available with PKCS \#11.

When an application submits a key to be unwrapped, the application can also provide its own unwrap template. If you specify an unwrap template and the application provides its own unwrap template, the HSM uses both templates to apply attribute names and values to the key. However, if during the unwrap request a value in the trusted key’s `CKA_UNWRAP_TEMPLATE` conflicts with an attribute provided by the application, the unwrap request fails.

To see an example on unwrapping a data key with a trusted key, refer to [this PKCS \#11 example](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/wrapping/unwrap_with_template.c).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

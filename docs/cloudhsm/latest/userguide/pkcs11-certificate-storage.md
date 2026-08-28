---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-certificate-storage.html
---

# Certificate storage with the PKCS \#11 library
<a name="pkcs11-certificate-storage"></a>

 The AWS CloudHSM PKCS \#11 library supports storing public key certificates as "public objects" (as defined in PKCS \#11 2.40) on hsm2m.medium clusters. This feature allows both public and private PKCS \#11 sessions to create, retrieve, modify, and delete public key certificates.

 To use certificate storage with the PKCS \#11 library, you need to enable it in your client configuration. Once enabled, you can manage certificate objects from your PKCS \#11 applications. Operations that apply to both certificate and key objects, such as [C\_FindObjects](http://docs.oasis-open.org/pkcs11/pkcs11-base/v2.40/os/pkcs11-base-v2.40-os.html#_Toc323205461), will return results from both key and certificate storage.

**Certificate storage limits**
 Certificate storage limits the number of stored certificates for each cluster, and the rate of read and write operations for each HSM. For more information, see [Certificate storage limits](pkcs11-certificate-storage-limits.md).

**Topics**
+ [Enable certificate storage](pkcs11-certificate-storage-configuration.md)
+ [Certificate storage API](pkcs11-certificate-storage-api.md)
+ [Certificate attributes](pkcs11-certificate-storage-attributes.md)
+ [Certificate storage audit logs](pkcs11-certificate-storage-audit-logs.md)
+ [Limits](pkcs11-certificate-storage-limits.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

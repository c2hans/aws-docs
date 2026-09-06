---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_protect_compute_validate_software_integrity.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC06-BP06 Validate software integrity
<a name="sec_protect_compute_validate_software_integrity"></a>

 Implement mechanisms (for example, code signing) to validate that the software, code and libraries used in the workload are from trusted sources and have not been tampered with. For example, you should verify the code signing certificate of binaries and scripts to confirm the author, and ensure it has not been tampered with since created by the author. [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) can help ensure the trust and integrity of your code by centrally managing the code- signing lifecycle, including signing certification and public and private keys. You can learn how to use advanced patterns and best practices for code signing with [AWS Lambda](https://aws.amazon.com/blogs/security/best-practices-and-advanced-patterns-for-lambda-code-signing/). Additionally, a checksum of software that you download, compared to that of the checksum from the provider, can help ensure it has not been tampered with.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Investigate mechanisms: Code signing is one mechanism that can be used to validate software integrity.
  +  [NIST: Security Considerations for Code Signing](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.01262018.pdf)

## Resources
<a name="resources"></a>

**Related documents:**
+ [AWS Signer](https://docs.aws.amazon.com/signer/index.html)
+ [New – Code Signing, a Trust and Integrity Control for AWS Lambda](https://aws.amazon.com/blogs/aws/new-code-signing-a-trust-and-integrity-control-for-aws-lambda/)

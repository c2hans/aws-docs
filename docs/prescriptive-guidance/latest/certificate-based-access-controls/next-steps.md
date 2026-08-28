---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/certificate-based-access-controls/next-steps.html
---

# Next steps and resources
<a name="next-steps"></a>

Now that you understand how to implement secure access controls by using certificate attributes with AWS Identity and Access Management Roles Anywhere, consider reviewing your existing hybrid workload architectures. Identify workloads that currently use long-term credentials or require secure access to AWS resources from outside of the AWS Cloud. Evaluate opportunities to enhance security by implementing certificate-based authentication and applying the fine-grained access controls described in this guide. Consider starting with a small proof of concept before expanding to production workloads. Validate that certificate attributes and trust policies align with your security requirements and organizational structure.

For new accounts and workloads, incorporate these recommendations from the design phase. Use the sample configurations and policies provided in this guide as a foundation. You can adapt them to your specific use cases while maintaining the principle of least privilege. If you need additional guidance or have specific questions about implementing IAM Roles Anywhere in your environment, contact your AWS account team or AWS Professional Services.

## Resources
<a name="next-steps-resources"></a>

### AWS Private Certificate Authority resources
<a name="9999999999999999pcalong--resources.3b119fb1-2013-5a10-9011-2a286452a936"></a>
+ [Security best practices for cross-account access to private CAs](https://docs.aws.amazon.com/privateca/latest/userguide/pca-resource-sharing.html) (AWS Private CA documentation)
+ [Resource-based policies for AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html) (AWS Private CA documentation)
+ [How to use AWS RAM to share your ACM Private CA cross-account](https://aws.amazon.com/blogs/security/how-to-use-aws-ram-to-share-your-acm-private-ca-cross-account/) (AWS blog post)
+ [How do I share my ACM Private Certificate Authority with another AWS account?](https://repost.aws/knowledge-center/acm-share-pca-with-another-account) (AWS Knowledge Center)

### IAM Roles Anywhere and IAM resources
<a name="9999999999999999iamroles--and-9999999999999999iam--resources.278ea895-eb9f-5d16-8ca8-9ead56d68587"></a>
+ [The IAM Roles Anywhere authentication signing process](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-sign-process.html) (IAM Roles Anywhere documentation)
+ [IAM Roles Anywhere Credential Helper](https://github.com/aws/rolesanywhere-credential-helper/tree/main) (GitHub)
+ [Certificate attribute mapping](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/attribute-mapping.html) (IAM Roles Anywhere documentation)
+ [Attribute mapping and trust policy](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/attribute-mappping-and-trust-policy.html) (IAM Roles Anywhere documentation)
+ [Logging IAM Roles Anywhere API calls using AWS CloudTrail](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/logging-using-cloudtrail.html) (IAM Roles Anywhere documentation)
+ [Viewing session tags in CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_ctlogs) (IAM documentation)

### Post-quantum cryptography resources
<a name="post-quantum-cryptography-resources.f53aa505-a4cf-5acb-9435-e666458bbddb"></a>
+ [NIST FIPS 204: Module-Lattice-Based Digital Signature Standard](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.204.pdf) (NIST documentation)
+ [IAM Roles Anywhere ML-DSA certificate support announcement](https://aws.amazon.com/about-aws/whats-new/2026/03/iam-roles-anywhere-post-quantum-digital-certificates/) (AWS What's New post)
+ [Post-quantum cryptography on AWS](https://aws.amazon.com/blogs/security/tag/post-quantum-cryptography/) (AWS Security Blog)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

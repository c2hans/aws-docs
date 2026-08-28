---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/issuess-with-specific-remediations.html
---

# Issues with specific remediations
<a name="issuess-with-specific-remediations"></a>

 **SetSSLBucketPolicy fails with AccessDenied error**

Associated controls: AWS FSBP v1.0.0 S3.5, PCI v3.2.1 PCI.S3.5, CIS v1.4.0 2.1.2, SC v2.0.0 S3.5

 **Issue:** The SetSSLBucketPolicy fails with an AccessDenied error:

 *An error occurred (AccessDenied) when calling the PutBucketPolicy operation: Access Denied*

If the Block Public Access setting has been enabled for a bucket, attempts to put a bucket policy that includes statements that allow public access with fail with this error. This state can be reached by putting a bucket policy that contains such statements, then enabling the public access block for that bucket.

The remediation ConfigureS3BucketPublicAccessBlock (associated controls: AWS FSBP v1.0.0 S3.2, PCI v3.2.1 PCI.S3.2, CIS v1.4.0 2.1.5.2, SC v2.0.0 S3.2) can also put a bucket into this state because it sets the public access block setting without changing the bucket policy.

The SetSSLBucketPolicy adds a statement to the bucket policy to deny requests that do not use SSL. It does not modify the other statements in the policy, so if there are statements that allow public access, the remediation will fail attempting to put the modified bucket policy that still includes those statements.

 **Resolution:** Modify the bucket policy to remove statements that allow public access in conflict with the block public access setting on the bucket.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

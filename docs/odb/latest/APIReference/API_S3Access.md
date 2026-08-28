---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_S3Access.html
---

# S3Access
<a name="API_S3Access"></a>

The configuration for Amazon S3 access from the ODB network.

## Contents
<a name="API_S3Access_Contents"></a>

 ** domainName **   <a name="odb-Type-S3Access-domainName"></a>
The domain name for the Amazon S3 access.
Type: String
Required: No

 ** ipv4Addresses **   <a name="odb-Type-S3Access-ipv4Addresses"></a>
The IPv4 addresses for the Amazon S3 access.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** s3PolicyDocument **   <a name="odb-Type-S3Access-s3PolicyDocument"></a>
The endpoint policy for the Amazon S3 access.
Type: String
Required: No

 ** status **   <a name="odb-Type-S3Access-status"></a>
The status of the Amazon S3 access.
Type: String
Valid Values: `ENABLED | ENABLING | DISABLED | DISABLING`
Required: No

## See Also
<a name="API_S3Access_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/S3Access)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/S3Access)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/S3Access)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

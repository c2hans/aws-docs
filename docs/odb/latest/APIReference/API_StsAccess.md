---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_StsAccess.html
---

# StsAccess
<a name="API_StsAccess"></a>

Configuration for AWS Security Token Service (STS) access from the ODB network.

## Contents
<a name="API_StsAccess_Contents"></a>

 ** domainName **   <a name="odb-Type-StsAccess-domainName"></a>
The domain name for AWS Security Token Service (STS) access configuration.
Type: String
Required: No

 ** ipv4Addresses **   <a name="odb-Type-StsAccess-ipv4Addresses"></a>
The IPv4 addresses allowed for AWS Security Token Service (STS) access.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** status **   <a name="odb-Type-StsAccess-status"></a>
The current status of the AWS Security Token Service (STS) access configuration.
Type: String
Valid Values: `ENABLED | ENABLING | DISABLED | DISABLING`
Required: No

 ** stsPolicyDocument **   <a name="odb-Type-StsAccess-stsPolicyDocument"></a>
The AWS Security Token Service (STS) policy document that defines permissions for token service usage.
Type: String
Required: No

## See Also
<a name="API_StsAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/StsAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/StsAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/StsAccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

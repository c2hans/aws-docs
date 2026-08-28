---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Association.html
---

# Association
<a name="API_Association"></a>

An object that represents the custom domain name association.

## Contents
<a name="API_Association_Contents"></a>

 ** customDomainCertificateArn **   <a name="redshiftserverless-Type-Association-customDomainCertificateArn"></a>
The custom domain name’s certificate Amazon resource name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*.*`
Required: No

 ** customDomainCertificateExpiryTime **   <a name="redshiftserverless-Type-Association-customDomainCertificateExpiryTime"></a>
The expiration time for the certificate.
Type: Timestamp
Required: No

 ** customDomainName **   <a name="redshiftserverless-Type-Association-customDomainName"></a>
The custom domain name associated with the workgroup.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`
Required: No

 ** workgroupName **   <a name="redshiftserverless-Type-Association-workgroupName"></a>
The name of the workgroup associated with the database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: No

## See Also
<a name="API_Association_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/Association)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/Association)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/Association)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

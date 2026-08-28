---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Credentials.html
---

# Credentials
<a name="API_control_Credentials"></a>

The AWS Security Token Service temporary credential that S3 Access Grants vends to grantees and client applications.

## Contents
<a name="API_control_Credentials_Contents"></a>

 ** AccessKeyId **   <a name="AmazonS3-Type-control_Credentials-AccessKeyId"></a>
The unique access key ID of the AWS STS temporary credential that S3 Access Grants vends to grantees and client applications.
Type: String
Required: No

 ** Expiration **   <a name="AmazonS3-Type-control_Credentials-Expiration"></a>
The expiration date and time of the temporary credential that S3 Access Grants vends to grantees and client applications.
Type: Timestamp
Required: No

 ** SecretAccessKey **   <a name="AmazonS3-Type-control_Credentials-SecretAccessKey"></a>
The secret access key of the AWS STS temporary credential that S3 Access Grants vends to grantees and client applications.
Type: String
Required: No

 ** SessionToken **   <a name="AmazonS3-Type-control_Credentials-SessionToken"></a>
The AWS STS temporary credential that S3 Access Grants vends to grantees and client applications.
Type: String
Required: No

## See Also
<a name="API_control_Credentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Credentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Credentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Credentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

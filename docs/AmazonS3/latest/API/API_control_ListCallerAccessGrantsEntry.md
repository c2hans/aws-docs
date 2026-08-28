---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListCallerAccessGrantsEntry.html
---

# ListCallerAccessGrantsEntry
<a name="API_control_ListCallerAccessGrantsEntry"></a>

Part of `ListCallerAccessGrantsResult`. Each entry includes the permission level (READ, WRITE, or READWRITE) and the grant scope of the access grant. If the grant also includes an application ARN, the grantee can only access the S3 data through this application.

## Contents
<a name="API_control_ListCallerAccessGrantsEntry_Contents"></a>

 ** ApplicationArn **   <a name="AmazonS3-Type-control_ListCallerAccessGrantsEntry-ApplicationArn"></a>
The Amazon Resource Name (ARN) of an AWS IAM Identity Center application associated with your Identity Center instance. If the grant includes an application ARN, the grantee can only access the S3 data through this application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[^:]+:sso::\d{12}:application/.*$`
Required: No

 ** GrantScope **   <a name="AmazonS3-Type-control_ListCallerAccessGrantsEntry-GrantScope"></a>
The S3 path of the data to which you have been granted access.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^.+$`
Required: No

 ** Permission **   <a name="AmazonS3-Type-control_ListCallerAccessGrantsEntry-Permission"></a>
The type of permission granted, which can be one of the following values:
+  `READ` - Grants read-only access to the S3 data.
+  `WRITE` - Grants write-only access to the S3 data.
+  `READWRITE` - Grants both read and write access to the S3 data.
Type: String
Valid Values: `READ | WRITE | READWRITE`
Required: No

## See Also
<a name="API_control_ListCallerAccessGrantsEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListCallerAccessGrantsEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListCallerAccessGrantsEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListCallerAccessGrantsEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

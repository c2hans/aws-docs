---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantEntry.html
---

# ListAccessGrantEntry
<a name="API_control_ListAccessGrantEntry"></a>

Information about the access grant.

## Contents
<a name="API_control_ListAccessGrantEntry_Contents"></a>

 ** AccessGrantArn **   <a name="AmazonS3-Type-control_ListAccessGrantEntry-AccessGrantArn"></a>
The Amazon Resource Name (ARN) of the access grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/grant/[a-zA-Z0-9\-]+`
Required: No

 ** AccessGrantId **   <a name="AmazonS3-Type-control_ListAccessGrantEntry-AccessGrantId"></a>
The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** AccessGrantsLocationConfiguration **   <a name="AmazonS3-Type-control_ListAccessGrantEntry-AccessGrantsLocationConfiguration"></a>
The configuration options of the grant location. The grant location is the S3 path to the data to which you are granting access.
Type: [AccessGrantsLocationConfiguration](API_control_AccessGrantsLocationConfiguration.md) data type
Required: No

 ** AccessGrantsLocationId **   <a name="AmazonS3-Type-control_ListAccessGrantEntry-AccessGrantsLocationId"></a>
The ID of the registered location to which you are granting access. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID `default` to the default location `s3://` and assigns an auto-generated ID to other locations that you register.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** ApplicationArn **   <a name="AmazonS3-Type-control_ListAccessGrantEntry-ApplicationArn"></a>
The Amazon Resource Name (ARN) of an AWS IAM Identity Center application associated with your Identity Center instance. If the grant includes an application ARN, the grantee can only access the S3 data through this application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[^:]+:sso::\d{12}:application/.*$`
Required: No

 ** CreatedAt **   <a name="AmazonS3-Type-control_ListAccessGrantEntry-CreatedAt"></a>
The date and time when you created the S3 Access Grants instance.
Type: Timestamp
Required: No

 ** Grantee **   <a name="AmazonS3-Type-control_ListAccessGrantEntry-Grantee"></a>
The user, group, or role to which you are granting access. You can grant access to an IAM user or role. If you have added your corporate directory to AWS IAM Identity Center and associated your Identity Center instance with your S3 Access Grants instance, the grantee can also be a corporate directory user or group.
Type: [Grantee](API_control_Grantee.md) data type
Required: No

 ** GrantScope **   <a name="AmazonS3-Type-control_ListAccessGrantEntry-GrantScope"></a>
The S3 path of the data to which you are granting access. It is the result of appending the `Subprefix` to the location scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^.+$`
Required: No

 ** Permission **   <a name="AmazonS3-Type-control_ListAccessGrantEntry-Permission"></a>
The type of access granted to your S3 data, which can be set to one of the following values:
+  `READ` – Grant read-only access to the S3 data.
+  `WRITE` – Grant write-only access to the S3 data.
+  `READWRITE` – Grant both read and write access to the S3 data.
Type: String
Valid Values: `READ | WRITE | READWRITE`
Required: No

## See Also
<a name="API_control_ListAccessGrantEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessGrantEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessGrantEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessGrantEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

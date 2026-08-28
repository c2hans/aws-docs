---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutPublicAccessBlock.html
---

# PutPublicAccessBlock
<a name="API_control_PutPublicAccessBlock"></a>

**Note**
This operation is not supported by directory buckets.

Creates or modifies the `PublicAccessBlock` configuration for an AWS account. This operation may be restricted when the account is managed by organization-level Block Public Access policies. You might get an Access Denied (403) error when the account is managed by organization-level Block Public Access policies. Organization-level policies override account-level settings, preventing direct account-level modifications. For this operation, users must have the `s3:PutAccountPublicAccessBlock` permission. For more information, see [ Using Amazon S3 block public access](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html).

Related actions include:
+  [GetPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetPublicAccessBlock.html)
+  [DeletePublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeletePublicAccessBlock.html)

## Request Syntax
<a name="API_control_PutPublicAccessBlock_RequestSyntax"></a>

```
PUT /v20180820/configuration/publicAccessBlock HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<PublicAccessBlockConfiguration xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <BlockPublicAcls>{{boolean}}</BlockPublicAcls>
   <IgnorePublicAcls>{{boolean}}</IgnorePublicAcls>
   <BlockPublicPolicy>{{boolean}}</BlockPublicPolicy>
   <RestrictPublicBuckets>{{boolean}}</RestrictPublicBuckets>
</PublicAccessBlockConfiguration>
```

## URI Request Parameters
<a name="API_control_PutPublicAccessBlock_RequestParameters"></a>

The request uses the following URI parameters.

 ** [x-amz-account-id](#API_control_PutPublicAccessBlock_RequestSyntax) **   <a name="AmazonS3-control_PutPublicAccessBlock-request-header-AccountId"></a>
The account ID for the AWS account whose `PublicAccessBlock` configuration you want to set.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_PutPublicAccessBlock_RequestBody"></a>

The request accepts the following data in XML format.

 ** [PublicAccessBlockConfiguration](#API_control_PutPublicAccessBlock_RequestSyntax) **   <a name="AmazonS3-control_PutPublicAccessBlock-request-PublicAccessBlockConfiguration"></a>
Root level tag for the PublicAccessBlockConfiguration parameters.
Required: Yes

 ** [BlockPublicAcls](#API_control_PutPublicAccessBlock_RequestSyntax) **   <a name="AmazonS3-control_PutPublicAccessBlock-request-BlockPublicAcls"></a>
Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets in this account. Setting this element to `TRUE` causes the following behavior:
+  `PutBucketAcl` and `PutObjectAcl` calls fail if the specified ACL is public.
+ PUT Object calls fail if the request includes a public ACL.
+ PUT Bucket calls fail if the request includes a public ACL.
Enabling this setting doesn't affect existing policies or ACLs.
This property is not supported for Amazon S3 on Outposts.
Type: Boolean
Required: No

 ** [BlockPublicPolicy](#API_control_PutPublicAccessBlock_RequestSyntax) **   <a name="AmazonS3-control_PutPublicAccessBlock-request-BlockPublicPolicy"></a>
Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to `TRUE` causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.
Enabling this setting doesn't affect existing bucket policies.
This property is not supported for Amazon S3 on Outposts.
Type: Boolean
Required: No

 ** [IgnorePublicAcls](#API_control_PutPublicAccessBlock_RequestSyntax) **   <a name="AmazonS3-control_PutPublicAccessBlock-request-IgnorePublicAcls"></a>
Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to `TRUE` causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain.
Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set.
This property is not supported for Amazon S3 on Outposts.
Type: Boolean
Required: No

 ** [RestrictPublicBuckets](#API_control_PutPublicAccessBlock_RequestSyntax) **   <a name="AmazonS3-control_PutPublicAccessBlock-request-RestrictPublicBuckets"></a>
Specifies whether Amazon S3 should restrict public bucket policies for buckets in this account. Setting this element to `TRUE` restricts access to buckets with public policies to only AWS service principals and authorized users within this account.
Enabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.
This property is not supported for Amazon S3 on Outposts.
Type: Boolean
Required: No

## Response Syntax
<a name="API_control_PutPublicAccessBlock_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_control_PutPublicAccessBlock_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## See Also
<a name="API_control_PutPublicAccessBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutPublicAccessBlock)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/PutPublicAccessBlock)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutPublicAccessBlock)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutPublicAccessBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutPublicAccessBlock)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutPublicAccessBlock)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutPublicAccessBlock)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutPublicAccessBlock)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutPublicAccessBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutPublicAccessBlock)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Grant.html
---

# Grant
<a name="API_Grant"></a>

Container for grant information.

## Contents
<a name="API_Grant_Contents"></a>

 ** Grantee **   <a name="AmazonS3-Type-Grant-Grantee"></a>
The person being granted permissions.
Type: [Grantee](API_Grantee.md) data type
Required: No

 ** Permission **   <a name="AmazonS3-Type-Grant-Permission"></a>
Specifies the permission given to the grantee.
Type: String
Valid Values: `FULL_CONTROL | WRITE | WRITE_ACP | READ | READ_ACP`
Required: No

## See Also
<a name="API_Grant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Grant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Grant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Grant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

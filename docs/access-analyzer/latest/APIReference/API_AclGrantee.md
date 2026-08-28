---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AclGrantee.html
---

# AclGrantee
<a name="API_AclGrantee"></a>

You specify each grantee as a type-value pair using one of these types. You can specify only one type of grantee. For more information, see [PutBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html).

## Contents
<a name="API_AclGrantee_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** id **   <a name="accessanalyzer-Type-AclGrantee-id"></a>
The value specified is the canonical user ID of an AWS account.
Type: String
Required: No

 ** uri **   <a name="accessanalyzer-Type-AclGrantee-uri"></a>
Used for granting permissions to a predefined group.
Type: String
Required: No

## See Also
<a name="API_AclGrantee_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AclGrantee)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AclGrantee)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AclGrantee)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

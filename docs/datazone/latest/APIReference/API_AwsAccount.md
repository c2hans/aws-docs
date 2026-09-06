---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AwsAccount.html
---

# AwsAccount
<a name="API_AwsAccount"></a>

The account ID of a project.

## Contents
<a name="API_AwsAccount_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsAccountId **   <a name="datazone-Type-AwsAccount-awsAccountId"></a>
The account ID of a project.
Type: String
Pattern: `\d{12}`
Required: No

 ** awsAccountIdPath **   <a name="datazone-Type-AwsAccount-awsAccountIdPath"></a>
The account ID path of a project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_AwsAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AwsAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AwsAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AwsAccount)

---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AthenaTableReference.html
---

# AthenaTableReference
<a name="API_AthenaTableReference"></a>

 A reference to a table within Athena.

## Contents
<a name="API_AthenaTableReference_Contents"></a>

 ** databaseName **   <a name="API-Type-AthenaTableReference-databaseName"></a>
 The database name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_]+-)*([a-zA-Z0-9_]+))?`
Required: Yes

 ** tableName **   <a name="API-Type-AthenaTableReference-tableName"></a>
 The table reference.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_]+)*([a-zA-Z0-9_]+))?`
Required: Yes

 ** workGroup **   <a name="API-Type-AthenaTableReference-workGroup"></a>
 The workgroup of the Athena table reference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([a-zA-Z0-9._-])*`
Required: Yes

 ** catalogName **   <a name="API-Type-AthenaTableReference-catalogName"></a>
 The catalog name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** outputLocation **   <a name="API-Type-AthenaTableReference-outputLocation"></a>
 The output location for the Athena table.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Pattern: `s3://[a-z0-9.-]{3,63}(.*)`
Required: No

 ** region **   <a name="API-Type-AthenaTableReference-region"></a>
The AWS Region where the Athena table is located. This parameter is required to uniquely identify and access tables across different Regions.
Type: String
Valid Values: `us-west-1 | us-west-2 | us-east-1 | us-east-2 | af-south-1 | ap-east-1 | ap-south-2 | ap-southeast-1 | ap-southeast-2 | ap-southeast-3 | ap-southeast-5 | ap-southeast-4 | ap-southeast-7 | ap-south-1 | ap-northeast-3 | ap-northeast-1 | ap-northeast-2 | ca-central-1 | ca-west-1 | eu-south-1 | eu-west-3 | eu-south-2 | eu-central-2 | eu-central-1 | eu-north-1 | eu-west-1 | eu-west-2 | me-south-1 | me-central-1 | il-central-1 | sa-east-1 | mx-central-1 | ap-east-2`
Required: No

## See Also
<a name="API_AthenaTableReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AthenaTableReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AthenaTableReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AthenaTableReference)

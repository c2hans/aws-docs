---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SourceBuildInformation.html
---

# SourceBuildInformation
<a name="API_SourceBuildInformation"></a>

Location of the source code for an application version.

## Contents
<a name="API_SourceBuildInformation_Contents"></a>

 ** SourceLocation **
The location of the source code, as a formatted string, depending on the value of `SourceRepository`
+ For `CodeCommit`, the format is the repository name and commit ID, separated by a forward slash. For example, `my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`.
+ For `S3`, the format is the S3 bucket name and object key, separated by a forward slash. For example, `my-s3-bucket/Folders/my-source-file`.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `.+/.+`
Required: Yes

 ** SourceRepository **
Location where the repository is stored.
+  `CodeCommit`
+  `S3`
Type: String
Valid Values: `CodeCommit | S3`
Required: Yes

 ** SourceType **
The type of repository.
+  `Git`
+  `Zip`
Type: String
Valid Values: `Git | Zip`
Required: Yes

## See Also
<a name="API_SourceBuildInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/SourceBuildInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/SourceBuildInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/SourceBuildInformation)

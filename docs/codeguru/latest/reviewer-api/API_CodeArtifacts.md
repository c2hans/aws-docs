---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeArtifacts.html
---

# CodeArtifacts
<a name="API_CodeArtifacts"></a>

Code artifacts are source code artifacts and build artifacts used in a repository analysis or a pull request review.
+ Source code artifacts are source code files in a Git repository that are compressed into a .zip file.
+ Build artifacts are .jar or .class files that are compressed in a .zip file.

## Contents
<a name="API_CodeArtifacts_Contents"></a>

 ** SourceCodeArtifactsObjectKey **   <a name="reviewer-Type-CodeArtifacts-SourceCodeArtifactsObjectKey"></a>
The S3 object key for a source code .zip file. This is required for all code reviews.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\S(.*\S)?$`
Required: Yes

 ** BuildArtifactsObjectKey **   <a name="reviewer-Type-CodeArtifacts-BuildArtifactsObjectKey"></a>
The S3 object key for a build artifacts .zip file that contains .jar or .class files. This is required for a code review with security analysis. For more information, see [Create code reviews with GitHub Actions](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/working-with-cicd.html) in the *Amazon CodeGuru Reviewer User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\S(.*\S)?$`
Required: No

## See Also
<a name="API_CodeArtifacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/CodeArtifacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/CodeArtifacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/CodeArtifacts)

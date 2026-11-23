---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_ProjectSummary.html
---

# ProjectSummary

A summary of a project, returned in the results of `ListProjects`.

## Contents
<a name="API_ProjectSummary_Contents"></a>

 ** CreationTime **   <a name="Textract-Type-ProjectSummary-CreationTime"></a>
The date and time that the project was created.
Type: Timestamp
Required: Yes

 ** ProjectArn **   <a name="Textract-Type-ProjectSummary-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):project/[a-zA-Z0-9-]{12,36}$`
Required: Yes

 ** LastModifiedTime **   <a name="Textract-Type-ProjectSummary-LastModifiedTime"></a>
The date and time that the project was last modified.
Type: Timestamp
Required: No

 ** ProjectName **   <a name="Textract-Type-ProjectSummary-ProjectName"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

## See Also
<a name="API_ProjectSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/ProjectSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/ProjectSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/ProjectSummary)

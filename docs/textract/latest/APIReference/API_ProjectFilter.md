---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_ProjectFilter.html
---

# ProjectFilter

A filter used to limit results to a specific project.

## Contents
<a name="API_ProjectFilter_Contents"></a>

 ** ProjectArn **   <a name="Textract-Type-ProjectFilter-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project to filter by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):project/[a-zA-Z0-9-]{12,36}$`
Required: Yes

## See Also
<a name="API_ProjectFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/ProjectFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/ProjectFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/ProjectFilter)

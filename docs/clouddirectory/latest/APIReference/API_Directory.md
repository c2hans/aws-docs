---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_Directory.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# Directory
<a name="API_Directory"></a>

Directory structure that includes the directory name and directory ARN.

## Contents
<a name="API_Directory_Contents"></a>

 ** CreationDateTime **   <a name="amazoncds-Type-Directory-CreationDateTime"></a>
The date and time when the directory was created.
Type: Timestamp
Required: No

 ** DirectoryArn **   <a name="amazoncds-Type-Directory-DirectoryArn"></a>
The Amazon Resource Name (ARN) that is associated with the directory. For more information, see [Arn Examples](arns.md).
Type: String
Required: No

 ** Name **   <a name="amazoncds-Type-Directory-Name"></a>
The name of the directory.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: No

 ** State **   <a name="amazoncds-Type-Directory-State"></a>
The state of the directory. Can be either `Enabled`, `Disabled`, or `Deleted`.
Type: String
Valid Values: `ENABLED | DISABLED | DELETED`
Required: No

## See Also
<a name="API_Directory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/Directory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/Directory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/Directory)

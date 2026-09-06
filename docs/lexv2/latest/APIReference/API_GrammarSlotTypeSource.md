---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_GrammarSlotTypeSource.html
---

# GrammarSlotTypeSource
<a name="API_GrammarSlotTypeSource"></a>

Describes the Amazon S3 bucket name and location for the grammar that is the source for the slot type.

## Contents
<a name="API_GrammarSlotTypeSource_Contents"></a>

 ** s3BucketName **   <a name="lexv2-Type-GrammarSlotTypeSource-s3BucketName"></a>
The name of the Amazon S3 bucket that contains the grammar source.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
Required: Yes

 ** s3ObjectKey **   <a name="lexv2-Type-GrammarSlotTypeSource-s3ObjectKey"></a>
The path to the grammar in the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\.\-\!\*\_\'\(\)a-zA-Z0-9][\.\-\!\*\_\'\(\)\/a-zA-Z0-9]*$`
Required: Yes

 ** kmsKeyArn **   <a name="lexv2-Type-GrammarSlotTypeSource-kmsKeyArn"></a>
The AWS KMS key required to decrypt the contents of the grammar, if any.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:[\w\-]+:kms:[\w\-]+:[\d]{12}:(?:key\/[\w\-]+|alias\/[a-zA-Z0-9:\/_\-]{1,256})$`
Required: No

## See Also
<a name="API_GrammarSlotTypeSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/GrammarSlotTypeSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/GrammarSlotTypeSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/GrammarSlotTypeSource)

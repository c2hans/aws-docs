---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_TestSetImportResourceSpecification.html
---

# TestSetImportResourceSpecification
<a name="API_TestSetImportResourceSpecification"></a>

Contains information about the test set that is imported.

## Contents
<a name="API_TestSetImportResourceSpecification_Contents"></a>

 ** importInputLocation **   <a name="lexv2-Type-TestSetImportResourceSpecification-importInputLocation"></a>
Contains information about the input location from where test-set should be imported.
Type: [TestSetImportInputLocation](API_TestSetImportInputLocation.md) object
Required: Yes

 ** modality **   <a name="lexv2-Type-TestSetImportResourceSpecification-modality"></a>
Specifies whether the test-set being imported contains written or spoken data.
Type: String
Valid Values: `Text | Audio`
Required: Yes

 ** roleArn **   <a name="lexv2-Type-TestSetImportResourceSpecification-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has permission to access the test set.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.*$`
Required: Yes

 ** storageLocation **   <a name="lexv2-Type-TestSetImportResourceSpecification-storageLocation"></a>
Contains information about the location that Amazon Lex uses to store the test-set.
Type: [TestSetStorageLocation](API_TestSetStorageLocation.md) object
Required: Yes

 ** testSetName **   <a name="lexv2-Type-TestSetImportResourceSpecification-testSetName"></a>
The name of the test set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** description **   <a name="lexv2-Type-TestSetImportResourceSpecification-description"></a>
The description of the test set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** testSetTags **   <a name="lexv2-Type-TestSetImportResourceSpecification-testSetTags"></a>
A list of tags to add to the test set. You can only add tags when you import/generate a new test set. You can't use the `UpdateTestSet` operation to update tags. To update tags, use the `TagResource` operation.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_TestSetImportResourceSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/TestSetImportResourceSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/TestSetImportResourceSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/TestSetImportResourceSpecification)

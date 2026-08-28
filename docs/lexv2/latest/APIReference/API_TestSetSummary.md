---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_TestSetSummary.html
---

# TestSetSummary
<a name="API_TestSetSummary"></a>

Contains summary information about the test set.

## Contents
<a name="API_TestSetSummary_Contents"></a>

 ** creationDateTime **   <a name="lexv2-Type-TestSetSummary-creationDateTime"></a>
The date and time at which the test set was created.
Type: Timestamp
Required: No

 ** description **   <a name="lexv2-Type-TestSetSummary-description"></a>
The description of the test set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** lastUpdatedDateTime **   <a name="lexv2-Type-TestSetSummary-lastUpdatedDateTime"></a>
The date and time at which the test set was last updated.
Type: Timestamp
Required: No

 ** modality **   <a name="lexv2-Type-TestSetSummary-modality"></a>
Specifies whether the test set contains written or spoken data.
Type: String
Valid Values: `Text | Audio`
Required: No

 ** numTurns **   <a name="lexv2-Type-TestSetSummary-numTurns"></a>
The number of turns in the test set.
Type: Integer
Required: No

 ** roleArn **   <a name="lexv2-Type-TestSetSummary-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has permission to access the test set.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.*$`
Required: No

 ** status **   <a name="lexv2-Type-TestSetSummary-status"></a>
The status of the test set.
Type: String
Valid Values: `Importing | PendingAnnotation | Deleting | ValidationError | Ready`
Required: No

 ** storageLocation **   <a name="lexv2-Type-TestSetSummary-storageLocation"></a>
Contains information about the location at which the test set is stored.
Type: [TestSetStorageLocation](API_TestSetStorageLocation.md) object
Required: No

 ** testSetId **   <a name="lexv2-Type-TestSetSummary-testSetId"></a>
The unique identifier of the test set.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: No

 ** testSetName **   <a name="lexv2-Type-TestSetSummary-testSetName"></a>
The name of the test set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

## See Also
<a name="API_TestSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/TestSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/TestSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/TestSetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

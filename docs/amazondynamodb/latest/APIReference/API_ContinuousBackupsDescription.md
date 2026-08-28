---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ContinuousBackupsDescription.html
---

# ContinuousBackupsDescription
<a name="API_ContinuousBackupsDescription"></a>

Represents the continuous backups and point in time recovery settings on the table.

## Contents
<a name="API_ContinuousBackupsDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContinuousBackupsStatus **   <a name="DDB-Type-ContinuousBackupsDescription-ContinuousBackupsStatus"></a>
 `ContinuousBackupsStatus` can be one of the following states: ENABLED, DISABLED
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** PointInTimeRecoveryDescription **   <a name="DDB-Type-ContinuousBackupsDescription-PointInTimeRecoveryDescription"></a>
The description of the point in time recovery settings applied to the table.
Type: [PointInTimeRecoveryDescription](API_PointInTimeRecoveryDescription.md) object
Required: No

## See Also
<a name="API_ContinuousBackupsDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ContinuousBackupsDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ContinuousBackupsDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ContinuousBackupsDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

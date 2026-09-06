---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RedshiftDataParameters.html
---

# RedshiftDataParameters
<a name="API_RedshiftDataParameters"></a>

These are custom parameters to be used when the target is a Amazon Redshift cluster to invoke the Amazon Redshift Data API ExecuteStatement based on EventBridge events.

## Contents
<a name="API_RedshiftDataParameters_Contents"></a>

 ** Database **   <a name="eventbridge-Type-RedshiftDataParameters-Database"></a>
The name of the database. Required when authenticating using temporary credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** DbUser **   <a name="eventbridge-Type-RedshiftDataParameters-DbUser"></a>
The database user name. Required when authenticating using temporary credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SecretManagerArn **   <a name="eventbridge-Type-RedshiftDataParameters-SecretManagerArn"></a>
The name or ARN of the secret that enables access to the database. Required when authenticating using AWS Secrets Manager.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:[a-z0-9-.]+:.*)|(\$(\.[\w_-]+(\[(\d+|\*)\])*)*)`
Required: No

 ** Sql **   <a name="eventbridge-Type-RedshiftDataParameters-Sql"></a>
The SQL statement text to run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Required: No

 ** Sqls **   <a name="eventbridge-Type-RedshiftDataParameters-Sqls"></a>
One or more SQL statements to run. The SQL statements are run as a single transaction. They run serially in the order of the array. Subsequent SQL statements don't start until the previous statement in the array completes. If any SQL statement fails, then because they are run as one transaction, all work is rolled back.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Length Constraints: Minimum length of 1. Maximum length of 100000.
Required: No

 ** StatementName **   <a name="eventbridge-Type-RedshiftDataParameters-StatementName"></a>
The name of the SQL statement. You can name the SQL statement when you create it to identify the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** WithEvent **   <a name="eventbridge-Type-RedshiftDataParameters-WithEvent"></a>
Indicates whether to send an event back to EventBridge after the SQL statement runs.
Type: Boolean
Required: No

## See Also
<a name="API_RedshiftDataParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/RedshiftDataParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/RedshiftDataParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/RedshiftDataParameters)

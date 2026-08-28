---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Integration.html
---

# Integration
<a name="API_Integration"></a>

A zero-ETL integration with Amazon Redshift.

## Contents
<a name="API_Integration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AdditionalEncryptionContext **  AdditionalEncryptionContext.entry.N.key (key)  AdditionalEncryptionContext.entry.N.value (value)
The encryption context for the integration. For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) in the * AWS Key Management Service Developer Guide*.
Type: String to string map
Required: No

 ** CreateTime **
The time when the integration was created, in Universal Coordinated Time (UTC).
Type: Timestamp
Required: No

 ** DataFilter **
Data filters for the integration. These filters determine which tables from the source database are sent to the target Amazon Redshift data warehouse.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25600.
Pattern: `[a-zA-Z0-9_ "\\\-$,*.:?+\/]*`
Required: No

 ** Description **
A description of the integration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `.*`
Required: No

 ** Errors.IntegrationError.N **
Any errors associated with the integration.
Type: Array of [IntegrationError](API_IntegrationError.md) objects
Required: No

 ** IntegrationArn **
The ARN of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws[a-z\-]*:rds(-[a-z]*)?:[a-z0-9\-]*:[0-9]*:integration:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** IntegrationName **
The name of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`
Required: No

 ** KMSKeyId **
The AWS Key Management System (AWS KMS) key identifier for the key used to to encrypt the integration.
Type: String
Required: No

 ** SourceArn **
The Amazon Resource Name (ARN) of the database used as the source for replication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws[a-z\-]*:rds(-[a-z]*)?:[a-z0-9\-]*:[0-9]*:(cluster|db):[a-z][a-z0-9]*(-[a-z0-9]+)*`
Required: No

 ** Status **
The current status of the integration.
Type: String
Valid Values: `creating | active | modifying | failed | deleting | syncing | needs_attention`
Required: No

 ** Tags.Tag.N **
A list of tags.
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TargetArn **
The ARN of the Redshift data warehouse used as the target for replication.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## See Also
<a name="API_Integration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/Integration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/Integration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/Integration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

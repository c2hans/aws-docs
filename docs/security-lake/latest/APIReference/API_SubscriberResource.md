---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_SubscriberResource.html
---

# SubscriberResource
<a name="API_SubscriberResource"></a>

Provides details about the Amazon Security Lake account subscription. Subscribers are notified of new objects for a source as the data is written to your Amazon S3 bucket for Security Lake.

## Contents
<a name="API_SubscriberResource_Contents"></a>

 ** sources **   <a name="securitylake-Type-SubscriberResource-sources"></a>
Amazon Security Lake supports log and event collection for natively supported AWS services. For more information, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/source-management.html).
Type: Array of [LogSourceResource](API_LogSourceResource.md) objects
Required: Yes

 ** subscriberArn **   <a name="securitylake-Type-SubscriberResource-subscriberArn"></a>
The subscriber ARN of the Amazon Security Lake subscriber account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:(aws|aws-us-gov|aws-cn):securitylake:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9][A-Za-z0-9_/.\-]{0,127}`
Required: Yes

 ** subscriberId **   <a name="securitylake-Type-SubscriberResource-subscriberId"></a>
The subscriber ID of the Amazon Security Lake subscriber account.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** subscriberIdentity **   <a name="securitylake-Type-SubscriberResource-subscriberIdentity"></a>
The AWS identity used to access your data.
Type: [AwsIdentity](API_AwsIdentity.md) object
Required: Yes

 ** subscriberName **   <a name="securitylake-Type-SubscriberResource-subscriberName"></a>
The name of your Amazon Security Lake subscriber account.
Type: String
Pattern: `[\\\w\-_:/.@=+]*`
Required: Yes

 ** accessTypes **   <a name="securitylake-Type-SubscriberResource-accessTypes"></a>
You can choose to notify subscribers of new objects with an Amazon Simple Queue Service (Amazon SQS) queue or through messaging to an HTTPS endpoint provided by the subscriber.
 Subscribers can consume data by directly querying AWS Lake Formation tables in your Amazon S3 bucket through services like Amazon Athena. This subscription type is defined as `LAKEFORMATION`.
Type: Array of strings
Valid Values: `LAKEFORMATION | S3`
Required: No

 ** createdAt **   <a name="securitylake-Type-SubscriberResource-createdAt"></a>
The date and time when the subscriber was created.
Type: Timestamp
Required: No

 ** resourceShareArn **   <a name="securitylake-Type-SubscriberResource-resourceShareArn"></a>
The Amazon Resource Name (ARN) which uniquely defines the AWS RAM resource share. Before accepting the RAM resource share invitation, you can view details related to the RAM resource share.
This field is available only for Lake Formation subscribers created after March 8, 2023.
Type: String
Required: No

 ** resourceShareName **   <a name="securitylake-Type-SubscriberResource-resourceShareName"></a>
The name of the resource share.
Type: String
Pattern: `LakeFormation(?:-V[0-9]+)-([a-zA-Z0-9]+)-([\\\w\-_:/.@=+]*)`
Required: No

 ** roleArn **   <a name="securitylake-Type-SubscriberResource-roleArn"></a>
The Amazon Resource Name (ARN) specifying the role of the subscriber.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** s3BucketArn **   <a name="securitylake-Type-SubscriberResource-s3BucketArn"></a>
The ARN for the Amazon S3 bucket.
Type: String
Required: No

 ** subscriberDescription **   <a name="securitylake-Type-SubscriberResource-subscriberDescription"></a>
The subscriber descriptions for a subscriber account. The description for a subscriber includes `subscriberName`, `accountID`, `externalID`, and `subscriberId`.
Type: String
Pattern: `[\\\w\-_:/.@=+]*`
Required: No

 ** subscriberEndpoint **   <a name="securitylake-Type-SubscriberResource-subscriberEndpoint"></a>
The subscriber endpoint to which exception messages are posted.
Type: String
Pattern: `[\\\w\-_:/.@=+]*`
Required: No

 ** subscriberStatus **   <a name="securitylake-Type-SubscriberResource-subscriberStatus"></a>
The subscriber status of the Amazon Security Lake subscriber account.
Type: String
Valid Values: `ACTIVE | DEACTIVATED | PENDING | READY`
Required: No

 ** updatedAt **   <a name="securitylake-Type-SubscriberResource-updatedAt"></a>
The date and time when the subscriber was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_SubscriberResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/SubscriberResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/SubscriberResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/SubscriberResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

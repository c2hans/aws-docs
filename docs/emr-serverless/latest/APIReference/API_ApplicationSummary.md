---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ApplicationSummary.html
---

# ApplicationSummary
<a name="API_ApplicationSummary"></a>

The summary of attributes associated with an application.

## Contents
<a name="API_ApplicationSummary_Contents"></a>

 ** arn **   <a name="emrserverless-Type-ApplicationSummary-arn"></a>
The ARN of the application.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `arn:(aws[a-zA-Z0-9-]*):emr-serverless:.+:(\d{12}):\/applications\/[0-9a-zA-Z]+`
Required: Yes

 ** createdAt **   <a name="emrserverless-Type-ApplicationSummary-createdAt"></a>
The date and time when the application was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="emrserverless-Type-ApplicationSummary-id"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** releaseLabel **   <a name="emrserverless-Type-ApplicationSummary-releaseLabel"></a>
The Amazon EMR release associated with the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/-]+`
Required: Yes

 ** state **   <a name="emrserverless-Type-ApplicationSummary-state"></a>
The state of the application.
Type: String
Valid Values: `CREATING | CREATED | STARTING | STARTED | STOPPING | STOPPED | TERMINATED`
Required: Yes

 ** type **   <a name="emrserverless-Type-ApplicationSummary-type"></a>
The type of application, such as Spark or Hive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** updatedAt **   <a name="emrserverless-Type-ApplicationSummary-updatedAt"></a>
The date and time when the application was last updated.
Type: Timestamp
Required: Yes

 ** architecture **   <a name="emrserverless-Type-ApplicationSummary-architecture"></a>
The CPU architecture of an application.
Type: String
Valid Values: `ARM64 | X86_64`
Required: No

 ** name **   <a name="emrserverless-Type-ApplicationSummary-name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/#-]+`
Required: No

 ** stateDetails **   <a name="emrserverless-Type-ApplicationSummary-stateDetails"></a>
The state details of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/ApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/ApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/ApplicationSummary)

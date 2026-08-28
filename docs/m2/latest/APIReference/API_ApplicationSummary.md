---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_ApplicationSummary.html
---

# ApplicationSummary
<a name="API_ApplicationSummary"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

A subset of the possible application attributes. Used in the application list.

## Contents
<a name="API_ApplicationSummary_Contents"></a>

 ** applicationArn **   <a name="m2-Type-ApplicationSummary-applicationArn"></a>
The Amazon Resource Name (ARN) of the application.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]|):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** applicationId **   <a name="m2-Type-ApplicationSummary-applicationId"></a>
The unique identifier of the application.
Type: String
Pattern: `\S{1,80}`
Required: Yes

 ** applicationVersion **   <a name="m2-Type-ApplicationSummary-applicationVersion"></a>
The version of the application.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** creationTime **   <a name="m2-Type-ApplicationSummary-creationTime"></a>
The timestamp when the application was created.
Type: Timestamp
Required: Yes

 ** engineType **   <a name="m2-Type-ApplicationSummary-engineType"></a>
The type of the target platform for this application.
Type: String
Valid Values: `microfocus | bluage`
Required: Yes

 ** name **   <a name="m2-Type-ApplicationSummary-name"></a>
The name of the application.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** status **   <a name="m2-Type-ApplicationSummary-status"></a>
The status of the application.
Type: String
Valid Values: `Creating | Created | Available | Ready | Starting | Running | Stopping | Stopped | Failed | Deleting | Deleting From Environment`
Required: Yes

 ** deploymentStatus **   <a name="m2-Type-ApplicationSummary-deploymentStatus"></a>
Indicates either an ongoing deployment or if the application has ever deployed successfully.
Type: String
Valid Values: `Deploying | Deployed`
Required: No

 ** description **   <a name="m2-Type-ApplicationSummary-description"></a>
The description of the application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** environmentId **   <a name="m2-Type-ApplicationSummary-environmentId"></a>
The unique identifier of the runtime environment that hosts this application.
Type: String
Pattern: `\S{1,80}`
Required: No

 ** lastStartTime **   <a name="m2-Type-ApplicationSummary-lastStartTime"></a>
The timestamp when you last started the application. Null until the application runs for the first time.
Type: Timestamp
Required: No

 ** roleArn **   <a name="m2-Type-ApplicationSummary-roleArn"></a>
The Amazon Resource Name (ARN) of the role associated with the application.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]|):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: No

 ** versionStatus **   <a name="m2-Type-ApplicationSummary-versionStatus"></a>
Indicates the status of the latest version of the application.
Type: String
Valid Values: `Creating | Available | Failed`
Required: No

## See Also
<a name="API_ApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/ApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/ApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/ApplicationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

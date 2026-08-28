---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Workteam.html
---

# Workteam
<a name="API_Workteam"></a>

Provides details about a labeling work team.

## Contents
<a name="API_Workteam_Contents"></a>

 ** Description **   <a name="sagemaker-Type-Workteam-Description"></a>
A description of the work team.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `.+`
Required: Yes

 ** MemberDefinitions **   <a name="sagemaker-Type-Workteam-MemberDefinitions"></a>
A list of `MemberDefinition` objects that contains objects that identify the workers that make up the work team.
Workforces can be created using Amazon Cognito or your own OIDC Identity Provider (IdP). For private workforces created using Amazon Cognito use `CognitoMemberDefinition`. For workforces created using your own OIDC identity provider (IdP) use `OidcMemberDefinition`.
Type: Array of [MemberDefinition](API_MemberDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** WorkteamArn **   <a name="sagemaker-Type-Workteam-WorkteamArn"></a>
The Amazon Resource Name (ARN) that identifies the work team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:workteam/.*`
Required: Yes

 ** WorkteamName **   <a name="sagemaker-Type-Workteam-WorkteamName"></a>
The name of the work team.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** CreateDate **   <a name="sagemaker-Type-Workteam-CreateDate"></a>
The date and time that the work team was created (timestamp).
Type: Timestamp
Required: No

 ** LastUpdatedDate **   <a name="sagemaker-Type-Workteam-LastUpdatedDate"></a>
The date and time that the work team was last updated (timestamp).
Type: Timestamp
Required: No

 ** NotificationConfiguration **   <a name="sagemaker-Type-Workteam-NotificationConfiguration"></a>
Configures SNS notifications of available or expiring work items for work teams.
Type: [NotificationConfiguration](API_NotificationConfiguration.md) object
Required: No

 ** ProductListingIds **   <a name="sagemaker-Type-Workteam-ProductListingIds"></a>
The Amazon Marketplace identifier for a vendor's work team.
Type: Array of strings
Required: No

 ** SubDomain **   <a name="sagemaker-Type-Workteam-SubDomain"></a>
The URI of the labeling job's user interface. Workers open this URI to start labeling your data objects.
Type: String
Required: No

 ** WorkerAccessConfiguration **   <a name="sagemaker-Type-Workteam-WorkerAccessConfiguration"></a>
Describes any access constraints that have been defined for Amazon S3 resources.
Type: [WorkerAccessConfiguration](API_WorkerAccessConfiguration.md) object
Required: No

 ** WorkforceArn **   <a name="sagemaker-Type-Workteam-WorkforceArn"></a>
The Amazon Resource Name (ARN) of the workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:workforce/.*`
Required: No

## See Also
<a name="API_Workteam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Workteam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Workteam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Workteam)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HubInfo.html
---

# HubInfo
<a name="API_HubInfo"></a>

Information about a hub.

## Contents
<a name="API_HubInfo_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-HubInfo-CreationTime"></a>
The date and time that the hub was created.
Type: Timestamp
Required: Yes

 ** HubArn **   <a name="sagemaker-Type-HubInfo-HubArn"></a>
The Amazon Resource Name (ARN) of the hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** HubName **   <a name="sagemaker-Type-HubInfo-HubName"></a>
The name of the hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** HubStatus **   <a name="sagemaker-Type-HubInfo-HubStatus"></a>
The status of the hub.
Type: String
Valid Values: `InService | Creating | Updating | Deleting | CreateFailed | UpdateFailed | DeleteFailed`
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-HubInfo-LastModifiedTime"></a>
The date and time that the hub was last modified.
Type: Timestamp
Required: Yes

 ** HubDescription **   <a name="sagemaker-Type-HubInfo-HubDescription"></a>
A description of the hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Pattern: `.*`
Required: No

 ** HubDisplayName **   <a name="sagemaker-Type-HubInfo-HubDisplayName"></a>
The display name of the hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** HubSearchKeywords **   <a name="sagemaker-Type-HubInfo-HubSearchKeywords"></a>
The searchable keywords for the hub.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[^A-Z]*`
Required: No

## See Also
<a name="API_HubInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HubInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HubInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HubInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

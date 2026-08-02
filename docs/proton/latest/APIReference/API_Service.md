---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_Service.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# Service
<a name="API_Service"></a>

Detailed data of an AWS Proton service resource.

## Contents
<a name="API_Service_Contents"></a>

 ** arn **   <a name="proton-Type-Service-arn"></a>
The Amazon Resource Name (ARN) of the service.
Type: String
Required: Yes

 ** createdAt **   <a name="proton-Type-Service-createdAt"></a>
The time when the service was created.
Type: Timestamp
Required: Yes

 ** lastModifiedAt **   <a name="proton-Type-Service-lastModifiedAt"></a>
The time when the service was last modified.
Type: Timestamp
Required: Yes

 ** name **   <a name="proton-Type-Service-name"></a>
The name of the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** spec **   <a name="proton-Type-Service-spec"></a>
The formatted specification that defines the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: Yes

 ** status **   <a name="proton-Type-Service-status"></a>
The status of the service.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED_CLEANUP_IN_PROGRESS | CREATE_FAILED_CLEANUP_COMPLETE | CREATE_FAILED_CLEANUP_FAILED | CREATE_FAILED | ACTIVE | DELETE_IN_PROGRESS | DELETE_FAILED | UPDATE_IN_PROGRESS | UPDATE_FAILED_CLEANUP_IN_PROGRESS | UPDATE_FAILED_CLEANUP_COMPLETE | UPDATE_FAILED_CLEANUP_FAILED | UPDATE_FAILED | UPDATE_COMPLETE_CLEANUP_FAILED`
Required: Yes

 ** templateName **   <a name="proton-Type-Service-templateName"></a>
The name of the service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** branchName **   <a name="proton-Type-Service-branchName"></a>
The name of the code repository branch that holds the code that's deployed in AWS Proton.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** description **   <a name="proton-Type-Service-description"></a>
A description of the service.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** pipeline **   <a name="proton-Type-Service-pipeline"></a>
The service pipeline detail data.
Type: [ServicePipeline](API_ServicePipeline.md) object
Required: No

 ** repositoryConnectionArn **   <a name="proton-Type-Service-repositoryConnectionArn"></a>
The Amazon Resource Name (ARN) of the repository connection. For more information, see [Setting up an AWS CodeStar connection](https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html#setting-up-vcontrol) in the * AWS Proton User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: No

 ** repositoryId **   <a name="proton-Type-Service-repositoryId"></a>
The ID of the source code repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** statusMessage **   <a name="proton-Type-Service-statusMessage"></a>
A service status message.
Type: String
Required: No

## See Also
<a name="API_Service_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/Service)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/Service)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/Service)

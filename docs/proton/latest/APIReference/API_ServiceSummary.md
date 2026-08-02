---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ServiceSummary.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ServiceSummary
<a name="API_ServiceSummary"></a>

Summary data of an AWS Proton service resource.

## Contents
<a name="API_ServiceSummary_Contents"></a>

 ** arn **   <a name="proton-Type-ServiceSummary-arn"></a>
The Amazon Resource Name (ARN) of the service.
Type: String
Required: Yes

 ** createdAt **   <a name="proton-Type-ServiceSummary-createdAt"></a>
The time when the service was created.
Type: Timestamp
Required: Yes

 ** lastModifiedAt **   <a name="proton-Type-ServiceSummary-lastModifiedAt"></a>
The time when the service was last modified.
Type: Timestamp
Required: Yes

 ** name **   <a name="proton-Type-ServiceSummary-name"></a>
The name of the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** status **   <a name="proton-Type-ServiceSummary-status"></a>
The status of the service.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED_CLEANUP_IN_PROGRESS | CREATE_FAILED_CLEANUP_COMPLETE | CREATE_FAILED_CLEANUP_FAILED | CREATE_FAILED | ACTIVE | DELETE_IN_PROGRESS | DELETE_FAILED | UPDATE_IN_PROGRESS | UPDATE_FAILED_CLEANUP_IN_PROGRESS | UPDATE_FAILED_CLEANUP_COMPLETE | UPDATE_FAILED_CLEANUP_FAILED | UPDATE_FAILED | UPDATE_COMPLETE_CLEANUP_FAILED`
Required: Yes

 ** templateName **   <a name="proton-Type-ServiceSummary-templateName"></a>
The name of the service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** description **   <a name="proton-Type-ServiceSummary-description"></a>
A description of the service.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** statusMessage **   <a name="proton-Type-ServiceSummary-statusMessage"></a>
A service status message.
Type: String
Required: No

## See Also
<a name="API_ServiceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ServiceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ServiceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ServiceSummary)

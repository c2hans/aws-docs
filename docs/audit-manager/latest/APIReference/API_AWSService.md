---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AWSService.html
---

# AWSService
<a name="API_AWSService"></a>

 An AWS service such as Amazon S3 or AWS CloudTrail.

For an example of how to find an AWS service name and how to define it in your assessment scope, see the following:
+  [Finding an AWS service name to use in your assessment scope](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetServicesInScope.html#API_GetServicesInScope_Example_2)
+  [Defining an AWS service name in your assessment scope](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetServicesInScope.html#API_GetServicesInScope_Example_3)

## Contents
<a name="API_AWSService_Contents"></a>

 ** serviceName **   <a name="auditmanager-Type-AWSService-serviceName"></a>
 The name of the AWS service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `^[a-zA-Z0-9-\s().]+$`
Required: No

## See Also
<a name="API_AWSService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AWSService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AWSService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AWSService)

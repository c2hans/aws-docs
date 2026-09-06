---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_EventResource.html
---

# EventResource
<a name="API_EventResource"></a>

 The AWS resource that emitted an event. AWS resource events and metrics are analyzed by DevOps Guru to find anomalous behavior and provide recommendations to improve your operational solutions.

## Contents
<a name="API_EventResource_Contents"></a>

 ** Arn **   <a name="DevOpsGuru-Type-EventResource-Arn"></a>
 The Amazon Resource Name (ARN) of the resource that emitted an event.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 2048.
Pattern: `^arn:aws[-a-z]*:[a-z0-9-]*:[a-z0-9-]*:\d{12}:.*$`
Required: No

 ** Name **   <a name="DevOpsGuru-Type-EventResource-Name"></a>
 The name of the resource that emitted an event.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `^.*$`
Required: No

 ** Type **   <a name="DevOpsGuru-Type-EventResource-Type"></a>
 The type of resource that emitted an event.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `^.*$`
Required: No

## See Also
<a name="API_EventResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/EventResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/EventResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/EventResource)

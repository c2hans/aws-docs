---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationOperationDescription.html
---

# ApplicationOperationDescription
<a name="API_ApplicationOperationDescription"></a>

Describes the application operation that initiated a snapshot operation. To get information about the application operation, use `DescribeApplicationOperation`.

## Contents
<a name="API_ApplicationOperationDescription_Contents"></a>

 ** ApplicationName **   <a name="APIReference-Type-ApplicationOperationDescription-ApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** ApplicationOperationId **   <a name="APIReference-Type-ApplicationOperationDescription-ApplicationOperationId"></a>
The operation ID of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_ApplicationOperationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationOperationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationOperationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationOperationDescription)

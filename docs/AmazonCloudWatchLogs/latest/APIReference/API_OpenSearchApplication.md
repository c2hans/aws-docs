---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_OpenSearchApplication.html
---

# OpenSearchApplication
<a name="API_OpenSearchApplication"></a>

This structure contains information about the OpenSearch Service application used for this integration. An OpenSearch Service application is the web application created by the integration with CloudWatch Logs. It hosts the vended logs dashboards.

## Contents
<a name="API_OpenSearchApplication_Contents"></a>

 ** applicationArn **   <a name="CWL-Type-OpenSearchApplication-applicationArn"></a>
The Amazon Resource Name (ARN) of the application.
Type: String
Required: No

 ** applicationEndpoint **   <a name="CWL-Type-OpenSearchApplication-applicationEndpoint"></a>
The endpoint of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^https://[\.\-_/#:A-Za-z0-9]+\.com$`
Required: No

 ** applicationId **   <a name="CWL-Type-OpenSearchApplication-applicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** status **   <a name="CWL-Type-OpenSearchApplication-status"></a>
This structure contains information about the status of this OpenSearch Service resource.
Type: [OpenSearchResourceStatus](API_OpenSearchResourceStatus.md) object
Required: No

## See Also
<a name="API_OpenSearchApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/OpenSearchApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/OpenSearchApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/OpenSearchApplication)

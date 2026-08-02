---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_OpenSearchResourceConfig.html
---

# OpenSearchResourceConfig
<a name="API_OpenSearchResourceConfig"></a>

This structure contains configuration details about an integration between CloudWatch Logs and OpenSearch Service.

## Contents
<a name="API_OpenSearchResourceConfig_Contents"></a>

 ** dashboardViewerPrincipals **   <a name="CWL-Type-OpenSearchResourceConfig-dashboardViewerPrincipals"></a>
Specify the ARNs of IAM roles and IAM users who you want to grant permission to for viewing the dashboards.
In addition to specifying these users here, you must also grant them the **CloudWatchOpenSearchDashboardAccess** IAM policy. For more information, see [IAM policies for users](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-UserRoles.html).
Type: Array of strings
Required: Yes

 ** dataSourceRoleArn **   <a name="CWL-Type-OpenSearchResourceConfig-dataSourceRoleArn"></a>
Specify the ARN of an IAM role that CloudWatch Logs will use to create the integration. This role must have the permissions necessary to access the OpenSearch Service collection to be able to create the dashboards. For more information about the permissions needed, see [Permissions that the integration needs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-CreateRole.html) in the CloudWatch Logs User Guide.
Type: String
Required: Yes

 ** retentionDays **   <a name="CWL-Type-OpenSearchResourceConfig-retentionDays"></a>
Specify how many days that you want the data derived by OpenSearch Service to be retained in the index that the dashboard refers to. This also sets the maximum time period that you can choose when viewing data in the dashboard. Choosing a longer time frame will incur additional costs.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 30.
Required: Yes

 ** applicationArn **   <a name="CWL-Type-OpenSearchResourceConfig-applicationArn"></a>
If you want to use an existing OpenSearch Service application for your integration with OpenSearch Service, specify it here. If you omit this, a new application will be created.
Type: String
Required: No

 ** kmsKeyArn **   <a name="CWL-Type-OpenSearchResourceConfig-kmsKeyArn"></a>
To have the vended dashboard data encrypted with AWS KMS instead of the CloudWatch Logs default encryption method, specify the ARN of the AWS KMS key that you want to use.
Type: String
Required: No

## See Also
<a name="API_OpenSearchResourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/OpenSearchResourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/OpenSearchResourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/OpenSearchResourceConfig)

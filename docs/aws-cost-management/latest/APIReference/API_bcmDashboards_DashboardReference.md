---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_DashboardReference.html
---

# DashboardReference
<a name="API_bcmDashboards_DashboardReference"></a>

Contains basic information about a dashboard, including its ARN, name, type, and timestamps.

## Contents
<a name="API_bcmDashboards_DashboardReference_Contents"></a>

 ** arn **   <a name="awscostmanagement-Type-bcmDashboards_DashboardReference-arn"></a>
The ARN of the referenced dashboard.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:dashboard/(\*|[-a-z0-9]+)`
Required: Yes

 ** createdAt **   <a name="awscostmanagement-Type-bcmDashboards_DashboardReference-createdAt"></a>
The timestamp when the dashboard was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="awscostmanagement-Type-bcmDashboards_DashboardReference-name"></a>
The name of the referenced dashboard.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `(?!.* {2})[a-zA-Z][a-zA-Z0-9 _-]{0,48}[a-zA-Z0-9_-]`
Required: Yes

 ** type **   <a name="awscostmanagement-Type-bcmDashboards_DashboardReference-type"></a>
The dashboard type. The following values are valid:
+  `CUSTOM` – A dashboard that you create and manage
+  `AWS_MANAGED` – A predefined, read-only dashboard that AWS authors and maintains
Type: String
Valid Values: `CUSTOM | AWS_MANAGED`
Required: Yes

 ** updatedAt **   <a name="awscostmanagement-Type-bcmDashboards_DashboardReference-updatedAt"></a>
The timestamp when the dashboard was last modified.
Type: Timestamp
Required: Yes

 ** description **   <a name="awscostmanagement-Type-bcmDashboards_DashboardReference-description"></a>
The description of the referenced dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!.* {2})[ a-zA-Z0-9.,!?;:@#$%&\-_/\\]*`
Required: No

## See Also
<a name="API_bcmDashboards_DashboardReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/DashboardReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/DashboardReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/DashboardReference)

---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_MonitorSummary.html
---

# MonitorSummary
<a name="API_MonitorSummary"></a>

Provides information about a monitor in Deadline Cloud.

## Contents
<a name="API_MonitorSummary_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-MonitorSummary-createdAt"></a>
The UNIX timestamp of the date and time that the monitor was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-MonitorSummary-createdBy"></a>
The user name of the person that created the monitor.
Type: String
Required: Yes

 ** displayName **   <a name="deadlinecloud-Type-MonitorSummary-displayName"></a>
The name of the monitor that displays on the Deadline Cloud console.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** identityCenterApplicationArn **   <a name="deadlinecloud-Type-MonitorSummary-identityCenterApplicationArn"></a>
The Amazon Resource Name that the IAM Identity Center assigned to the monitor when it was created.
Type: String
Required: Yes

 ** identityCenterInstanceArn **   <a name="deadlinecloud-Type-MonitorSummary-identityCenterInstanceArn"></a>
The Amazon Resource Name of the IAM Identity Center instance responsible for authenticating monitor users.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** monitorId **   <a name="deadlinecloud-Type-MonitorSummary-monitorId"></a>
The unique identifier for the monitor.
Type: String
Pattern: `monitor-[0-9a-f]{32}`
Required: Yes

 ** roleArn **   <a name="deadlinecloud-Type-MonitorSummary-roleArn"></a>
The Amazon Resource Name of the IAM role for the monitor. Users of the monitor use this role to access Deadline Cloud resources.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+`
Required: Yes

 ** subdomain **   <a name="deadlinecloud-Type-MonitorSummary-subdomain"></a>
The subdomain used for the monitor URL. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.
Type: String
Pattern: `[a-z0-9-]{1,100}`
Required: Yes

 ** url **   <a name="deadlinecloud-Type-MonitorSummary-url"></a>
The complete URL of the monitor. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.
Type: String
Required: Yes

 ** identityCenterRegion **   <a name="deadlinecloud-Type-MonitorSummary-identityCenterRegion"></a>
The Region where IAM Identity Center is enabled.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `[a-z0-9-]+`
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-MonitorSummary-updatedAt"></a>
The UNIX timestamp of the date and time that the monitor was last updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-MonitorSummary-updatedBy"></a>
The user name of the person that last updated the monitor.
Type: String
Required: No

## See Also
<a name="API_MonitorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/MonitorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/MonitorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/MonitorSummary)

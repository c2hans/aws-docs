---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_ServiceSummary.html
---

# ServiceSummary
<a name="API_ServiceSummary"></a>

Provides summary information for an AWS App Runner service.

This type contains limited information about a service. It doesn't include configuration details. It's returned by the [ListServices](https://docs.aws.amazon.com/apprunner/latest/api/API_ListServices.html) action. Complete service information is returned by the [CreateService](https://docs.aws.amazon.com/apprunner/latest/api/API_CreateService.html), [DescribeService](https://docs.aws.amazon.com/apprunner/latest/api/API_DescribeService.html), and [DeleteService](https://docs.aws.amazon.com/apprunner/latest/api/API_DeleteService.html) actions using the [Service](https://docs.aws.amazon.com/apprunner/latest/api/API_Service.html) type.

## Contents
<a name="API_ServiceSummary_Contents"></a>

 ** CreatedAt **   <a name="apprunner-Type-ServiceSummary-CreatedAt"></a>
The time when the App Runner service was created. It's in the Unix time stamp format.
Type: Timestamp
Required: No

 ** ServiceArn **   <a name="apprunner-Type-ServiceSummary-ServiceArn"></a>
The Amazon Resource Name (ARN) of this service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** ServiceId **   <a name="apprunner-Type-ServiceSummary-ServiceId"></a>
An ID that App Runner generated for this service. It's unique within the AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`
Required: No

 ** ServiceName **   <a name="apprunner-Type-ServiceSummary-ServiceName"></a>
The customer-provided service name.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Pattern: `[A-Za-z0-9][A-Za-z0-9-_]{3,39}`
Required: No

 ** ServiceUrl **   <a name="apprunner-Type-ServiceSummary-ServiceUrl"></a>
A subdomain URL that App Runner generated for this service. You can use this URL to access your service web application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

 ** Status **   <a name="apprunner-Type-ServiceSummary-Status"></a>
The current state of the App Runner service. These particular values mean the following.
+  `CREATE_FAILED` – The service failed to create. The failed service isn't usable, and still counts towards your service quota. To troubleshoot this failure, read the failure events and logs, change any parameters that need to be fixed, and rebuild your service using `UpdateService`.
+  `DELETE_FAILED` – The service failed to delete and can't be successfully recovered. Retry the service deletion call to ensure that all related resources are removed.
Type: String
Valid Values: `CREATE_FAILED | RUNNING | DELETED | DELETE_FAILED | PAUSED | OPERATION_IN_PROGRESS`
Required: No

 ** UpdatedAt **   <a name="apprunner-Type-ServiceSummary-UpdatedAt"></a>
The time when the App Runner service was last updated. It's in theUnix time stamp format.
Type: Timestamp
Required: No

## See Also
<a name="API_ServiceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/ServiceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/ServiceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/ServiceSummary)

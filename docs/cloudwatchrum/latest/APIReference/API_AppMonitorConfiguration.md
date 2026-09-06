---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_AppMonitorConfiguration.html
---

# AppMonitorConfiguration
<a name="API_AppMonitorConfiguration"></a>

This structure contains much of the configuration data for the app monitor.

## Contents
<a name="API_AppMonitorConfiguration_Contents"></a>

 ** AllowCookies **   <a name="cloudwatchrum-Type-AppMonitorConfiguration-AllowCookies"></a>
If you set this to `true`, the RUM web client sets two cookies, a session cookie and a user cookie. The cookies allow the RUM web client to collect data relating to the number of users an application has and the behavior of the application across a sequence of events. Cookies are stored in the top-level domain of the current page.
Type: Boolean
Required: No

 ** EnableXRay **   <a name="cloudwatchrum-Type-AppMonitorConfiguration-EnableXRay"></a>
If you set this to `true`, RUM enables AWS X-Ray tracing for the user sessions that RUM samples. RUM adds an X-Ray trace header to allowed HTTP requests. It also records an X-Ray segment for allowed HTTP requests. You can see traces and segments from these user sessions in the X-Ray console and the CloudWatch ServiceLens console. For more information, see [What is AWS X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
Type: Boolean
Required: No

 ** ExcludedPages **   <a name="cloudwatchrum-Type-AppMonitorConfiguration-ExcludedPages"></a>
A list of URLs in your website or application to exclude from RUM data collection.
You can't include both `ExcludedPages` and `IncludedPages` in the same operation.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 1260.
Pattern: `.*https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&*//=]*).*`
Required: No

 ** FavoritePages **   <a name="cloudwatchrum-Type-AppMonitorConfiguration-FavoritePages"></a>
A list of pages in your application that are to be displayed with a "favorite" icon in the CloudWatch RUM console.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** GuestRoleArn **   <a name="cloudwatchrum-Type-AppMonitorConfiguration-GuestRoleArn"></a>
The ARN of the guest IAM role that is attached to the Amazon Cognito identity pool that is used to authorize the sending of data to RUM.
It is possible that an app monitor does not have a value for `GuestRoleArn`. For example, this can happen when you use the console to create an app monitor and you allow CloudWatch RUM to create a new identity pool for Authorization. In this case, `GuestRoleArn` is not present in the [GetAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetAppMonitor.html) response because it is not stored by the service.
If this issue affects you, you can take one of the following steps:
+ Use the AWS Cloud Development Kit (AWS CDK) to create an identity pool and the associated IAM role, and use that for your app monitor.
+ Make a separate [GetIdentityPoolRoles](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetIdentityPoolRoles.html) call to Amazon Cognito to retrieve the `GuestRoleArn`.
Type: String
Pattern: `.*arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
Required: No

 ** IdentityPoolId **   <a name="cloudwatchrum-Type-AppMonitorConfiguration-IdentityPoolId"></a>
The ID of the Amazon Cognito identity pool that is used to authorize the sending of data to RUM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `.*[\w-]+:[0-9a-f-]+.*`
Required: No

 ** IncludedPages **   <a name="cloudwatchrum-Type-AppMonitorConfiguration-IncludedPages"></a>
If this app monitor is to collect data from only certain pages in your application, this structure lists those pages.
You can't include both `ExcludedPages` and `IncludedPages` in the same operation.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 1260.
Pattern: `.*https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&*//=]*).*`
Required: No

 ** SessionSampleRate **   <a name="cloudwatchrum-Type-AppMonitorConfiguration-SessionSampleRate"></a>
Specifies the portion of user sessions to use for RUM data collection. Choosing a higher portion gives you more data but also incurs more costs.
The range for this value is 0 to 1 inclusive. Setting this to 1 means that 100% of user sessions are sampled, and setting it to 0.1 means that 10% of user sessions are sampled.
If you omit this parameter, the default of 0.1 is used, and 10% of sessions will be sampled.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** Telemetries **   <a name="cloudwatchrum-Type-AppMonitorConfiguration-Telemetries"></a>
An array that lists the types of telemetry data that this app monitor is to collect.
+  `errors` indicates that RUM collects data about unhandled JavaScript errors raised by your application.
+  `performance` indicates that RUM collects performance data about how your application and its resources are loaded and rendered. This includes Core Web Vitals.
+  `http` indicates that RUM collects data about HTTP errors thrown by your application.
Type: Array of strings
Valid Values: `errors | performance | http`
Required: No

## See Also
<a name="API_AppMonitorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/AppMonitorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/AppMonitorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/AppMonitorConfiguration)

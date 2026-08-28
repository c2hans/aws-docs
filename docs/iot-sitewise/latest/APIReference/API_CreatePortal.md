---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreatePortal.html
---

# CreatePortal
<a name="API_CreatePortal"></a>

**Important**
The AWS IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025 . If you would like to use the AWS IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS IoT SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

Creates a portal, which can contain projects and dashboards. AWS IoT SiteWise Monitor uses IAM Identity Center or IAM to authenticate portal users and manage user permissions.

**Note**
Before you can sign in to a new portal, you must add at least one identity to that portal. For more information, see [Adding or removing portal administrators](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html#portal-change-admins) in the * AWS IoT SiteWise User Guide*.

## Request Syntax
<a name="API_CreatePortal_RequestSyntax"></a>

```
POST /portals HTTP/1.1
Content-type: application/json

{
   "alarms": {
      "alarmRoleArn": "{{string}}",
      "notificationLambdaArn": "{{string}}"
   },
   "clientToken": "{{string}}",
   "notificationSenderEmail": "{{string}}",
   "portalAuthMode": "{{string}}",
   "portalContactEmail": "{{string}}",
   "portalDescription": "{{string}}",
   "portalLogoImageFile": {
      "data": {{blob}},
      "type": "{{string}}"
   },
   "portalName": "{{string}}",
   "portalType": "{{string}}",
   "portalTypeConfiguration": {
      "{{string}}" : {
         "portalTools": [ "{{string}}" ]
      }
   },
   "roleArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePortal_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePortal_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [alarms](#API_CreatePortal_RequestSyntax) **   <a name="iotsitewise-CreatePortal-request-alarms"></a>
Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see [Monitoring with alarms](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html) in the * AWS IoT SiteWise Application Guide*.
Type: [Alarms](API_Alarms.md) object
Required: No

 ** [clientToken](#API_CreatePortal_RequestSyntax) **   <a name="iotsitewise-CreatePortal-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [notificationSenderEmail](#API_CreatePortal_RequestSyntax) **   <a name="iotsitewise-CreatePortal-request-notificationSenderEmail"></a>
The email address that sends alarm notifications.
If you use the [AWS IoT Events managed Lambda function](https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html) to manage your emails, you must [verify the sender email address in Amazon SES](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-\.\+]+@[a-zA-Z0-9_\-\.\+]+\.[a-zA-Z]{2,}$`
Required: No

 ** [portalAuthMode](#API_CreatePortal_RequestSyntax) **   <a name="iotsitewise-CreatePortal-request-portalAuthMode"></a>
The service to use to authenticate users to the portal. Choose from the following options:
+  `SSO` – The portal uses AWS IAM Identity Center to authenticate users and manage user permissions. Before you can create a portal that uses IAM Identity Center, you must enable IAM Identity Center. For more information, see [Enabling IAM Identity Center](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-get-started.html#mon-gs-sso) in the * AWS IoT SiteWise User Guide*. This option is only available in AWS Regions other than the China Regions.
+  `IAM` – The portal uses AWS Identity and Access Management to authenticate users and manage user permissions.
You can't change this value after you create a portal.
Default: `SSO`
Type: String
Valid Values: `IAM | SSO`
Required: No

 ** [portalContactEmail](#API_CreatePortal_RequestSyntax) **   <a name="iotsitewise-CreatePortal-request-portalContactEmail"></a>
The AWS administrator's contact email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-\.\+]+@[a-zA-Z0-9_\-\.\+]+\.[a-zA-Z]{2,}$`
Required: Yes

 ** [portalDescription](#API_CreatePortal_RequestSyntax) **   <a name="iotsitewise-CreatePortal-request-portalDescription"></a>
A description for the portal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [portalLogoImageFile](#API_CreatePortal_RequestSyntax) **   <a name="iotsitewise-CreatePortal-request-portalLogoImageFile"></a>
A logo image to display in the portal. Upload a square, high-resolution image. The image is displayed on a dark background.
Type: [ImageFile](API_ImageFile.md) object
Required: No

 ** [portalName](#API_CreatePortal_RequestSyntax) **   <a name="iotsitewise-CreatePortal-request-portalName"></a>
A friendly name for the portal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** [portalType](#API_CreatePortal_RequestSyntax) **   <a name="iotsitewise-CreatePortal-request-portalType"></a>
Define the type of portal. The value for AWS IoT SiteWise Monitor (Classic) is `SITEWISE_PORTAL_V1`. The value for AWS IoT SiteWise Monitor (AI-aware) is `SITEWISE_PORTAL_V2`.
Type: String
Valid Values: `SITEWISE_PORTAL_V1 | SITEWISE_PORTAL_V2`
Required: No

 ** [portalTypeConfiguration](#API_CreatePortal_RequestSyntax) **   <a name="iotsitewise-CreatePortal-request-portalTypeConfiguration"></a>
The configuration entry associated with the specific portal type. The value for AWS IoT SiteWise Monitor (Classic) is `SITEWISE_PORTAL_V1`. The value for AWS IoT SiteWise Monitor (AI-aware) is `SITEWISE_PORTAL_V2`.
Type: String to [PortalTypeEntry](API_PortalTypeEntry.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [roleArn](#API_CreatePortal_RequestSyntax) **   <a name="iotsitewise-CreatePortal-request-roleArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of a service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf. For more information, see [Using service roles for AWS IoT SiteWise Monitor](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.\+=,@]+$`
Required: Yes

 ** [tags](#API_CreatePortal_RequestSyntax) **   <a name="iotsitewise-CreatePortal-request-tags"></a>
A list of key-value pairs that contain metadata for the portal. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the * AWS IoT SiteWise User Guide*.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreatePortal_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "portalArn": "string",
   "portalId": "string",
   "portalStartUrl": "string",
   "portalStatus": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "state": "string"
   },
   "ssoApplicationId": "string"
}
```

## Response Elements
<a name="API_CreatePortal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [portalArn](#API_CreatePortal_ResponseSyntax) **   <a name="iotsitewise-CreatePortal-response-portalArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the portal, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:portal/${PortalId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [portalId](#API_CreatePortal_ResponseSyntax) **   <a name="iotsitewise-CreatePortal-response-portalId"></a>
The ID of the created portal.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [portalStartUrl](#API_CreatePortal_ResponseSyntax) **   <a name="iotsitewise-CreatePortal-response-portalStartUrl"></a>
The URL for the AWS IoT SiteWise Monitor portal. You can use this URL to access portals that use IAM Identity Center for authentication. For portals that use IAM for authentication, you must use the AWS IoT SiteWise console to get a URL that you can use to access the portal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^(http|https)\://\S+`

 ** [portalStatus](#API_CreatePortal_ResponseSyntax) **   <a name="iotsitewise-CreatePortal-response-portalStatus"></a>
The status of the portal, which contains a state (`CREATING` after successfully calling this operation) and any error message.
Type: [PortalStatus](API_PortalStatus.md) object

 ** [ssoApplicationId](#API_CreatePortal_ResponseSyntax) **   <a name="iotsitewise-CreatePortal-response-ssoApplicationId"></a>
The associated IAM Identity Center application ID, if the portal uses IAM Identity Center.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[!-~]*`

## Errors
<a name="API_CreatePortal_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_CreatePortal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreatePortal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreatePortal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreatePortal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreatePortal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreatePortal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreatePortal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreatePortal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreatePortal)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreatePortal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreatePortal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

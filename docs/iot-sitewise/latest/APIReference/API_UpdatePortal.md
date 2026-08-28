---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdatePortal.html
---

# UpdatePortal
<a name="API_UpdatePortal"></a>

**Important**
The AWS IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025 . If you would like to use the AWS IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS IoT SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

Updates an AWS IoT SiteWise Monitor portal.

## Request Syntax
<a name="API_UpdatePortal_RequestSyntax"></a>

```
PUT /portals/{{portalId}} HTTP/1.1
Content-type: application/json

{
   "alarms": {
      "alarmRoleArn": "{{string}}",
      "notificationLambdaArn": "{{string}}"
   },
   "clientToken": "{{string}}",
   "notificationSenderEmail": "{{string}}",
   "portalContactEmail": "{{string}}",
   "portalDescription": "{{string}}",
   "portalLogoImage": {
      "file": {
         "data": {{blob}},
         "type": "{{string}}"
      },
      "id": "{{string}}"
   },
   "portalName": "{{string}}",
   "portalType": "{{string}}",
   "portalTypeConfiguration": {
      "{{string}}" : {
         "portalTools": [ "{{string}}" ]
      }
   },
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePortal_RequestParameters"></a>

The request uses the following URI parameters.

 ** [portalId](#API_UpdatePortal_RequestSyntax) **   <a name="iotsitewise-UpdatePortal-request-uri-portalId"></a>
The ID of the portal to update.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Request Body
<a name="API_UpdatePortal_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [alarms](#API_UpdatePortal_RequestSyntax) **   <a name="iotsitewise-UpdatePortal-request-alarms"></a>
Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see [Monitoring with alarms](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html) in the * AWS IoT SiteWise Application Guide*.
Type: [Alarms](API_Alarms.md) object
Required: No

 ** [clientToken](#API_UpdatePortal_RequestSyntax) **   <a name="iotsitewise-UpdatePortal-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [notificationSenderEmail](#API_UpdatePortal_RequestSyntax) **   <a name="iotsitewise-UpdatePortal-request-notificationSenderEmail"></a>
The email address that sends alarm notifications.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-\.\+]+@[a-zA-Z0-9_\-\.\+]+\.[a-zA-Z]{2,}$`
Required: No

 ** [portalContactEmail](#API_UpdatePortal_RequestSyntax) **   <a name="iotsitewise-UpdatePortal-request-portalContactEmail"></a>
The AWS administrator's contact email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-\.\+]+@[a-zA-Z0-9_\-\.\+]+\.[a-zA-Z]{2,}$`
Required: Yes

 ** [portalDescription](#API_UpdatePortal_RequestSyntax) **   <a name="iotsitewise-UpdatePortal-request-portalDescription"></a>
A new description for the portal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [portalLogoImage](#API_UpdatePortal_RequestSyntax) **   <a name="iotsitewise-UpdatePortal-request-portalLogoImage"></a>
Contains an image that is one of the following:
+ An image file. Choose this option to upload a new image.
+ The ID of an existing image. Choose this option to keep an existing image.
Type: [Image](API_Image.md) object
Required: No

 ** [portalName](#API_UpdatePortal_RequestSyntax) **   <a name="iotsitewise-UpdatePortal-request-portalName"></a>
A new friendly name for the portal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** [portalType](#API_UpdatePortal_RequestSyntax) **   <a name="iotsitewise-UpdatePortal-request-portalType"></a>
Define the type of portal. The value for AWS IoT SiteWise Monitor (Classic) is `SITEWISE_PORTAL_V1`. The value for AWS IoT SiteWise Monitor (AI-aware) is `SITEWISE_PORTAL_V2`.
Type: String
Valid Values: `SITEWISE_PORTAL_V1 | SITEWISE_PORTAL_V2`
Required: No

 ** [portalTypeConfiguration](#API_UpdatePortal_RequestSyntax) **   <a name="iotsitewise-UpdatePortal-request-portalTypeConfiguration"></a>
The configuration entry associated with the specific portal type. The value for AWS IoT SiteWise Monitor (Classic) is `SITEWISE_PORTAL_V1`. The value for AWS IoT SiteWise Monitor (AI-aware) is `SITEWISE_PORTAL_V2`.
Type: String to [PortalTypeEntry](API_PortalTypeEntry.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [roleArn](#API_UpdatePortal_RequestSyntax) **   <a name="iotsitewise-UpdatePortal-request-roleArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of a service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf. For more information, see [Using service roles for AWS IoT SiteWise Monitor](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.\+=,@]+$`
Required: Yes

## Response Syntax
<a name="API_UpdatePortal_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "portalStatus": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "state": "string"
   }
}
```

## Response Elements
<a name="API_UpdatePortal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [portalStatus](#API_UpdatePortal_ResponseSyntax) **   <a name="iotsitewise-UpdatePortal-response-portalStatus"></a>
The status of the portal, which contains a state (`UPDATING` after successfully calling this operation) and any error message.
Type: [PortalStatus](API_PortalStatus.md) object

## Errors
<a name="API_UpdatePortal_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_UpdatePortal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/UpdatePortal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/UpdatePortal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/UpdatePortal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/UpdatePortal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/UpdatePortal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/UpdatePortal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/UpdatePortal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/UpdatePortal)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/UpdatePortal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/UpdatePortal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

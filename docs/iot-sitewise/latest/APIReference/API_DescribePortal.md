---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribePortal.html
---

# DescribePortal
<a name="API_DescribePortal"></a>

Retrieves information about a portal.

## Request Syntax
<a name="API_DescribePortal_RequestSyntax"></a>

```
GET /portals/{{portalId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribePortal_RequestParameters"></a>

The request uses the following URI parameters.

 ** [portalId](#API_DescribePortal_RequestSyntax) **   <a name="iotsitewise-DescribePortal-request-uri-portalId"></a>
The ID of the portal.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Request Body
<a name="API_DescribePortal_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribePortal_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "alarms": {
      "alarmRoleArn": "string",
      "notificationLambdaArn": "string"
   },
   "notificationSenderEmail": "string",
   "portalArn": "string",
   "portalAuthMode": "string",
   "portalClientId": "string",
   "portalContactEmail": "string",
   "portalCreationDate": number,
   "portalDescription": "string",
   "portalId": "string",
   "portalLastUpdateDate": number,
   "portalLogoImageLocation": {
      "id": "string",
      "url": "string"
   },
   "portalName": "string",
   "portalStartUrl": "string",
   "portalStatus": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "state": "string"
   },
   "portalType": "string",
   "portalTypeConfiguration": {
      "string" : {
         "portalTools": [ "string" ]
      }
   },
   "roleArn": "string"
}
```

## Response Elements
<a name="API_DescribePortal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [alarms](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-alarms"></a>
Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal.
Type: [Alarms](API_Alarms.md) object

 ** [notificationSenderEmail](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-notificationSenderEmail"></a>
The email address that sends alarm notifications.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-\.\+]+@[a-zA-Z0-9_\-\.\+]+\.[a-zA-Z]{2,}$`

 ** [portalArn](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the portal, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:portal/${PortalId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [portalAuthMode](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalAuthMode"></a>
The service to use to authenticate users to the portal.
Type: String
Valid Values: `IAM | SSO`

 ** [portalClientId](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalClientId"></a>
The IAM Identity Center application generated client ID (used with IAM Identity Center API operations). AWS IoT SiteWise includes `portalClientId` for only portals that use IAM Identity Center to authenticate users.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[!-~]*`

 ** [portalContactEmail](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalContactEmail"></a>
The AWS administrator's contact email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-\.\+]+@[a-zA-Z0-9_\-\.\+]+\.[a-zA-Z]{2,}$`

 ** [portalCreationDate](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalCreationDate"></a>
The date the portal was created, in Unix epoch time.
Type: Timestamp

 ** [portalDescription](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalDescription"></a>
The portal's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [portalId](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalId"></a>
The ID of the portal.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [portalLastUpdateDate](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalLastUpdateDate"></a>
The date the portal was last updated, in Unix epoch time.
Type: Timestamp

 ** [portalLogoImageLocation](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalLogoImageLocation"></a>
The portal's logo image, which is available at a URL.
Type: [ImageLocation](API_ImageLocation.md) object

 ** [portalName](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalName"></a>
The name of the portal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [portalStartUrl](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalStartUrl"></a>
The URL for the AWS IoT SiteWise Monitor portal. You can use this URL to access portals that use IAM Identity Center for authentication. For portals that use IAM for authentication, you must use the AWS IoT SiteWise console to get a URL that you can use to access the portal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^(http|https)\://\S+`

 ** [portalStatus](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalStatus"></a>
The current status of the portal, which contains a state and any error message.
Type: [PortalStatus](API_PortalStatus.md) object

 ** [portalType](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalType"></a>
Define the type of portal. The value for AWS IoT SiteWise Monitor (Classic) is `SITEWISE_PORTAL_V1`. The value for AWS IoT SiteWise Monitor (AI-aware) is `SITEWISE_PORTAL_V2`.
Type: String
Valid Values: `SITEWISE_PORTAL_V1 | SITEWISE_PORTAL_V2`

 ** [portalTypeConfiguration](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-portalTypeConfiguration"></a>
The configuration entry associated with the specific portal type. The value for AWS IoT SiteWise Monitor (Classic) is `SITEWISE_PORTAL_V1`. The value for AWS IoT SiteWise Monitor (AI-aware) is `SITEWISE_PORTAL_V2`.
Type: String to [PortalTypeEntry](API_PortalTypeEntry.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [roleArn](#API_DescribePortal_ResponseSyntax) **   <a name="iotsitewise-DescribePortal-response-roleArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf. For more information, see [Using service roles for AWS IoT SiteWise Monitor](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.\+=,@]+$`

## Errors
<a name="API_DescribePortal_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DescribePortal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribePortal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribePortal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribePortal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribePortal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribePortal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribePortal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribePortal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribePortal)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribePortal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribePortal)

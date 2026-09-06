---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAccessPolicy.html
---

# CreateAccessPolicy
<a name="API_CreateAccessPolicy"></a>

**Important**
The AWS IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025 . If you would like to use the AWS IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS IoT SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

Creates an access policy that grants the specified identity (IAM Identity Center user, IAM Identity Center group, or IAM user) access to the specified AWS IoT SiteWise Monitor portal or project resource.

**Note**
Support for access policies that use an SSO Group as the identity is not supported at this time.

## Request Syntax
<a name="API_CreateAccessPolicy_RequestSyntax"></a>

```
POST /access-policies HTTP/1.1
Content-type: application/json

{
   "accessPolicyIdentity": {
      "group": {
         "id": "{{string}}"
      },
      "iamRole": {
         "arn": "{{string}}"
      },
      "iamUser": {
         "arn": "{{string}}"
      },
      "user": {
         "id": "{{string}}"
      }
   },
   "accessPolicyPermission": "{{string}}",
   "accessPolicyResource": {
      "portal": {
         "id": "{{string}}"
      },
      "project": {
         "id": "{{string}}"
      }
   },
   "clientToken": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAccessPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAccessPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accessPolicyIdentity](#API_CreateAccessPolicy_RequestSyntax) **   <a name="iotsitewise-CreateAccessPolicy-request-accessPolicyIdentity"></a>
The identity for this access policy. Choose an IAM Identity Center user, an IAM Identity Center group, or an IAM user.
Type: [Identity](API_Identity.md) object
Required: Yes

 ** [accessPolicyPermission](#API_CreateAccessPolicy_RequestSyntax) **   <a name="iotsitewise-CreateAccessPolicy-request-accessPolicyPermission"></a>
The permission level for this access policy. Note that a project `ADMINISTRATOR` is also known as a project owner.
Type: String
Valid Values: `ADMINISTRATOR | VIEWER`
Required: Yes

 ** [accessPolicyResource](#API_CreateAccessPolicy_RequestSyntax) **   <a name="iotsitewise-CreateAccessPolicy-request-accessPolicyResource"></a>
The AWS IoT SiteWise Monitor resource for this access policy. Choose either a portal or a project.
Type: [Resource](API_Resource.md) object
Required: Yes

 ** [clientToken](#API_CreateAccessPolicy_RequestSyntax) **   <a name="iotsitewise-CreateAccessPolicy-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [tags](#API_CreateAccessPolicy_RequestSyntax) **   <a name="iotsitewise-CreateAccessPolicy-request-tags"></a>
A list of key-value pairs that contain metadata for the access policy. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the * AWS IoT SiteWise User Guide*.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateAccessPolicy_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "accessPolicyArn": "string",
   "accessPolicyId": "string"
}
```

## Response Elements
<a name="API_CreateAccessPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [accessPolicyArn](#API_CreateAccessPolicy_ResponseSyntax) **   <a name="iotsitewise-CreateAccessPolicy-response-accessPolicyArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the access policy, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:access-policy/${AccessPolicyId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [accessPolicyId](#API_CreateAccessPolicy_ResponseSyntax) **   <a name="iotsitewise-CreateAccessPolicy-response-accessPolicyId"></a>
The ID of the access policy.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

## Errors
<a name="API_CreateAccessPolicy_Errors"></a>

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
<a name="API_CreateAccessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreateAccessPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreateAccessPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreateAccessPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreateAccessPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreateAccessPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreateAccessPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreateAccessPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreateAccessPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreateAccessPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreateAccessPolicy)

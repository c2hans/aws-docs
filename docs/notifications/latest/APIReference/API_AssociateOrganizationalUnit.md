---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_AssociateOrganizationalUnit.html
---

# AssociateOrganizationalUnit
<a name="API_AssociateOrganizationalUnit"></a>

Associates an organizational unit with a notification configuration.

## Request Syntax
<a name="API_AssociateOrganizationalUnit_RequestSyntax"></a>

```
POST /organizational-units/associate/{{organizationalUnitId}} HTTP/1.1
Content-type: application/json

{
   "notificationConfigurationArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateOrganizationalUnit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [organizationalUnitId](#API_AssociateOrganizationalUnit_RequestSyntax) **   <a name="Notifications-AssociateOrganizationalUnit-request-uri-organizationalUnitId"></a>
The unique identifier of the organizational unit to associate.
Pattern: `(Root|r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: Yes

## Request Body
<a name="API_AssociateOrganizationalUnit_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [notificationConfigurationArn](#API_AssociateOrganizationalUnit_RequestSyntax) **   <a name="Notifications-AssociateOrganizationalUnit-request-notificationConfigurationArn"></a>
The Amazon Resource Name (ARN) of the notification configuration to associate with the organizational unit.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`
Required: Yes

## Response Syntax
<a name="API_AssociateOrganizationalUnit_ResponseSyntax"></a>

```
HTTP/1.1 201
```

## Response Elements
<a name="API_AssociateOrganizationalUnit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response with an empty HTTP body.

## Errors
<a name="API_AssociateOrganizationalUnit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** resourceId **
The resource ID that prompted the conflict error.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The ID of the resource that wasn't found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
 ** quotaCode **
The code for the service quota in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
 ** resourceId **
The ID of the resource that exceeds the service quota.
 ** resourceType **
The type of the resource that exceeds the service quota.
 ** serviceCode **
The code for the service quota exceeded in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service being throttled.
HTTP Status Code: 429

 ** ValidationException **
This exception is thrown when the notification event fails validation.
 ** fieldList **
The list of input fields that are invalid.
 ** reason **
The reason why your input is considered invalid.
HTTP Status Code: 400

## See Also
<a name="API_AssociateOrganizationalUnit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/AssociateOrganizationalUnit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/AssociateOrganizationalUnit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/AssociateOrganizationalUnit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/AssociateOrganizationalUnit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/AssociateOrganizationalUnit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/AssociateOrganizationalUnit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/AssociateOrganizationalUnit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/AssociateOrganizationalUnit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/AssociateOrganizationalUnit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/AssociateOrganizationalUnit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

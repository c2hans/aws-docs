---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_DisassociateUser.html
---

# DisassociateUser
<a name="API_DisassociateUser"></a>

Disassociates the user from an EC2 instance providing user-based subscriptions.

## Request Syntax
<a name="API_DisassociateUser_RequestSyntax"></a>

```
POST /user/DisassociateUser HTTP/1.1
Content-type: application/json

{
   "Domain": "{{string}}",
   "IdentityProvider": { ... },
   "InstanceId": "{{string}}",
   "InstanceUserArn": "{{string}}",
   "Username": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DisassociateUser_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DisassociateUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Domain](#API_DisassociateUser_RequestSyntax) **   <a name="licensemanagerusersubscriptions-DisassociateUser-request-Domain"></a>
The domain name of the Active Directory that contains information for the user to disassociate.
Type: String
Required: No

 ** [IdentityProvider](#API_DisassociateUser_RequestSyntax) **   <a name="licensemanagerusersubscriptions-DisassociateUser-request-IdentityProvider"></a>
An object that specifies details for the Active Directory identity provider.
Type: [IdentityProvider](API_IdentityProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [InstanceId](#API_DisassociateUser_RequestSyntax) **   <a name="licensemanagerusersubscriptions-DisassociateUser-request-InstanceId"></a>
The ID of the EC2 instance which provides user-based subscriptions.
Type: String
Required: No

 ** [InstanceUserArn](#API_DisassociateUser_RequestSyntax) **   <a name="licensemanagerusersubscriptions-DisassociateUser-request-InstanceUserArn"></a>
The Amazon Resource Name (ARN) of the user to disassociate from the EC2 instance.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-zA-Z0-9-\.]{1,510}/[a-zA-Z0-9-\.]{1,510}`
Required: No

 ** [Username](#API_DisassociateUser_RequestSyntax) **   <a name="licensemanagerusersubscriptions-DisassociateUser-request-Username"></a>
The user name from the Active Directory identity provider for the user.
Type: String
Required: No

## Response Syntax
<a name="API_DisassociateUser_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "InstanceUserSummary": {
      "AssociationDate": "string",
      "DisassociationDate": "string",
      "Domain": "string",
      "IdentityProvider": { ... },
      "InstanceId": "string",
      "InstanceUserArn": "string",
      "Status": "string",
      "StatusMessage": "string",
      "Username": "string"
   }
}
```

## Response Elements
<a name="API_DisassociateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceUserSummary](#API_DisassociateUser_ResponseSyntax) **   <a name="licensemanagerusersubscriptions-DisassociateUser-response-InstanceUserSummary"></a>
Metadata that describes the associate user operation.
Type: [InstanceUserSummary](API_InstanceUserSummary.md) object

## Errors
<a name="API_DisassociateUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request couldn't be completed because it conflicted with the current state of the resource.
HTTP Status Code: 500

 ** InternalServerException **
An exception occurred with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request failed because a service quota is exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because of request throttling. Retry the request.
HTTP Status Code: 400

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-user-subscriptions-2018-05-10/DisassociateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-user-subscriptions-2018-05-10/DisassociateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/DisassociateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-user-subscriptions-2018-05-10/DisassociateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/DisassociateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-user-subscriptions-2018-05-10/DisassociateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-user-subscriptions-2018-05-10/DisassociateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-user-subscriptions-2018-05-10/DisassociateUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-user-subscriptions-2018-05-10/DisassociateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/DisassociateUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager User Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-user-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

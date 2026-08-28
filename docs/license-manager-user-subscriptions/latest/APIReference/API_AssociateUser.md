---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_AssociateUser.html
---

# AssociateUser
<a name="API_AssociateUser"></a>

Associates the user to an EC2 instance to utilize user-based subscriptions.

**Note**
Your estimated bill for charges on the number of users and related costs will take 48 hours to appear for billing periods that haven't closed (marked as **Pending** billing status) in AWS Billing. For more information, see [Viewing your monthly charges](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/invoice.html) in the * AWS Billing User Guide*.

## Request Syntax
<a name="API_AssociateUser_RequestSyntax"></a>

```
POST /user/AssociateUser HTTP/1.1
Content-type: application/json

{
   "Domain": "{{string}}",
   "IdentityProvider": { ... },
   "InstanceId": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Username": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateUser_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AssociateUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Domain](#API_AssociateUser_RequestSyntax) **   <a name="licensemanagerusersubscriptions-AssociateUser-request-Domain"></a>
The domain name of the Active Directory that contains information for the user to associate.
Type: String
Required: No

 ** [IdentityProvider](#API_AssociateUser_RequestSyntax) **   <a name="licensemanagerusersubscriptions-AssociateUser-request-IdentityProvider"></a>
The identity provider for the user.
Type: [IdentityProvider](API_IdentityProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [InstanceId](#API_AssociateUser_RequestSyntax) **   <a name="licensemanagerusersubscriptions-AssociateUser-request-InstanceId"></a>
The ID of the EC2 instance that provides the user-based subscription.
Type: String
Required: Yes

 ** [Tags](#API_AssociateUser_RequestSyntax) **   <a name="licensemanagerusersubscriptions-AssociateUser-request-Tags"></a>
The tags that apply for the user association.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [Username](#API_AssociateUser_RequestSyntax) **   <a name="licensemanagerusersubscriptions-AssociateUser-request-Username"></a>
The user name from the identity provider.
Type: String
Required: Yes

## Response Syntax
<a name="API_AssociateUser_ResponseSyntax"></a>

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
<a name="API_AssociateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceUserSummary](#API_AssociateUser_ResponseSyntax) **   <a name="licensemanagerusersubscriptions-AssociateUser-response-InstanceUserSummary"></a>
Metadata that describes the associate user operation.
Type: [InstanceUserSummary](API_InstanceUserSummary.md) object

## Errors
<a name="API_AssociateUser_Errors"></a>

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
<a name="API_AssociateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-user-subscriptions-2018-05-10/AssociateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-user-subscriptions-2018-05-10/AssociateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/AssociateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-user-subscriptions-2018-05-10/AssociateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/AssociateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-user-subscriptions-2018-05-10/AssociateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-user-subscriptions-2018-05-10/AssociateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-user-subscriptions-2018-05-10/AssociateUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-user-subscriptions-2018-05-10/AssociateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/AssociateUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager User Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-user-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

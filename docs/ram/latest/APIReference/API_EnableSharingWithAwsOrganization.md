---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_EnableSharingWithAwsOrganization.html
---

# EnableSharingWithAwsOrganization
<a name="API_EnableSharingWithAwsOrganization"></a>

Enables resource sharing within your organization in AWS Organizations. This operation creates a service-linked role called `AWSServiceRoleForResourceAccessManager` that has the IAM managed policy named AWSResourceAccessManagerServiceRolePolicy attached. This role permits AWS RAM to retrieve information about the organization and its structure. This lets you share resources with all of the accounts in the calling account's organization by specifying the organization ID, or all of the accounts in an organizational unit (OU) by specifying the OU ID. Until you enable sharing within the organization, you can specify only individual AWS accounts, or for supported resource types, IAM roles and users.

You must call this operation from an IAM role or user in the organization's management account.

## Request Syntax
<a name="API_EnableSharingWithAwsOrganization_RequestSyntax"></a>

```
POST /enablesharingwithawsorganization HTTP/1.1
```

## URI Request Parameters
<a name="API_EnableSharingWithAwsOrganization_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_EnableSharingWithAwsOrganization_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_EnableSharingWithAwsOrganization_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "returnValue": boolean
}
```

## Response Elements
<a name="API_EnableSharingWithAwsOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [returnValue](#API_EnableSharingWithAwsOrganization_ResponseSyntax) **   <a name="ram-EnableSharingWithAwsOrganization-response-returnValue"></a>
A return value of `true` indicates that the request succeeded. A value of `false` indicates that the request failed.
Type: Boolean

## Errors
<a name="API_EnableSharingWithAwsOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedException **
The operation failed because the requested operation isn't permitted.
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

## See Also
<a name="API_EnableSharingWithAwsOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/EnableSharingWithAwsOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/EnableSharingWithAwsOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/EnableSharingWithAwsOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/EnableSharingWithAwsOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/EnableSharingWithAwsOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/EnableSharingWithAwsOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/EnableSharingWithAwsOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/EnableSharingWithAwsOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/EnableSharingWithAwsOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/EnableSharingWithAwsOrganization)

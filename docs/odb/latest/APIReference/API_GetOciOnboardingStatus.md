---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_GetOciOnboardingStatus.html
---

# GetOciOnboardingStatus
<a name="API_GetOciOnboardingStatus"></a>

Returns the tenancy activation link and onboarding status for your AWS account.

## Response Syntax
<a name="API_GetOciOnboardingStatus_ResponseSyntax"></a>

```
{
   "autonomousDatabaseOciIntegrationIamRoles": [
      {
         "awsIntegration": "string",
         "iamRoleArn": "string",
         "status": "string",
         "statusReason": "string"
      }
   ],
   "existingTenancyActivationLink": "string",
   "linkedOciCompartmentId": "string",
   "linkedOciTenancyId": "string",
   "newTenancyActivationLink": "string",
   "ociIdentityDomain": {
      "accountSetupCloudFormationUrl": "string",
      "ociIdentityDomainId": "string",
      "ociIdentityDomainResourceUrl": "string",
      "ociIdentityDomainUrl": "string",
      "status": "string",
      "statusReason": "string"
   },
   "status": "string",
   "subscriptionErrors": [
      {
         "errorMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetOciOnboardingStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autonomousDatabaseOciIntegrationIamRoles](#API_GetOciOnboardingStatus_ResponseSyntax) **   <a name="odb-GetOciOnboardingStatus-response-autonomousDatabaseOciIntegrationIamRoles"></a>
The list of AWS Identity and Access Management (IAM) service roles used for Autonomous Database integration with Oracle Cloud Infrastructure (OCI).
Type: Array of [OciIamRole](API_OciIamRole.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [existingTenancyActivationLink](#API_GetOciOnboardingStatus_ResponseSyntax) **   <a name="odb-GetOciOnboardingStatus-response-existingTenancyActivationLink"></a>
The existing OCI tenancy activation link for your AWS account.
Type: String

 ** [linkedOciCompartmentId](#API_GetOciOnboardingStatus_ResponseSyntax) **   <a name="odb-GetOciOnboardingStatus-response-linkedOciCompartmentId"></a>
The unique identifier of the Oracle Cloud Infrastructure (OCI) compartment that is linked to your AWS account.
Type: String

 ** [linkedOciTenancyId](#API_GetOciOnboardingStatus_ResponseSyntax) **   <a name="odb-GetOciOnboardingStatus-response-linkedOciTenancyId"></a>
The unique identifier of the Oracle Cloud Infrastructure (OCI) tenancy that is linked to your AWS account.
Type: String

 ** [newTenancyActivationLink](#API_GetOciOnboardingStatus_ResponseSyntax) **   <a name="odb-GetOciOnboardingStatus-response-newTenancyActivationLink"></a>
A new OCI tenancy activation link for your AWS account.
Type: String

 ** [ociIdentityDomain](#API_GetOciOnboardingStatus_ResponseSyntax) **   <a name="odb-GetOciOnboardingStatus-response-ociIdentityDomain"></a>
The Oracle Cloud Infrastructure (OCI) identity domain information in the onboarding status response.
Type: [OciIdentityDomain](API_OciIdentityDomain.md) object

 ** [status](#API_GetOciOnboardingStatus_ResponseSyntax) **   <a name="odb-GetOciOnboardingStatus-response-status"></a>

Type: String
Valid Values: `NOT_STARTED | PENDING_LINK_GENERATION | PENDING_CUSTOMER_ACTION | PENDING_INITIALIZATION | ACTIVATING | ACTIVE_IN_HOME_REGION | ACTIVE | ACTIVE_LIMITED | FAILED | PUBLIC_OFFER_UNSUPPORTED | SUSPENDED | CANCELED`

 ** [subscriptionErrors](#API_GetOciOnboardingStatus_ResponseSyntax) **   <a name="odb-GetOciOnboardingStatus-response-subscriptionErrors"></a>
The list of errors that occurred during the subscription process for your AWS account, if any.
Type: Array of [SubscriptionError](API_SubscriptionError.md) objects

## Errors
<a name="API_GetOciOnboardingStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_GetOciOnboardingStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/GetOciOnboardingStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/GetOciOnboardingStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/GetOciOnboardingStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/GetOciOnboardingStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/GetOciOnboardingStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/GetOciOnboardingStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/GetOciOnboardingStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/GetOciOnboardingStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/GetOciOnboardingStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/GetOciOnboardingStatus)

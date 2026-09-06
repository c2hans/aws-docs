---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetMembership.html
---

# GetMembership
<a name="API_GetMembership"></a>

Returns the attributes of a membership.

## Request Syntax
<a name="API_GetMembership_RequestSyntax"></a>

```
GET /v1/membership/{{membershipId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMembership_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipId](#API_GetMembership_RequestSyntax) **   <a name="securityir-GetMembership-request-uri-membershipId"></a>
Required element for GetMembership to identify the membership ID to query.
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `m-[a-z0-9]{10,32}`
Required: Yes

## Request Body
<a name="API_GetMembership_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMembership_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accountId": "string",
   "customerType": "string",
   "incidentResponseTeam": [
      {
         "communicationPreferences": [ "string" ],
         "email": "string",
         "jobTitle": "string",
         "name": "string"
      }
   ],
   "membershipAccountsConfigurations": {
      "coverEntireOrganization": boolean,
      "organizationalUnits": [ "string" ]
   },
   "membershipActivationTimestamp": number,
   "membershipArn": "string",
   "membershipDeactivationTimestamp": number,
   "membershipId": "string",
   "membershipName": "string",
   "membershipStatus": "string",
   "numberOfAccountsCovered": number,
   "optInFeatures": [
      {
         "featureName": "string",
         "isEnabled": boolean
      }
   ],
   "region": "string"
}
```

## Response Elements
<a name="API_GetMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountId](#API_GetMembership_ResponseSyntax) **   <a name="securityir-GetMembership-response-accountId"></a>
Response element for GetMembership that provides the account configured to manage the membership.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [customerType](#API_GetMembership_ResponseSyntax) **   <a name="securityir-GetMembership-response-customerType"></a>
Response element for GetMembership that provides the configured membership type. Options include ` Standalone | Organizations`.
Type: String
Valid Values: `Standalone | Organization`

 ** [incidentResponseTeam](#API_GetMembership_ResponseSyntax) **   <a name="securityir-GetMembership-response-incidentResponseTeam"></a>
Response element for GetMembership that provides the configured membership incident response team members.
Type: Array of [IncidentResponder](API_IncidentResponder.md) objects
Array Members: Minimum number of 2 items. Maximum number of 10 items.

 ** [membershipAccountsConfigurations](#API_GetMembership_ResponseSyntax) **   <a name="securityir-GetMembership-response-membershipAccountsConfigurations"></a>
The `membershipAccountsConfigurations` field contains the configuration details for member accounts within the AWS Organizations membership structure.
This field returns a structure containing information about:
+ Account configurations for member accounts
+ Membership settings and preferences
+ Account-level permissions and roles
Type: [MembershipAccountsConfigurations](API_MembershipAccountsConfigurations.md) object

 ** [membershipActivationTimestamp](#API_GetMembership_ResponseSyntax) **   <a name="securityir-GetMembership-response-membershipActivationTimestamp"></a>
Response element for GetMembership that provides the configured membership activation timestamp.
Type: Timestamp

 ** [membershipArn](#API_GetMembership_ResponseSyntax) **   <a name="securityir-GetMembership-response-membershipArn"></a>
Response element for GetMembership that provides the membership ARN.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 80.
Pattern: `arn:aws:security-ir:\w+?-\w+?-\d+:[0-9]{12}:membership/m-[a-z0-9]{10,32}`

 ** [membershipDeactivationTimestamp](#API_GetMembership_ResponseSyntax) **   <a name="securityir-GetMembership-response-membershipDeactivationTimestamp"></a>
Response element for GetMembership that provides the configured membership name deactivation timestamp.
Type: Timestamp

 ** [membershipId](#API_GetMembership_ResponseSyntax) **   <a name="securityir-GetMembership-response-membershipId"></a>
Response element for GetMembership that provides the queried membership ID.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `m-[a-z0-9]{10,32}`

 ** [membershipName](#API_GetMembership_ResponseSyntax) **   <a name="securityir-GetMembership-response-membershipName"></a>
Response element for GetMembership that provides the configured membership name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 50.

 ** [membershipStatus](#API_GetMembership_ResponseSyntax) **   <a name="securityir-GetMembership-response-membershipStatus"></a>
Response element for GetMembership that provides the current membership status.
Type: String
Valid Values: `Active | Cancelled | Terminated`

 ** [numberOfAccountsCovered](#API_GetMembership_ResponseSyntax) **   <a name="securityir-GetMembership-response-numberOfAccountsCovered"></a>
Response element for GetMembership that provides the number of accounts in the membership.
Type: Long

 ** [optInFeatures](#API_GetMembership_ResponseSyntax) **   <a name="securityir-GetMembership-response-optInFeatures"></a>
Response element for GetMembership that provides the if opt-in features have been enabled.
Type: Array of [OptInFeature](API_OptInFeature.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [region](#API_GetMembership_ResponseSyntax) **   <a name="securityir-GetMembership-response-region"></a>
Response element for GetMembership that provides the region configured to manage the membership.
Type: String
Valid Values: `af-south-1 | ap-east-1 | ap-east-2 | ap-northeast-1 | ap-northeast-2 | ap-northeast-3 | ap-south-1 | ap-south-2 | ap-southeast-1 | ap-southeast-2 | ap-southeast-3 | ap-southeast-4 | ap-southeast-5 | ap-southeast-6 | ap-southeast-7 | ca-central-1 | ca-west-1 | cn-north-1 | cn-northwest-1 | eu-central-1 | eu-central-2 | eu-north-1 | eu-south-1 | eu-south-2 | eu-west-1 | eu-west-2 | eu-west-3 | il-central-1 | me-central-1 | me-south-1 | mx-central-1 | sa-east-1 | us-east-1 | us-east-2 | us-west-1 | us-west-2`

## Errors
<a name="API_GetMembership_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** message **
The ID of the resource which lead to the access denial.
HTTP Status Code: 403

 ** ConflictException **
Returned when there is a conflict with the current state of the resource.
For UpdateResolverType, this error may occur when attempting to change an AWS-supported case to Self-managed, which is not supported.
 ** message **
The exception message.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **

 ** message **
The exception message.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
HTTP Status Code: 500

 ** InvalidTokenException **

 ** message **
The exception message.
HTTP Status Code: 423

 ** ResourceNotFoundException **

 ** message **
The exception message.
HTTP Status Code: 404

 ** SecurityIncidentResponseNotActiveException **

 ** message **
The exception message.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **

 ** message **
The exception message.
 ** quotaCode **
The code of the quota.
 ** resourceId **
The ID of the requested resource which lead to the service quota exception.
 ** resourceType **
The type of the requested resource which lead to the service quota exception.
 ** serviceCode **
The service code of the quota.
HTTP Status Code: 402

 ** ThrottlingException **

 ** message **
The exception message.
 ** quotaCode **
The quota code of the exception.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
 ** serviceCode **
The service code of the exception.
HTTP Status Code: 429

 ** ValidationException **
Returned when the request contains invalid parameters.
For UpdateResolverType, this error may occur when attempting an unsupported resolver type transition.
 ** fieldList **
The fields which lead to the exception.
 ** message **
The exception message.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/GetMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/GetMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/GetMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/GetMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/GetMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/GetMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/GetMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/GetMembership)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/GetMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/GetMembership)

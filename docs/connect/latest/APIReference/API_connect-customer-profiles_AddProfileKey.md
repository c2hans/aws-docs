---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_AddProfileKey.html
---

# AddProfileKey
<a name="API_connect-customer-profiles_AddProfileKey"></a>

Associates a new key value with a specific profile, such as a Contact Record ContactId.

A profile object can have a single unique key and any number of additional keys that can be used to identify the profile that it belongs to.

## Request Syntax
<a name="API_connect-customer-profiles_AddProfileKey_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/profiles/keys HTTP/1.1
Content-type: application/json

{
   "KeyName": "{{string}}",
   "ProfileId": "{{string}}",
   "Values": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_AddProfileKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_AddProfileKey_RequestSyntax) **   <a name="connect-connect-customer-profiles_AddProfileKey-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_AddProfileKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [KeyName](#API_connect-customer-profiles_AddProfileKey_RequestSyntax) **   <a name="connect-connect-customer-profiles_AddProfileKey-request-KeyName"></a>
A searchable identifier of a customer profile. The predefined keys you can use include: \_account, \_profileId, \_assetId, \_caseId, \_orderId, \_fullName, \_phone, \_email, \_ctrContactId, \_marketoLeadId, \_salesforceAccountId, \_salesforceContactId, \_salesforceAssetId, \_zendeskUserId, \_zendeskExternalId, \_zendeskTicketId, \_serviceNowSystemId, \_serviceNowIncidentId, \_segmentUserId, \_shopifyCustomerId, \_shopifyOrderId.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [ProfileId](#API_connect-customer-profiles_AddProfileKey_RequestSyntax) **   <a name="connect-connect-customer-profiles_AddProfileKey-request-ProfileId"></a>
The unique identifier of a customer profile.
Type: String
Pattern: `[a-f0-9]{32}`
Required: Yes

 ** [Values](#API_connect-customer-profiles_AddProfileKey_RequestSyntax) **   <a name="connect-connect-customer-profiles_AddProfileKey-request-Values"></a>
A list of key values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_AddProfileKey_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "KeyName": "string",
   "Values": [ "string" ]
}
```

## Response Elements
<a name="API_connect-customer-profiles_AddProfileKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyName](#API_connect-customer-profiles_AddProfileKey_ResponseSyntax) **   <a name="connect-connect-customer-profiles_AddProfileKey-response-KeyName"></a>
A searchable identifier of a customer profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [Values](#API_connect-customer-profiles_AddProfileKey_ResponseSyntax) **   <a name="connect-connect-customer-profiles_AddProfileKey-response-Values"></a>
A list of key values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_connect-customer-profiles_AddProfileKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## Examples
<a name="API_connect-customer-profiles_AddProfileKey_Examples"></a>

### Example
<a name="API_connect-customer-profiles_AddProfileKey_Example_1"></a>

This example illustrates one usage of AddProfileKey.

#### Sample Request
<a name="API_connect-customer-profiles_AddProfileKey_Example_1_Request"></a>

```
POST /v1/domains/ExampleDomainName/profiles/keys

Content-type: application/json
{
  "ProfileId": "3991a7d959d248bba82546b2dEXAMPLE",
  "KeyName": "_ctrContactId",
  "Values": ["valueOfTheContactId"]
}
```

#### Sample Response
<a name="API_connect-customer-profiles_AddProfileKey_Example_1_Response"></a>

```
Content-type: application/json
{
   "KeyName": "_ctrContactId",
   "Values": ["valueOfTheContactId"]
}
```

## See Also
<a name="API_connect-customer-profiles_AddProfileKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/AddProfileKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/AddProfileKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/AddProfileKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/AddProfileKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/AddProfileKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/AddProfileKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/AddProfileKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/AddProfileKey)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/AddProfileKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/AddProfileKey)

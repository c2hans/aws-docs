---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetCalculatedAttributeForProfile.html
---

# GetCalculatedAttributeForProfile
<a name="API_connect-customer-profiles_GetCalculatedAttributeForProfile"></a>

Retrieve a calculated attribute for a customer profile.

## Request Syntax
<a name="API_connect-customer-profiles_GetCalculatedAttributeForProfile_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/profile/{{ProfileId}}/calculated-attributes/{{CalculatedAttributeName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetCalculatedAttributeForProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CalculatedAttributeName](#API_connect-customer-profiles_GetCalculatedAttributeForProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeForProfile-request-uri-CalculatedAttributeName"></a>
The unique name of the calculated attribute.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

 ** [DomainName](#API_connect-customer-profiles_GetCalculatedAttributeForProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeForProfile-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [ProfileId](#API_connect-customer-profiles_GetCalculatedAttributeForProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeForProfile-request-uri-ProfileId"></a>
The unique identifier of a customer profile.
Pattern: `[a-f0-9]{32}`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetCalculatedAttributeForProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetCalculatedAttributeForProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CalculatedAttributeName": "string",
   "DisplayName": "string",
   "IsDataPartial": "string",
   "LastObjectTimestamp": number,
   "Value": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetCalculatedAttributeForProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CalculatedAttributeName](#API_connect-customer-profiles_GetCalculatedAttributeForProfile_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeForProfile-response-CalculatedAttributeName"></a>
The unique name of the calculated attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`

 ** [DisplayName](#API_connect-customer-profiles_GetCalculatedAttributeForProfile_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeForProfile-response-DisplayName"></a>
The display name of the calculated attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-\s]*$`

 ** [IsDataPartial](#API_connect-customer-profiles_GetCalculatedAttributeForProfile_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeForProfile-response-IsDataPartial"></a>
Indicates whether the calculated attribute’s value is based on partial data. If data is partial, it is set to true.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [LastObjectTimestamp](#API_connect-customer-profiles_GetCalculatedAttributeForProfile_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeForProfile-response-LastObjectTimestamp"></a>
The timestamp of the newest object included in the calculated attribute calculation.
Type: Timestamp

 ** [Value](#API_connect-customer-profiles_GetCalculatedAttributeForProfile_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeForProfile-response-Value"></a>
The value of the calculated attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_connect-customer-profiles_GetCalculatedAttributeForProfile_Errors"></a>

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

## See Also
<a name="API_connect-customer-profiles_GetCalculatedAttributeForProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetCalculatedAttributeForProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetCalculatedAttributeForProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetCalculatedAttributeForProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetCalculatedAttributeForProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetCalculatedAttributeForProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetCalculatedAttributeForProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetCalculatedAttributeForProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetCalculatedAttributeForProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetCalculatedAttributeForProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetCalculatedAttributeForProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

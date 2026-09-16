---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_BatchGetCalculatedAttributeForProfile.html
---

# BatchGetCalculatedAttributeForProfile
<a name="API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile"></a>

Fetch the possible attribute values given the attribute name.

## Request Syntax
<a name="API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/calculated-attributes/{{CalculatedAttributeName}}/batch-get-for-profiles HTTP/1.1
Content-type: application/json

{
   "ConditionOverrides": {
      "Range": {
         "End": {{number}},
         "Start": {{number}},
         "Unit": "{{string}}"
      }
   },
   "ProfileIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CalculatedAttributeName](#API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_BatchGetCalculatedAttributeForProfile-request-uri-CalculatedAttributeName"></a>
The unique name of the calculated attribute.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

 ** [DomainName](#API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_BatchGetCalculatedAttributeForProfile-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConditionOverrides](#API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_BatchGetCalculatedAttributeForProfile-request-ConditionOverrides"></a>
Overrides the condition block within the original calculated attribute definition.
Type: [ConditionOverrides](API_connect-customer-profiles_ConditionOverrides.md) object
Required: No

 ** [ProfileIds](#API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_BatchGetCalculatedAttributeForProfile-request-ProfileIds"></a>
List of unique identifiers for customer profiles to retrieve.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `[a-f0-9]{32}`
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CalculatedAttributeValues": [
      {
         "CalculatedAttributeName": "string",
         "DisplayName": "string",
         "IsDataPartial": "string",
         "LastObjectTimestamp": number,
         "ProfileId": "string",
         "Value": "string"
      }
   ],
   "ConditionOverrides": {
      "Range": {
         "End": number,
         "Start": number,
         "Unit": "string"
      }
   },
   "Errors": [
      {
         "Code": "string",
         "Message": "string",
         "ProfileId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CalculatedAttributeValues](#API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_ResponseSyntax) **   <a name="connect-connect-customer-profiles_BatchGetCalculatedAttributeForProfile-response-CalculatedAttributeValues"></a>
List of calculated attribute values retrieved.
Type: Array of [CalculatedAttributeValue](API_connect-customer-profiles_CalculatedAttributeValue.md) objects

 ** [ConditionOverrides](#API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_ResponseSyntax) **   <a name="connect-connect-customer-profiles_BatchGetCalculatedAttributeForProfile-response-ConditionOverrides"></a>
Overrides the condition block within the original calculated attribute definition.
Type: [ConditionOverrides](API_connect-customer-profiles_ConditionOverrides.md) object

 ** [Errors](#API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_ResponseSyntax) **   <a name="connect-connect-customer-profiles_BatchGetCalculatedAttributeForProfile-response-Errors"></a>
List of errors for calculated attribute values that could not be retrieved.
Type: Array of [BatchGetCalculatedAttributeForProfileError](API_connect-customer-profiles_BatchGetCalculatedAttributeForProfileError.md) objects

## Errors
<a name="API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_Errors"></a>

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
<a name="API_connect-customer-profiles_BatchGetCalculatedAttributeForProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/BatchGetCalculatedAttributeForProfile)

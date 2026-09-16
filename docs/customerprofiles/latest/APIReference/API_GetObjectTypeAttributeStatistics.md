---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetObjectTypeAttributeStatistics.html
---

# GetObjectTypeAttributeStatistics
<a name="API_connect-customer-profiles_GetObjectTypeAttributeStatistics"></a>

The GetObjectTypeAttributeValues API delivers statistical insights about attributes within a specific object type, but is exclusively available for domains with data store enabled. This API performs daily calculations to provide statistical information about your attribute values, helping you understand patterns and trends in your data. The statistical calculations are performed once per day, providing a consistent snapshot of your attribute data characteristics.

**Note**
You'll receive null values in two scenarios:
During the first period after enabling data vault (unless a calculation cycle occurs, which happens once daily).
For attributes that don't contain numeric values.

## Request Syntax
<a name="API_connect-customer-profiles_GetObjectTypeAttributeStatistics_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/object-types/{{ObjectTypeName}}/attributes/{{AttributeName}}/statistics HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetObjectTypeAttributeStatistics_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AttributeName](#API_connect-customer-profiles_GetObjectTypeAttributeStatistics_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetObjectTypeAttributeStatistics-request-uri-AttributeName"></a>
The attribute name.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** [DomainName](#API_connect-customer-profiles_GetObjectTypeAttributeStatistics_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetObjectTypeAttributeStatistics-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [ObjectTypeName](#API_connect-customer-profiles_GetObjectTypeAttributeStatistics_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetObjectTypeAttributeStatistics-request-uri-ObjectTypeName"></a>
The unique name of the domain object type.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetObjectTypeAttributeStatistics_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetObjectTypeAttributeStatistics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CalculatedAt": number,
   "Statistics": {
      "Average": number,
      "Maximum": number,
      "Minimum": number,
      "Percentiles": {
         "P25": number,
         "P5": number,
         "P50": number,
         "P75": number,
         "P95": number
      },
      "StandardDeviation": number
   }
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetObjectTypeAttributeStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CalculatedAt](#API_connect-customer-profiles_GetObjectTypeAttributeStatistics_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetObjectTypeAttributeStatistics-response-CalculatedAt"></a>
Time when this statistics was calculated.
Type: Timestamp

 ** [Statistics](#API_connect-customer-profiles_GetObjectTypeAttributeStatistics_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetObjectTypeAttributeStatistics-response-Statistics"></a>
The statistics.
Type: [GetObjectTypeAttributeStatisticsStats](API_connect-customer-profiles_GetObjectTypeAttributeStatisticsStats.md) object

## Errors
<a name="API_connect-customer-profiles_GetObjectTypeAttributeStatistics_Errors"></a>

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
<a name="API_connect-customer-profiles_GetObjectTypeAttributeStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetObjectTypeAttributeStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetObjectTypeAttributeStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetObjectTypeAttributeStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetObjectTypeAttributeStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetObjectTypeAttributeStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetObjectTypeAttributeStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetObjectTypeAttributeStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetObjectTypeAttributeStatistics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetObjectTypeAttributeStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetObjectTypeAttributeStatistics)

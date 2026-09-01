---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetCalculatedAttributeDefinition.html
---

# GetCalculatedAttributeDefinition
<a name="API_connect-customer-profiles_GetCalculatedAttributeDefinition"></a>

Provides more information on a calculated attribute definition for Customer Profiles.

## Request Syntax
<a name="API_connect-customer-profiles_GetCalculatedAttributeDefinition_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/calculated-attributes/{{CalculatedAttributeName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetCalculatedAttributeDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CalculatedAttributeName](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-request-uri-CalculatedAttributeName"></a>
The unique name of the calculated attribute.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

 ** [DomainName](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetCalculatedAttributeDefinition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AttributeDetails": {
      "Attributes": [
         {
            "Name": "string"
         }
      ],
      "Expression": "string"
   },
   "CalculatedAttributeName": "string",
   "Conditions": {
      "ObjectCount": number,
      "Range": {
         "TimestampFormat": "string",
         "TimestampSource": "string",
         "Unit": "string",
         "Value": number,
         "ValueRange": {
            "End": number,
            "Start": number
         }
      },
      "Threshold": {
         "Operator": "string",
         "Value": "string"
      }
   },
   "CreatedAt": number,
   "Description": "string",
   "DisplayName": "string",
   "Filter": {
      "Groups": [
         {
            "Dimensions": [
               {
                  "Attributes": {
                     "string" : {
                        "DimensionType": "string",
                        "Values": [ "string" ]
                     }
                  }
               }
            ],
            "Type": "string"
         }
      ],
      "Include": "string"
   },
   "LastUpdatedAt": number,
   "Readiness": {
      "Message": "string",
      "ProgressPercentage": number
   },
   "Statistic": "string",
   "Status": "string",
   "Tags": {
      "string" : "string"
   },
   "UseHistoricalData": boolean
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttributeDetails](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-response-AttributeDetails"></a>
Mathematical expression and a list of attribute items specified in that expression.
Type: [AttributeDetails](API_connect-customer-profiles_AttributeDetails.md) object

 ** [CalculatedAttributeName](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-response-CalculatedAttributeName"></a>
The unique name of the calculated attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`

 ** [Conditions](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-response-Conditions"></a>
The conditions including range, object count, and threshold for the calculated attribute.
Type: [Conditions](API_connect-customer-profiles_Conditions.md) object

 ** [CreatedAt](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-response-CreatedAt"></a>
The timestamp of when the calculated attribute definition was created.
Type: Timestamp

 ** [Description](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-response-Description"></a>
The description of the calculated attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [DisplayName](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-response-DisplayName"></a>
The display name of the calculated attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-\s]*$`

 ** [Filter](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-response-Filter"></a>
The filter assigned to this calculated attribute definition.
Type: [Filter](API_connect-customer-profiles_Filter.md) object

 ** [LastUpdatedAt](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-response-LastUpdatedAt"></a>
The timestamp of when the calculated attribute definition was most recently edited.
Type: Timestamp

 ** [Readiness](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-response-Readiness"></a>
Information indicating if the Calculated Attribute is ready for use by confirming all historical data has been processed and reflected.
Type: [Readiness](API_connect-customer-profiles_Readiness.md) object

 ** [Statistic](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-response-Statistic"></a>
The aggregation operation to perform for the calculated attribute.
Type: String
Valid Values: `FIRST_OCCURRENCE | LAST_OCCURRENCE | COUNT | SUM | MINIMUM | MAXIMUM | AVERAGE | MAX_OCCURRENCE | RECENT_OCCURRENCES`

 ** [Status](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-response-Status"></a>
Status of the Calculated Attribute creation (whether all historical data has been indexed).
Type: String
Valid Values: `PREPARING | IN_PROGRESS | COMPLETED | FAILED`

 ** [Tags](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

 ** [UseHistoricalData](#API_connect-customer-profiles_GetCalculatedAttributeDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetCalculatedAttributeDefinition-response-UseHistoricalData"></a>
Whether historical data ingested before the Calculated Attribute was created should be included in calculations.
Type: Boolean

## Errors
<a name="API_connect-customer-profiles_GetCalculatedAttributeDefinition_Errors"></a>

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
<a name="API_connect-customer-profiles_GetCalculatedAttributeDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetCalculatedAttributeDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetCalculatedAttributeDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetCalculatedAttributeDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetCalculatedAttributeDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetCalculatedAttributeDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetCalculatedAttributeDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetCalculatedAttributeDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetCalculatedAttributeDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetCalculatedAttributeDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetCalculatedAttributeDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

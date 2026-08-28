---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetSegmentDefinition.html
---

# GetSegmentDefinition
<a name="API_connect-customer-profiles_GetSegmentDefinition"></a>

Gets a segment definition from the domain.

## Request Syntax
<a name="API_connect-customer-profiles_GetSegmentDefinition_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/segment-definitions/{{SegmentDefinitionName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetSegmentDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetSegmentDefinition_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentDefinition-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [SegmentDefinitionName](#API_connect-customer-profiles_GetSegmentDefinition_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentDefinition-request-uri-SegmentDefinitionName"></a>
The unique name of the segment definition.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetSegmentDefinition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetSegmentDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": number,
   "Description": "string",
   "DisplayName": "string",
   "SegmentDefinitionArn": "string",
   "SegmentDefinitionName": "string",
   "SegmentGroups": {
      "Groups": [
         {
            "Dimensions": [
               { ... }
            ],
            "SourceSegments": [
               {
                  "SegmentDefinitionName": "string"
               }
            ],
            "SourceType": "string",
            "Type": "string"
         }
      ],
      "Include": "string"
   },
   "SegmentSort": {
      "Attributes": [
         {
            "DataType": "string",
            "Name": "string",
            "Order": "string",
            "Type": "string"
         }
      ]
   },
   "SegmentSqlQuery": "string",
   "SegmentType": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetSegmentDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_connect-customer-profiles_GetSegmentDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentDefinition-response-CreatedAt"></a>
The timestamp of when the segment definition was created.
Type: Timestamp

 ** [Description](#API_connect-customer-profiles_GetSegmentDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentDefinition-response-Description"></a>
The description of the segment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.

 ** [DisplayName](#API_connect-customer-profiles_GetSegmentDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentDefinition-response-DisplayName"></a>
The display name of the segment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [SegmentDefinitionArn](#API_connect-customer-profiles_GetSegmentDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentDefinition-response-SegmentDefinitionArn"></a>
The arn of the segment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [SegmentDefinitionName](#API_connect-customer-profiles_GetSegmentDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentDefinition-response-SegmentDefinitionName"></a>
The name of the segment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [SegmentGroups](#API_connect-customer-profiles_GetSegmentDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentDefinition-response-SegmentGroups"></a>
The segment criteria associated with this definition.
Type: [SegmentGroup](API_connect-customer-profiles_SegmentGroup.md) object

 ** [SegmentSort](#API_connect-customer-profiles_GetSegmentDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentDefinition-response-SegmentSort"></a>
The segment sort.
Type: [SegmentSort](API_connect-customer-profiles_SegmentSort.md) object

 ** [SegmentSqlQuery](#API_connect-customer-profiles_GetSegmentDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentDefinition-response-SegmentSqlQuery"></a>
The segment SQL query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50000.

 ** [SegmentType](#API_connect-customer-profiles_GetSegmentDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentDefinition-response-SegmentType"></a>
The segment type.
 Classic : Segments created using traditional SegmentGroup structure
 Enhanced : Segments created using SQL queries
Type: String
Valid Values: `CLASSIC | ENHANCED`

 ** [Tags](#API_connect-customer-profiles_GetSegmentDefinition_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentDefinition-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-customer-profiles_GetSegmentDefinition_Errors"></a>

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
<a name="API_connect-customer-profiles_GetSegmentDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetSegmentDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetSegmentDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetSegmentDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetSegmentDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetSegmentDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetSegmentDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetSegmentDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetSegmentDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetSegmentDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetSegmentDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

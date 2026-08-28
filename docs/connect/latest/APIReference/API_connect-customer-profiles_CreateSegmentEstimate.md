---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_CreateSegmentEstimate.html
---

# CreateSegmentEstimate
<a name="API_connect-customer-profiles_CreateSegmentEstimate"></a>

Creates a segment estimate query.

## Request Syntax
<a name="API_connect-customer-profiles_CreateSegmentEstimate_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/segment-estimates HTTP/1.1
Content-type: application/json

{
   "SegmentQuery": {
      "Groups": [
         {
            "Dimensions": [
               { ... }
            ],
            "SourceSegments": [
               {
                  "SegmentDefinitionName": "{{string}}"
               }
            ],
            "SourceType": "{{string}}",
            "Type": "{{string}}"
         }
      ],
      "Include": "{{string}}"
   },
   "SegmentSqlQuery": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_CreateSegmentEstimate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_CreateSegmentEstimate_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateSegmentEstimate-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_CreateSegmentEstimate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SegmentQuery](#API_connect-customer-profiles_CreateSegmentEstimate_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateSegmentEstimate-request-SegmentQuery"></a>
The segment query for calculating a segment estimate.
Type: [SegmentGroupStructure](API_connect-customer-profiles_SegmentGroupStructure.md) object
Required: No

 ** [SegmentSqlQuery](#API_connect-customer-profiles_CreateSegmentEstimate_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateSegmentEstimate-request-SegmentSqlQuery"></a>
The segment SQL query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50000.
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_CreateSegmentEstimate_ResponseSyntax"></a>

```
HTTP/1.1 {{StatusCode}}
Content-type: application/json

{
   "DomainName": "string",
   "EstimateId": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_CreateSegmentEstimate_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [StatusCode](#API_connect-customer-profiles_CreateSegmentEstimate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateSegmentEstimate-response-StatusCode"></a>
The status code for the response.

The following data is returned in JSON format by the service.

 ** [DomainName](#API_connect-customer-profiles_CreateSegmentEstimate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateSegmentEstimate-response-DomainName"></a>
The unique name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [EstimateId](#API_connect-customer-profiles_CreateSegmentEstimate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateSegmentEstimate-response-EstimateId"></a>
A unique identifier for the resource. The value can be passed to `GetSegmentEstimate` to retrieve the result of segment estimate status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_connect-customer-profiles_CreateSegmentEstimate_Errors"></a>

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
<a name="API_connect-customer-profiles_CreateSegmentEstimate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/CreateSegmentEstimate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/CreateSegmentEstimate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/CreateSegmentEstimate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/CreateSegmentEstimate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/CreateSegmentEstimate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/CreateSegmentEstimate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/CreateSegmentEstimate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/CreateSegmentEstimate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/CreateSegmentEstimate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/CreateSegmentEstimate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListAccountIntegrations.html
---

# ListAccountIntegrations
<a name="API_connect-customer-profiles_ListAccountIntegrations"></a>

Lists all of the integrations associated to a specific URI in the AWS account.

## Request Syntax
<a name="API_connect-customer-profiles_ListAccountIntegrations_RequestSyntax"></a>

```
POST /integrations?include-hidden={{IncludeHidden}}&max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "Uri": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_ListAccountIntegrations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IncludeHidden](#API_connect-customer-profiles_ListAccountIntegrations_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListAccountIntegrations-request-uri-IncludeHidden"></a>
Boolean to indicate if hidden integration should be returned. Defaults to `False`.

 ** [MaxResults](#API_connect-customer-profiles_ListAccountIntegrations_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListAccountIntegrations-request-uri-MaxResults"></a>
The maximum number of objects returned per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_ListAccountIntegrations_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListAccountIntegrations-request-uri-NextToken"></a>
The pagination token from the previous ListAccountIntegrations API call.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_connect-customer-profiles_ListAccountIntegrations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Uri](#API_connect-customer-profiles_ListAccountIntegrations_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListAccountIntegrations-request-Uri"></a>
The URI of the S3 bucket or any other type of data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_ListAccountIntegrations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "CreatedAt": number,
         "DomainName": "string",
         "EventTriggerNames": [ "string" ],
         "IsUnstructured": boolean,
         "LastUpdatedAt": number,
         "ObjectTypeName": "string",
         "ObjectTypeNames": {
            "string" : "string"
         },
         "RoleArn": "string",
         "Scope": "string",
         "Tags": {
            "string" : "string"
         },
         "Uri": "string",
         "WorkflowId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_ListAccountIntegrations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_connect-customer-profiles_ListAccountIntegrations_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListAccountIntegrations-response-Items"></a>
The list of ListAccountIntegration instances.
Type: Array of [ListIntegrationItem](API_connect-customer-profiles_ListIntegrationItem.md) objects

 ** [NextToken](#API_connect-customer-profiles_ListAccountIntegrations_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListAccountIntegrations-response-NextToken"></a>
The pagination token from the previous ListAccountIntegrations API call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_connect-customer-profiles_ListAccountIntegrations_Errors"></a>

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
<a name="API_connect-customer-profiles_ListAccountIntegrations_Examples"></a>

### Example
<a name="API_connect-customer-profiles_ListAccountIntegrations_Example_1"></a>

This example illustrates one usage of ListAccountIntegrations.

#### Sample Request
<a name="API_connect-customer-profiles_ListAccountIntegrations_Example_1_Request"></a>

```
POST /integrations?max-results=10&next-token={NextToken} HTTP/1.1

{
   "Uri": "arn:aws:sqs:us-east-1:123456789012:URIOfIntegration1"
}
```

#### Sample Response
<a name="API_connect-customer-profiles_ListAccountIntegrations_Example_1_Response"></a>

```
Content-type: application/json
{
   "Items": [
      {
         "CreatedAt": 1479249799770,
         "DomainName": "ExampleDomainName",
         "LastUpdatedAt": 1479249799770,
         "ObjectTypeName": "MyCustomObject",
         "Uri": "arn:aws:flow:us-east-1:123456789012:URIOfIntegration1"
      }
   ],
   "NextToken": "e17145a2-916b-42a2-b4d3-0267fEXAMPLE"
}
```

## See Also
<a name="API_connect-customer-profiles_ListAccountIntegrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/ListAccountIntegrations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/ListAccountIntegrations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListAccountIntegrations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/ListAccountIntegrations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListAccountIntegrations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/ListAccountIntegrations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/ListAccountIntegrations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/ListAccountIntegrations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/ListAccountIntegrations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListAccountIntegrations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjectTypes.html
---

# ListProfileObjectTypes
<a name="API_connect-customer-profiles_ListProfileObjectTypes"></a>

Lists all of the templates available within the service.

## Request Syntax
<a name="API_connect-customer-profiles_ListProfileObjectTypes_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/object-types?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_ListProfileObjectTypes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_ListProfileObjectTypes_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileObjectTypes-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [MaxResults](#API_connect-customer-profiles_ListProfileObjectTypes_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileObjectTypes-request-uri-MaxResults"></a>
The maximum number of objects returned per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_ListProfileObjectTypes_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileObjectTypes-request-uri-NextToken"></a>
Identifies the next page of results to return.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_connect-customer-profiles_ListProfileObjectTypes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_ListProfileObjectTypes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "CreatedAt": number,
         "Description": "string",
         "LastUpdatedAt": number,
         "MaxAvailableProfileObjectCount": number,
         "MaxProfileObjectCount": number,
         "ObjectTypeName": "string",
         "SourcePriority": number,
         "Tags": {
            "string" : "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_ListProfileObjectTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_connect-customer-profiles_ListProfileObjectTypes_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListProfileObjectTypes-response-Items"></a>
The list of ListProfileObjectTypes instances.
Type: Array of [ListProfileObjectTypeItem](API_connect-customer-profiles_ListProfileObjectTypeItem.md) objects

 ** [NextToken](#API_connect-customer-profiles_ListProfileObjectTypes_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListProfileObjectTypes-response-NextToken"></a>
Identifies the next page of results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_connect-customer-profiles_ListProfileObjectTypes_Errors"></a>

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
<a name="API_connect-customer-profiles_ListProfileObjectTypes_Examples"></a>

### Example
<a name="API_connect-customer-profiles_ListProfileObjectTypes_Example_1"></a>

This example illustrates one usage of ListProfileObjectTypes.

#### Sample Request
<a name="API_connect-customer-profiles_ListProfileObjectTypes_Example_1_Request"></a>

```
GET /domains/ExampleDomainName/object-types?max-results=10&next-token=nextToken HTTP/1.1
```

#### Sample Response
<a name="API_connect-customer-profiles_ListProfileObjectTypes_Example_1_Response"></a>

```
Content-type: application/json
{
   "Items": [
      {
         "CreatedAt": 1479249799770,
         "Description": "Example Description 1",
         "LastUpdatedAt": 1479249799770,
         "ObjectTypeName": "MyCustomObjectType",
         "SourcePriority": 2
      },
      {
         "CreatedAt": 147924988889,
         "Description": "Example Description 2",
         "LastUpdatedAt": 147924988889,
         "ObjectTypeName": "AnotherCustomObjectType"
      }
   ],
   "NextToken": "e17145a2-916b-42a2-b4d3-0267fEXAMPLE"
}
```

## See Also
<a name="API_connect-customer-profiles_ListProfileObjectTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/ListProfileObjectTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/ListProfileObjectTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListProfileObjectTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/ListProfileObjectTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListProfileObjectTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/ListProfileObjectTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/ListProfileObjectTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/ListProfileObjectTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/ListProfileObjectTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListProfileObjectTypes)

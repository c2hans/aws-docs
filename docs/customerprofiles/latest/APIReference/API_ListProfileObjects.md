---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjects.html
---

# ListProfileObjects
<a name="API_connect-customer-profiles_ListProfileObjects"></a>

Returns a list of objects associated with a profile of a given ProfileObjectType.

## Request Syntax
<a name="API_connect-customer-profiles_ListProfileObjects_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/profiles/objects?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "ObjectFilter": {
      "KeyName": "{{string}}",
      "Values": [ "{{string}}" ]
   },
   "ObjectTypeName": "{{string}}",
   "ProfileId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_ListProfileObjects_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_ListProfileObjects_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileObjects-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [MaxResults](#API_connect-customer-profiles_ListProfileObjects_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileObjects-request-uri-MaxResults"></a>
The maximum number of objects returned per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_ListProfileObjects_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileObjects-request-uri-NextToken"></a>
The pagination token from the previous call to ListProfileObjects.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_connect-customer-profiles_ListProfileObjects_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ObjectFilter](#API_connect-customer-profiles_ListProfileObjects_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileObjects-request-ObjectFilter"></a>
Applies a filter to the response to include profile objects with the specified index values.
Type: [ObjectFilter](API_connect-customer-profiles_ObjectFilter.md) object
Required: No

 ** [ObjectTypeName](#API_connect-customer-profiles_ListProfileObjects_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileObjects-request-ObjectTypeName"></a>
The name of the profile object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

 ** [ProfileId](#API_connect-customer-profiles_ListProfileObjects_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileObjects-request-ProfileId"></a>
The unique identifier of a customer profile.
Type: String
Pattern: `[a-f0-9]{32}`
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_ListProfileObjects_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Object": "string",
         "ObjectTypeName": "string",
         "ProfileObjectUniqueKey": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_ListProfileObjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_connect-customer-profiles_ListProfileObjects_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListProfileObjects-response-Items"></a>
The list of ListProfileObject instances.
Type: Array of [ListProfileObjectsItem](API_connect-customer-profiles_ListProfileObjectsItem.md) objects

 ** [NextToken](#API_connect-customer-profiles_ListProfileObjects_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListProfileObjects-response-NextToken"></a>
The pagination token from the previous call to ListProfileObjects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_connect-customer-profiles_ListProfileObjects_Errors"></a>

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
<a name="API_connect-customer-profiles_ListProfileObjects_Examples"></a>

### Example 1: List raw Contact Record objects
<a name="API_connect-customer-profiles_ListProfileObjects_Example_1"></a>

This example illustrates one usage of ListProfileObjects.

#### Sample Request
<a name="API_connect-customer-profiles_ListProfileObjects_Example_1_Request"></a>

```
POST /domains/ExampleDomainName/profiles/objects?max-results=10&next-token=nextToken
Content-type: application/json

{
   "ObjectTypeName": "MyCustomObject",
   "ProfileId": "3991a7d959d248bba82546b2dEXAMPLE"
}
```

#### Sample Response
<a name="API_connect-customer-profiles_ListProfileObjects_Example_1_Response"></a>

```
Content-type: application/json
{
   "Items": [
      {
         "Object": "{\"firstName\": \"John\",\n       \"lastName\": \"Smith\",\n       \"isAlive\": true,\n       \"age\": 27,\n       \"address\": {\"streetAddress\": \"21 2nd Street\",\"city\": \"New York\",\"state\": \"NY\",\"postalCode\": \"10021-3100\"},\n       \"phoneNumbers\": [{\"type\": \"home\",\"number\": \"212 555-1234\"},\n                        {\"type\": \"office\",\"number\": \"646 555-4567\"}],\n       \"children\": [],\n       \"spouse\": null}",
         "ObjectTypeName": "MyCustomObject",
         "ProfileObjectUniqueKey": "UniqueKeyOfTheProfileObject"
      },
      {
         "Object": "{\"firstName\": \"John\",\n       \"lastName\": \"Smith\",\n       \"isAlive\": true,\n       \"age\": 27,\n       \"address\": {\"streetAddress\": \"21 2nd Street\",\"city\": \"New York\",\"state\": \"NY\",\"postalCode\": \"10021-3100\"},\n       \"phoneNumbers\": [{\"type\": \"home\",\"number\": \"212 555-1234\"},\n                        {\"type\": \"office\",\"number\": \"646 555-4567\"}],\n       \"children\": [],\n       \"spouse\": null}",
         "ObjectTypeName": "MyCustomObject",
         "ProfileObjectUniqueKey": "UniqueKeyOfTheProfileObject"
      }
   ],
   "NextToken": "e17145a2-916b-42a2-b4d3-0267fEXAMPLE"
}
```

### Example 2: Filter Standard Asset Objects
<a name="API_connect-customer-profiles_ListProfileObjects_Example_2"></a>

This example illustrates one usage of ListProfileObjects.

#### Sample Request
<a name="API_connect-customer-profiles_ListProfileObjects_Example_2_Request"></a>

```
POST /domains/ExampleDomainName/profiles/objects?max-results=10&next-token=nextToken
Content-type: application/json

{
   "ObjectTypeName": "_asset",
   "ProfileId": "3991a7d959d248bba82546b2dEXAMPLE",
   "ObjectFilter": {
      "KeyName": "_assetId",
      "Values": [ "991a7d959d248bba82546b2dEXAMPLE2" ]
   }
}
```

#### Sample Response
<a name="API_connect-customer-profiles_ListProfileObjects_Example_2_Response"></a>

```
Content-type: application/json
{
   "Items": [
      {
         "Object": "{\"AssetId\": \"991a7d959d248bba82546b2dEXAMPLE2\",\n       \"AssetName\": \"MyAsset\",\n       \"SerialNumber\": \"123\",\n       \"ModelNumber\": \"1\",\n        \"ModelName\": \"name\",\n        \"ProductSKU\": \"21\",\n        \"PurchaseDate\": \"07-04-2021\",\n        \"UsageEndDate\": \"07-04-2021\",\n        \"Status\": \"Delivered\",\n        \"Price\": \"10\",\n        \"Quantity\": \"5\",\n        \"Description\": \"This is an asset\",\n        \"Location\": \"Office\",\n        \"AdditionalInformation\": \"None\",\n        \"DataSource\": \"Salesforce-Asset\",\n        \"Attributes\": {} }",
         "ObjectTypeName": "_asset",
         "ProfileObjectUniqueKey": "UniqueKeyOfTheProfileObject"
      }
   ],
   "NextToken": "e17145a2-916b-42a2-b4d3-0267fEXAMPLE"
}
```

## See Also
<a name="API_connect-customer-profiles_ListProfileObjects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/ListProfileObjects)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/ListProfileObjects)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListProfileObjects)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/ListProfileObjects)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListProfileObjects)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/ListProfileObjects)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/ListProfileObjects)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/ListProfileObjects)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/ListProfileObjects)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListProfileObjects)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

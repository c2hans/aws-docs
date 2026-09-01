---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_BatchPutProfileObject.html
---

# BatchPutProfileObject
<a name="API_connect-customer-profiles_BatchPutProfileObject"></a>

Adds multiple profile objects to a domain of a given ObjectType in a single API call.

When adding a specific profile object, like a Contact Record, an inferred profile can get created if it is not mapped to an existing profile. The resulting profile will only have a phone number populated in the standard ProfileObject. Any additional Contact Records with the same phone number will be mapped to the same inferred profile.

When a ProfileObject is created and if a ProfileObjectType already exists for the ProfileObject, it will provide data to a standard profile depending on the ProfileObjectType definition.

BatchPutProfileObject needs an ObjectType, which can be created using PutProfileObjectType.

## Request Syntax
<a name="API_connect-customer-profiles_BatchPutProfileObject_RequestSyntax"></a>

```
PUT /domains/{{DomainName}}/profiles/objects/batch-put-profile-object HTTP/1.1
Content-type: application/json

{
   "Items": [
      {
         "Id": "{{string}}",
         "Object": "{{string}}"
      }
   ],
   "ObjectTypeName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_BatchPutProfileObject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_BatchPutProfileObject_RequestSyntax) **   <a name="connect-connect-customer-profiles_BatchPutProfileObject-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_BatchPutProfileObject_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Items](#API_connect-customer-profiles_BatchPutProfileObject_RequestSyntax) **   <a name="connect-connect-customer-profiles_BatchPutProfileObject-request-Items"></a>
A list of items to add to the domain.
Type: Array of [BatchPutProfileObjectRequestItem](API_connect-customer-profiles_BatchPutProfileObjectRequestItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [ObjectTypeName](#API_connect-customer-profiles_BatchPutProfileObject_RequestSyntax) **   <a name="connect-connect-customer-profiles_BatchPutProfileObject-request-ObjectTypeName"></a>
The name of the profile object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_BatchPutProfileObject_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Failed": [
      {
         "Code": number,
         "Id": "string",
         "Message": "string"
      }
   ],
   "Successful": [
      {
         "Id": "string",
         "ProfileObjectUniqueKey": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-customer-profiles_BatchPutProfileObject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_connect-customer-profiles_BatchPutProfileObject_ResponseSyntax) **   <a name="connect-connect-customer-profiles_BatchPutProfileObject-response-Failed"></a>
A list of items that failed to be added to the domain.
Type: Array of [BatchPutProfileObjectErrorItem](API_connect-customer-profiles_BatchPutProfileObjectErrorItem.md) objects

 ** [Successful](#API_connect-customer-profiles_BatchPutProfileObject_ResponseSyntax) **   <a name="connect-connect-customer-profiles_BatchPutProfileObject-response-Successful"></a>
A list of items that were successfully added to the domain.
Type: Array of [BatchPutProfileObjectResponseItem](API_connect-customer-profiles_BatchPutProfileObjectResponseItem.md) objects

## Errors
<a name="API_connect-customer-profiles_BatchPutProfileObject_Errors"></a>

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
<a name="API_connect-customer-profiles_BatchPutProfileObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/BatchPutProfileObject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/BatchPutProfileObject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/BatchPutProfileObject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/BatchPutProfileObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/BatchPutProfileObject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/BatchPutProfileObject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/BatchPutProfileObject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/BatchPutProfileObject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/BatchPutProfileObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/BatchPutProfileObject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

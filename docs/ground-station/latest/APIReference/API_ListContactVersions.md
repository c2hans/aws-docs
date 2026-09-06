---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListContactVersions.html
---

# ListContactVersions
<a name="API_ListContactVersions"></a>

Returns a list of versions for a specified contact.

## Request Syntax
<a name="API_ListContactVersions_RequestSyntax"></a>

```
GET /contact/{{contactId}}/versions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListContactVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [contactId](#API_ListContactVersions_RequestSyntax) **   <a name="groundstation-ListContactVersions-request-uri-contactId"></a>
UUID of a contact.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [maxResults](#API_ListContactVersions_RequestSyntax) **   <a name="groundstation-ListContactVersions-request-uri-maxResults"></a>
Maximum number of contact versions returned.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListContactVersions_RequestSyntax) **   <a name="groundstation-ListContactVersions-request-uri-nextToken"></a>
Next token returned in the request of a previous `ListContactVersions` call. Used to get the next page of results.
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

## Request Body
<a name="API_ListContactVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListContactVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "contactVersionsList": [
      {
         "activated": number,
         "created": number,
         "failureCodes": [ "string" ],
         "failureMessage": "string",
         "lastUpdated": number,
         "status": "string",
         "superseded": number,
         "versionId": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListContactVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [contactVersionsList](#API_ListContactVersions_ResponseSyntax) **   <a name="groundstation-ListContactVersions-response-contactVersionsList"></a>
List of contact versions.
Type: Array of [ContactVersion](API_ContactVersion.md) objects

 ** [nextToken](#API_ListContactVersions_ResponseSyntax) **   <a name="groundstation-ListContactVersions-response-nextToken"></a>
Next token to be used in a subsequent `ListContactVersions` call to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

## Errors
<a name="API_ListContactVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyException **
Dependency encountered an error.
 ** parameterName **
Name of the parameter that caused the exception.
HTTP Status Code: 531

 ** InvalidParameterException **
One or more parameters are not valid.
 ** parameterName **
Name of the invalid parameter.
HTTP Status Code: 431

 ** ResourceNotFoundException **
Resource was not found.
HTTP Status Code: 434

## See Also
<a name="API_ListContactVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/ListContactVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/ListContactVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ListContactVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/ListContactVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ListContactVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/ListContactVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/ListContactVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/ListContactVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/ListContactVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ListContactVersions)

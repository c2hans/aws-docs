---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetSubdomains.html
---

# GetSubdomains
<a name="API_GetSubdomains"></a>

Returns information about one or more of your Lightsail subdomains.

When you don't specify a subdomain, the response lists your top-level subdomains, and each top-level subdomain includes its nested subdomains.

The results are paginated. To get the next page of results, use the `pageToken` parameter.

## Request Syntax
<a name="API_GetSubdomains_RequestSyntax"></a>

```
{
   "pageToken": "{{string}}",
   "subdomainName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSubdomains_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pageToken](#API_GetSubdomains_RequestSyntax) **   <a name="Lightsail-GetSubdomains-request-pageToken"></a>
The token to advance to the next page of results from your request.
To get a page token, perform an initial `GetSubdomains` request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.
Type: String
Required: No

 ** [subdomainName](#API_GetSubdomains_RequestSyntax) **   <a name="Lightsail-GetSubdomains-request-subdomainName"></a>
The subdomain for which to return information (for example, `mysite` or `blog.mysite`), not its web address.
When omitted, the response includes all of your subdomains.
You can't specify this parameter together with the `pageToken` parameter.
Type: String
Required: No

## Response Syntax
<a name="API_GetSubdomains_ResponseSyntax"></a>

```
{
   "nextPageToken": "string",
   "subdomains": [
      {
         "arn": "string",
         "attachedResource": {
            "arn": "string",
            "attachedAt": number,
            "name": "string"
         },
         "attachingResource": {
            "arn": "string",
            "attachedAt": number,
            "name": "string"
         },
         "children": [
            "Subdomain"
         ],
         "createdAt": number,
         "depth": number,
         "fqdn": "string",
         "location": {
            "availabilityZone": "string",
            "regionName": "string"
         },
         "parentFqdn": "string",
         "state": "string",
         "subdomainName": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetSubdomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextPageToken](#API_GetSubdomains_ResponseSyntax) **   <a name="Lightsail-GetSubdomains-response-nextPageToken"></a>
The token to advance to the next page of results from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another `GetSubdomains` request and specify the next page token using the `pageToken` parameter.
Type: String

 ** [subdomains](#API_GetSubdomains_ResponseSyntax) **   <a name="Lightsail-GetSubdomains-response-subdomains"></a>
An array of objects that describe your subdomains.
Type: Array of [Subdomain](API_Subdomain.md) objects

## Errors
<a name="API_GetSubdomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_GetSubdomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetSubdomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetSubdomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetSubdomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetSubdomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetSubdomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetSubdomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetSubdomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetSubdomains)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetSubdomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetSubdomains)

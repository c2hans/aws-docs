---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetDistributions.html
---

# GetDistributions
<a name="API_GetDistributions"></a>

Returns information about one or more of your Amazon Lightsail content delivery network (CDN) distributions.

## Request Syntax
<a name="API_GetDistributions_RequestSyntax"></a>

```
{
   "distributionName": "{{string}}",
   "pageToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDistributions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [distributionName](#API_GetDistributions_RequestSyntax) **   <a name="Lightsail-GetDistributions-request-distributionName"></a>
The name of the distribution for which to return information.
When omitted, the response includes all of your distributions in the AWS Region where the request is made.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [pageToken](#API_GetDistributions_RequestSyntax) **   <a name="Lightsail-GetDistributions-request-pageToken"></a>
The token to advance to the next page of results from your request.
To get a page token, perform an initial `GetDistributions` request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.
Type: String
Required: No

## Response Syntax
<a name="API_GetDistributions_ResponseSyntax"></a>

```
{
   "distributions": [
      {
         "ableToUpdateBundle": boolean,
         "alternativeDomainNames": [ "string" ],
         "arn": "string",
         "bundleId": "string",
         "cacheBehaviors": [
            {
               "behavior": "string",
               "path": "string"
            }
         ],
         "cacheBehaviorSettings": {
            "allowedHTTPMethods": "string",
            "cachedHTTPMethods": "string",
            "defaultTTL": number,
            "forwardedCookies": {
               "cookiesAllowList": [ "string" ],
               "option": "string"
            },
            "forwardedHeaders": {
               "headersAllowList": [ "string" ],
               "option": "string"
            },
            "forwardedQueryStrings": {
               "option": boolean,
               "queryStringsAllowList": [ "string" ]
            },
            "maximumTTL": number,
            "minimumTTL": number
         },
         "certificateName": "string",
         "createdAt": number,
         "defaultCacheBehavior": {
            "behavior": "string"
         },
         "domainName": "string",
         "ipAddressType": "string",
         "isEnabled": boolean,
         "location": {
            "availabilityZone": "string",
            "regionName": "string"
         },
         "name": "string",
         "origin": {
            "ipAddressType": "string",
            "name": "string",
            "protocolPolicy": "string",
            "regionName": "string",
            "resourceType": "string",
            "responseTimeout": number
         },
         "originPublicDNS": "string",
         "resourceType": "string",
         "status": "string",
         "supportCode": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "viewerMinimumTlsProtocolVersion": "string"
      }
   ],
   "nextPageToken": "string"
}
```

## Response Elements
<a name="API_GetDistributions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [distributions](#API_GetDistributions_ResponseSyntax) **   <a name="Lightsail-GetDistributions-response-distributions"></a>
An array of objects that describe your distributions.
Type: Array of [LightsailDistribution](API_LightsailDistribution.md) objects

 ** [nextPageToken](#API_GetDistributions_ResponseSyntax) **   <a name="Lightsail-GetDistributions-response-nextPageToken"></a>
The token to advance to the next page of results from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another `GetDistributions` request and specify the next page token using the `pageToken` parameter.
Type: String

## Errors
<a name="API_GetDistributions_Errors"></a>

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

 ** OperationFailureException **
Lightsail throws this exception when an operation fails to execute.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_GetDistributions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetDistributions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetDistributions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetDistributions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetDistributions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetDistributions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetDistributions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetDistributions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetDistributions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetDistributions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetDistributions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

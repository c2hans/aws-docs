---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateDistribution.html
---

# CreateDistribution
<a name="API_CreateDistribution"></a>

Creates an Amazon Lightsail content delivery network (CDN) distribution.

A distribution is a globally distributed network of caching servers that improve the performance of your website or web application hosted on a Lightsail instance. For more information, see [Content delivery networks in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-content-delivery-network-distributions).

## Request Syntax
<a name="API_CreateDistribution_RequestSyntax"></a>

```
{
   "bundleId": "{{string}}",
   "cacheBehaviors": [
      {
         "behavior": "{{string}}",
         "path": "{{string}}"
      }
   ],
   "cacheBehaviorSettings": {
      "allowedHTTPMethods": "{{string}}",
      "cachedHTTPMethods": "{{string}}",
      "defaultTTL": {{number}},
      "forwardedCookies": {
         "cookiesAllowList": [ "{{string}}" ],
         "option": "{{string}}"
      },
      "forwardedHeaders": {
         "headersAllowList": [ "{{string}}" ],
         "option": "{{string}}"
      },
      "forwardedQueryStrings": {
         "option": {{boolean}},
         "queryStringsAllowList": [ "{{string}}" ]
      },
      "maximumTTL": {{number}},
      "minimumTTL": {{number}}
   },
   "certificateName": "{{string}}",
   "defaultCacheBehavior": {
      "behavior": "{{string}}"
   },
   "distributionName": "{{string}}",
   "ipAddressType": "{{string}}",
   "origin": {
      "ipAddressType": "{{string}}",
      "name": "{{string}}",
      "protocolPolicy": "{{string}}",
      "regionName": "{{string}}",
      "responseTimeout": {{number}}
   },
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "viewerMinimumTlsProtocolVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateDistribution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bundleId](#API_CreateDistribution_RequestSyntax) **   <a name="Lightsail-CreateDistribution-request-bundleId"></a>
The bundle ID to use for the distribution.
A distribution bundle describes the specifications of your distribution, such as the monthly cost and monthly network transfer quota.
Use the `GetDistributionBundles` action to get a list of distribution bundle IDs that you can specify.
Type: String
Required: Yes

 ** [cacheBehaviors](#API_CreateDistribution_RequestSyntax) **   <a name="Lightsail-CreateDistribution-request-cacheBehaviors"></a>
An array of objects that describe the per-path cache behavior for the distribution.
Type: Array of [CacheBehaviorPerPath](API_CacheBehaviorPerPath.md) objects
Required: No

 ** [cacheBehaviorSettings](#API_CreateDistribution_RequestSyntax) **   <a name="Lightsail-CreateDistribution-request-cacheBehaviorSettings"></a>
An object that describes the cache behavior settings for the distribution.
Type: [CacheSettings](API_CacheSettings.md) object
Required: No

 ** [certificateName](#API_CreateDistribution_RequestSyntax) **   <a name="Lightsail-CreateDistribution-request-certificateName"></a>
The name of the SSL/TLS certificate that you want to attach to the distribution.
Use the [GetCertificates](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetCertificates.html) action to get a list of certificate names that you can specify.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [defaultCacheBehavior](#API_CreateDistribution_RequestSyntax) **   <a name="Lightsail-CreateDistribution-request-defaultCacheBehavior"></a>
An object that describes the default cache behavior for the distribution.
Type: [CacheBehavior](API_CacheBehavior.md) object
Required: Yes

 ** [distributionName](#API_CreateDistribution_RequestSyntax) **   <a name="Lightsail-CreateDistribution-request-distributionName"></a>
The name for the distribution.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [ipAddressType](#API_CreateDistribution_RequestSyntax) **   <a name="Lightsail-CreateDistribution-request-ipAddressType"></a>
The IP address type for the distribution.
The possible values are `ipv4` for IPv4 only, and `dualstack` for IPv4 and IPv6.
The default value is `dualstack`.
Type: String
Valid Values: `dualstack | ipv4 | ipv6`
Required: No

 ** [origin](#API_CreateDistribution_RequestSyntax) **   <a name="Lightsail-CreateDistribution-request-origin"></a>
An object that describes the origin resource for the distribution, such as a Lightsail instance, bucket, or load balancer.
The distribution pulls, caches, and serves content from the origin.
Type: [InputOrigin](API_InputOrigin.md) object
Required: Yes

 ** [tags](#API_CreateDistribution_RequestSyntax) **   <a name="Lightsail-CreateDistribution-request-tags"></a>
The tag keys and optional values to add to the distribution during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [viewerMinimumTlsProtocolVersion](#API_CreateDistribution_RequestSyntax) **   <a name="Lightsail-CreateDistribution-request-viewerMinimumTlsProtocolVersion"></a>
The minimum TLS protocol version for the SSL/TLS certificate.
Type: String
Valid Values: `TLSv1.1_2016 | TLSv1.2_2018 | TLSv1.2_2019 | TLSv1.2_2021`
Required: No

## Response Syntax
<a name="API_CreateDistribution_ResponseSyntax"></a>

```
{
   "distribution": {
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
   },
   "operation": {
      "createdAt": number,
      "errorCode": "string",
      "errorDetails": "string",
      "id": "string",
      "isTerminal": boolean,
      "location": {
         "availabilityZone": "string",
         "regionName": "string"
      },
      "operationDetails": "string",
      "operationType": "string",
      "resourceName": "string",
      "resourceType": "string",
      "status": "string",
      "statusChangedAt": number
   }
}
```

## Response Elements
<a name="API_CreateDistribution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [distribution](#API_CreateDistribution_ResponseSyntax) **   <a name="Lightsail-CreateDistribution-response-distribution"></a>
An object that describes the distribution created.
Type: [LightsailDistribution](API_LightsailDistribution.md) object

 ** [operation](#API_CreateDistribution_ResponseSyntax) **   <a name="Lightsail-CreateDistribution-response-operation"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: [Operation](API_Operation.md) object

## Errors
<a name="API_CreateDistribution_Errors"></a>

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
<a name="API_CreateDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateDistribution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateDistribution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateDistribution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateDistribution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateDistribution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateDistribution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateDistribution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateDistribution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

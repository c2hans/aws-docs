---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateDistribution.html
---

# UpdateDistribution
<a name="API_UpdateDistribution"></a>

Updates an existing Amazon Lightsail content delivery network (CDN) distribution.

Use this action to update the configuration of your existing distribution.

## Request Syntax
<a name="API_UpdateDistribution_RequestSyntax"></a>

```
{
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
   "customErrorResponses": [
      {
         "errorCachingMinTTL": {{number}},
         "errorCode": {{number}},
         "responseCode": "{{string}}",
         "responsePagePath": "{{string}}"
      }
   ],
   "defaultCacheBehavior": {
      "behavior": "{{string}}"
   },
   "defaultRootObject": "{{string}}",
   "distributionName": "{{string}}",
   "enablePrivateOriginAccess": {{boolean}},
   "enableWaf": {{boolean}},
   "isEnabled": {{boolean}},
   "origin": {
      "ipAddressType": "{{string}}",
      "name": "{{string}}",
      "protocolPolicy": "{{string}}",
      "regionName": "{{string}}",
      "responseTimeout": {{number}}
   },
   "useDefaultCertificate": {{boolean}},
   "viewerMinimumTlsProtocolVersion": "{{string}}",
   "wafRules": [
      {
         "acfpConfig": {
            "creationPath": "{{string}}",
            "payloadType": "{{string}}",
            "registrationPagePath": "{{string}}",
            "responseInspection": {
               "failureCodes": [ {{number}} ],
               "successCodes": [ {{number}} ]
            }
         },
         "atpConfig": {
            "loginPath": "{{string}}",
            "passwordField": "{{string}}",
            "payloadType": "{{string}}",
            "responseInspection": {
               "failureCodes": [ {{number}} ],
               "successCodes": [ {{number}} ]
            },
            "usernameField": "{{string}}"
         },
         "botControlConfig": {
            "inspectionLevel": "{{string}}"
         },
         "name": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateDistribution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cacheBehaviors](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-cacheBehaviors"></a>
An array of objects that describe the per-path cache behavior for the distribution.
Type: Array of [CacheBehaviorPerPath](API_CacheBehaviorPerPath.md) objects
Required: No

 ** [cacheBehaviorSettings](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-cacheBehaviorSettings"></a>
An object that describes the cache behavior settings for the distribution.
The `cacheBehaviorSettings` specified in your `UpdateDistributionRequest` will replace your distribution's existing settings.
Type: [CacheSettings](API_CacheSettings.md) object
Required: No

 ** [certificateName](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-certificateName"></a>
The name of the SSL/TLS certificate that you want to attach to the distribution.
Only certificates with a status of `ISSUED` can be attached to a distribution.
Use the [GetCertificates](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetCertificates.html) action to get a list of certificate names that you can specify.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [customErrorResponses](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-customErrorResponses"></a>
An array of objects that describe the custom error responses for the distribution. With a custom error response, you can specify the page to return when the origin responds with a given HTTP error code. You can also specify the HTTP status code to send to the viewer.
Type: Array of [DistributionCustomErrorResponse](API_DistributionCustomErrorResponse.md) objects
Required: No

 ** [defaultCacheBehavior](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-defaultCacheBehavior"></a>
An object that describes the default cache behavior for the distribution.
Type: [CacheBehavior](API_CacheBehavior.md) object
Required: No

 ** [defaultRootObject](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-defaultRootObject"></a>
The object (for example, `index.html`) that the distribution returns when a viewer requests the root URL of the distribution (`/`) instead of a specific object. The object that you specify must be available from the origin.
Type: String
Required: No

 ** [distributionName](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-distributionName"></a>
The name of the distribution to update.
Use the `GetDistributions` action to get a list of distribution names that you can specify.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [enablePrivateOriginAccess](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-enablePrivateOriginAccess"></a>
Specifies whether to enable private origin access for the distribution. With private origin access, the distribution can serve objects that aren't publicly accessible from a Lightsail bucket.
Lightsail grants the distribution permission to read the bucket's objects. Enabling private origin access doesn't change the bucket's access settings, and you can still retrieve publicly accessible objects directly from the bucket's endpoint.
When you include this parameter, you must also include the `origin` parameter with the resource name, even if the origin is not changing.
You can enable private origin access only when the distribution's origin is a Lightsail bucket. If the origin is another resource type, the request fails.
Type: Boolean
Required: No

 ** [enableWaf](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-enableWaf"></a>
Specifies whether to enable Web Application Firewall (WAF) for the distribution. WAF inspects viewer requests and blocks requests that match the WAF rule groups that you enable.
When you enable WAF without specifying the `wafRules` parameter, the distribution has no WAF rule groups enabled and doesn't block any requests.
WAF is available only for distributions that use the `medium_1_0` or `large_1_0` bundle.
Setting this parameter to `false` disables WAF for the distribution and removes its WAF rule groups. You must enable the WAF rule groups again if you enable WAF again.
Type: Boolean
Required: No

 ** [isEnabled](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-isEnabled"></a>
Indicates whether to enable the distribution.
Type: Boolean
Required: No

 ** [origin](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-origin"></a>
An object that describes the origin resource for the distribution, such as a Lightsail instance, bucket, or load balancer.
The distribution pulls, caches, and serves content from the origin.
Type: [InputOrigin](API_InputOrigin.md) object
Required: No

 ** [useDefaultCertificate](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-useDefaultCertificate"></a>
Indicates whether the default SSL/TLS certificate is attached to the distribution. The default value is `true`. When `true`, the distribution uses the default domain name such as `d111111abcdef8.cloudfront.net`.
 Set this value to `false` to attach a new certificate to the distribution.
Type: Boolean
Required: No

 ** [viewerMinimumTlsProtocolVersion](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-viewerMinimumTlsProtocolVersion"></a>
Use this parameter to update the minimum TLS protocol version for the SSL/TLS certificate that's attached to the distribution.
Type: String
Valid Values: `TLSv1.1_2016 | TLSv1.2_2018 | TLSv1.2_2019 | TLSv1.2_2021`
Required: No

 ** [wafRules](#API_UpdateDistribution_RequestSyntax) **   <a name="Lightsail-UpdateDistribution-request-wafRules"></a>
An array of objects that describe the WAF rule groups to enable for the distribution.
The array that you specify replaces the existing WAF rule groups of the distribution. To keep a WAF rule group enabled, include it in the array. To disable all WAF rule groups, specify an empty array.
You can specify this parameter only when WAF is enabled for the distribution.
The WAF rule groups that you can specify depend on the bundle of the distribution:
+  `medium_1_0` – Supports the `AWSManagedRulesCommonRuleSet`, `AWSManagedRulesKnownBadInputsRuleSet`, and `AWSManagedRulesAnonymousIpList` rule groups.
+  `large_1_0` – Supports the rule groups for `medium_1_0`, plus `AWSManagedRulesAdminProtectionRuleSet`, `AWSManagedRulesSQLiRuleSet`, `AWSManagedRulesLinuxRuleSet`, `AWSManagedRulesUnixRuleSet`, `AWSManagedRulesWindowsRuleSet`, `AWSManagedRulesPHPRuleSet`, `AWSManagedRulesWordPressRuleSet`, `AWSManagedRulesAmazonIpReputationList`, `AWSManagedRulesATPRuleSet`, `AWSManagedRulesACFPRuleSet`, and `AWSManagedRulesBotControlRuleSet` rule groups.
Type: Array of [WafRule](API_WafRule.md) objects
Required: No

## Response Syntax
<a name="API_UpdateDistribution_ResponseSyntax"></a>

```
{
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
<a name="API_UpdateDistribution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operation](#API_UpdateDistribution_ResponseSyntax) **   <a name="Lightsail-UpdateDistribution-response-operation"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: [Operation](API_Operation.md) object

## Errors
<a name="API_UpdateDistribution_Errors"></a>

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
<a name="API_UpdateDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/UpdateDistribution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/UpdateDistribution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/UpdateDistribution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/UpdateDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/UpdateDistribution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/UpdateDistribution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/UpdateDistribution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/UpdateDistribution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/UpdateDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/UpdateDistribution)

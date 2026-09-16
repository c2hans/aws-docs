---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBuckets.html
---

# GetBuckets
<a name="API_GetBuckets"></a>

Returns information about one or more Amazon Lightsail buckets. The information returned includes the synchronization status of the Amazon Simple Storage Service (Amazon S3) account-level block public access feature for your Lightsail buckets.

For more information about buckets, see [Buckets in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/buckets-in-amazon-lightsail) in the *Amazon Lightsail Developer Guide*.

## Request Syntax
<a name="API_GetBuckets_RequestSyntax"></a>

```
{
   "bucketName": "{{string}}",
   "includeConnectedResources": {{boolean}},
   "includeCors": {{boolean}},
   "pageToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetBuckets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bucketName](#API_GetBuckets_RequestSyntax) **   <a name="Lightsail-GetBuckets-request-bucketName"></a>
The name of the bucket for which to return information.
When omitted, the response includes all of your buckets in the AWS Region where the request is made.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 54.
Pattern: `^[a-z0-9][a-z0-9-]{1,52}[a-z0-9]$`
Required: No

 ** [includeConnectedResources](#API_GetBuckets_RequestSyntax) **   <a name="Lightsail-GetBuckets-request-includeConnectedResources"></a>
A Boolean value that indicates whether to include Lightsail instances that were given access to the bucket using the [SetResourceAccessForBucket](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetResourceAccessForBucket.html) action.
Type: Boolean
Required: No

 ** [includeCors](#API_GetBuckets_RequestSyntax) **   <a name="Lightsail-GetBuckets-request-includeCors"></a>
A Boolean value that indicates whether to include Lightsail bucket CORS configuration in the response. For more information, see [Configuring cross-origin resource sharing (CORS)](https://docs.aws.amazon.com/lightsail/latest/userguide/configure-cors.html).
This parameter is only supported when getting a single bucket with `bucketName` specified. The default value for this parameter is `False`.
Type: Boolean
Required: No

 ** [pageToken](#API_GetBuckets_RequestSyntax) **   <a name="Lightsail-GetBuckets-request-pageToken"></a>
The token to advance to the next page of results from your request.
To get a page token, perform an initial `GetBuckets` request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.
Type: String
Required: No

## Response Syntax
<a name="API_GetBuckets_ResponseSyntax"></a>

```
{
   "accountLevelBpaSync": {
      "bpaImpactsLightsail": boolean,
      "lastSyncedAt": number,
      "message": "string",
      "status": "string"
   },
   "buckets": [
      {
         "ableToUpdateBundle": boolean,
         "accessLogConfig": {
            "destination": "string",
            "enabled": boolean,
            "prefix": "string"
         },
         "accessRules": {
            "allowPublicOverrides": boolean,
            "getObject": "string"
         },
         "arn": "string",
         "bundleId": "string",
         "cors": {
            "rules": [
               {
                  "allowedHeaders": [ "string" ],
                  "allowedMethods": [ "string" ],
                  "allowedOrigins": [ "string" ],
                  "exposeHeaders": [ "string" ],
                  "id": "string",
                  "maxAgeSeconds": number
               }
            ]
         },
         "createdAt": number,
         "location": {
            "availabilityZone": "string",
            "regionName": "string"
         },
         "name": "string",
         "objectVersioning": "string",
         "readonlyAccessAccounts": [ "string" ],
         "resourcesReceivingAccess": [
            {
               "name": "string",
               "resourceType": "string"
            }
         ],
         "resourceType": "string",
         "state": {
            "code": "string",
            "message": "string"
         },
         "supportCode": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "url": "string"
      }
   ],
   "nextPageToken": "string"
}
```

## Response Elements
<a name="API_GetBuckets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountLevelBpaSync](#API_GetBuckets_ResponseSyntax) **   <a name="Lightsail-GetBuckets-response-accountLevelBpaSync"></a>
An object that describes the synchronization status of the Amazon S3 account-level block public access feature for your Lightsail buckets.
For more information about this feature and how it affects Lightsail buckets, see [Block public access for buckets in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-block-public-access-for-buckets).
Type: [AccountLevelBpaSync](API_AccountLevelBpaSync.md) object

 ** [buckets](#API_GetBuckets_ResponseSyntax) **   <a name="Lightsail-GetBuckets-response-buckets"></a>
An array of objects that describe buckets.
Type: Array of [Bucket](API_Bucket.md) objects

 ** [nextPageToken](#API_GetBuckets_ResponseSyntax) **   <a name="Lightsail-GetBuckets-response-nextPageToken"></a>
The token to advance to the next page of results from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another `GetBuckets` request and specify the next page token using the `pageToken` parameter.
Type: String

## Errors
<a name="API_GetBuckets_Errors"></a>

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

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_GetBuckets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetBuckets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetBuckets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetBuckets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetBuckets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetBuckets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetBuckets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetBuckets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetBuckets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetBuckets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetBuckets)

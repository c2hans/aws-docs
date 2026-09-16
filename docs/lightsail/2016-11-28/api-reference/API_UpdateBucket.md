---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateBucket.html
---

# UpdateBucket
<a name="API_UpdateBucket"></a>

Updates an existing Amazon Lightsail bucket.

Use this action to update the configuration of an existing bucket, such as versioning, public accessibility, and the AWS accounts that can access the bucket.

## Request Syntax
<a name="API_UpdateBucket_RequestSyntax"></a>

```
{
   "accessLogConfig": {
      "destination": "{{string}}",
      "enabled": {{boolean}},
      "prefix": "{{string}}"
   },
   "accessRules": {
      "allowPublicOverrides": {{boolean}},
      "getObject": "{{string}}"
   },
   "bucketName": "{{string}}",
   "cors": {
      "rules": [
         {
            "allowedHeaders": [ "{{string}}" ],
            "allowedMethods": [ "{{string}}" ],
            "allowedOrigins": [ "{{string}}" ],
            "exposeHeaders": [ "{{string}}" ],
            "id": "{{string}}",
            "maxAgeSeconds": {{number}}
         }
      ]
   },
   "readonlyAccessAccounts": [ "{{string}}" ],
   "versioning": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateBucket_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accessLogConfig](#API_UpdateBucket_RequestSyntax) **   <a name="Lightsail-UpdateBucket-request-accessLogConfig"></a>
An object that describes the access log configuration for the bucket.
Type: [BucketAccessLogConfig](API_BucketAccessLogConfig.md) object
Required: No

 ** [accessRules](#API_UpdateBucket_RequestSyntax) **   <a name="Lightsail-UpdateBucket-request-accessRules"></a>
An object that sets the public accessibility of objects in the specified bucket.
Type: [AccessRules](API_AccessRules.md) object
Required: No

 ** [bucketName](#API_UpdateBucket_RequestSyntax) **   <a name="Lightsail-UpdateBucket-request-bucketName"></a>
The name of the bucket to update.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 54.
Pattern: `^[a-z0-9][a-z0-9-]{1,52}[a-z0-9]$`
Required: Yes

 ** [cors](#API_UpdateBucket_RequestSyntax) **   <a name="Lightsail-UpdateBucket-request-cors"></a>
Sets the cross-origin resource sharing (CORS) configuration for your bucket. If a CORS configuration exists, it is replaced with the specified configuration. For AWS CLI operations, this parameter can also be passed as a file. For more information, see [Configuring cross-origin resource sharing (CORS)](https://docs.aws.amazon.com/lightsail/latest/userguide/configure-cors.html).
CORS information is only returned in a response when you update the CORS policy.
Type: [BucketCorsConfig](API_BucketCorsConfig.md) object
Required: No

 ** [readonlyAccessAccounts](#API_UpdateBucket_RequestSyntax) **   <a name="Lightsail-UpdateBucket-request-readonlyAccessAccounts"></a>
An array of strings to specify the AWS account IDs that can access the bucket.
You can give a maximum of 10 AWS accounts access to a bucket.
Type: Array of strings
Array Members: Maximum number of 10 items.
Pattern: `.*\S.*`
Required: No

 ** [versioning](#API_UpdateBucket_RequestSyntax) **   <a name="Lightsail-UpdateBucket-request-versioning"></a>
Specifies whether to enable or suspend versioning of objects in the bucket.
The following options can be specified:
+  `Enabled` - Enables versioning of objects in the specified bucket.
+  `Suspended` - Suspends versioning of objects in the specified bucket. Existing object versions are retained.
Type: String
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_UpdateBucket_ResponseSyntax"></a>

```
{
   "bucket": {
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
   },
   "operations": [
      {
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
   ]
}
```

## Response Elements
<a name="API_UpdateBucket_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [bucket](#API_UpdateBucket_ResponseSyntax) **   <a name="Lightsail-UpdateBucket-response-bucket"></a>
An object that describes the bucket that is updated.
Type: [Bucket](API_Bucket.md) object

 ** [operations](#API_UpdateBucket_ResponseSyntax) **   <a name="Lightsail-UpdateBucket-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_UpdateBucket_Errors"></a>

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
<a name="API_UpdateBucket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/UpdateBucket)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/UpdateBucket)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/UpdateBucket)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/UpdateBucket)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/UpdateBucket)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/UpdateBucket)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/UpdateBucket)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/UpdateBucket)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/UpdateBucket)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/UpdateBucket)

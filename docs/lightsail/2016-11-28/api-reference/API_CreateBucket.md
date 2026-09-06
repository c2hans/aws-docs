---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateBucket.html
---

# CreateBucket
<a name="API_CreateBucket"></a>

Creates an Amazon Lightsail bucket.

A bucket is a cloud storage resource available in the Lightsail object storage service. Use buckets to store objects such as data and its descriptive metadata. For more information about buckets, see [Buckets in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/buckets-in-amazon-lightsail) in the *Amazon Lightsail Developer Guide*.

## Request Syntax
<a name="API_CreateBucket_RequestSyntax"></a>

```
{
   "bucketName": "{{string}}",
   "bundleId": "{{string}}",
   "enableObjectVersioning": {{boolean}},
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateBucket_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bucketName](#API_CreateBucket_RequestSyntax) **   <a name="Lightsail-CreateBucket-request-bucketName"></a>
The name for the bucket.
For more information about bucket names, see [Bucket naming rules in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/bucket-naming-rules-in-amazon-lightsail) in the *Amazon Lightsail Developer Guide*.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 54.
Pattern: `^[a-z0-9][a-z0-9-]{1,52}[a-z0-9]$`
Required: Yes

 ** [bundleId](#API_CreateBucket_RequestSyntax) **   <a name="Lightsail-CreateBucket-request-bundleId"></a>
The ID of the bundle to use for the bucket.
A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket.
Use the [GetBucketBundles](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBucketBundles.html) action to get a list of bundle IDs that you can specify.
Use the [UpdateBucketBundle](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateBucketBundle.html) action to change the bundle after the bucket is created.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [enableObjectVersioning](#API_CreateBucket_RequestSyntax) **   <a name="Lightsail-CreateBucket-request-enableObjectVersioning"></a>
A Boolean value that indicates whether to enable versioning of objects in the bucket.
For more information about versioning, see [Enabling and suspending object versioning in a bucket in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-managing-bucket-object-versioning) in the *Amazon Lightsail Developer Guide*.
Type: Boolean
Required: No

 ** [tags](#API_CreateBucket_RequestSyntax) **   <a name="Lightsail-CreateBucket-request-tags"></a>
The tag keys and optional values to add to the bucket during creation.
Use the [TagResource](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_TagResource.html) action to tag the bucket after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateBucket_ResponseSyntax"></a>

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
<a name="API_CreateBucket_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [bucket](#API_CreateBucket_ResponseSyntax) **   <a name="Lightsail-CreateBucket-response-bucket"></a>
An object that describes the bucket that is created.
Type: [Bucket](API_Bucket.md) object

 ** [operations](#API_CreateBucket_ResponseSyntax) **   <a name="Lightsail-CreateBucket-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_CreateBucket_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
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
<a name="API_CreateBucket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateBucket)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateBucket)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateBucket)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateBucket)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateBucket)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateBucket)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateBucket)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateBucket)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateBucket)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateBucket)

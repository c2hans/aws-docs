---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DeleteBucket.html
---

# DeleteBucket
<a name="API_DeleteBucket"></a>

Deletes a Amazon Lightsail bucket.

**Note**
When you delete your bucket, the bucket name is released and can be reused for a new bucket in your account or another AWS account.

## Request Syntax
<a name="API_DeleteBucket_RequestSyntax"></a>

```
{
   "bucketName": "{{string}}",
   "forceDelete": {{boolean}}
}
```

## Request Parameters
<a name="API_DeleteBucket_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bucketName](#API_DeleteBucket_RequestSyntax) **   <a name="Lightsail-DeleteBucket-request-bucketName"></a>
The name of the bucket to delete.
Use the [GetBuckets](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBuckets.html) action to get a list of bucket names that you can specify.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 54.
Pattern: `^[a-z0-9][a-z0-9-]{1,52}[a-z0-9]$`
Required: Yes

 ** [forceDelete](#API_DeleteBucket_RequestSyntax) **   <a name="Lightsail-DeleteBucket-request-forceDelete"></a>
A Boolean value that indicates whether to force delete the bucket.
You must force delete the bucket if it has one of the following conditions:
+ The bucket is the origin of a distribution.
+ The bucket has instances that were granted access to it using the [SetResourceAccessForBucket](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetResourceAccessForBucket.html) action.
+ The bucket has objects.
+ The bucket has access keys.
Force deleting a bucket might impact other resources that rely on the bucket, such as instances, distributions, or software that use the issued access keys.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DeleteBucket_ResponseSyntax"></a>

```
{
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
<a name="API_DeleteBucket_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_DeleteBucket_ResponseSyntax) **   <a name="Lightsail-DeleteBucket-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_DeleteBucket_Errors"></a>

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
<a name="API_DeleteBucket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/DeleteBucket)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/DeleteBucket)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/DeleteBucket)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/DeleteBucket)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/DeleteBucket)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/DeleteBucket)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/DeleteBucket)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/DeleteBucket)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/DeleteBucket)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/DeleteBucket)

---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetDisks.html
---

# GetDisks
<a name="API_GetDisks"></a>

Returns information about all block storage disks in your AWS account and region.

## Request Syntax
<a name="API_GetDisks_RequestSyntax"></a>

```
{
   "pageToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDisks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pageToken](#API_GetDisks_RequestSyntax) **   <a name="Lightsail-GetDisks-request-pageToken"></a>
The token to advance to the next page of results from your request.
To get a page token, perform an initial `GetDisks` request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.
Type: String
Required: No

## Response Syntax
<a name="API_GetDisks_ResponseSyntax"></a>

```
{
   "disks": [
      {
         "addOns": [
            {
               "duration": "string",
               "name": "string",
               "nextSnapshotTimeOfDay": "string",
               "snapshotTimeOfDay": "string",
               "status": "string",
               "threshold": "string"
            }
         ],
         "arn": "string",
         "attachedTo": "string",
         "attachmentState": "string",
         "autoMountStatus": "string",
         "createdAt": number,
         "gbInUse": number,
         "iops": number,
         "isAttached": boolean,
         "isSystemDisk": boolean,
         "location": {
            "availabilityZone": "string",
            "regionName": "string"
         },
         "name": "string",
         "path": "string",
         "resourceType": "string",
         "sizeInGb": number,
         "state": "string",
         "supportCode": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ],
   "nextPageToken": "string"
}
```

## Response Elements
<a name="API_GetDisks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [disks](#API_GetDisks_ResponseSyntax) **   <a name="Lightsail-GetDisks-response-disks"></a>
An array of objects containing information about all block storage disks.
Type: Array of [Disk](API_Disk.md) objects

 ** [nextPageToken](#API_GetDisks_ResponseSyntax) **   <a name="Lightsail-GetDisks-response-nextPageToken"></a>
The token to advance to the next page of results from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another `GetDisks` request and specify the next page token using the `pageToken` parameter.
Type: String

## Errors
<a name="API_GetDisks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** AccountSetupInProgressException **
Lightsail throws this exception when an account is still in the setup in progress state.
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
<a name="API_GetDisks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetDisks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetDisks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetDisks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetDisks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetDisks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetDisks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetDisks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetDisks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetDisks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetDisks)

---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateDisk.html
---

# CreateDisk
<a name="API_CreateDisk"></a>

Creates a block storage disk that can be attached to an Amazon Lightsail instance in the same Availability Zone (`us-east-2a`).

The `create disk` operation supports tag-based access control via request tags. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_CreateDisk_RequestSyntax"></a>

```
{
   "addOns": [
      {
         "addOnType": "{{string}}",
         "autoSnapshotAddOnRequest": {
            "snapshotTimeOfDay": "{{string}}"
         },
         "stopInstanceOnIdleRequest": {
            "duration": "{{string}}",
            "threshold": "{{string}}"
         }
      }
   ],
   "availabilityZone": "{{string}}",
   "diskName": "{{string}}",
   "sizeInGb": {{number}},
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateDisk_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [addOns](#API_CreateDisk_RequestSyntax) **   <a name="Lightsail-CreateDisk-request-addOns"></a>
An array of objects that represent the add-ons to enable for the new disk.
Type: Array of [AddOnRequest](API_AddOnRequest.md) objects
Required: No

 ** [availabilityZone](#API_CreateDisk_RequestSyntax) **   <a name="Lightsail-CreateDisk-request-availabilityZone"></a>
The Availability Zone where you want to create the disk (`us-east-2a`). Use the same Availability Zone as the Lightsail instance to which you want to attach the disk.
Use the `get regions` operation to list the Availability Zones where Lightsail is currently available.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [diskName](#API_CreateDisk_RequestSyntax) **   <a name="Lightsail-CreateDisk-request-diskName"></a>
The unique Lightsail disk name (`my-disk`).
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [sizeInGb](#API_CreateDisk_RequestSyntax) **   <a name="Lightsail-CreateDisk-request-sizeInGb"></a>
The size of the disk in GB (`32`).
Type: Integer
Required: Yes

 ** [tags](#API_CreateDisk_RequestSyntax) **   <a name="Lightsail-CreateDisk-request-tags"></a>
The tag keys and optional values to add to the resource during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateDisk_ResponseSyntax"></a>

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
<a name="API_CreateDisk_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_CreateDisk_ResponseSyntax) **   <a name="Lightsail-CreateDisk-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_CreateDisk_Errors"></a>

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
<a name="API_CreateDisk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateDisk)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateDisk)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateDisk)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateDisk)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateDisk)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateDisk)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateDisk)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateDisk)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateDisk)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateDisk)

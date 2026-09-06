---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DeleteDisk.html
---

# DeleteDisk
<a name="API_DeleteDisk"></a>

Deletes the specified block storage disk. The disk must be in the `available` state (not attached to a Lightsail instance).

**Note**
The disk may remain in the `deleting` state for several minutes.

The `delete disk` operation supports tag-based access control via resource tags applied to the resource identified by `disk name`. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_DeleteDisk_RequestSyntax"></a>

```
{
   "diskName": "{{string}}",
   "forceDeleteAddOns": {{boolean}}
}
```

## Request Parameters
<a name="API_DeleteDisk_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [diskName](#API_DeleteDisk_RequestSyntax) **   <a name="Lightsail-DeleteDisk-request-diskName"></a>
The unique name of the disk you want to delete (`my-disk`).
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [forceDeleteAddOns](#API_DeleteDisk_RequestSyntax) **   <a name="Lightsail-DeleteDisk-request-forceDeleteAddOns"></a>
A Boolean value to indicate whether to delete all add-ons for the disk.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DeleteDisk_ResponseSyntax"></a>

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
<a name="API_DeleteDisk_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_DeleteDisk_ResponseSyntax) **   <a name="Lightsail-DeleteDisk-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_DeleteDisk_Errors"></a>

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
<a name="API_DeleteDisk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/DeleteDisk)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/DeleteDisk)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/DeleteDisk)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/DeleteDisk)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/DeleteDisk)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/DeleteDisk)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/DeleteDisk)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/DeleteDisk)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/DeleteDisk)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/DeleteDisk)

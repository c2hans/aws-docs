---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateInstancesFromSnapshot.html
---

# CreateInstancesFromSnapshot
<a name="API_CreateInstancesFromSnapshot"></a>

Creates one or more new instances from a manual or automatic snapshot of an instance.

The `create instances from snapshot` operation supports tag-based access control via request tags and resource tags applied to the resource identified by `instance snapshot name`. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_CreateInstancesFromSnapshot_RequestSyntax"></a>

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
   "attachedDiskMapping": {
      "{{string}}" : [
         {
            "newDiskName": "{{string}}",
            "originalDiskPath": "{{string}}"
         }
      ]
   },
   "availabilityZone": "{{string}}",
   "bundleId": "{{string}}",
   "instanceNames": [ "{{string}}" ],
   "instanceSnapshotName": "{{string}}",
   "ipAddressType": "{{string}}",
   "keyPairName": "{{string}}",
   "restoreDate": "{{string}}",
   "sourceInstanceName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "useLatestRestorableAutoSnapshot": {{boolean}},
   "userData": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateInstancesFromSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [addOns](#API_CreateInstancesFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-request-addOns"></a>
An array of objects representing the add-ons to enable for the new instance.
Type: Array of [AddOnRequest](API_AddOnRequest.md) objects
Required: No

 ** [attachedDiskMapping](#API_CreateInstancesFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-request-attachedDiskMapping"></a>
An object containing information about one or more disk mappings.
Type: String to array of [DiskMap](API_DiskMap.md) objects map
Key Pattern: `\w[\w\-]*\w`
Required: No

 ** [availabilityZone](#API_CreateInstancesFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-request-availabilityZone"></a>
The Availability Zone where you want to create your instances. Use the following formatting: `us-east-2a` (case sensitive). You can get a list of Availability Zones by using the [get regions](http://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html) operation. Be sure to add the `include Availability Zones` parameter to your request.
Type: String
Required: Yes

 ** [bundleId](#API_CreateInstancesFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-request-bundleId"></a>
The bundle of specification information for your virtual private server (or *instance*), including the pricing plan (`micro_x_x`).
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [instanceNames](#API_CreateInstancesFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-request-instanceNames"></a>
The names for your new instances.
Type: Array of strings
Required: Yes

 ** [instanceSnapshotName](#API_CreateInstancesFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-request-instanceSnapshotName"></a>
The name of the instance snapshot on which you are basing your new instances. Use the get instance snapshots operation to return information about your existing snapshots.
Constraint:
+ This parameter cannot be defined together with the `source instance name` parameter. The `instance snapshot name` and `source instance name` parameters are mutually exclusive.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [ipAddressType](#API_CreateInstancesFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-request-ipAddressType"></a>
The IP address type for the instance.
The possible values are `ipv4` for IPv4 only, `ipv6` for IPv6 only, and `dualstack` for IPv4 and IPv6.
The default value is `dualstack`.
Type: String
Valid Values: `dualstack | ipv4 | ipv6`
Required: No

 ** [keyPairName](#API_CreateInstancesFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-request-keyPairName"></a>
The name for your key pair.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [restoreDate](#API_CreateInstancesFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-request-restoreDate"></a>
The date of the automatic snapshot to use for the new instance. Use the `get auto snapshots` operation to identify the dates of the available automatic snapshots.
Constraints:
+ Must be specified in `YYYY-MM-DD` format.
+ This parameter cannot be defined together with the `use latest restorable auto snapshot` parameter. The `restore date` and `use latest restorable auto snapshot` parameters are mutually exclusive.
+ Define this parameter only when creating a new instance from an automatic snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots).
Type: String
Required: No

 ** [sourceInstanceName](#API_CreateInstancesFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-request-sourceInstanceName"></a>
The name of the source instance from which the source automatic snapshot was created.
Constraints:
+ This parameter cannot be defined together with the `instance snapshot name` parameter. The `source instance name` and `instance snapshot name` parameters are mutually exclusive.
+ Define this parameter only when creating a new instance from an automatic snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots).
Type: String
Required: No

 ** [tags](#API_CreateInstancesFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-request-tags"></a>
The tag keys and optional values to add to the resource during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [useLatestRestorableAutoSnapshot](#API_CreateInstancesFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-request-useLatestRestorableAutoSnapshot"></a>
A Boolean value to indicate whether to use the latest available automatic snapshot.
Constraints:
+ This parameter cannot be defined together with the `restore date` parameter. The `use latest restorable auto snapshot` and `restore date` parameters are mutually exclusive.
+ Define this parameter only when creating a new instance from an automatic snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots).
Type: Boolean
Required: No

 ** [userData](#API_CreateInstancesFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-request-userData"></a>
You can create a launch script that configures a server with additional user data. For example, `apt-get -y update`.
Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use `yum`, Debian and Ubuntu use `apt-get`, and FreeBSD uses `pkg`. For a complete list, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/compare-options-choose-lightsail-instance-image).
Type: String
Required: No

## Response Syntax
<a name="API_CreateInstancesFromSnapshot_ResponseSyntax"></a>

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
<a name="API_CreateInstancesFromSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_CreateInstancesFromSnapshot_ResponseSyntax) **   <a name="Lightsail-CreateInstancesFromSnapshot-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_CreateInstancesFromSnapshot_Errors"></a>

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
<a name="API_CreateInstancesFromSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateInstancesFromSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateInstancesFromSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateInstancesFromSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateInstancesFromSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateInstancesFromSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateInstancesFromSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateInstancesFromSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateInstancesFromSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateInstancesFromSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateInstancesFromSnapshot)

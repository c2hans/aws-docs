---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateDiskFromSnapshot.html
---

# CreateDiskFromSnapshot
<a name="API_CreateDiskFromSnapshot"></a>

Creates a block storage disk from a manual or automatic snapshot of a disk. The resulting disk can be attached to an Amazon Lightsail instance in the same Availability Zone (`us-east-2a`).

The `create disk from snapshot` operation supports tag-based access control via request tags and resource tags applied to the resource identified by `disk snapshot name`. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_CreateDiskFromSnapshot_RequestSyntax"></a>

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
   "diskSnapshotName": "{{string}}",
   "restoreDate": "{{string}}",
   "sizeInGb": {{number}},
   "sourceDiskName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "useLatestRestorableAutoSnapshot": {{boolean}}
}
```

## Request Parameters
<a name="API_CreateDiskFromSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [addOns](#API_CreateDiskFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateDiskFromSnapshot-request-addOns"></a>
An array of objects that represent the add-ons to enable for the new disk.
Type: Array of [AddOnRequest](API_AddOnRequest.md) objects
Required: No

 ** [availabilityZone](#API_CreateDiskFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateDiskFromSnapshot-request-availabilityZone"></a>
The Availability Zone where you want to create the disk (`us-east-2a`). Choose the same Availability Zone as the Lightsail instance where you want to create the disk.
Use the GetRegions operation to list the Availability Zones where Lightsail is currently available.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [diskName](#API_CreateDiskFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateDiskFromSnapshot-request-diskName"></a>
The unique Lightsail disk name (`my-disk`).
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [diskSnapshotName](#API_CreateDiskFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateDiskFromSnapshot-request-diskSnapshotName"></a>
The name of the disk snapshot (`my-snapshot`) from which to create the new storage disk.
Constraint:
+ This parameter cannot be defined together with the `source disk name` parameter. The `disk snapshot name` and `source disk name` parameters are mutually exclusive.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [restoreDate](#API_CreateDiskFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateDiskFromSnapshot-request-restoreDate"></a>
The date of the automatic snapshot to use for the new disk. Use the `get auto snapshots` operation to identify the dates of the available automatic snapshots.
Constraints:
+ Must be specified in `YYYY-MM-DD` format.
+ This parameter cannot be defined together with the `use latest restorable auto snapshot` parameter. The `restore date` and `use latest restorable auto snapshot` parameters are mutually exclusive.
+ Define this parameter only when creating a new disk from an automatic snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots).
Type: String
Required: No

 ** [sizeInGb](#API_CreateDiskFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateDiskFromSnapshot-request-sizeInGb"></a>
The size of the disk in GB (`32`).
Type: Integer
Required: Yes

 ** [sourceDiskName](#API_CreateDiskFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateDiskFromSnapshot-request-sourceDiskName"></a>
The name of the source disk from which the source automatic snapshot was created.
Constraints:
+ This parameter cannot be defined together with the `disk snapshot name` parameter. The `source disk name` and `disk snapshot name` parameters are mutually exclusive.
+ Define this parameter only when creating a new disk from an automatic snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots).
Type: String
Required: No

 ** [tags](#API_CreateDiskFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateDiskFromSnapshot-request-tags"></a>
The tag keys and optional values to add to the resource during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [useLatestRestorableAutoSnapshot](#API_CreateDiskFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateDiskFromSnapshot-request-useLatestRestorableAutoSnapshot"></a>
A Boolean value to indicate whether to use the latest available automatic snapshot.
Constraints:
+ This parameter cannot be defined together with the `restore date` parameter. The `use latest restorable auto snapshot` and `restore date` parameters are mutually exclusive.
+ Define this parameter only when creating a new disk from an automatic snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots).
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateDiskFromSnapshot_ResponseSyntax"></a>

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
<a name="API_CreateDiskFromSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_CreateDiskFromSnapshot_ResponseSyntax) **   <a name="Lightsail-CreateDiskFromSnapshot-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_CreateDiskFromSnapshot_Errors"></a>

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
<a name="API_CreateDiskFromSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateDiskFromSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateDiskFromSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateDiskFromSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateDiskFromSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateDiskFromSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateDiskFromSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateDiskFromSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateDiskFromSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateDiskFromSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateDiskFromSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetAutoSnapshots.html
---

# GetAutoSnapshots
<a name="API_GetAutoSnapshots"></a>

Returns the available automatic snapshots for an instance or disk. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots).

## Request Syntax
<a name="API_GetAutoSnapshots_RequestSyntax"></a>

```
{
   "resourceName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAutoSnapshots_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceName](#API_GetAutoSnapshots_RequestSyntax) **   <a name="Lightsail-GetAutoSnapshots-request-resourceName"></a>
The name of the source instance or disk from which to get automatic snapshot information.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

## Response Syntax
<a name="API_GetAutoSnapshots_ResponseSyntax"></a>

```
{
   "autoSnapshots": [
      {
         "createdAt": number,
         "date": "string",
         "fromAttachedDisks": [
            {
               "path": "string",
               "sizeInGb": number
            }
         ],
         "status": "string"
      }
   ],
   "resourceName": "string",
   "resourceType": "string"
}
```

## Response Elements
<a name="API_GetAutoSnapshots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autoSnapshots](#API_GetAutoSnapshots_ResponseSyntax) **   <a name="Lightsail-GetAutoSnapshots-response-autoSnapshots"></a>
An array of objects that describe the automatic snapshots that are available for the specified source instance or disk.
Type: Array of [AutoSnapshotDetails](API_AutoSnapshotDetails.md) objects

 ** [resourceName](#API_GetAutoSnapshots_ResponseSyntax) **   <a name="Lightsail-GetAutoSnapshots-response-resourceName"></a>
The name of the source instance or disk for the automatic snapshots.
Type: String
Pattern: `\w[\w\-]*\w`

 ** [resourceType](#API_GetAutoSnapshots_ResponseSyntax) **   <a name="Lightsail-GetAutoSnapshots-response-resourceType"></a>
The resource type of the automatic snapshot. The possible values are `Instance`, and `Disk`.
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`

## Errors
<a name="API_GetAutoSnapshots_Errors"></a>

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
<a name="API_GetAutoSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetAutoSnapshots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetAutoSnapshots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetAutoSnapshots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetAutoSnapshots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetAutoSnapshots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetAutoSnapshots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetAutoSnapshots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetAutoSnapshots)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetAutoSnapshots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetAutoSnapshots)

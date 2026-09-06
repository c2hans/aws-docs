---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetExportSnapshotRecords.html
---

# GetExportSnapshotRecords
<a name="API_GetExportSnapshotRecords"></a>

Returns all export snapshot records created as a result of the `export snapshot` operation.

An export snapshot record can be used to create a new Amazon EC2 instance and its related resources with the [CreateCloudFormationStack](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateCloudFormationStack.html) action.

## Request Syntax
<a name="API_GetExportSnapshotRecords_RequestSyntax"></a>

```
{
   "pageToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetExportSnapshotRecords_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pageToken](#API_GetExportSnapshotRecords_RequestSyntax) **   <a name="Lightsail-GetExportSnapshotRecords-request-pageToken"></a>
The token to advance to the next page of results from your request.
To get a page token, perform an initial `GetExportSnapshotRecords` request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.
Type: String
Required: No

## Response Syntax
<a name="API_GetExportSnapshotRecords_ResponseSyntax"></a>

```
{
   "exportSnapshotRecords": [
      {
         "arn": "string",
         "createdAt": number,
         "destinationInfo": {
            "id": "string",
            "service": "string"
         },
         "location": {
            "availabilityZone": "string",
            "regionName": "string"
         },
         "name": "string",
         "resourceType": "string",
         "sourceInfo": {
            "arn": "string",
            "createdAt": number,
            "diskSnapshotInfo": {
               "sizeInGb": number
            },
            "fromResourceArn": "string",
            "fromResourceName": "string",
            "instanceSnapshotInfo": {
               "fromBlueprintId": "string",
               "fromBundleId": "string",
               "fromDiskInfo": [
                  {
                     "isSystemDisk": boolean,
                     "name": "string",
                     "path": "string",
                     "sizeInGb": number
                  }
               ]
            },
            "name": "string",
            "resourceType": "string"
         },
         "state": "string"
      }
   ],
   "nextPageToken": "string"
}
```

## Response Elements
<a name="API_GetExportSnapshotRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [exportSnapshotRecords](#API_GetExportSnapshotRecords_ResponseSyntax) **   <a name="Lightsail-GetExportSnapshotRecords-response-exportSnapshotRecords"></a>
A list of objects describing the export snapshot records.
Type: Array of [ExportSnapshotRecord](API_ExportSnapshotRecord.md) objects

 ** [nextPageToken](#API_GetExportSnapshotRecords_ResponseSyntax) **   <a name="Lightsail-GetExportSnapshotRecords-response-nextPageToken"></a>
The token to advance to the next page of results from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another `GetExportSnapshotRecords` request and specify the next page token using the `pageToken` parameter.
Type: String

## Errors
<a name="API_GetExportSnapshotRecords_Errors"></a>

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
<a name="API_GetExportSnapshotRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetExportSnapshotRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetExportSnapshotRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetExportSnapshotRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetExportSnapshotRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetExportSnapshotRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetExportSnapshotRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetExportSnapshotRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetExportSnapshotRecords)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetExportSnapshotRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetExportSnapshotRecords)

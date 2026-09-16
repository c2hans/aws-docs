---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxDataview.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# GetKxDataview
<a name="API_GetKxDataview"></a>

 Retrieves details of the dataview.

## Request Syntax
<a name="API_GetKxDataview_RequestSyntax"></a>

```
GET /kx/environments/{{environmentId}}/databases/{{databaseName}}/dataviews/{{dataviewName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetKxDataview_RequestParameters"></a>

The request uses the following URI parameters.

 ** [databaseName](#API_GetKxDataview_RequestSyntax) **   <a name="finspace-GetKxDataview-request-uri-databaseName"></a>
 The name of the database where you created the dataview.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [dataviewName](#API_GetKxDataview_RequestSyntax) **   <a name="finspace-GetKxDataview-request-uri-dataviewName"></a>
A unique identifier for the dataview.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [environmentId](#API_GetKxDataview_RequestSyntax) **   <a name="finspace-GetKxDataview-request-uri-environmentId"></a>
A unique identifier for the kdb environment, from where you want to retrieve the dataview details.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetKxDataview_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetKxDataview_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "activeVersions": [
      {
         "attachedClusters": [ "string" ],
         "changesetId": "string",
         "createdTimestamp": number,
         "segmentConfigurations": [
            {
               "dbPaths": [ "string" ],
               "onDemand": boolean,
               "volumeName": "string"
            }
         ],
         "versionId": "string"
      }
   ],
   "autoUpdate": boolean,
   "availabilityZoneId": "string",
   "azMode": "string",
   "changesetId": "string",
   "createdTimestamp": number,
   "databaseName": "string",
   "dataviewName": "string",
   "description": "string",
   "environmentId": "string",
   "lastModifiedTimestamp": number,
   "readWrite": boolean,
   "segmentConfigurations": [
      {
         "dbPaths": [ "string" ],
         "onDemand": boolean,
         "volumeName": "string"
      }
   ],
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_GetKxDataview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [activeVersions](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-activeVersions"></a>
 The current active changeset versions of the database on the given dataview.
Type: Array of [KxDataviewActiveVersion](API_KxDataviewActiveVersion.md) objects

 ** [autoUpdate](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-autoUpdate"></a>
The option to specify whether you want to apply all the future additions and corrections automatically to the dataview when new changesets are ingested. The default value is false.
Type: Boolean

 ** [availabilityZoneId](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-availabilityZoneId"></a>
 The identifier of the availability zones.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [azMode](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-azMode"></a>
The number of availability zones you want to assign per volume. Currently, FinSpace only supports `SINGLE` for volumes. This places dataview in a single AZ.
Type: String
Valid Values: `SINGLE | MULTI`

 ** [changesetId](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-changesetId"></a>
 A unique identifier of the changeset that you want to use to ingest data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]+$`

 ** [createdTimestamp](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-createdTimestamp"></a>
The timestamp at which the dataview was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [databaseName](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-databaseName"></a>
 The name of the database where you created the dataview.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [dataviewName](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-dataviewName"></a>
A unique identifier for the dataview.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [description](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-description"></a>
A description of the dataview.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`

 ** [environmentId](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-environmentId"></a>
A unique identifier for the kdb environment, from where you want to retrieve the dataview details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`

 ** [lastModifiedTimestamp](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-lastModifiedTimestamp"></a>
 The last time that the dataview was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [readWrite](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-readWrite"></a>
Returns True if the dataview is created as writeable and False otherwise.
Type: Boolean

 ** [segmentConfigurations](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-segmentConfigurations"></a>
 The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment.
Type: Array of [KxDataviewSegmentConfiguration](API_KxDataviewSegmentConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [status](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-status"></a>
 The status of dataview creation.
+  `CREATING` – The dataview creation is in progress.
+  `UPDATING` – The dataview is in the process of being updated.
+  `ACTIVE` – The dataview is active.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | FAILED | DELETING`

 ** [statusReason](#API_GetKxDataview_ResponseSyntax) **   <a name="finspace-GetKxDataview-response-statusReason"></a>
 The error message when a failed state occurs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^[a-zA-Z0-9\_\-\.\s]+$`

## Errors
<a name="API_GetKxDataview_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetKxDataview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/GetKxDataview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/GetKxDataview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/GetKxDataview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/GetKxDataview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/GetKxDataview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/GetKxDataview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/GetKxDataview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/GetKxDataview)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/GetKxDataview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/GetKxDataview)

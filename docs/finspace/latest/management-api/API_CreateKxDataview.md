---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxDataview.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# CreateKxDataview
<a name="API_CreateKxDataview"></a>

 Creates a snapshot of kdb database with tiered storage capabilities and a pre-warmed cache, ready for mounting on kdb clusters. Dataviews are only available for clusters running on a scaling group. They are not supported on dedicated clusters.

## Request Syntax
<a name="API_CreateKxDataview_RequestSyntax"></a>

```
POST /kx/environments/{{environmentId}}/databases/{{databaseName}}/dataviews HTTP/1.1
Content-type: application/json

{
   "autoUpdate": {{boolean}},
   "availabilityZoneId": "{{string}}",
   "azMode": "{{string}}",
   "changesetId": "{{string}}",
   "clientToken": "{{string}}",
   "dataviewName": "{{string}}",
   "description": "{{string}}",
   "readWrite": {{boolean}},
   "segmentConfigurations": [
      {
         "dbPaths": [ "{{string}}" ],
         "onDemand": {{boolean}},
         "volumeName": "{{string}}"
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateKxDataview_RequestParameters"></a>

The request uses the following URI parameters.

 ** [databaseName](#API_CreateKxDataview_RequestSyntax) **   <a name="finspace-CreateKxDataview-request-uri-databaseName"></a>
 The name of the database where you want to create a dataview.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [environmentId](#API_CreateKxDataview_RequestSyntax) **   <a name="finspace-CreateKxDataview-request-uri-environmentId"></a>
A unique identifier for the kdb environment, where you want to create the dataview.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_CreateKxDataview_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [azMode](#API_CreateKxDataview_RequestSyntax) **   <a name="finspace-CreateKxDataview-request-azMode"></a>
The number of availability zones you want to assign per volume. Currently, FinSpace only supports `SINGLE` for volumes. This places dataview in a single AZ.
Type: String
Valid Values: `SINGLE | MULTI`
Required: Yes

 ** [clientToken](#API_CreateKxDataview_RequestSyntax) **   <a name="finspace-CreateKxDataview-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [dataviewName](#API_CreateKxDataview_RequestSyntax) **   <a name="finspace-CreateKxDataview-request-dataviewName"></a>
A unique identifier for the dataview.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [autoUpdate](#API_CreateKxDataview_RequestSyntax) **   <a name="finspace-CreateKxDataview-request-autoUpdate"></a>
The option to specify whether you want to apply all the future additions and corrections automatically to the dataview, when you ingest new changesets. The default value is false.
Type: Boolean
Required: No

 ** [availabilityZoneId](#API_CreateKxDataview_RequestSyntax) **   <a name="finspace-CreateKxDataview-request-availabilityZoneId"></a>
 The identifier of the availability zones.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** [changesetId](#API_CreateKxDataview_RequestSyntax) **   <a name="finspace-CreateKxDataview-request-changesetId"></a>
 A unique identifier of the changeset that you want to use to ingest data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** [description](#API_CreateKxDataview_RequestSyntax) **   <a name="finspace-CreateKxDataview-request-description"></a>
A description of the dataview.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`
Required: No

 ** [readWrite](#API_CreateKxDataview_RequestSyntax) **   <a name="finspace-CreateKxDataview-request-readWrite"></a>
 The option to specify whether you want to make the dataview writable to perform database maintenance. The following are some considerations related to writable dataviews.
+ You cannot create partial writable dataviews. When you create writeable dataviews you must provide the entire database path.
+ You cannot perform updates on a writeable dataview. Hence, `autoUpdate` must be set as **False** if `readWrite` is **True** for a dataview.
+ You must also use a unique volume for creating a writeable dataview. So, if you choose a volume that is already in use by another dataview, the dataview creation fails.
+ Once you create a dataview as writeable, you cannot change it to read-only. So, you cannot update the `readWrite` parameter later.
Type: Boolean
Required: No

 ** [segmentConfigurations](#API_CreateKxDataview_RequestSyntax) **   <a name="finspace-CreateKxDataview-request-segmentConfigurations"></a>
 The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment.
Type: Array of [KxDataviewSegmentConfiguration](API_KxDataviewSegmentConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [tags](#API_CreateKxDataview_RequestSyntax) **   <a name="finspace-CreateKxDataview-request-tags"></a>
 A list of key-value pairs to label the dataview. You can add up to 50 tags to a dataview.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `^[a-zA-Z0-9+-=._:@ ]+$`
Required: No

## Response Syntax
<a name="API_CreateKxDataview_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
   "status": "string"
}
```

## Response Elements
<a name="API_CreateKxDataview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autoUpdate](#API_CreateKxDataview_ResponseSyntax) **   <a name="finspace-CreateKxDataview-response-autoUpdate"></a>
The option to select whether you want to apply all the future additions and corrections automatically to the dataview when you ingest new changesets. The default value is false.
Type: Boolean

 ** [availabilityZoneId](#API_CreateKxDataview_ResponseSyntax) **   <a name="finspace-CreateKxDataview-response-availabilityZoneId"></a>
 The identifier of the availability zones.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [azMode](#API_CreateKxDataview_ResponseSyntax) **   <a name="finspace-CreateKxDataview-response-azMode"></a>
The number of availability zones you want to assign per volume. Currently, FinSpace only supports `SINGLE` for volumes. This places dataview in a single AZ.
Type: String
Valid Values: `SINGLE | MULTI`

 ** [changesetId](#API_CreateKxDataview_ResponseSyntax) **   <a name="finspace-CreateKxDataview-response-changesetId"></a>
A unique identifier for the changeset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]+$`

 ** [createdTimestamp](#API_CreateKxDataview_ResponseSyntax) **   <a name="finspace-CreateKxDataview-response-createdTimestamp"></a>
 The timestamp at which the dataview was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [databaseName](#API_CreateKxDataview_ResponseSyntax) **   <a name="finspace-CreateKxDataview-response-databaseName"></a>
The name of the database where you want to create a dataview.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [dataviewName](#API_CreateKxDataview_ResponseSyntax) **   <a name="finspace-CreateKxDataview-response-dataviewName"></a>
A unique identifier for the dataview.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [description](#API_CreateKxDataview_ResponseSyntax) **   <a name="finspace-CreateKxDataview-response-description"></a>
A description of the dataview.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`

 ** [environmentId](#API_CreateKxDataview_ResponseSyntax) **   <a name="finspace-CreateKxDataview-response-environmentId"></a>
A unique identifier for the kdb environment, where you want to create the dataview.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`

 ** [lastModifiedTimestamp](#API_CreateKxDataview_ResponseSyntax) **   <a name="finspace-CreateKxDataview-response-lastModifiedTimestamp"></a>
 The last time that the dataview was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [readWrite](#API_CreateKxDataview_ResponseSyntax) **   <a name="finspace-CreateKxDataview-response-readWrite"></a>
Returns True if the dataview is created as writeable and False otherwise.
Type: Boolean

 ** [segmentConfigurations](#API_CreateKxDataview_ResponseSyntax) **   <a name="finspace-CreateKxDataview-response-segmentConfigurations"></a>
 The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment.
Type: Array of [KxDataviewSegmentConfiguration](API_KxDataviewSegmentConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [status](#API_CreateKxDataview_ResponseSyntax) **   <a name="finspace-CreateKxDataview-response-status"></a>
 The status of dataview creation.
+  `CREATING` – The dataview creation is in progress.
+  `UPDATING` – The dataview is in the process of being updated.
+  `ACTIVE` – The dataview is active.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | FAILED | DELETING`

## Errors
<a name="API_CreateKxDataview_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict with this action, and it could not be completed.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** LimitExceededException **
A service limit or quota is exceeded.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource group already exists.
HTTP Status Code: 409

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
<a name="API_CreateKxDataview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/CreateKxDataview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/CreateKxDataview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/CreateKxDataview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/CreateKxDataview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/CreateKxDataview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/CreateKxDataview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/CreateKxDataview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/CreateKxDataview)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/CreateKxDataview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/CreateKxDataview)

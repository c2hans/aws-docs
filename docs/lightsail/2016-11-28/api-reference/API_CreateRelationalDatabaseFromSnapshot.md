---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateRelationalDatabaseFromSnapshot.html
---

# CreateRelationalDatabaseFromSnapshot
<a name="API_CreateRelationalDatabaseFromSnapshot"></a>

Creates a new database from an existing database snapshot in Amazon Lightsail.

You can create a new database from a snapshot in if something goes wrong with your original database, or to change it to a different plan, such as a high availability or standard plan.

The `create relational database from snapshot` operation supports tag-based access control via request tags and resource tags applied to the resource identified by relationalDatabaseSnapshotName. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_CreateRelationalDatabaseFromSnapshot_RequestSyntax"></a>

```
{
   "availabilityZone": "{{string}}",
   "publiclyAccessible": {{boolean}},
   "relationalDatabaseBundleId": "{{string}}",
   "relationalDatabaseName": "{{string}}",
   "relationalDatabaseSnapshotName": "{{string}}",
   "restoreTime": {{number}},
   "sourceRelationalDatabaseName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "useLatestRestorableTime": {{boolean}}
}
```

## Request Parameters
<a name="API_CreateRelationalDatabaseFromSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [availabilityZone](#API_CreateRelationalDatabaseFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabaseFromSnapshot-request-availabilityZone"></a>
The Availability Zone in which to create your new database. Use the `us-east-2a` case-sensitive format.
You can get a list of Availability Zones by using the `get regions` operation. Be sure to add the `include relational database Availability Zones` parameter to your request.
Type: String
Required: No

 ** [publiclyAccessible](#API_CreateRelationalDatabaseFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabaseFromSnapshot-request-publiclyAccessible"></a>
Specifies the accessibility options for your new database. A value of `true` specifies a database that is available to resources outside of your Lightsail account. A value of `false` specifies a database that is available only to your Lightsail resources in the same region as your database.
Type: Boolean
Required: No

 ** [relationalDatabaseBundleId](#API_CreateRelationalDatabaseFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabaseFromSnapshot-request-relationalDatabaseBundleId"></a>
The bundle ID for your new database. A bundle describes the performance specifications for your database.
You can get a list of database bundle IDs by using the `get relational database bundles` operation.
When creating a new database from a snapshot, you cannot choose a bundle that is smaller than the bundle of the source database.
Type: String
Required: No

 ** [relationalDatabaseName](#API_CreateRelationalDatabaseFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabaseFromSnapshot-request-relationalDatabaseName"></a>
The name to use for your new Lightsail database resource.
Constraints:
+ Must contain from 2 to 255 alphanumeric characters, or hyphens.
+ The first and last character must be a letter or number.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [relationalDatabaseSnapshotName](#API_CreateRelationalDatabaseFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabaseFromSnapshot-request-relationalDatabaseSnapshotName"></a>
The name of the database snapshot from which to create your new database.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [restoreTime](#API_CreateRelationalDatabaseFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabaseFromSnapshot-request-restoreTime"></a>
The date and time to restore your database from.
Constraints:
+ Must be before the latest restorable time for the database.
+ Cannot be specified if the `use latest restorable time` parameter is `true`.
+ Specified in Coordinated Universal Time (UTC).
+ Specified in the Unix time format.

  For example, if you wish to use a restore time of October 1, 2018, at 8 PM UTC, then you input `1538424000` as the restore time.
Type: Timestamp
Required: No

 ** [sourceRelationalDatabaseName](#API_CreateRelationalDatabaseFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabaseFromSnapshot-request-sourceRelationalDatabaseName"></a>
The name of the source database.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** [tags](#API_CreateRelationalDatabaseFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabaseFromSnapshot-request-tags"></a>
The tag keys and optional values to add to the resource during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [useLatestRestorableTime](#API_CreateRelationalDatabaseFromSnapshot_RequestSyntax) **   <a name="Lightsail-CreateRelationalDatabaseFromSnapshot-request-useLatestRestorableTime"></a>
Specifies whether your database is restored from the latest backup time. A value of `true` restores from the latest backup time.
Default: `false`
Constraints: Cannot be specified if the `restore time` parameter is provided.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateRelationalDatabaseFromSnapshot_ResponseSyntax"></a>

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
<a name="API_CreateRelationalDatabaseFromSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_CreateRelationalDatabaseFromSnapshot_ResponseSyntax) **   <a name="Lightsail-CreateRelationalDatabaseFromSnapshot-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_CreateRelationalDatabaseFromSnapshot_Errors"></a>

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
<a name="API_CreateRelationalDatabaseFromSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateRelationalDatabaseFromSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateRelationalDatabaseFromSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateRelationalDatabaseFromSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateRelationalDatabaseFromSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateRelationalDatabaseFromSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateRelationalDatabaseFromSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateRelationalDatabaseFromSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateRelationalDatabaseFromSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateRelationalDatabaseFromSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateRelationalDatabaseFromSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

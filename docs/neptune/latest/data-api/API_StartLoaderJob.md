---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_StartLoaderJob.html
---

# StartLoaderJob
<a name="API_StartLoaderJob"></a>

Starts a Neptune bulk loader job to load data from an Amazon S3 bucket into a Neptune DB instance. See [Using the Amazon Neptune Bulk Loader to Ingest Data](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html).

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:StartLoaderJob](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#startloaderjob) IAM action in that cluster.

## Request Syntax
<a name="API_StartLoaderJob_RequestSyntax"></a>

```
POST /loader HTTP/1.1
Content-type: application/json

{
   "dependencies": [ "{{string}}" ],
   "failOnError": {{boolean}},
   "format": "{{string}}",
   "iamRoleArn": "{{string}}",
   "mode": "{{string}}",
   "parallelism": "{{string}}",
   "parserConfiguration": {
      "{{string}}" : "{{string}}"
   },
   "queueRequest": {{boolean}},
   "region": "{{string}}",
   "source": "{{string}}",
   "updateSingleCardinalityProperties": {{boolean}},
   "userProvidedEdgeIds": {{boolean}}
}
```

## URI Request Parameters
<a name="API_StartLoaderJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartLoaderJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dependencies](#API_StartLoaderJob_RequestSyntax) **   <a name="neptunedata-StartLoaderJob-request-dependencies"></a>
This is an optional parameter that can make a queued load request contingent on the successful completion of one or more previous jobs in the queue.
Neptune can queue up as many as 64 load requests at a time, if their `queueRequest` parameters are set to `"TRUE"`. The `dependencies` parameter lets you make execution of such a queued request dependent on the successful completion of one or more specified previous requests in the queue.
For example, if load `Job-A` and `Job-B` are independent of each other, but load `Job-C` needs `Job-A` and `Job-B` to be finished before it begins, proceed as follows:

1. Submit `load-job-A` and `load-job-B` one after another in any order, and save their load-ids.

1. Submit `load-job-C` with the load-ids of the two jobs in its `dependencies` field:
Because of the `dependencies` parameter, the bulk loader will not start `Job-C` until `Job-A` and `Job-B` have completed successfully. If either one of them fails, Job-C will not be executed, and its status will be set to `LOAD_FAILED_BECAUSE_DEPENDENCY_NOT_SATISFIED`.
You can set up multiple levels of dependency in this way, so that the failure of one job will cause all requests that are directly or indirectly dependent on it to be cancelled.
Type: Array of strings
Required: No

 ** [failOnError](#API_StartLoaderJob_RequestSyntax) **   <a name="neptunedata-StartLoaderJob-request-failOnError"></a>
 ** `failOnError` **   –   A flag to toggle a complete stop on an error.
 *Allowed values*: `"TRUE"`, `"FALSE"`.
 *Default value*: `"TRUE"`.
When this parameter is set to `"FALSE"`, the loader tries to load all the data in the location specified, skipping any entries with errors.
When this parameter is set to `"TRUE"`, the loader stops as soon as it encounters an error. Data loaded up to that point persists.
Type: Boolean
Required: No

 ** [format](#API_StartLoaderJob_RequestSyntax) **   <a name="neptunedata-StartLoaderJob-request-format"></a>
The format of the data. For more information about data formats for the Neptune `Loader` command, see [Load Data Formats](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format.html).

**Allowed values**
+  ** `csv` ** for the [Gremlin CSV data format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html).
+  ** `opencypher` ** for the [openCypher CSV data format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html).
+  ** `ntriples` ** for the [N-Triples RDF data format](https://www.w3.org/TR/n-triples/).
+  ** `nquads` ** for the [N-Quads RDF data format](https://www.w3.org/TR/n-quads/).
+  ** `rdfxml` ** for the [RDF\\XML RDF data format](https://www.w3.org/TR/rdf-syntax-grammar/).
+  ** `turtle` ** for the [Turtle RDF data format](https://www.w3.org/TR/turtle/).
Type: String
Valid Values: `csv | opencypher | ntriples | nquads | rdfxml | turtle`
Required: Yes

 ** [iamRoleArn](#API_StartLoaderJob_RequestSyntax) **   <a name="neptunedata-StartLoaderJob-request-iamRoleArn"></a>
The Amazon Resource Name (ARN) for an IAM role to be assumed by the Neptune DB instance for access to the S3 bucket. The IAM role ARN provided here should be attached to the DB cluster (see [Adding the IAM Role to an Amazon Neptune Cluster](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-IAM-add-role-cluster.html).
Type: String
Required: Yes

 ** [mode](#API_StartLoaderJob_RequestSyntax) **   <a name="neptunedata-StartLoaderJob-request-mode"></a>
The load job mode.
 *Allowed values*: `RESUME`, `NEW`, `AUTO`.
 *Default value*: `AUTO`.
+  `RESUME`   –   In RESUME mode, the loader looks for a previous load from this source, and if it finds one, resumes that load job. If no previous load job is found, the loader stops.

  The loader avoids reloading files that were successfully loaded in a previous job. It only tries to process failed files. If you dropped previously loaded data from your Neptune cluster, that data is not reloaded in this mode. If a previous load job loaded all files from the same source successfully, nothing is reloaded, and the loader returns success.
+  `NEW`   –   In NEW mode, the creates a new load request regardless of any previous loads. You can use this mode to reload all the data from a source after dropping previously loaded data from your Neptune cluster, or to load new data available at the same source.
+  `AUTO`   –   In AUTO mode, the loader looks for a previous load job from the same source, and if it finds one, resumes that job, just as in `RESUME` mode.

  If the loader doesn't find a previous load job from the same source, it loads all data from the source, just as in `NEW` mode.
Type: String
Valid Values: `RESUME | NEW | AUTO`
Required: No

 ** [parallelism](#API_StartLoaderJob_RequestSyntax) **   <a name="neptunedata-StartLoaderJob-request-parallelism"></a>
The optional `parallelism` parameter can be set to reduce the number of threads used by the bulk load process.
 *Allowed values*:
+  `LOW` –   The number of threads used is the number of available vCPUs divided by 8.
+  `MEDIUM` –   The number of threads used is the number of available vCPUs divided by 2.
+  `HIGH` –   The number of threads used is the same as the number of available vCPUs.
+  `OVERSUBSCRIBE` –   The number of threads used is the number of available vCPUs multiplied by 2. If this value is used, the bulk loader takes up all available resources.

  This does not mean, however, that the `OVERSUBSCRIBE` setting results in 100% CPU utilization. Because the load operation is I/O bound, the highest CPU utilization to expect is in the 60% to 70% range.
 *Default value*: `HIGH`
The `parallelism` setting can sometimes result in a deadlock between threads when loading openCypher data. When this happens, Neptune returns the `LOAD_DATA_DEADLOCK` error. You can generally fix the issue by setting `parallelism` to a lower setting and retrying the load command.
Type: String
Valid Values: `LOW | MEDIUM | HIGH | OVERSUBSCRIBE`
Required: No

 ** [parserConfiguration](#API_StartLoaderJob_RequestSyntax) **   <a name="neptunedata-StartLoaderJob-request-parserConfiguration"></a>
 ** `parserConfiguration` **   –   An optional object with additional parser configuration values. Each of the child parameters is also optional:
+  ** `namedGraphUri` **   –   The default graph for all RDF formats when no graph is specified (for non-quads formats and NQUAD entries with no graph).

  The default is `https://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph`.
+  ** `baseUri` **   –   The base URI for RDF/XML and Turtle formats.

  The default is `https://aws.amazon.com/neptune/default`.
+  ** `allowEmptyStrings` **   –   Gremlin users need to be able to pass empty string values("") as node and edge properties when loading CSV data. If `allowEmptyStrings` is set to `false` (the default), such empty strings are treated as nulls and are not loaded.

  If `allowEmptyStrings` is set to `true`, the loader treats empty strings as valid property values and loads them accordingly.
Type: String to string map
Required: No

 ** [queueRequest](#API_StartLoaderJob_RequestSyntax) **   <a name="neptunedata-StartLoaderJob-request-queueRequest"></a>
This is an optional flag parameter that indicates whether the load request can be queued up or not.
You don't have to wait for one load job to complete before issuing the next one, because Neptune can queue up as many as 64 jobs at a time, provided that their `queueRequest` parameters are all set to `"TRUE"`. The queue order of the jobs will be first-in-first-out (FIFO).
If the `queueRequest` parameter is omitted or set to `"FALSE"`, the load request will fail if another load job is already running.
 *Allowed values*: `"TRUE"`, `"FALSE"`.
 *Default value*: `"FALSE"`.
Type: Boolean
Required: No

 ** [region](#API_StartLoaderJob_RequestSyntax) **   <a name="neptunedata-StartLoaderJob-request-region"></a>
The Amazon region of the S3 bucket. This must match the Amazon Region of the DB cluster.
Type: String
Valid Values: `us-east-1 | us-east-2 | us-west-1 | us-west-2 | ca-central-1 | sa-east-1 | eu-north-1 | eu-west-1 | eu-west-2 | eu-west-3 | eu-central-1 | me-south-1 | af-south-1 | ap-east-1 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | cn-north-1 | cn-northwest-1 | us-gov-west-1 | us-gov-east-1`
Required: Yes

 ** [source](#API_StartLoaderJob_RequestSyntax) **   <a name="neptunedata-StartLoaderJob-request-source"></a>
The `source` parameter accepts an S3 URI that identifies a single file, multiple files, a folder, or multiple folders. Neptune loads every data file in any folder that is specified.
The URI can be in any of the following formats.
+  `s3://(bucket_name)/(object-key-name)`
+  `https://s3.amazonaws.com/(bucket_name)/(object-key-name)`
+  `https://s3.us-east-1.amazonaws.com/(bucket_name)/(object-key-name)`
The `object-key-name` element of the URI is equivalent to the [prefix](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html#API_ListObjects_RequestParameters) parameter in an S3 [ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html) API call. It identifies all the objects in the specified S3 bucket whose names begin with that prefix. That can be a single file or folder, or multiple files and/or folders.
The specified folder or folders can contain multiple vertex files and multiple edge files.
Type: String
Required: Yes

 ** [updateSingleCardinalityProperties](#API_StartLoaderJob_RequestSyntax) **   <a name="neptunedata-StartLoaderJob-request-updateSingleCardinalityProperties"></a>
 `updateSingleCardinalityProperties` is an optional parameter that controls how the bulk loader treats a new value for single-cardinality vertex or edge properties. This is not supported for loading openCypher data.
 *Allowed values*: `"TRUE"`, `"FALSE"`.
 *Default value*: `"FALSE"`.
By default, or when `updateSingleCardinalityProperties` is explicitly set to `"FALSE"`, the loader treats a new value as an error, because it violates single cardinality.
When `updateSingleCardinalityProperties` is set to `"TRUE"`, on the other hand, the bulk loader replaces the existing value with the new one. If multiple edge or single-cardinality vertex property values are provided in the source file(s) being loaded, the final value at the end of the bulk load could be any one of those new values. The loader only guarantees that the existing value has been replaced by one of the new ones.
Type: Boolean
Required: No

 ** [userProvidedEdgeIds](#API_StartLoaderJob_RequestSyntax) **   <a name="neptunedata-StartLoaderJob-request-userProvidedEdgeIds"></a>
This parameter is required only when loading openCypher data that contains relationship IDs. It must be included and set to `True` when openCypher relationship IDs are explicitly provided in the load data (recommended).
When `userProvidedEdgeIds` is absent or set to `True`, an `:ID` column must be present in every relationship file in the load.
When `userProvidedEdgeIds` is present and set to `False`, relationship files in the load **must not** contain an `:ID` column. Instead, the Neptune loader automatically generates an ID for each relationship.
It's useful to provide relationship IDs explicitly so that the loader can resume loading after error in the CSV data have been fixed, without having to reload any relationships that have already been loaded. If relationship IDs have not been explicitly assigned, the loader cannot resume a failed load if any relationship file has had to be corrected, and must instead reload all the relationships.
Type: Boolean
Required: No

## Response Syntax
<a name="API_StartLoaderJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "payload": {
      "string" : "string"
   },
   "status": "string"
}
```

## Response Elements
<a name="API_StartLoaderJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [payload](#API_StartLoaderJob_ResponseSyntax) **   <a name="neptunedata-StartLoaderJob-response-payload"></a>
Contains a `loadId` name-value pair that provides an identifier for the load operation.
Type: String to string map

 ** [status](#API_StartLoaderJob_ResponseSyntax) **   <a name="neptunedata-StartLoaderJob-response-status"></a>
The HTTP return code indicating the status of the load job.
Type: String

## Errors
<a name="API_StartLoaderJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
Raised when a request is submitted that cannot be processed.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the bad request.
HTTP Status Code: 400

 ** BulkLoadIdNotFoundException **
Raised when a specified bulk-load job ID cannot be found.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The bulk-load job ID that could not be found.
HTTP Status Code: 404

 ** ClientTimeoutException **
Raised when a request timed out in the client.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 408

 ** ConstraintViolationException **
Raised when a value in a request field did not satisfy required constraints.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** IllegalArgumentException **
Raised when an argument in a request is not supported.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** InternalFailureException **
Raised when the processing of the request failed unexpectedly.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 500

 ** InvalidArgumentException **
Raised when an argument in a request has an invalid value.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** InvalidParameterException **
Raised when a parameter value is not valid.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that includes an invalid parameter.
HTTP Status Code: 400

 ** LoadUrlAccessDeniedException **
Raised when access is denied to a specified load URL.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** MissingParameterException **
Raised when a required parameter is missing.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in which the parameter is missing.
HTTP Status Code: 400

 ** PreconditionsFailedException **
Raised when a precondition for processing a request is not satisfied.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** S3Exception **
Raised when there is a problem accessing Amazon S3.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

 ** TooManyRequestsException **
Raised when the number of requests being processed exceeds the limit.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request that could not be processed for this reason.
HTTP Status Code: 429

 ** UnsupportedOperationException **
Raised when a request attempts to initiate an operation that is not supported.
 ** code **
The HTTP status code returned with the exception.
 ** detailedMessage **
A detailed message describing the problem.
 ** requestId **
The ID of the request in question.
HTTP Status Code: 400

## See Also
<a name="API_StartLoaderJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptunedata-2023-08-01/StartLoaderJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptunedata-2023-08-01/StartLoaderJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/StartLoaderJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptunedata-2023-08-01/StartLoaderJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/StartLoaderJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptunedata-2023-08-01/StartLoaderJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptunedata-2023-08-01/StartLoaderJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptunedata-2023-08-01/StartLoaderJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptunedata-2023-08-01/StartLoaderJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/StartLoaderJob)

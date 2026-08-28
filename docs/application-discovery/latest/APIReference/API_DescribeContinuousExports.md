---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeContinuousExports.html
---

# DescribeContinuousExports
<a name="API_DescribeContinuousExports"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Lists exports as specified by ID. All continuous exports associated with your user can be listed if you call `DescribeContinuousExports` as is without passing any parameters.

## Request Syntax
<a name="API_DescribeContinuousExports_RequestSyntax"></a>

```
{
   "exportIds": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeContinuousExports_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [exportIds](#API_DescribeContinuousExports_RequestSyntax) **   <a name="DiscServ-DescribeContinuousExports-request-exportIds"></a>
The unique IDs assigned to the exports.
Type: Array of strings
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: No

 ** [maxResults](#API_DescribeContinuousExports_RequestSyntax) **   <a name="DiscServ-DescribeContinuousExports-request-maxResults"></a>
A number between 1 and 100 specifying the maximum number of continuous export descriptions returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeContinuousExports_RequestSyntax) **   <a name="DiscServ-DescribeContinuousExports-request-nextToken"></a>
The token from the previous call to `DescribeExportTasks`.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeContinuousExports_ResponseSyntax"></a>

```
{
   "descriptions": [
      {
         "dataSource": "string",
         "exportId": "string",
         "s3Bucket": "string",
         "schemaStorageConfig": {
            "string" : "string"
         },
         "startTime": number,
         "status": "string",
         "statusDetail": "string",
         "stopTime": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeContinuousExports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [descriptions](#API_DescribeContinuousExports_ResponseSyntax) **   <a name="DiscServ-DescribeContinuousExports-response-descriptions"></a>
A list of continuous export descriptions.
Type: Array of [ContinuousExportDescription](API_ContinuousExportDescription.md) objects

 ** [nextToken](#API_DescribeContinuousExports_ResponseSyntax) **   <a name="DiscServ-DescribeContinuousExports-response-nextToken"></a>
The token from the previous call to `DescribeExportTasks`.
Type: String

## Errors
<a name="API_DescribeContinuousExports_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationErrorException **
The user does not have permission to perform the action. Check the IAM policy associated with this user.
HTTP Status Code: 400

 ** HomeRegionNotSetException **
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).
The home Region is not set. Set the home Region to continue.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters are not valid. Verify the parameters and try again.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.
HTTP Status Code: 400

 ** OperationNotPermittedException **
This operation is not permitted.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified configuration ID was not located. Verify the configuration ID and try again.
HTTP Status Code: 400

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## Examples
<a name="API_DescribeContinuousExports_Examples"></a>

### Describe a continuous export
<a name="API_DescribeContinuousExports_Example_1"></a>

The following example shows the request and response of describing a particular continuous export specified by passing in a value to `exportId` as well as other filtering parameters.

#### Sample Request
<a name="API_DescribeContinuousExports_Example_1_Request"></a>

```
{
    "maxResults": 10,
    "nextToken": "rLH9RloHsWvY1sljKfLwlmHioorNIJJ1TC9MDO6HolpInQgsQKfk30Zu5n9YP59JZ5k5NzAqs6YerZWY",
    "exportIds": [
        "continuous-export-181b77c3-7jf3-4610-924e-7acafe5bbc59"
    ]
}
```

#### Sample Response
<a name="API_DescribeContinuousExports_Example_1_Response"></a>

```
{
    "descriptions": [
        {
            "exportId": "continuous-export-181b77c3-7jf3-4610-924e-7acafe5bbc59",
            "status": "ACTIVE"
        },
        {
            "schemaStorageConfig": {
                "databaseName": "application_discovery_service_database"
            },
            "startTime": 1531248144.117,
            "exportId": "continuous-export-181b77c3-7jf3-4610-924e-7acafe5bbc59",
            "s3Bucket": "aws-application-discovery-service-92costafer5c9vn0qjane94mi",
            "status": "STOP_IN_PROGRESS",
            "stopTime": 1531248232.085,
            "statusDetail": "",
            "dataSource": "AGENT"
        }
    ]
}
```

## See Also
<a name="API_DescribeContinuousExports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/DescribeContinuousExports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/DescribeContinuousExports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/DescribeContinuousExports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/DescribeContinuousExports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/DescribeContinuousExports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/DescribeContinuousExports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/DescribeContinuousExports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/DescribeContinuousExports)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/DescribeContinuousExports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/DescribeContinuousExports)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

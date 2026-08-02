---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html
---

# StartExportTask
<a name="API_StartExportTask"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Begins the export of a discovered data report to an Amazon S3 bucket managed by AWS.

**Note**
Exports might provide an estimate of fees and savings based on certain information that you provide. Fee estimates do not include any taxes that might apply. Your actual fees and savings depend on a variety of factors, including your actual usage of AWS services, which might vary from the estimates provided in this report.

If you do not specify `preferences` or `agentIds` in the filter, a summary of all servers, applications, tags, and performance is generated. This data is an aggregation of all server data collected through on-premises tooling, file import, application grouping and applying tags.

If you specify `agentIds` in a filter, the task exports up to 72 hours of detailed data collected by the identified Application Discovery Agent, including network, process, and performance details. A time range for exported agent data may be set by using `startTime` and `endTime`. Export of detailed agent data is limited to five concurrently running exports. Export of detailed agent data is limited to two exports per day.

If you enable `ec2RecommendationsPreferences` in `preferences` [ExportPreferences](API_ExportPreferences.md), an Amazon EC2 instance matching the characteristics of each server in Application Discovery Service is generated. Changing the attributes of the `ec2RecommendationsPreferences` changes the criteria of the recommendation.

## Request Syntax
<a name="API_StartExportTask_RequestSyntax"></a>

```
{
   "endTime": {{number}},
   "exportDataFormat": [ "{{string}}" ],
   "filters": [
      {
         "condition": "{{string}}",
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "preferences": { ... },
   "startTime": {{number}}
}
```

## Request Parameters
<a name="API_StartExportTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endTime](#API_StartExportTask_RequestSyntax) **   <a name="DiscServ-StartExportTask-request-endTime"></a>
The end timestamp for exported data from the single Application Discovery Agent selected in the filters. If no value is specified, exported data includes the most recent data collected by the agent.
Type: Timestamp
Required: No

 ** [exportDataFormat](#API_StartExportTask_RequestSyntax) **   <a name="DiscServ-StartExportTask-request-exportDataFormat"></a>
The file format for the returned export data. Default value is `CSV`. **Note:** *The* `GRAPHML` *option has been deprecated.*
Type: Array of strings
Valid Values: `CSV`
Required: No

 ** [filters](#API_StartExportTask_RequestSyntax) **   <a name="DiscServ-StartExportTask-request-filters"></a>
If a filter is present, it selects the single `agentId` of the Application Discovery Agent for which data is exported. The `agentId` can be found in the results of the `DescribeAgents` API or CLI. If no filter is present, `startTime` and `endTime` are ignored and exported data includes both AWS Application Discovery Service Agentless Collector collectors data and summary data from Application Discovery Agent agents.
Type: Array of [ExportFilter](API_ExportFilter.md) objects
Required: No

 ** [preferences](#API_StartExportTask_RequestSyntax) **   <a name="DiscServ-StartExportTask-request-preferences"></a>
 Indicates the type of data that needs to be exported. Only one [ExportPreferences](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ExportPreferences.html) can be enabled at any time.
Type: [ExportPreferences](API_ExportPreferences.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [startTime](#API_StartExportTask_RequestSyntax) **   <a name="DiscServ-StartExportTask-request-startTime"></a>
The start timestamp for exported data from the single Application Discovery Agent selected in the filters. If no value is specified, data is exported starting from the first data collected by the agent.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_StartExportTask_ResponseSyntax"></a>

```
{
   "exportId": "string"
}
```

## Response Elements
<a name="API_StartExportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [exportId](#API_StartExportTask_ResponseSyntax) **   <a name="DiscServ-StartExportTask-response-exportId"></a>
A unique identifier used to query the status of an export request.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S*`

## Errors
<a name="API_StartExportTask_Errors"></a>

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

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## Examples
<a name="API_StartExportTask_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Specify export preferences
<a name="API_StartExportTask_Example_1"></a>

This example illustrates one usage of StartExportTask.

#### Sample Request
<a name="API_StartExportTask_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: discovery.us-west-2.amazonaws.com
Accept-Encoding: gzip, deflate
X-Amz-Target: AWSPoseidonService_V2015_11_01.StartExportTask
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "preferences": {
        "ec2RecommendationsPreferences": {
            "enabled": true,
            "cpuPerformanceMetricBasis": {
                "name": "AVG",
                "percentageAdjust": 3.14159
            },
            "ramPerformanceMetricBasis": {
                "name": "MAX",
                "percentageAdjust": 3.14159
            },
            "tenancy": "DEDICATED",
            "excludedInstanceTypes": ["m5.4xlarge", "r3.large", "t3"],
            "preferredRegion": "us-west-2",
            "reservedInstanceOptions": {
                "purchasingOption": "ALL_UPFRONT",
                "offeringClass": "STANDARD",
                "termLength": "ONE_YEAR"
            }
        }
    }
}
```

#### Sample Response
<a name="API_StartExportTask_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f
Content-Type: application/x-amz-json-1.1
Content-Length: 58
Date: Tue, 13 Jun 2023 00:44:54 GMT

{
   "exportId":"export-123a4b56-7c89-01d2-3ef4-example5678f"
}
```

## See Also
<a name="API_StartExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/StartExportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/StartExportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/StartExportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/StartExportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/StartExportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/StartExportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/StartExportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/StartExportTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/StartExportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/StartExportTask)

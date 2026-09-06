---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeBatchDeleteConfigurationTask.html
---

# DescribeBatchDeleteConfigurationTask
<a name="API_DescribeBatchDeleteConfigurationTask"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

 Takes a unique deletion task identifier as input and returns metadata about a configuration deletion task.

## Request Syntax
<a name="API_DescribeBatchDeleteConfigurationTask_RequestSyntax"></a>

```
{
   "taskId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeBatchDeleteConfigurationTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [taskId](#API_DescribeBatchDeleteConfigurationTask_RequestSyntax) **   <a name="DiscServ-DescribeBatchDeleteConfigurationTask-request-taskId"></a>
 The ID of the task to delete.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeBatchDeleteConfigurationTask_ResponseSyntax"></a>

```
{
   "task": {
      "configurationType": "string",
      "deletedConfigurations": [ "string" ],
      "deletionWarnings": [
         {
            "configurationId": "string",
            "warningCode": number,
            "warningText": "string"
         }
      ],
      "endTime": number,
      "failedConfigurations": [
         {
            "configurationId": "string",
            "errorMessage": "string",
            "errorStatusCode": number
         }
      ],
      "requestedConfigurations": [ "string" ],
      "startTime": number,
      "status": "string",
      "taskId": "string"
   }
}
```

## Response Elements
<a name="API_DescribeBatchDeleteConfigurationTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [task](#API_DescribeBatchDeleteConfigurationTask_ResponseSyntax) **   <a name="DiscServ-DescribeBatchDeleteConfigurationTask-response-task"></a>
 The `BatchDeleteConfigurationTask` that represents the deletion task being executed.
Type: [BatchDeleteConfigurationTask](API_BatchDeleteConfigurationTask.md) object

## Errors
<a name="API_DescribeBatchDeleteConfigurationTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationErrorException **
The user does not have permission to perform the action. Check the IAM policy associated with this user.
HTTP Status Code: 400

 ** HomeRegionNotSetException **
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).
The home Region is not set. Set the home Region to continue.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.
HTTP Status Code: 400

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## Examples
<a name="API_DescribeBatchDeleteConfigurationTask_Examples"></a>

###
<a name="API_DescribeBatchDeleteConfigurationTask_Example_1"></a>

The following example shows the request syntax for a deletion task that was previously started using [StartBatchDeleteConfigurationTask](API_StartBatchDeleteConfigurationTask.md) specified by the value passed to the required `taskId` parameter.

#### Sample Request
<a name="API_DescribeBatchDeleteConfigurationTask_Example_1_Request"></a>

```
{
    "taskId": "b941cc54-b0df-4cdd-90fc-70ef4293dfce"
}
```

###
<a name="API_DescribeBatchDeleteConfigurationTask_Example_2"></a>

The following example shows the response for a successful `DescribeBatchDeleteConfigurationTask` API call.

#### Sample Response
<a name="API_DescribeBatchDeleteConfigurationTask_Example_2_Response"></a>

```
{
      "task": {
        "configurationType": "SERVER",
        "deletedConfigurations": ["d-server-029yqlktuw2udm", "d-server-03alnm4z74f77f"],
        "deletionWarnings": [],
        "endTime": 1695765672.384,
        "failedConfigurations": [],
        "requestedConfigurations": ["d-server-029yqlktuw2udm", "d-server-03alnm4z74f77f"],
        "startTime": 1695755672.129,
        "status": "COMPLETED",
        "taskId": "b941cc54-b0df-4cdd-90fc-70ef4293dfce"
    }
}
```

## See Also
<a name="API_DescribeBatchDeleteConfigurationTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/DescribeBatchDeleteConfigurationTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/DescribeBatchDeleteConfigurationTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/DescribeBatchDeleteConfigurationTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/DescribeBatchDeleteConfigurationTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/DescribeBatchDeleteConfigurationTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/DescribeBatchDeleteConfigurationTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/DescribeBatchDeleteConfigurationTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/DescribeBatchDeleteConfigurationTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/DescribeBatchDeleteConfigurationTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/DescribeBatchDeleteConfigurationTask)

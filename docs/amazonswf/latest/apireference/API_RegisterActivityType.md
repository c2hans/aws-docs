---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html
---

# RegisterActivityType
<a name="API_RegisterActivityType"></a>

Registers a new *activity type* along with its configuration settings in the specified domain.

**Important**
A `TypeAlreadyExists` fault is returned if the type already exists in the domain. You cannot change any configuration settings of the type after its registration, and it must be registered as a new version.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ Constrain the following parameters by using a `Condition` element with the appropriate keys.
  +  `defaultTaskList.name`: String constraint. The key is `swf:defaultTaskList.name`.
  +  `name`: String constraint. The key is `swf:name`.
  +  `version`: String constraint. The key is `swf:version`.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_RegisterActivityType_RequestSyntax"></a>

```
{
   "defaultTaskHeartbeatTimeout": "{{string}}",
   "defaultTaskList": {
      "name": "{{string}}"
   },
   "defaultTaskPriority": "{{string}}",
   "defaultTaskScheduleToCloseTimeout": "{{string}}",
   "defaultTaskScheduleToStartTimeout": "{{string}}",
   "defaultTaskStartToCloseTimeout": "{{string}}",
   "description": "{{string}}",
   "domain": "{{string}}",
   "name": "{{string}}",
   "version": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterActivityType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [defaultTaskHeartbeatTimeout](#API_RegisterActivityType_RequestSyntax) **   <a name="SWF-RegisterActivityType-request-defaultTaskHeartbeatTimeout"></a>
If set, specifies the default maximum time before which a worker processing a task of this type must report progress by calling [RecordActivityTaskHeartbeat](API_RecordActivityTaskHeartbeat.md). If the timeout is exceeded, the activity task is automatically timed out. This default can be overridden when scheduling an activity task using the `ScheduleActivityTask` [Decision](API_Decision.md). If the activity worker subsequently attempts to record a heartbeat or returns a result, the activity worker receives an `UnknownResource` fault. In this case, Amazon SWF no longer considers the activity task to be valid; the activity worker should clean up the activity task.
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** [defaultTaskList](#API_RegisterActivityType_RequestSyntax) **   <a name="SWF-RegisterActivityType-request-defaultTaskList"></a>
If set, specifies the default task list to use for scheduling tasks of this activity type. This default task list is used if a task list isn't provided when a task is scheduled through the `ScheduleActivityTask` [Decision](API_Decision.md).
Type: [TaskList](API_TaskList.md) object
Required: No

 ** [defaultTaskPriority](#API_RegisterActivityType_RequestSyntax) **   <a name="SWF-RegisterActivityType-request-defaultTaskPriority"></a>
The default task priority to assign to the activity type. If not assigned, then `0` is used. Valid values are integers that range from Java's `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *in the *Amazon SWF Developer Guide*.*.
Type: String
Required: No

 ** [defaultTaskScheduleToCloseTimeout](#API_RegisterActivityType_RequestSyntax) **   <a name="SWF-RegisterActivityType-request-defaultTaskScheduleToCloseTimeout"></a>
If set, specifies the default maximum duration for a task of this activity type. This default can be overridden when scheduling an activity task using the `ScheduleActivityTask` [Decision](API_Decision.md).
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** [defaultTaskScheduleToStartTimeout](#API_RegisterActivityType_RequestSyntax) **   <a name="SWF-RegisterActivityType-request-defaultTaskScheduleToStartTimeout"></a>
If set, specifies the default maximum duration that a task of this activity type can wait before being assigned to a worker. This default can be overridden when scheduling an activity task using the `ScheduleActivityTask` [Decision](API_Decision.md).
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** [defaultTaskStartToCloseTimeout](#API_RegisterActivityType_RequestSyntax) **   <a name="SWF-RegisterActivityType-request-defaultTaskStartToCloseTimeout"></a>
If set, specifies the default maximum duration that a worker can take to process tasks of this activity type. This default can be overridden when scheduling an activity task using the `ScheduleActivityTask` [Decision](API_Decision.md).
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** [description](#API_RegisterActivityType_RequestSyntax) **   <a name="SWF-RegisterActivityType-request-description"></a>
A textual description of the activity type.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [domain](#API_RegisterActivityType_RequestSyntax) **   <a name="SWF-RegisterActivityType-request-domain"></a>
The name of the domain in which this activity is to be registered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [name](#API_RegisterActivityType_RequestSyntax) **   <a name="SWF-RegisterActivityType-request-name"></a>
The name of the activity type within the domain.
The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` \| `\u007f-\u009f`). Also, it must *not* be the literal string `arn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [version](#API_RegisterActivityType_RequestSyntax) **   <a name="SWF-RegisterActivityType-request-version"></a>
The version of the activity type.
The activity type consists of the name and version, the combination of which must be unique within the domain.
The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` \| `\u007f-\u009f`). Also, it must *not* be the literal string `arn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Elements
<a name="API_RegisterActivityType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RegisterActivityType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededFault **
Returned by any operation if a system imposed limitation has been reached. To address this fault you should either clean up unused resources or increase the limit by contacting AWS.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** OperationNotPermittedFault **
Returned when the caller doesn't have sufficient permissions to invoke the action.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** TypeAlreadyExistsFault **
Returned if the type already exists in the specified domain. You may get this fault if you are registering a type that is either already registered or deprecated, or if you undeprecate a type that is currently registered.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** UnknownResourceFault **
Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

## Examples
<a name="API_RegisterActivityType_Examples"></a>

### RegisterActivityType Example
<a name="API_RegisterActivityType_Example_1"></a>

This example illustrates one usage of RegisterActivityType.

#### Sample Request
<a name="API_RegisterActivityType_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: swf.us-east-1.amazonaws.com
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.25) Gecko/20111212 Firefox/3.6.25 ( .NET CLR 3.5.30729; .NET4.0E)
Accept: application/json, text/javascript, */*
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive
Content-Type: application/x-amz-json-1.0
X-Requested-With: XMLHttpRequest
X-Amz-Date: Sun, 15 Jan 2012 00:14:06 GMT
X-Amz-Target: SimpleWorkflowService.RegisterActivityType
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=F9cptqaGWa2H7LW3dpctF9J5svsB6FRZ4krghCRnml0=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 343
Pragma: no-cache
Cache-Control: no-cache

{
  "domain": "867530901",
  "defaultTaskScheduleToStartTimeout": "300",
  "name": "activityVerify",
  "defaultTaskHeartbeatTimeout": "120",
  "defaultTaskPriority": "10",
  "defaultTaskStartToCloseTimeout": "600",
  "defaultTaskScheduleToCloseTimeout": "900",
  "version": "1.0",
  "defaultTaskList": {
  "name": "mainTaskList"
  },
  "description": "Verify the customer credit card"
}
```

#### Sample Response
<a name="API_RegisterActivityType_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/json
x-amzn-RequestId: d68969c7-3f0d-11e1-9b11-7182192d0b57
```

## See Also
<a name="API_RegisterActivityType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/RegisterActivityType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/RegisterActivityType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/RegisterActivityType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/RegisterActivityType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/RegisterActivityType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/RegisterActivityType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/RegisterActivityType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/RegisterActivityType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/RegisterActivityType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/RegisterActivityType)

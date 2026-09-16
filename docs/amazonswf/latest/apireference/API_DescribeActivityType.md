---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeActivityType.html
---

# DescribeActivityType
<a name="API_DescribeActivityType"></a>

Returns information about the specified activity type. This includes configuration settings provided when the type was registered and other general information about the type.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ Constrain the following parameters by using a `Condition` element with the appropriate keys.
  +  `activityType.name`: String constraint. The key is `swf:activityType.name`.
  +  `activityType.version`: String constraint. The key is `swf:activityType.version`.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_DescribeActivityType_RequestSyntax"></a>

```
{
   "activityType": {
      "name": "{{string}}",
      "version": "{{string}}"
   },
   "domain": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeActivityType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [activityType](#API_DescribeActivityType_RequestSyntax) **   <a name="SWF-DescribeActivityType-request-activityType"></a>
The activity type to get information about. Activity types are identified by the `name` and `version` that were supplied when the activity was registered.
Type: [ActivityType](API_ActivityType.md) object
Required: Yes

 ** [domain](#API_DescribeActivityType_RequestSyntax) **   <a name="SWF-DescribeActivityType-request-domain"></a>
The name of the domain in which the activity type is registered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_DescribeActivityType_ResponseSyntax"></a>

```
{
   "configuration": {
      "defaultTaskHeartbeatTimeout": "string",
      "defaultTaskList": {
         "name": "string"
      },
      "defaultTaskPriority": "string",
      "defaultTaskScheduleToCloseTimeout": "string",
      "defaultTaskScheduleToStartTimeout": "string",
      "defaultTaskStartToCloseTimeout": "string"
   },
   "typeInfo": {
      "activityType": {
         "name": "string",
         "version": "string"
      },
      "creationDate": number,
      "deprecationDate": number,
      "description": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_DescribeActivityType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_DescribeActivityType_ResponseSyntax) **   <a name="SWF-DescribeActivityType-response-configuration"></a>
The configuration settings registered with the activity type.
Type: [ActivityTypeConfiguration](API_ActivityTypeConfiguration.md) object

 ** [typeInfo](#API_DescribeActivityType_ResponseSyntax) **   <a name="SWF-DescribeActivityType-response-typeInfo"></a>
General information about the activity type.
The status of activity type (returned in the ActivityTypeInfo structure) can be one of the following.
+  `REGISTERED` – The type is registered and available. Workers supporting this type should be running.
+  `DEPRECATED` – The type was deprecated using [DeprecateActivityType](API_DeprecateActivityType.md), but is still in use. You should keep workers supporting this type running. You cannot create new tasks of this type.
Type: [ActivityTypeInfo](API_ActivityTypeInfo.md) object

## Errors
<a name="API_DescribeActivityType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedFault **
Returned when the caller doesn't have sufficient permissions to invoke the action.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** UnknownResourceFault **
Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

## Examples
<a name="API_DescribeActivityType_Examples"></a>

### DescribeActivityType Example
<a name="API_DescribeActivityType_Example_1"></a>

This example illustrates one usage of DescribeActivityType.

#### Sample Request
<a name="API_DescribeActivityType_Example_1_Request"></a>

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
X-Amz-Date: Sun, 15 Jan 2012 03:04:10 GMT
X-Amz-Target: SimpleWorkflowService.DescribeActivityType
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=XiGRwOZNLt+ic3VBWvIlRGdcFcRJVSE8J7zyZLU3oXg=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 95
Pragma: no-cache
Cache-Control: no-cache

{
  "domain": "867530901",
  "activityType": {
  "version": "1.0",
  "name": "activityVerify"
  }
}
```

#### Sample Response
<a name="API_DescribeActivityType_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 387
Content-Type: application/json
x-amzn-RequestId: 98d56ff5-3f25-11e1-9b11-7182192d0b57

{
  "configuration": {
  "defaultTaskHeartbeatTimeout": "120",
  "defaultTaskList": {"name": "mainTaskList"},
  "defaultTaskPriority", "100",
  "defaultTaskScheduleToCloseTimeout": "900",
  "defaultTaskScheduleToStartTimeout": "300",
  "defaultTaskStartToCloseTimeout": "600"
  },
  "typeInfo": {
  "activityType": {"name": "activityVerify", "version": "1.0"},
  "creationDate": 1326586446.471,
  "description": "Verify the customer credit",
  "status": "REGISTERED"
  }
}
```

## See Also
<a name="API_DescribeActivityType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/DescribeActivityType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/DescribeActivityType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/DescribeActivityType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/DescribeActivityType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/DescribeActivityType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/DescribeActivityType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/DescribeActivityType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/DescribeActivityType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/DescribeActivityType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/DescribeActivityType)

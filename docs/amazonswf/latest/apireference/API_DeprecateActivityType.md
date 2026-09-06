---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateActivityType.html
---

# DeprecateActivityType
<a name="API_DeprecateActivityType"></a>

Deprecates the specified *activity type*. After an activity type has been deprecated, you cannot create new tasks of that activity type. Tasks of this type that were scheduled before the type was deprecated continue to run.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ Constrain the following parameters by using a `Condition` element with the appropriate keys.
  +  `activityType.name`: String constraint. The key is `swf:activityType.name`.
  +  `activityType.version`: String constraint. The key is `swf:activityType.version`.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_DeprecateActivityType_RequestSyntax"></a>

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
<a name="API_DeprecateActivityType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [activityType](#API_DeprecateActivityType_RequestSyntax) **   <a name="SWF-DeprecateActivityType-request-activityType"></a>
The activity type to deprecate.
Type: [ActivityType](API_ActivityType.md) object
Required: Yes

 ** [domain](#API_DeprecateActivityType_RequestSyntax) **   <a name="SWF-DeprecateActivityType-request-domain"></a>
The name of the domain in which the activity type is registered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Elements
<a name="API_DeprecateActivityType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeprecateActivityType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedFault **
Returned when the caller doesn't have sufficient permissions to invoke the action.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** TypeDeprecatedFault **
Returned when the specified activity or workflow type was already deprecated.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** UnknownResourceFault **
Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

## Examples
<a name="API_DeprecateActivityType_Examples"></a>

### DeprecateActivityType Example
<a name="API_DeprecateActivityType_Example_1"></a>

This example illustrates one usage of DeprecateActivityType.

#### Sample Request
<a name="API_DeprecateActivityType_Example_1_Request"></a>

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
X-Amz-Date: Mon, 16 Jan 2012 05:01:06 GMT
X-Amz-Target: SimpleWorkflowService.DeprecateActivityType
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=iX/mNMtNH6IaSNwfZq9hHOhDlLnp7buuj9tO93kRIrQ=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 95
Pragma: no-cache
Cache-Control: no-cache

{"domain": "867530901",
"activityType":
{"name": "activityVerify",
"version": "1.0"}
}
```

#### Sample Response
<a name="API_DeprecateActivityType_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/json
x-amzn-RequestId: 191ee17e-3fff-11e1-a23a-99d60383ae71
```

## See Also
<a name="API_DeprecateActivityType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/DeprecateActivityType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/DeprecateActivityType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/DeprecateActivityType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/DeprecateActivityType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/DeprecateActivityType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/DeprecateActivityType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/DeprecateActivityType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/DeprecateActivityType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/DeprecateActivityType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/DeprecateActivityType)

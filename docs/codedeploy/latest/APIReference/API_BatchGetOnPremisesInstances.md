---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetOnPremisesInstances.html
---

# BatchGetOnPremisesInstances
<a name="API_BatchGetOnPremisesInstances"></a>

Gets information about one or more on-premises instances. The maximum number of on-premises instances that can be returned is 25.

## Request Syntax
<a name="API_BatchGetOnPremisesInstances_RequestSyntax"></a>

```
{
   "instanceNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetOnPremisesInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [instanceNames](#API_BatchGetOnPremisesInstances_RequestSyntax) **   <a name="CodeDeploy-BatchGetOnPremisesInstances-request-instanceNames"></a>
The names of the on-premises instances about which to get information. The maximum number of instance names you can specify is 25.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetOnPremisesInstances_ResponseSyntax"></a>

```
{
   "instanceInfos": [
      {
         "deregisterTime": number,
         "iamSessionArn": "string",
         "iamUserArn": "string",
         "instanceArn": "string",
         "instanceName": "string",
         "registerTime": number,
         "tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetOnPremisesInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instanceInfos](#API_BatchGetOnPremisesInstances_ResponseSyntax) **   <a name="CodeDeploy-BatchGetOnPremisesInstances-response-instanceInfos"></a>
Information about the on-premises instances.
Type: Array of [InstanceInfo](API_InstanceInfo.md) objects

## Errors
<a name="API_BatchGetOnPremisesInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BatchLimitExceededException **
The maximum number of names or IDs allowed for this request (100) was exceeded.
HTTP Status Code: 400

 ** InstanceNameRequiredException **
An on-premises instance name was not specified.
HTTP Status Code: 400

 ** InvalidInstanceNameException **
The on-premises instance name was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_BatchGetOnPremisesInstances_Examples"></a>

### Example
<a name="API_BatchGetOnPremisesInstances_Example_1"></a>

This example illustrates one usage of BatchGetOnPremisesInstances.

#### Sample Request
<a name="API_BatchGetOnPremisesInstances_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 63
X-Amz-Target: CodeDeploy_20141006.BatchGetOnPremisesInstances
X-Amz-Date: 20160707T232825Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "instanceNames": [
        "grp-a-inst-1",
        "grp-a-inst-3"
    ]
}
```

#### Sample Response
<a name="API_BatchGetOnPremisesInstances_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: e895fb62-88cb-11e5-a908-6dc86959d072
Content-Type: application/x-amz-json-1.1
Content-Length: 303

{
    "instanceInfos": [
        {
            "iamUserArn": "arn:aws:iam::444455556666:user/janedoe",
            "instanceArn": "arn:aws:codedeploy:us-east-1:444455556666:instance/grp-a-inst-1_rDH556dxUG",
            "instanceName": "grp-a-inst-1",
            "registerTime": 1428086184.401,
            "tags": [
                {
                    "Key": "Name",
                    "Value": "Project-DEF"
                }
            ]
        }
    ]
}
```

## See Also
<a name="API_BatchGetOnPremisesInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/BatchGetOnPremisesInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/BatchGetOnPremisesInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/BatchGetOnPremisesInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/BatchGetOnPremisesInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/BatchGetOnPremisesInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/BatchGetOnPremisesInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/BatchGetOnPremisesInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/BatchGetOnPremisesInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/BatchGetOnPremisesInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/BatchGetOnPremisesInstances)

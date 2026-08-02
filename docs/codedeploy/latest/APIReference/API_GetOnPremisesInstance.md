---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetOnPremisesInstance.html
---

# GetOnPremisesInstance
<a name="API_GetOnPremisesInstance"></a>

 Gets information about an on-premises instance.

## Request Syntax
<a name="API_GetOnPremisesInstance_RequestSyntax"></a>

```
{
   "instanceName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetOnPremisesInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [instanceName](#API_GetOnPremisesInstance_RequestSyntax) **   <a name="CodeDeploy-GetOnPremisesInstance-request-instanceName"></a>
 The name of the on-premises instance about which to get information.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetOnPremisesInstance_ResponseSyntax"></a>

```
{
   "instanceInfo": {
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
}
```

## Response Elements
<a name="API_GetOnPremisesInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instanceInfo](#API_GetOnPremisesInstance_ResponseSyntax) **   <a name="CodeDeploy-GetOnPremisesInstance-response-instanceInfo"></a>
 Information about the on-premises instance.
Type: [InstanceInfo](API_InstanceInfo.md) object

## Errors
<a name="API_GetOnPremisesInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InstanceNameRequiredException **
An on-premises instance name was not specified.
HTTP Status Code: 400

 ** InstanceNotRegisteredException **
The specified on-premises instance is not registered.
HTTP Status Code: 400

 ** InvalidInstanceNameException **
The on-premises instance name was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_GetOnPremisesInstance_Examples"></a>

### Example
<a name="API_GetOnPremisesInstance_Example_1"></a>

This example illustrates one usage of GetOnPremisesInstance.

#### Sample Request
<a name="API_GetOnPremisesInstance_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 31
X-Amz-Target: CodeDeploy_20141006.GetOnPremisesInstance
X-Amz-Date: 20160707T020614Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
	"instanceName": "grp-c-inst-2"
}
```

#### Sample Response
<a name="API_GetOnPremisesInstance_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: caf06837-88e1-11e5-b0f5-a331fa97e4b5
Content-Type: application/x-amz-json-1.1
Content-Length: 386

{
    "InstanceInfo": {
        "deregisterTime": 1.446744190402E9,
        "iamUserArn": "arn:aws:iam::444455556666:user/janedoe",
        "instanceArn": "arn:aws:codedeploy:us-east-1:444455556666:instance/grp-e-inst-3_EJFIFC3LrD",
        "instanceName": "grp-o-inst-7",
        "registerTime": 1.446744207564E9,
        "tags": [
            {
                "Key": "Name",
                "Value": "Cost-Center-765"
            }
        ]
    }
}
```

## See Also
<a name="API_GetOnPremisesInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/GetOnPremisesInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/GetOnPremisesInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/GetOnPremisesInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/GetOnPremisesInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/GetOnPremisesInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/GetOnPremisesInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/GetOnPremisesInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/GetOnPremisesInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/GetOnPremisesInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/GetOnPremisesInstance)

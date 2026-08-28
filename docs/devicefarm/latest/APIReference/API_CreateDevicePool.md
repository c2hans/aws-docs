---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateDevicePool.html
---

# CreateDevicePool
<a name="API_CreateDevicePool"></a>

Creates a device pool.

## Request Syntax
<a name="API_CreateDevicePool_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "maxDevices": {{number}},
   "name": "{{string}}",
   "projectArn": "{{string}}",
   "rules": [
      {
         "attribute": "{{string}}",
         "operator": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateDevicePool_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateDevicePool_RequestSyntax) **   <a name="devicefarm-CreateDevicePool-request-description"></a>
The device pool's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** [maxDevices](#API_CreateDevicePool_RequestSyntax) **   <a name="devicefarm-CreateDevicePool-request-maxDevices"></a>
The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the `rules` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.
By specifying the maximum number of devices, you can control the costs that you incur by running tests.
Type: Integer
Required: No

 ** [name](#API_CreateDevicePool_RequestSyntax) **   <a name="devicefarm-CreateDevicePool-request-name"></a>
The device pool's name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** [projectArn](#API_CreateDevicePool_RequestSyntax) **   <a name="devicefarm-CreateDevicePool-request-projectArn"></a>
The ARN of the project for the device pool.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [rules](#API_CreateDevicePool_RequestSyntax) **   <a name="devicefarm-CreateDevicePool-request-rules"></a>
The device pool's rules.
Type: Array of [Rule](API_Rule.md) objects
Required: Yes

## Response Syntax
<a name="API_CreateDevicePool_ResponseSyntax"></a>

```
{
   "devicePool": {
      "arn": "string",
      "description": "string",
      "maxDevices": number,
      "name": "string",
      "rules": [
         {
            "attribute": "string",
            "operator": "string",
            "value": "string"
         }
      ],
      "type": "string"
   }
}
```

## Response Elements
<a name="API_CreateDevicePool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [devicePool](#API_CreateDevicePool_ResponseSyntax) **   <a name="devicefarm-CreateDevicePool-response-devicePool"></a>
The newly created device pool.
Type: [DevicePool](API_DevicePool.md) object

## Errors
<a name="API_CreateDevicePool_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit was exceeded.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateDevicePool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/CreateDevicePool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/CreateDevicePool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/CreateDevicePool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/CreateDevicePool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/CreateDevicePool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/CreateDevicePool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/CreateDevicePool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/CreateDevicePool)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/CreateDevicePool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/CreateDevicePool)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

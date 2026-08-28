---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateNetworkProfile.html
---

# CreateNetworkProfile
<a name="API_CreateNetworkProfile"></a>

Creates a network profile.

## Request Syntax
<a name="API_CreateNetworkProfile_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "downlinkBandwidthBits": {{number}},
   "downlinkDelayMs": {{number}},
   "downlinkJitterMs": {{number}},
   "downlinkLossPercent": {{number}},
   "name": "{{string}}",
   "projectArn": "{{string}}",
   "type": "{{string}}",
   "uplinkBandwidthBits": {{number}},
   "uplinkDelayMs": {{number}},
   "uplinkJitterMs": {{number}},
   "uplinkLossPercent": {{number}}
}
```

## Request Parameters
<a name="API_CreateNetworkProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateNetworkProfile_RequestSyntax) **   <a name="devicefarm-CreateNetworkProfile-request-description"></a>
The description of the network profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** [downlinkBandwidthBits](#API_CreateNetworkProfile_RequestSyntax) **   <a name="devicefarm-CreateNetworkProfile-request-downlinkBandwidthBits"></a>
The data throughput rate in bits per second, as an integer from 0 to 104857600.
Type: Long
Required: No

 ** [downlinkDelayMs](#API_CreateNetworkProfile_RequestSyntax) **   <a name="devicefarm-CreateNetworkProfile-request-downlinkDelayMs"></a>
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
Type: Long
Required: No

 ** [downlinkJitterMs](#API_CreateNetworkProfile_RequestSyntax) **   <a name="devicefarm-CreateNetworkProfile-request-downlinkJitterMs"></a>
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
Type: Long
Required: No

 ** [downlinkLossPercent](#API_CreateNetworkProfile_RequestSyntax) **   <a name="devicefarm-CreateNetworkProfile-request-downlinkLossPercent"></a>
Proportion of received packets that fail to arrive from 0 to 100 percent.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [name](#API_CreateNetworkProfile_RequestSyntax) **   <a name="devicefarm-CreateNetworkProfile-request-name"></a>
The name for the new network profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** [projectArn](#API_CreateNetworkProfile_RequestSyntax) **   <a name="devicefarm-CreateNetworkProfile-request-projectArn"></a>
The Amazon Resource Name (ARN) of the project for which you want to create a network profile.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [type](#API_CreateNetworkProfile_RequestSyntax) **   <a name="devicefarm-CreateNetworkProfile-request-type"></a>
The type of network profile to create. Valid values are listed here.
Type: String
Valid Values: `CURATED | PRIVATE`
Required: No

 ** [uplinkBandwidthBits](#API_CreateNetworkProfile_RequestSyntax) **   <a name="devicefarm-CreateNetworkProfile-request-uplinkBandwidthBits"></a>
The data throughput rate in bits per second, as an integer from 0 to 104857600.
Type: Long
Required: No

 ** [uplinkDelayMs](#API_CreateNetworkProfile_RequestSyntax) **   <a name="devicefarm-CreateNetworkProfile-request-uplinkDelayMs"></a>
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
Type: Long
Required: No

 ** [uplinkJitterMs](#API_CreateNetworkProfile_RequestSyntax) **   <a name="devicefarm-CreateNetworkProfile-request-uplinkJitterMs"></a>
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
Type: Long
Required: No

 ** [uplinkLossPercent](#API_CreateNetworkProfile_RequestSyntax) **   <a name="devicefarm-CreateNetworkProfile-request-uplinkLossPercent"></a>
Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## Response Syntax
<a name="API_CreateNetworkProfile_ResponseSyntax"></a>

```
{
   "networkProfile": {
      "arn": "string",
      "description": "string",
      "downlinkBandwidthBits": number,
      "downlinkDelayMs": number,
      "downlinkJitterMs": number,
      "downlinkLossPercent": number,
      "name": "string",
      "type": "string",
      "uplinkBandwidthBits": number,
      "uplinkDelayMs": number,
      "uplinkJitterMs": number,
      "uplinkLossPercent": number
   }
}
```

## Response Elements
<a name="API_CreateNetworkProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [networkProfile](#API_CreateNetworkProfile_ResponseSyntax) **   <a name="devicefarm-CreateNetworkProfile-response-networkProfile"></a>
The network profile that is returned by the create network profile request.
Type: [NetworkProfile](API_NetworkProfile.md) object

## Errors
<a name="API_CreateNetworkProfile_Errors"></a>

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
<a name="API_CreateNetworkProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/CreateNetworkProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/CreateNetworkProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/CreateNetworkProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/CreateNetworkProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/CreateNetworkProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/CreateNetworkProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/CreateNetworkProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/CreateNetworkProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/CreateNetworkProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/CreateNetworkProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

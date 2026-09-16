---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html
---

# DescribeConfigurationRecorders
<a name="API_DescribeConfigurationRecorders"></a>

Returns details for the configuration recorder you specify.

If a configuration recorder is not specified, this operation returns details for the customer managed configuration recorder configured for the account, if applicable.

**Note**
When making a request to this operation, you can only specify one configuration recorder.

## Request Syntax
<a name="API_DescribeConfigurationRecorders_RequestSyntax"></a>

```
{
   "Arn": "{{string}}",
   "ConfigurationRecorderNames": [ "{{string}}" ],
   "ServicePrincipal": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConfigurationRecorders_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Arn](#API_DescribeConfigurationRecorders_RequestSyntax) **   <a name="config-DescribeConfigurationRecorders-request-Arn"></a>
The Amazon Resource Name (ARN) of the configuration recorder that you want to specify.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** [ConfigurationRecorderNames](#API_DescribeConfigurationRecorders_RequestSyntax) **   <a name="config-DescribeConfigurationRecorders-request-ConfigurationRecorderNames"></a>
A list of names of the configuration recorders that you want to specify.
When making a request to this operation, you can only specify one configuration recorder.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [ServicePrincipal](#API_DescribeConfigurationRecorders_RequestSyntax) **   <a name="config-DescribeConfigurationRecorders-request-ServicePrincipal"></a>
For service-linked configuration recorders, you can use the service principal of the linked AWS service to specify the configuration recorder. This field is only supported for AWS service principals. For third-party service-linked configuration recorders, use `Arn` instead.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

## Response Syntax
<a name="API_DescribeConfigurationRecorders_ResponseSyntax"></a>

```
{
   "ConfigurationRecorders": [
      {
         "arn": "string",
         "connectorArn": "string",
         "name": "string",
         "recordingGroup": {
            "allSupported": boolean,
            "exclusionByResourceTypes": {
               "resourceTypes": [ "string" ]
            },
            "includeGlobalResourceTypes": boolean,
            "recordingStrategy": {
               "useOnly": "string"
            },
            "resourceTypes": [ "string" ]
         },
         "recordingMode": {
            "recordingFrequency": "string",
            "recordingModeOverrides": [
               {
                  "description": "string",
                  "recordingFrequency": "string",
                  "resourceTypes": [ "string" ]
               }
            ]
         },
         "recordingScope": "string",
         "roleARN": "string",
         "scopeConfiguration": {
            "allRegions": boolean,
            "includedRegions": [ "string" ],
            "scopeType": "string",
            "scopeValues": [ "string" ]
         },
         "servicePrincipal": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeConfigurationRecorders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationRecorders](#API_DescribeConfigurationRecorders_ResponseSyntax) **   <a name="config-DescribeConfigurationRecorders-response-ConfigurationRecorders"></a>
A list that contains the descriptions of the specified configuration recorders.
Type: Array of [ConfigurationRecorder](API_ConfigurationRecorder.md) objects

## Errors
<a name="API_DescribeConfigurationRecorders_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchConfigurationRecorderException **
You have specified a configuration recorder that does not exist.
HTTP Status Code: 400

 ** ValidationException **
The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.
For [PutStoredQuery](https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html), one of the following errors:
+ There are missing required fields.
+ The input value fails the validation.
+ You are trying to create more than 300 queries.
For [DescribeConfigurationRecorders](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html) and [DescribeConfigurationRecorderStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html), one of the following errors:
+ You have specified more than one configuration recorder.
+ You have provided a service principal for service-linked configuration recorder that is not valid.
For [AssociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html) and [DisassociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html), one of the following errors:
+ Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.
+ One or more of the specified resource types are already associated or disassociated with the configuration recorder.
+ For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.
For [DeleteServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html), one of the following errors:
+ You have provided both `Arn` and `ServicePrincipal`. Only one of `Arn` or `ServicePrincipal` can be specified.
+ You have provided a service principal for service-linked configuration recorder that is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeConfigurationRecorders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeConfigurationRecorders)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeConfigurationRecorders)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeConfigurationRecorders)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeConfigurationRecorders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeConfigurationRecorders)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeConfigurationRecorders)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeConfigurationRecorders)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeConfigurationRecorders)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeConfigurationRecorders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeConfigurationRecorders)

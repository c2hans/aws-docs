---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html
---

# PutConfigurationRecorder
<a name="API_PutConfigurationRecorder"></a>

Creates or updates the customer managed configuration recorder.

You can use this operation to create a new customer managed configuration recorder or to update the `roleARN` and the `recordingGroup` for an existing customer managed configuration recorder.

To start the customer managed configuration recorder and begin recording configuration changes for the resource types you specify, use the [StartConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigurationRecorder.html) operation.

For more information, see [**Working with the Configuration Recorder**](https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html) in the * AWS Config Developer Guide*.

**Note**
 **One customer managed configuration recorder per account per Region**
You can create only one customer managed configuration recorder for each account for each AWS Region.
 **Default is to record all supported resource types, excluding the global IAM resource types**
If you have not specified values for the `recordingGroup` field, the default for the customer managed configuration recorder is to record all supported resource types, excluding the global IAM resource types: `AWS::IAM::Group`, `AWS::IAM::Policy`, `AWS::IAM::Role`, and `AWS::IAM::User`.
 **Tags are added at creation and cannot be updated**
 `PutConfigurationRecorder` is an idempotent API. Subsequent requests won’t create a duplicate resource if one was already created. If a following request has different tags values, AWS Config will ignore these differences and treat it as an idempotent request of the previous. In this case, tags will not be updated, even if they are different.
Use [TagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html) to update tags after creation.

## Request Syntax
<a name="API_PutConfigurationRecorder_RequestSyntax"></a>

```
{
   "ConfigurationRecorder": {
      "arn": "{{string}}",
      "connectorArn": "{{string}}",
      "name": "{{string}}",
      "recordingGroup": {
         "allSupported": {{boolean}},
         "exclusionByResourceTypes": {
            "resourceTypes": [ "{{string}}" ]
         },
         "includeGlobalResourceTypes": {{boolean}},
         "recordingStrategy": {
            "useOnly": "{{string}}"
         },
         "resourceTypes": [ "{{string}}" ]
      },
      "recordingMode": {
         "recordingFrequency": "{{string}}",
         "recordingModeOverrides": [
            {
               "description": "{{string}}",
               "recordingFrequency": "{{string}}",
               "resourceTypes": [ "{{string}}" ]
            }
         ]
      },
      "recordingScope": "{{string}}",
      "roleARN": "{{string}}",
      "scopeConfiguration": {
         "allRegions": {{boolean}},
         "includedRegions": [ "{{string}}" ],
         "scopeType": "{{string}}",
         "scopeValues": [ "{{string}}" ]
      },
      "servicePrincipal": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutConfigurationRecorder_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationRecorder](#API_PutConfigurationRecorder_RequestSyntax) **   <a name="config-PutConfigurationRecorder-request-ConfigurationRecorder"></a>
An object for the configuration recorder. A configuration recorder records configuration changes for the resource types in scope.
Type: [ConfigurationRecorder](API_ConfigurationRecorder.md) object
Required: Yes

 ** [Tags](#API_PutConfigurationRecorder_RequestSyntax) **   <a name="config-PutConfigurationRecorder-request-Tags"></a>
The tags for the customer managed configuration recorder. Each tag consists of a key and an optional value, both of which you define.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Elements
<a name="API_PutConfigurationRecorder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutConfigurationRecorder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRecorderNameException **
The configuration recorder name is not valid. The prefix "`AWSConfigurationRecorderFor`" is reserved for service-linked configuration recorders.
HTTP Status Code: 400

 ** InvalidRecordingGroupException **
One of the following errors:
+ You have provided a combination of parameter values that is not valid. For example:
  + Setting the `allSupported` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) to `true`, but providing a non-empty list for the `resourceTypes`field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html).
  + Setting the `allSupported` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) to `true`, but also setting the `useOnly` field of [RecordingStrategy](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html) to `EXCLUSION_BY_RESOURCE_TYPES`.
+ Every parameter is either null, false, or empty.
+ You have reached the limit of the number of resource types you can provide for the recording group.
+ You have provided resource types or a recording strategy that are not valid.
HTTP Status Code: 400

 ** InvalidRoleException **
You have provided a null or empty Amazon Resource Name (ARN) for the IAM role assumed by AWS Config and used by the customer managed configuration recorder.
HTTP Status Code: 400

 ** MaxNumberOfConfigurationRecordersExceededException **
You have reached the limit of the number of configuration recorders you can create.
HTTP Status Code: 400

 ** UnmodifiableEntityException **
The requested operation is not valid.
For [PutConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html), you will see this exception because you cannot use this operation to create a service-linked configuration recorder. Use the [PutServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html) operation to create a service-linked configuration recorder.
For [DeleteConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConfigurationRecorder.html), you will see this exception because you cannot use this operation to delete a service-linked configuration recorder. Use the [DeleteServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html) operation to delete a service-linked configuration recorder.
For [StartConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigurationRecorder.html) and [StopConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html), you will see this exception because these operations do not affect service-linked configuration recorders. Service-linked configuration recorders are always recording. To stop recording, you must delete the service-linked configuration recorder. Use the [DeleteServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html) operation to delete a service-linked configuration recorder.
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
<a name="API_PutConfigurationRecorder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/PutConfigurationRecorder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/PutConfigurationRecorder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PutConfigurationRecorder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/PutConfigurationRecorder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PutConfigurationRecorder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/PutConfigurationRecorder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/PutConfigurationRecorder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/PutConfigurationRecorder)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutConfigurationRecorder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PutConfigurationRecorder)

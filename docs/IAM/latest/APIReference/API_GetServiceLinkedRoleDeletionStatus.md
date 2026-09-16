---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.html
---

# GetServiceLinkedRoleDeletionStatus
<a name="API_GetServiceLinkedRoleDeletionStatus"></a>

Retrieves the status of your service-linked role deletion. After you use [DeleteServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteServiceLinkedRole.html) to submit a service-linked role for deletion, you can use the `DeletionTaskId` parameter in `GetServiceLinkedRoleDeletionStatus` to check the status of the deletion. If the deletion fails, this operation returns the reason that it failed, if that information is returned by the service.

## Request Parameters
<a name="API_GetServiceLinkedRoleDeletionStatus_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DeletionTaskId **
The deletion task identifier. This identifier is returned by the [DeleteServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteServiceLinkedRole.html) operation in the format `task/aws-service-role/<service-principal-name>/<role-name>/<task-uuid>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Response Elements
<a name="API_GetServiceLinkedRoleDeletionStatus_ResponseElements"></a>

The following elements are returned by the service.

 ** Reason **
An object that contains details about the reason the deletion failed.
Type: [DeletionTaskFailureReasonType](API_DeletionTaskFailureReasonType.md) object

 ** Status **
The status of the deletion.
Type: String
Valid Values: `SUCCEEDED | IN_PROGRESS | FAILED | NOT_STARTED`

## Errors
<a name="API_GetServiceLinkedRoleDeletionStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GetServiceLinkedRoleDeletionStatus_Examples"></a>

### Example
<a name="API_GetServiceLinkedRoleDeletionStatus_Example_1"></a>

The following example shows how to retrieve the status of the `DeletionTaskId` service-lined role deletion.

#### Sample Request
<a name="API_GetServiceLinkedRoleDeletionStatus_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetServiceLinkedRoleDeletionStatus
&DeletionTaskId=task%2Faws-service-role%2Flex.amazonaws.com%2AWSServiceRoleForLexBots%2Fec720f7a-c0ba-4838-be33-f72e1873dd52
&Version=2010-05-08
```

### Example
<a name="API_GetServiceLinkedRoleDeletionStatus_Example_2"></a>

The following example shows the status of the successful `DeletionTaskId` service-lined role deletion.

#### Sample Response
<a name="API_GetServiceLinkedRoleDeletionStatus_Example_2_Response"></a>

```
<GetServiceLinkedRoleDeletionStatusResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetServiceLinkedRoleDeletionStatusResult>
    <Status>SUCCEEDED</Status>
  </GetServiceLinkedRoleDeletionStatusResult>
  <ResponseMetadata>
    <RequestId>aa9259f4-8297-11e7-9f8f-8b008627ec76</RequestId>
  </ResponseMetadata>
</GetServiceLinkedRoleDeletionStatusResponse>
```

### Example
<a name="API_GetServiceLinkedRoleDeletionStatus_Example_3"></a>

The following example shows the status of the failed `DeletionTaskId` service-lined role deletion.

#### Sample Response
<a name="API_GetServiceLinkedRoleDeletionStatus_Example_3_Response"></a>

```
<GetServiceLinkedRoleDeletionStatusResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetServiceLinkedRoleDeletionStatusResult>
    <Status>FAILED</Status>
  </GetServiceLinkedRoleDeletionStatusResult>
  <DeletionTaskFailureReasonType>
    <Reason>role is being used</Reason>
    <RoleUsageList>
      <RoleUsageType>
        <Region>us-east-1</Region>
        <Resources>
          <Resource>arn1<Resource>
          <Resource>arn2<Resource>
        </Resources>
      </RoleUsageType>
      <RoleUsageType>
        <Region>us-west-2</Region>
        <Resources>
          <Resource>arn3<Resource>
          <Resource>arn4<Resource>
        </Resources>
      </RoleUsageType>
    </RoleUsageList>
  </DeletionTaskFailureReasonType>
  <ResponseMetadata>
    <RequestId>aa9259f4-8297-11e7-9f8f-8b008627ec76</RequestId>
  </ResponseMetadata>
</GetServiceLinkedRoleDeletionStatusResponse>
```

## See Also
<a name="API_GetServiceLinkedRoleDeletionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetServiceLinkedRoleDeletionStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetServiceLinkedRoleDeletionStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetServiceLinkedRoleDeletionStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetServiceLinkedRoleDeletionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetServiceLinkedRoleDeletionStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetServiceLinkedRoleDeletionStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetServiceLinkedRoleDeletionStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetServiceLinkedRoleDeletionStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetServiceLinkedRoleDeletionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetServiceLinkedRoleDeletionStatus)

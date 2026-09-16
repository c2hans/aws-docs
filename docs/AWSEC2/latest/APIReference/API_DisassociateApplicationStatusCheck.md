---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateApplicationStatusCheck.html
---

# DisassociateApplicationStatusCheck
<a name="API_DisassociateApplicationStatusCheck"></a>

Disassociates an application status check from instances or [tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html). After disassociation, health monitoring stops for the affected instances. The following rules apply:
+ You must specify either `TargetTagAssociations` or `InstanceIds`, but not both. Specifying both results in an `InvalidParameterCombination` error.
+ The application status check must already exist and belong to your account.
+ Tag keys must not be blank.

## Request Parameters
<a name="API_DisassociateApplicationStatusCheck_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ApplicationStatusCheckId**
The ID of the application status check to disassociate.
Type: String
Required: Yes

 **ClientToken**
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a request with the same token, the service ignores the request but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId.N**
The IDs of the instances to disassociate from the application status check.
Type: Array of strings
Required: No

 **TargetTagAssociation.N**
The [tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) to disassociate from the application status check. Specify the same key-value pairs that were used during association.
Type: Array of [CustomTagKeyValueRequestPair](API_CustomTagKeyValueRequestPair.md) objects
Required: No

## Response Elements
<a name="API_DisassociateApplicationStatusCheck_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **successfulResultSet**
The associations that were successfully removed.
Type: Array of [SuccessfulAssociationResponseObject](API_SuccessfulAssociationResponseObject.md) objects

 **unsuccessfulResultSet**
The associations that failed to be removed.
Type: Array of [UnsuccessfulAssociationResponseObject](API_UnsuccessfulAssociationResponseObject.md) objects

## Errors
<a name="API_DisassociateApplicationStatusCheck_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisassociateApplicationStatusCheck_Examples"></a>

### To disassociate an application status check from instances
<a name="API_DisassociateApplicationStatusCheck_Example_1"></a>

This example disassociates an application status check from the specified instance.

#### Sample Request
<a name="API_DisassociateApplicationStatusCheck_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisassociateApplicationStatusCheck
&ApplicationStatusCheckId=asc-0123456789abcdef0
&InstanceId.1=i-0123456789abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisassociateApplicationStatusCheck_Example_1_Response"></a>

```
<DisassociateApplicationStatusCheckResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <successfulResultSet>
        <item>
            <applicationStatusCheckId>asc-0123456789abcdef0</applicationStatusCheckId>
            <associationType>INSTANCE_ID</associationType>
            <associationValue>i-0123456789abcdef0</associationValue>
        </item>
    </successfulResultSet>
</DisassociateApplicationStatusCheckResult>
```

### To disassociate an application status check from tags
<a name="API_DisassociateApplicationStatusCheck_Example_2"></a>

The following example disassociates an application status check from instances with the specified tag.

#### Sample Request
<a name="API_DisassociateApplicationStatusCheck_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisassociateApplicationStatusCheck
&ApplicationStatusCheckId=asc-0123456789abcdef0
&TargetTagAssociation.1.Key=environment
&TargetTagAssociation.1.Value=production
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisassociateApplicationStatusCheck_Example_2_Response"></a>

```
<DisassociateApplicationStatusCheckResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <successfulResultSet>
        <item>
            <applicationStatusCheckId>asc-0123456789abcdef0</applicationStatusCheckId>
            <associationType>EC2TAG</associationType>
            <associationValue>environment=production</associationValue>
        </item>
    </successfulResultSet>
</DisassociateApplicationStatusCheckResult>
```

## See Also
<a name="API_DisassociateApplicationStatusCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisassociateApplicationStatusCheck)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisassociateApplicationStatusCheck)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisassociateApplicationStatusCheck)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisassociateApplicationStatusCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisassociateApplicationStatusCheck)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisassociateApplicationStatusCheck)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisassociateApplicationStatusCheck)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisassociateApplicationStatusCheck)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisassociateApplicationStatusCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisassociateApplicationStatusCheck)

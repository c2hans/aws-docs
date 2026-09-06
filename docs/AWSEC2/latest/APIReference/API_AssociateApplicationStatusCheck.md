---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateApplicationStatusCheck.html
---

# AssociateApplicationStatusCheck
<a name="API_AssociateApplicationStatusCheck"></a>

Associates an application status check with instances or [tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html). Once you create an association, health monitoring automatically begins for the specified instances or for instances that match the specified tags. The following rules apply:
+ You must specify either `TargetTagAssociations` or `InstanceIds`, but not both. Specifying both results in an `InvalidParameterCombination` error.
+ You must own the application status check. The check must already exist in your account.
+ You must not leave tag keys blank.
+ You can create a maximum of 50 tag associations for each application status check.
+ You can use `DisassociateApplicationStatusCheck` to remove associations.
+ You can associate [tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) so that the application status check automatically monitors all current and future instances that have the specified tags.

## Request Parameters
<a name="API_AssociateApplicationStatusCheck_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ApplicationStatusCheckId**
The ID of the application status check to associate.
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
The IDs of the instances to associate with the application status check.
Type: Array of strings
Required: No

 **TargetTagAssociation.N**
The [tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) to associate the application status check with. Each tag is a key-value pair. When you associate tags, the application status check automatically monitors all instances that have the specified tags.
Type: Array of [CustomTagKeyValueRequestPair](API_CustomTagKeyValueRequestPair.md) objects
Required: No

## Response Elements
<a name="API_AssociateApplicationStatusCheck_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **successfulResultSet**
The associations that were successfully created.
Type: Array of [SuccessfulAssociationResponseObject](API_SuccessfulAssociationResponseObject.md) objects

 **unsuccessfulResultSet**
The associations that failed to be created.
Type: Array of [UnsuccessfulAssociationResponseObject](API_UnsuccessfulAssociationResponseObject.md) objects

## Errors
<a name="API_AssociateApplicationStatusCheck_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AssociateApplicationStatusCheck_Examples"></a>

### To associate an application status check with instances
<a name="API_AssociateApplicationStatusCheck_Example_1"></a>

This example associates an application status check with the specified instance.

#### Sample Request
<a name="API_AssociateApplicationStatusCheck_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssociateApplicationStatusCheck
&ApplicationStatusCheckId=asc-0123456789abcdef0
&InstanceId.1=i-0123456789abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_AssociateApplicationStatusCheck_Example_1_Response"></a>

```
<AssociateApplicationStatusCheckResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <successfulResultSet>
        <item>
            <applicationStatusCheckId>asc-0123456789abcdef0</applicationStatusCheckId>
            <associationType>INSTANCE_ID</associationType>
            <associationValue>i-0123456789abcdef0</associationValue>
        </item>
    </successfulResultSet>
</AssociateApplicationStatusCheckResult>
```

### To associate an application status check with tags
<a name="API_AssociateApplicationStatusCheck_Example_2"></a>

The following example associates an application status check with instances that have the specified tag. All current and future instances with this tag are automatically monitored.

#### Sample Request
<a name="API_AssociateApplicationStatusCheck_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssociateApplicationStatusCheck
&ApplicationStatusCheckId=asc-0123456789abcdef0
&TargetTagAssociation.1.Key=environment
&TargetTagAssociation.1.Value=production
&AUTHPARAMS
```

#### Sample Response
<a name="API_AssociateApplicationStatusCheck_Example_2_Response"></a>

```
<AssociateApplicationStatusCheckResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <successfulResultSet>
        <item>
            <applicationStatusCheckId>asc-0123456789abcdef0</applicationStatusCheckId>
            <associationType>EC2TAG</associationType>
            <associationValue>environment=production</associationValue>
        </item>
    </successfulResultSet>
</AssociateApplicationStatusCheckResult>
```

## See Also
<a name="API_AssociateApplicationStatusCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssociateApplicationStatusCheck)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssociateApplicationStatusCheck)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociateApplicationStatusCheck)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssociateApplicationStatusCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociateApplicationStatusCheck)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssociateApplicationStatusCheck)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssociateApplicationStatusCheck)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssociateApplicationStatusCheck)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssociateApplicationStatusCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociateApplicationStatusCheck)

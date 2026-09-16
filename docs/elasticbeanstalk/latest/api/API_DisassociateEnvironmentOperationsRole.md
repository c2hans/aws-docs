---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DisassociateEnvironmentOperationsRole.html
---

# DisassociateEnvironmentOperationsRole
<a name="API_DisassociateEnvironmentOperationsRole"></a>

**Important**
The operations role feature of AWS Elastic Beanstalk is in beta release and is subject to change.

Disassociate the operations role from an environment. After this call is made, Elastic Beanstalk uses the caller's permissions for permissions to downstream services during subsequent calls acting on this environment.

## Request Parameters
<a name="API_DisassociateEnvironmentOperationsRole_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EnvironmentName **
The name of the environment from which to disassociate the operations role.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: Yes

## Errors
<a name="API_DisassociateEnvironmentOperationsRole_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

## Examples
<a name="API_DisassociateEnvironmentOperationsRole_Examples"></a>

### Example
<a name="API_DisassociateEnvironmentOperationsRole_Example_1"></a>

This example illustrates one usage of DisassociateEnvironmentOperationsRole.

#### Sample Request
<a name="API_DisassociateEnvironmentOperationsRole_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?EnvironmentName=MyEnv
&Operation=DisassociateEnvironmentOperationsRole
&AuthParams
```

#### Sample Response
<a name="API_DisassociateEnvironmentOperationsRole_Example_1_Response"></a>

```
<DisassociateEnvironmentOperationsRoleResponse xmlns="http://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <ResponseMetadata>
    <RequestId>f4e1b145-9080-11e0-8e5a-a558e0ce1fc4</RequestId>
  </ResponseMetadata>
</DisassociateEnvironmentOperationsRoleResponse>
```

## See Also
<a name="API_DisassociateEnvironmentOperationsRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DisassociateEnvironmentOperationsRole)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DisassociateEnvironmentOperationsRole)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DisassociateEnvironmentOperationsRole)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DisassociateEnvironmentOperationsRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DisassociateEnvironmentOperationsRole)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DisassociateEnvironmentOperationsRole)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DisassociateEnvironmentOperationsRole)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DisassociateEnvironmentOperationsRole)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DisassociateEnvironmentOperationsRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DisassociateEnvironmentOperationsRole)

---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_BatchDisassociateUserStack.html
---

# BatchDisassociateUserStack
<a name="API_BatchDisassociateUserStack"></a>

Disassociates the specified users from the specified stacks.

## Request Syntax
<a name="API_BatchDisassociateUserStack_RequestSyntax"></a>

```
{
   "UserStackAssociations": [
      {
         "AuthenticationType": "{{string}}",
         "SendEmailNotification": {{boolean}},
         "StackName": "{{string}}",
         "UserName": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_BatchDisassociateUserStack_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [UserStackAssociations](#API_BatchDisassociateUserStack_RequestSyntax) **   <a name="WorkSpacesApplications-BatchDisassociateUserStack-request-UserStackAssociations"></a>
The list of UserStackAssociation objects.
Type: Array of [UserStackAssociation](API_UserStackAssociation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_BatchDisassociateUserStack_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "UserStackAssociation": {
            "AuthenticationType": "string",
            "SendEmailNotification": boolean,
            "StackName": "string",
            "UserName": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_BatchDisassociateUserStack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchDisassociateUserStack_ResponseSyntax) **   <a name="WorkSpacesApplications-BatchDisassociateUserStack-response-errors"></a>
The list of UserStackAssociationError objects.
Type: Array of [UserStackAssociationError](API_UserStackAssociationError.md) objects

## Errors
<a name="API_BatchDisassociateUserStack_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_BatchDisassociateUserStack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/BatchDisassociateUserStack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/BatchDisassociateUserStack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/BatchDisassociateUserStack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/BatchDisassociateUserStack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/BatchDisassociateUserStack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/BatchDisassociateUserStack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/BatchDisassociateUserStack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/BatchDisassociateUserStack)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/BatchDisassociateUserStack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/BatchDisassociateUserStack)

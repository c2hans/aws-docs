---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StopAppBlockBuilder.html
---

# StopAppBlockBuilder
<a name="API_StopAppBlockBuilder"></a>

Stops an app block builder.

Stopping an app block builder terminates the instance, and the instance state is not persisted.

## Request Syntax
<a name="API_StopAppBlockBuilder_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_StopAppBlockBuilder_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_StopAppBlockBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-StopAppBlockBuilder-request-Name"></a>
The name of the app block builder.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Syntax
<a name="API_StopAppBlockBuilder_ResponseSyntax"></a>

```
{
   "AppBlockBuilder": {
      "AccessEndpoints": [
         {
            "EndpointType": "string",
            "VpceId": "string"
         }
      ],
      "AppBlockBuilderErrors": [
         {
            "ErrorCode": "string",
            "ErrorMessage": "string",
            "ErrorTimestamp": number
         }
      ],
      "Arn": "string",
      "CreatedTime": number,
      "Description": "string",
      "DisableIMDSV1": boolean,
      "DisplayName": "string",
      "EnableDefaultInternetAccess": boolean,
      "IamRoleArn": "string",
      "InstanceType": "string",
      "Name": "string",
      "Platform": "string",
      "State": "string",
      "StateChangeReason": {
         "Code": "string",
         "Message": "string"
      },
      "VpcConfig": {
         "SecurityGroupIds": [ "string" ],
         "SubnetIds": [ "string" ]
      }
   }
}
```

## Response Elements
<a name="API_StopAppBlockBuilder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppBlockBuilder](#API_StopAppBlockBuilder_ResponseSyntax) **   <a name="WorkSpacesApplications-StopAppBlockBuilder-response-AppBlockBuilder"></a>
Describes an app block builder.
Type: [AppBlockBuilder](API_AppBlockBuilder.md) object

## Errors
<a name="API_StopAppBlockBuilder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_StopAppBlockBuilder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/StopAppBlockBuilder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/StopAppBlockBuilder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/StopAppBlockBuilder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/StopAppBlockBuilder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/StopAppBlockBuilder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/StopAppBlockBuilder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/StopAppBlockBuilder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/StopAppBlockBuilder)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/StopAppBlockBuilder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/StopAppBlockBuilder)

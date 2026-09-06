---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeCustomWorkspaceImageImport.html
---

# DescribeCustomWorkspaceImageImport
<a name="API_DescribeCustomWorkspaceImageImport"></a>

Retrieves information about a WorkSpace BYOL image being imported via ImportCustomWorkspaceImage.

## Request Syntax
<a name="API_DescribeCustomWorkspaceImageImport_RequestSyntax"></a>

```
{
   "ImageId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCustomWorkspaceImageImport_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ImageId](#API_DescribeCustomWorkspaceImageImport_RequestSyntax) **   <a name="WorkSpaces-DescribeCustomWorkspaceImageImport-request-ImageId"></a>
The identifier of the WorkSpace image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`
Required: Yes

## Response Syntax
<a name="API_DescribeCustomWorkspaceImageImport_ResponseSyntax"></a>

```
{
   "Created": number,
   "ErrorDetails": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string"
      }
   ],
   "ImageBuilderInstanceId": "string",
   "ImageId": "string",
   "ImageSource": { ... },
   "InfrastructureConfigurationArn": "string",
   "LastUpdatedTime": number,
   "ProgressPercentage": number,
   "State": "string",
   "StateMessage": "string"
}
```

## Response Elements
<a name="API_DescribeCustomWorkspaceImageImport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Created](#API_DescribeCustomWorkspaceImageImport_ResponseSyntax) **   <a name="WorkSpaces-DescribeCustomWorkspaceImageImport-response-Created"></a>
The timestamp when the WorkSpace image import was created.
Type: Timestamp

 ** [ErrorDetails](#API_DescribeCustomWorkspaceImageImport_ResponseSyntax) **   <a name="WorkSpaces-DescribeCustomWorkspaceImageImport-response-ErrorDetails"></a>
Describes in-depth details about the error. These details include the possible causes of the error and troubleshooting information.
Type: Array of [CustomWorkspaceImageImportErrorDetails](API_CustomWorkspaceImageImportErrorDetails.md) objects

 ** [ImageBuilderInstanceId](#API_DescribeCustomWorkspaceImageImport_ResponseSyntax) **   <a name="WorkSpaces-DescribeCustomWorkspaceImageImport-response-ImageBuilderInstanceId"></a>
The image builder instance ID of the WorkSpace image.
Type: String
Length Constraints: Minimum length of 1.

 ** [ImageId](#API_DescribeCustomWorkspaceImageImport_ResponseSyntax) **   <a name="WorkSpaces-DescribeCustomWorkspaceImageImport-response-ImageId"></a>
The identifier of the WorkSpace image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`

 ** [ImageSource](#API_DescribeCustomWorkspaceImageImport_ResponseSyntax) **   <a name="WorkSpaces-DescribeCustomWorkspaceImageImport-response-ImageSource"></a>
Describes the image import source.
Type: [ImageSourceIdentifier](API_ImageSourceIdentifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [InfrastructureConfigurationArn](#API_DescribeCustomWorkspaceImageImport_ResponseSyntax) **   <a name="WorkSpaces-DescribeCustomWorkspaceImageImport-response-InfrastructureConfigurationArn"></a>
The infrastructure configuration ARN that specifies how the WorkSpace image is built.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`

 ** [LastUpdatedTime](#API_DescribeCustomWorkspaceImageImport_ResponseSyntax) **   <a name="WorkSpaces-DescribeCustomWorkspaceImageImport-response-LastUpdatedTime"></a>
The timestamp when the WorkSpace image import was last updated.
Type: Timestamp

 ** [ProgressPercentage](#API_DescribeCustomWorkspaceImageImport_ResponseSyntax) **   <a name="WorkSpaces-DescribeCustomWorkspaceImageImport-response-ProgressPercentage"></a>
The estimated progress percentage of the WorkSpace image import workflow.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [State](#API_DescribeCustomWorkspaceImageImport_ResponseSyntax) **   <a name="WorkSpaces-DescribeCustomWorkspaceImageImport-response-State"></a>
The state of the WorkSpace image.
Type: String
Valid Values: `PENDING | IN_PROGRESS | PROCESSING_SOURCE_IMAGE | IMAGE_TESTING_START | UPDATING_OPERATING_SYSTEM | IMAGE_COMPATIBILITY_CHECKING | IMAGE_TESTING_GENERALIZATION | CREATING_TEST_INSTANCE | INSTALLING_COMPONENTS | GENERALIZING | VALIDATING | PUBLISHING | COMPLETED | ERROR`

 ** [StateMessage](#API_DescribeCustomWorkspaceImageImport_ResponseSyntax) **   <a name="WorkSpaces-DescribeCustomWorkspaceImageImport-response-StateMessage"></a>
The state message of the WorkSpace image import workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

## Errors
<a name="API_DescribeCustomWorkspaceImageImport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCustomWorkspaceImageImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeCustomWorkspaceImageImport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeCustomWorkspaceImageImport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeCustomWorkspaceImageImport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeCustomWorkspaceImageImport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeCustomWorkspaceImageImport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeCustomWorkspaceImageImport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeCustomWorkspaceImageImport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeCustomWorkspaceImageImport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeCustomWorkspaceImageImport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeCustomWorkspaceImageImport)

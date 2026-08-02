---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_StartDeployment.html
---

# StartDeployment
<a name="API_StartDeployment"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Initiate a manual deployment of the latest commit in a source code repository or the latest image in a source image repository to an AWS App Runner service.

For a source code repository, App Runner retrieves the commit and builds a Docker image. For a source image repository, App Runner retrieves the latest Docker image. In both cases, App Runner then deploys the new image to your service and starts a new container instance.

This is an asynchronous operation. On a successful call, you can use the returned `OperationId` and the [ListOperations](API_ListOperations.md) call to track the operation's progress.

## Request Syntax
<a name="API_StartDeployment_RequestSyntax"></a>

```
{
   "ServiceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_StartDeployment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ServiceArn](#API_StartDeployment_RequestSyntax) **   <a name="apprunner-StartDeployment-request-ServiceArn"></a>
The Amazon Resource Name (ARN) of the App Runner service that you want to manually deploy to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

## Response Syntax
<a name="API_StartDeployment_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_StartDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_StartDeployment_ResponseSyntax) **   <a name="apprunner-StartDeployment-response-OperationId"></a>
The unique ID of the asynchronous operation that this request started. You can use it combined with the [ListOperations](API_ListOperations.md) call to track the operation's progress.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`

## Errors
<a name="API_StartDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource doesn't exist for the specified Amazon Resource Name (ARN) in your AWS account.
HTTP Status Code: 400

## Examples
<a name="API_StartDeployment_Examples"></a>

### Initiate a manual deployment
<a name="API_StartDeployment_Example_1"></a>

This example illustrates how to perform a manual deployment to an App Runner service.

#### Sample Request
<a name="API_StartDeployment_Example_1_Request"></a>

```
$ aws apprunner start-deployment --cli-input-json "`cat`"
{
  "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa"
}
```

#### Sample Response
<a name="API_StartDeployment_Example_1_Response"></a>

```
{
  "OperationId": "853a7d5b-fc9f-4730-831b-fd8037ab832a"
}
```

## See Also
<a name="API_StartDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/StartDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/StartDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/StartDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/StartDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/StartDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/StartDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/StartDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/StartDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/StartDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/StartDeployment)

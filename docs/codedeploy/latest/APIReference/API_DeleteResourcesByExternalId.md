---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteResourcesByExternalId.html
---

# DeleteResourcesByExternalId
<a name="API_DeleteResourcesByExternalId"></a>

Deletes resources linked to an external ID. This action only applies if you have configured blue/green deployments through CloudFormation.

**Note**
It is not necessary to call this action directly. CloudFormation calls it on your behalf when it needs to delete stack resources. This action is offered publicly in case you need to delete resources to comply with General Data Protection Regulation (GDPR) requirements.

## Request Syntax
<a name="API_DeleteResourcesByExternalId_RequestSyntax"></a>

```
{
   "externalId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteResourcesByExternalId_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [externalId](#API_DeleteResourcesByExternalId_RequestSyntax) **   <a name="CodeDeploy-DeleteResourcesByExternalId-request-externalId"></a>
The unique ID of an external resource (for example, a CloudFormation stack ID) that is linked to one or more CodeDeploy resources.
Type: String
Required: No

## Response Elements
<a name="API_DeleteResourcesByExternalId_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteResourcesByExternalId_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DeleteResourcesByExternalId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/DeleteResourcesByExternalId)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/DeleteResourcesByExternalId)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/DeleteResourcesByExternalId)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/DeleteResourcesByExternalId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/DeleteResourcesByExternalId)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/DeleteResourcesByExternalId)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/DeleteResourcesByExternalId)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/DeleteResourcesByExternalId)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/DeleteResourcesByExternalId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/DeleteResourcesByExternalId)

---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_CancelCluster.html
---

# CancelCluster
<a name="API_CancelCluster"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Cancels a cluster job. You can only cancel a cluster job while it's in the `AwaitingQuorum` status. You'll have at least an hour after creating a cluster job to cancel it.

## Request Syntax
<a name="API_CancelCluster_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_CancelCluster_RequestSyntax) **   <a name="Snowball-CancelCluster-request-ClusterId"></a>
The 39-character ID for the cluster that you want to cancel, for example `CID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `CID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Elements
<a name="API_CancelCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CancelCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidJobStateException **
The action can't be performed because the job's current state doesn't allow that action to be performed.
HTTP Status Code: 400

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

 ** KMSRequestFailedException **
The provided AWS Key Management Service key lacks the permissions to perform the specified [CreateJob](API_CreateJob.md) or [UpdateJob](API_UpdateJob.md) action.
HTTP Status Code: 400

## See Also
<a name="API_CancelCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/CancelCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/CancelCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/CancelCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/CancelCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/CancelCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/CancelCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/CancelCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/CancelCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/CancelCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/CancelCluster)

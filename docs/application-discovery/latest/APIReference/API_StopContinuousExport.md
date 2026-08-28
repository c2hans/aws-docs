---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StopContinuousExport.html
---

# StopContinuousExport
<a name="API_StopContinuousExport"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Stop the continuous flow of agent's discovered data into Amazon Athena.

## Request Syntax
<a name="API_StopContinuousExport_RequestSyntax"></a>

```
{
   "exportId": "{{string}}"
}
```

## Request Parameters
<a name="API_StopContinuousExport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [exportId](#API_StopContinuousExport_RequestSyntax) **   <a name="DiscServ-StopContinuousExport-request-exportId"></a>
The unique ID assigned to this export.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: Yes

## Response Syntax
<a name="API_StopContinuousExport_ResponseSyntax"></a>

```
{
   "startTime": number,
   "stopTime": number
}
```

## Response Elements
<a name="API_StopContinuousExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [startTime](#API_StopContinuousExport_ResponseSyntax) **   <a name="DiscServ-StopContinuousExport-response-startTime"></a>
Timestamp that represents when this continuous export started collecting data.
Type: Timestamp

 ** [stopTime](#API_StopContinuousExport_ResponseSyntax) **   <a name="DiscServ-StopContinuousExport-response-stopTime"></a>
Timestamp that represents when this continuous export was stopped.
Type: Timestamp

## Errors
<a name="API_StopContinuousExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationErrorException **
The user does not have permission to perform the action. Check the IAM policy associated with this user.
HTTP Status Code: 400

 ** HomeRegionNotSetException **
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).
The home Region is not set. Set the home Region to continue.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters are not valid. Verify the parameters and try again.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.
HTTP Status Code: 400

 ** OperationNotPermittedException **
This operation is not permitted.
HTTP Status Code: 400

 ** ResourceInUseException **
This issue occurs when the same `clientRequestToken` is used with the `StartImportTask` action, but with different parameters. For example, you use the same request token but have two different import URLs, you can encounter this issue. If the import tasks are meant to be different, use a different `clientRequestToken`, and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified configuration ID was not located. Verify the configuration ID and try again.
HTTP Status Code: 400

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## Examples
<a name="API_StopContinuousExport_Examples"></a>

### Stop a continuous export.
<a name="API_StopContinuousExport_Example_1"></a>

The following example shows the request and response of stopping a particular continuous export specified by passing in a value to `exportId`.

#### Sample Request
<a name="API_StopContinuousExport_Example_1_Request"></a>

```
{
    "exportId": "continuous-export-181b77c3-7jf3-4610-924e-7acafe5bbc59"
}
```

#### Sample Response
<a name="API_StopContinuousExport_Example_1_Response"></a>

```
{
    "ApplicationStatus": "IN_PROGRESS",
    "LastUpdatedTime": 1493405005.639
}
```

## See Also
<a name="API_StopContinuousExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/StopContinuousExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/StopContinuousExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/StopContinuousExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/StopContinuousExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/StopContinuousExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/StopContinuousExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/StopContinuousExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/StopContinuousExport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/StopContinuousExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/StopContinuousExport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

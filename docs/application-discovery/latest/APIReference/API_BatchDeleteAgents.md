---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_BatchDeleteAgents.html
---

# BatchDeleteAgents
<a name="API_BatchDeleteAgents"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

 Deletes one or more agents or collectors as specified by ID. Deleting an agent or collector does not delete the previously discovered data. To delete the data collected, use `StartBatchDeleteConfigurationTask`.

## Request Syntax
<a name="API_BatchDeleteAgents_RequestSyntax"></a>

```
{
   "deleteAgents": [
      {
         "agentId": "{{string}}",
         "force": {{boolean}}
      }
   ]
}
```

## Request Parameters
<a name="API_BatchDeleteAgents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deleteAgents](#API_BatchDeleteAgents_RequestSyntax) **   <a name="DiscServ-BatchDeleteAgents-request-deleteAgents"></a>
 The list of agents to delete.
Type: Array of [DeleteAgent](API_DeleteAgent.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_BatchDeleteAgents_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "agentId": "string",
         "errorCode": "string",
         "errorMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteAgents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchDeleteAgents_ResponseSyntax) **   <a name="DiscServ-BatchDeleteAgents-response-errors"></a>
 A list of agent IDs that failed to delete during the deletion task, each paired with an error message.
Type: Array of [BatchDeleteAgentError](API_BatchDeleteAgentError.md) objects

## Errors
<a name="API_BatchDeleteAgents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationErrorException **
The user does not have permission to perform the action. Check the IAM policy associated with this user.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters are not valid. Verify the parameters and try again.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.
HTTP Status Code: 400

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## Examples
<a name="API_BatchDeleteAgents_Examples"></a>

###
<a name="API_BatchDeleteAgents_Example_1"></a>

The following example shows the request syntax for a `BatchDeleteAgents` API call that deletes an agent from the account provided by the `agentId`.

#### Sample Request
<a name="API_BatchDeleteAgents_Example_1_Request"></a>

```
{
  "deleteAgents": [{
        "agentId": "o-3i7dc2x5a020kaq4s",
        "force": true
    }]
}
```

###
<a name="API_BatchDeleteAgents_Example_2"></a>

The following example shows the response for a successful `BatchDeleteAgents` API call.

#### Sample Response
<a name="API_BatchDeleteAgents_Example_2_Response"></a>

```
{
  "errors": []
}
```

## See Also
<a name="API_BatchDeleteAgents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/BatchDeleteAgents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/BatchDeleteAgents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/BatchDeleteAgents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/BatchDeleteAgents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/BatchDeleteAgents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/BatchDeleteAgents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/BatchDeleteAgents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/BatchDeleteAgents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/BatchDeleteAgents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/BatchDeleteAgents)

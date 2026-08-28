---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteEventSubscription.html
---

# DeleteEventSubscription
<a name="API_DeleteEventSubscription"></a>

 Deletes an AWS DMS event subscription.

## Request Syntax
<a name="API_DeleteEventSubscription_RequestSyntax"></a>

```
{
   "SubscriptionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteEventSubscription_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SubscriptionName](#API_DeleteEventSubscription_RequestSyntax) **   <a name="DMS-DeleteEventSubscription-request-SubscriptionName"></a>
The name of the DMS event notification subscription to be deleted.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteEventSubscription_ResponseSyntax"></a>

```
{
   "EventSubscription": {
      "CustomerAwsId": "string",
      "CustSubscriptionId": "string",
      "Enabled": boolean,
      "EventCategoriesList": [ "string" ],
      "SnsTopicArn": "string",
      "SourceIdsList": [ "string" ],
      "SourceType": "string",
      "Status": "string",
      "SubscriptionCreationTime": "string"
   }
}
```

## Response Elements
<a name="API_DeleteEventSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventSubscription](#API_DeleteEventSubscription_ResponseSyntax) **   <a name="DMS-DeleteEventSubscription-response-EventSubscription"></a>
The event subscription that was deleted.
Type: [EventSubscription](API_EventSubscription.md) object

## Errors
<a name="API_DeleteEventSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_DeleteEventSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DeleteEventSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DeleteEventSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DeleteEventSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DeleteEventSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DeleteEventSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DeleteEventSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DeleteEventSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DeleteEventSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DeleteEventSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DeleteEventSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
